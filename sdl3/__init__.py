"""A pure Python wrapper for SDL3."""

__version__ = "0.9.3b2"

import sys, os, requests, ctypes, platform, keyword, inspect, types, re, \
    asyncio, aiohttp, zipfile, typing, array, atexit, packaging.version

SDL_BINARY, SDL_IMAGE_BINARY, SDL_MIXER_BINARY, SDL_TTF_BINARY, SDL_RTF_BINARY, SDL_NET_BINARY = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_ttf", "SDL3_rtf", "SDL3_net"

SDL_BINARY_VAR_MAP: typing.Dict[str, str] = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_BINARY"):
        SDL_BINARY_VAR_MAP[i] = locals()[i]

SDL_BINARY_VAR_MAP_INV: typing.Dict[str, str] = {value: key for key, value in SDL_BINARY_VAR_MAP.items()}
SDL_REPOSITORIES: typing.List[str] = [key.replace("3", "") for key, _ in SDL_BINARY_VAR_MAP_INV.items()]

def SDL_FORMAT_ARCH(arch: str) -> str:
    """Format the architecture string."""
    if arch.lower() in ["x64", "x86_64", "amd64"]: return "AMD64"
    if arch.lower() in ["aarch64", "arm64"]: return "ARM64"
    assert False, "Unknown architecture."

SDL_SYSTEM, SDL_ARCH = platform.system(), SDL_FORMAT_ARCH(platform.machine())
SDL_BINARY_NAME_FORMAT: typing.Dict[str, str] = {"Darwin": "lib{}.dylib", "Linux": "lib{}.so", "Windows": "{}.dll"}

__doc_file__: str = os.path.join(os.path.dirname(__file__), "__doc__.py")
__doc_generator__: int = int(os.environ.get("SDL_DOC_GENERATOR", "1")) > 0

__initialized__: bool = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__: types.ModuleType = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

def SDL_DOWNLOAD_BINARIES(path: str, system: str = SDL_SYSTEM, arch: str = SDL_ARCH) -> None:
    """Download specific SDL3 binaries to the given path."""
    assert system.capitalize() in ["Darwin", "Linux", "Windows"], "Unknown system."
    assert arch.upper() in ["AMD64", "ARM64"], "Unknown architecture."
    if not os.path.exists(path): os.makedirs(path)

    headers = {"Accept": "application/vnd.github+json"}

    if "SDL_GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    try:
        for release in requests.get("https://api.github.com/repos/Aermoss/PySDL3-Build/releases", headers = headers).json():
            for asset in release["assets"]:
                if asset["name"] != f"{system.capitalize()}-{arch.upper()}-{release['tag_name']}.zip":
                    continue

                with requests.get(asset["browser_download_url"], headers = headers, stream = True) as response:
                    assert response.status_code == 200, f"failed to get binaries from github, status: {response.status_code}."
                    size, current = int(response.headers.get("content-length", 0)), 0

                    with open(os.path.join(path, asset["name"]), "wb") as file:
                        for chunk in response.iter_content(chunk_size = 8192):
                            if chunk: file.write(chunk); current += len(chunk)
                            print("\33[35m", f"downloading '{asset['browser_download_url']}'... {current / size * 100:.1f}% ({current / (1024 ** 2):.2f}/{size / (1024 ** 2):.2f} MB).", "\33[0m", sep = "", end = "\r", flush = True)

                        print("\n", end = "", flush = True)

                    with zipfile.ZipFile(os.path.join(path, asset["name"]), "r") as ref:
                        for name in ref.namelist():
                            if os.path.exists(os.path.join(path, name)):
                                os.remove(os.path.join(path, name))

                        ref.extractall(path)

                    os.remove(os.path.join(path, asset["name"]))
                    return
                
    except requests.RequestException as exc:
        print("\33[31m", f"failed to download binaries, exception: {str(exc).lower()}", "\33[0m", sep = "", flush = True)

def SDL_COUNT_BINARIES(path: str, system: str = SDL_SYSTEM, arch: str = SDL_ARCH) -> typing.Tuple[typing.List[str], typing.List[str]]:
    """Count redundant files and missing specific SDL3 binaries in the given path."""
    assert system.capitalize() in ["Darwin", "Linux", "Windows"], "Unknown system."
    assert arch.upper() in ["AMD64", "ARM64"], "Unknown architecture."
    if not os.path.exists(path): os.makedirs(path)

    redundant, missing = [], \
        [SDL_BINARY_NAME_FORMAT[system].format(i) for i in SDL_BINARY_VAR_MAP_INV.keys()]

    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)): continue
        if i in missing: missing.remove(i)
        else: redundant.append(i)

    return redundant, missing

if not __initialized__:
    if int(os.environ.get("SDL_CHECK_VERSION", "1")) > 0:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if packaging.version.parse(__version__) < packaging.version.parse(version):
                print("\33[35m", f"you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).", "\33[0m", sep = "", flush = True)

        except requests.RequestException:
            ...

    modules, binaryMap, currentBinary = {}, {}, None
    binaryPath = os.environ.get("SDL_BINARY_PATH", os.path.join(os.path.dirname(__file__), "bin"))
    redundant, missing = SDL_COUNT_BINARIES(binaryPath, SDL_SYSTEM, SDL_ARCH)

    if redundant and not int(os.environ.get("SDL_IGNORE_REDUNDANT_FILES", "0")) > 0:
        print("\33[35m", f"redundant file(s) detected in binary folder: {', '.join(redundant)}.", "\33[0m", sep = "", flush = True)

    if missing and int(os.environ.get("SDL_DOWNLOAD_BINARIES", "1")) > 0:
        print("\33[35m", f"missing binaries detected: {', '.join(missing)}.", "\33[0m", sep = "", flush = True)
        SDL_DOWNLOAD_BINARIES(binaryPath, SDL_SYSTEM, SDL_ARCH)

    for key, value in SDL_BINARY_VAR_MAP.items():
        modules[value], binaryMap[value] = {}, (ctypes.WinDLL if SDL_SYSTEM in ["Windows"] else ctypes.CDLL) \
            (os.path.join(binaryPath, SDL_BINARY_NAME_FORMAT[SDL_SYSTEM].format(value)))

def SDL_ARRAY(*args: typing.List[typing.Any], **kwargs: typing.Dict[str, typing.Any]) -> typing.Tuple[ctypes.Array[typing.Any], int]:
    """Create a ctypes array."""
    return ((kwargs.get("type") or args[0].__class__) * len(args))(*args), len(args)

def SDL_DEREFERENCE(value: typing.Any) -> typing.Any:
    """Dereference a ctypes pointer or object."""
    if isinstance(value, ctypes._Pointer): return value.contents
    elif hasattr(value, "_obj"): return value._obj
    else: return value

def SDL_CACHE_FUNC(func: typing.Callable) -> typing.Callable:
    """Simple function cache decorator."""
    cache = {}

    def __inner__(*args: typing.List[typing.Any], **kwargs: typing.Dict[str, typing.Any]) -> typing.Any:
        _hash = hash((args, tuple(frozenset(sorted(kwargs.items())))))
        if _hash not in cache: cache.update({_hash: func(*args, **kwargs)})
        return cache.get(_hash, None)

    return __inner__

@SDL_CACHE_FUNC
def SDL_GET_BINARY_NAME(binary: typing.Any) -> str:
    """Get the name of an SDL3 binary."""
    return {v: k for k, v in __module__.binaryMap.items()}[binary]

def SDL_GET_BINARY(name: str) -> typing.Any:
    """Get an SDL3 binary by its name."""
    return __module__.binaryMap[name]

def SDL_SET_CURRENT_BINARY(name: str) -> None:
    """Set the current SDL3 binary by its name."""
    __module__.currentBinary = SDL_GET_BINARY(name)

def SDL_GET_CURRENT_BINARY() -> typing.Any:
    """Get the current SDL3 binary."""
    return __module__.currentBinary

def SDL_FUNC(name: str, retType: typing.Any, *args: typing.List[typing.Any]) -> None:
    """Define an SDL3 function."""
    func = getattr(binary := SDL_GET_CURRENT_BINARY(), name)
    func.__binary__, func.restype, func.argtypes = binary, retType, args
    if not __doc_generator__: setattr(__module__, name, func)
    __module__.modules[SDL_GET_BINARY_NAME(binary)][name] = func

async def SDL_GET_LATEST_RELEASES() -> typing.Dict[str, str]:
    """Get latest releases of SDL3 modules from their official github repositories."""
    session, releases, tasks = aiohttp.ClientSession(), {}, []
    headers = {"Accept": "application/vnd.github+json"}

    if "SDL_GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    for repo in SDL_REPOSITORIES:
        url = f"https://api.github.com/repos/libsdl-org/{repo}/releases"
        print(f"sending a request to \"{url}\".", flush = True)
        tasks.append(asyncio.create_task(session.get(url, headers = headers, ssl = False)))

    responses = await asyncio.gather(*tasks)
    print(f"response gathering completed ({len(responses)} response(s)).", flush = True)

    for response, repo in zip(responses, SDL_REPOSITORIES):
        if response.status != 200:
            print((await response.json())["message"].lower(), flush = True)
            if response.status == 403: await session.close(); return releases
            print(f"failed to get latest releases of \"{response.url}\", skipping (status: {response.status}).", flush = True)
            releases[repo] = None

        else:
            latestRelease = (None, None)

            for release in await response.json():
                score = packaging.version.parse(release["tag_name"].split("-")[1])

                if not latestRelease[0] or score > latestRelease[0]:
                    latestRelease = (score, release["tag_name"])

            releases[repo] = latestRelease[1]

    await session.close()
    return releases

async def SDL_GET_FUNC_DESCRIPTIONS(funcs: typing.List[typing.Tuple[str, str]]) -> typing.Tuple[typing.List[str], typing.List[typing.List[str]]]:
    """Get descriptions and arguments of SDL3 functions from the official SDL3 wiki."""
    session, tasks = aiohttp.ClientSession(), []

    for module, func in funcs:
        url = f"https://wiki.libsdl.org/{module}/{func}"
        print(f"sending a request to \"{url}\".\n", end = "", flush = True)
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))
    
    responses = await asyncio.gather(*tasks)
    print(f"response gathering completed ({len(responses)} response(s)).\n", end = "", flush = True)
    descriptions, arguments = [], []

    for response in responses:
        if response.status != 200:
            print(f"failed to get description of \"{response.url}\", skipping (status: {response.status}).\n", end = "", flush = True)
            descriptions.append(None)
            arguments.append(None)

        else:
            content = (await response.content.read()).decode()

            if "no such page" in content.lower():
                print(f"no such page found for \"{response.url}\", skipping.\n", end = "", flush = True)
                descriptions.append(None)
                arguments.append(None)
                continue

            for a, b in zip(list(re.finditer(r"<p>", content)), list(re.finditer(r"</p>", content))):
                if content[a.end()] == "<": continue
                description = re.sub(r"<a href=\"([a-zA-Z0-9_]+)\">([a-zA-Z0-9_]+)</a>", rf"[\2]({'/'.join(str(response.url).split('/')[:-1])}/\1)", content[a.end():b.start()])
                descriptions.append(description.replace("<em>", "").replace("</em>", "").replace("<code>", "`").replace("</code>", "`").replace("<strong>", "").replace("</strong>", ""))
                break

            for a, b in zip(list(re.finditer(r"<code([a-zA-Z0-9_=#\s\"\-]*)>", content)), list(re.finditer(r"</code>", content))):
                if "sourceCode c" not in content[a.start():a.end()]: continue
                text = re.sub(r"<(/)?([a-zA-Z0-9_=#\s\"\-]+)>", r"", content[a.end():b.start()]).split(";")[0]
                if "\n" in text: text = " ".join(text.split("\n"))
                text = text[text.index("(") + 1:text.index(")") + 1].replace(")", ",").replace("[", "").replace("]", "")
                if text == "void,": text = ""
                arguments.append([text[arg.start():arg.end() - 1] for arg in re.finditer(r"([a-zA-Z0-9_]+)\,", text)])
                break

    await session.close()
    return descriptions, arguments

def SDL_GENERATE_DOCS() -> str:
    """Generate type hints and documentation for SDL3 functions."""

    __index, (descriptions, arguments) = -1, \
        asyncio.run(SDL_GET_FUNC_DESCRIPTIONS([(module, func) for module in __module__.modules for func in __module__.modules[module]]))

    for module in __module__.modules:
        for name in __module__.modules[module]:
            __module__.modules[module][name].__doc__ = \
                (descriptions[__index := __index + 1], arguments[__index])

    result = "\"\"\"This file is auto-generated.\"\"\"\n\nfrom .SDL import *\n\n"
    result += "from .__init__ import ctypes, typing, SDL_GET_BINARY, \\\n"
    result += f"{' ' * 4}{', '.join(list(SDL_BINARY_VAR_MAP.keys()))}\n\n"
    result += f"class POINTER:\n{' ' * 4}\"\"\"Simple pointer type.\"\"\"\n"
    result += f"{' ' * 4}@classmethod\n{' ' * 4}def __class_getitem__(cls, item):\n"
    result += f"{' ' * 8}return ctypes.POINTER(item)\n\n"
    types, definitions = set(), ""

    def SDL_GET_NAME(i):
        if i is None: return "None"
        if "CFunctionType" in i.__name__: return "ctypes._Pointer"
        if i.__name__.startswith("LP_"): types.add(i.__name__)
        if i.__name__.startswith("c_"): return f"ctypes.{i.__name__}"
        return i.__name__

    for index, module in enumerate(__module__.modules):
        if len(__module__.modules[module]) == 0: continue
        definitions += f"# {SDL_BINARY_NAME_FORMAT[platform.system()].format(module)} implementation.\n\n"

        for _index, name in enumerate(__module__.modules[module]):
            retType, argtypes, (description, arguments) = \
                __module__.modules[module][name].restype, __module__.modules[module][name].argtypes, __module__.modules[module][name].__doc__

            assert arguments is None or (arguments is not None and len(arguments) == len(argtypes)), f"argument count mismatch for 'https://wiki.libsdl.org/{module}/{name}'."
            arguments = [f"{'_' if arguments is None or arguments[i] in keyword.kwlist else ''}{i if arguments is None else arguments[i]}" for i in range(len(argtypes))]
            definitions += f"def {name}({', '.join([f'{arg}: {SDL_GET_NAME(type)}' for arg, type in zip(arguments, argtypes)])}) -> {SDL_GET_NAME(retType)}:\n"
            definitions += f"{' ' * 4}\"\"\"\n"
            if description is not None: definitions += f"    {description}\n"
            definitions += f"{' ' * 4}https://wiki.libsdl.org/{module}/{name}\n"
            definitions += f"{' ' * 4}\"\"\"\n"
            definitions += f"{' ' * 4}return SDL_GET_BINARY({SDL_BINARY_VAR_MAP_INV[module]}).{name}({', '.join(arguments)})"

            if _index != len(__module__.modules[module]) - 1:
                definitions += "\n\n"

        if index != len(__module__.modules) - 1 and len(list(__module__.modules.values())[index + 1]) != 0:
            definitions += "\n\n"

    for i in types:
        count, name = i.count("LP_"), i.replace("LP_", "")
        result += f"{i}: typing.TypeAlias = {'POINTER[' * count}{'ctypes.' if name.startswith('c_') else ''}{name}{']' * count}\n"

    return f"{result}\n{definitions}"

def SDL_GET_OR_GENERATE_DOCS() -> bytes:
    """Get type hints and documentation for SDL3 functions from github or generate it."""

    try:
        headers = {"Accept": "application/vnd.github+json"}

        if "SDL_GITHUB_TOKEN" in os.environ:
            headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

        for release in requests.get(f"https://api.github.com/repos/Aermoss/PySDL3/releases", headers = headers).json():
            if release["tag_name"] != f"v{__version__}":
                continue

            for asset in release["assets"]:
                if asset["name"] != f"{SDL_SYSTEM}-Docs.py":
                    continue

                with requests.get(asset["browser_download_url"], headers = headers, stream = True) as response:
                    assert response.status_code == 200, f"failed to get docs from github, status: {response.status_code}."
                    return bytearray().join([chunk for chunk in response.iter_content(chunk_size = 8192) if chunk])
            
    except requests.RequestException as exc:
        print(f"failed to get docs from github, exception: {str(exc).lower()}.", flush = True)

    return SDL_GENERATE_DOCS().encode("utf-8")

from sdl3.SDL import *

SDL_VERSIONNUM_STRING = lambda num: \
    f"{SDL_VERSIONNUM_MAJOR(num)}.{SDL_VERSIONNUM_MINOR(num)}.{SDL_VERSIONNUM_MICRO(num)}"

SDL_BINARY_VERSION, SDL_IMAGE_BINARY_VERSION, SDL_MIXER_BINARY_VERSION, SDL_TTF_BINARY_VERSION, SDL_RTF_BINARY_VERSION, SDL_NET_BINARY_VERSION = \
    SDL_GET_BINARY(SDL_BINARY).SDL_GetVersion(), SDL_GET_BINARY(SDL_IMAGE_BINARY).IMG_Version(), SDL_GET_BINARY(SDL_MIXER_BINARY).Mix_Version(), \
        SDL_GET_BINARY(SDL_TTF_BINARY).TTF_Version(), SDL_GET_BINARY(SDL_RTF_BINARY).RTF_Version(), SDL_GET_BINARY(SDL_NET_BINARY).SDLNet_Version()

if not __initialized__:
    if int(os.environ.get("SDL_CHECK_BINARY_VERSION", "1")) > 0:
        for i in SDL_BINARY_VAR_MAP:
            if (binaryVersion := locals()[f"{i}_VERSION"]) != (version := locals()[f"{i.replace('_BINARY', '')}_VERSION"]):
                print("\33[35m", f"version mismatch with binary: '{SDL_BINARY_NAME_FORMAT[SDL_SYSTEM].format(SDL_BINARY_VAR_MAP[i])}' (expected: {SDL_VERSIONNUM_STRING(version)}, got: {SDL_VERSIONNUM_STRING(binaryVersion)}).", "\33[0m", sep = "", flush = True)

    if __doc_generator__:
        if not os.path.exists(__doc_file__):
            with open(__doc_file__, "wb") as file:
                file.write(SDL_GET_OR_GENERATE_DOCS())

        from .__doc__ import *

    else:
        if os.path.exists(__doc_file__):
            os.remove(__doc_file__)
