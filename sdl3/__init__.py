"""A pure Python wrapper for SDL3."""

__version__ = "0.9.7b0"

import sys, os, requests, ctypes, ctypes.util, platform, keyword, inspect, collections.abc as abc, \
    asyncio, aiohttp, zipfile, typing, types, array, importlib, atexit, packaging.version, json, re

SDL_BINARY, SDL_IMAGE_BINARY, SDL_MIXER_BINARY, SDL_TTF_BINARY, SDL_RTF_BINARY, SDL_NET_BINARY, SDL_SHADERCROSS_BINARY = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_ttf", "SDL3_rtf", "SDL3_net", "SDL3_shadercross"

SDL_BINARY_VAR_MAP: dict[str, str] = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_BINARY"):
        SDL_BINARY_VAR_MAP[i] = locals()[i]

SDL_BINARY_VAR_MAP_INV: dict[str, str] = {value: key for key, value in SDL_BINARY_VAR_MAP.items()}
SDL_REPOSITORIES: list[str] = [key.replace("3", "") for key, _ in SDL_BINARY_VAR_MAP_INV.items()]

def SDL_FORMAT_ARCH(arch: str) -> str:
    """Format the architecture string."""
    if arch.lower() in ["x64", "x86_64", "amd64"]: return "AMD64"
    if arch.lower() in ["aarch64", "arm64"]: return "ARM64"
    assert False, "Unknown architecture."

SDL_SYSTEM, SDL_ARCH = platform.system(), SDL_FORMAT_ARCH(platform.machine())
SDL_BINARY_PATTERNS: dict[str, list[str]] = \
    {"Windows": ["{}.dll"], "Darwin": ["lib{}.dylib", "{0}.framework/{0}", "{0}.framework/Versions/A/{0}"], "Linux": ["lib{}.so"]}

def SDL_PLATFORM_SPECIFIC(system: list[str] = None, arch: list[str] = None) -> bool:
    """Check if the current platform is inside the given platforms."""
    if int(os.environ.get("SDL_PLATFORM_AGNOSTIC", "0")) > 0: return True
    return (not system or SDL_SYSTEM in system) and (not arch or SDL_ARCH in arch)

__frozen__: bool = getattr(sys, "frozen", False)
__doc_file__: str = os.path.join(os.path.dirname(__file__), "__doc__.py")
__doc_generator__: int = int(os.environ.get("SDL_DOC_GENERATOR", str(int(not __frozen__)))) > 0

__initialized__: bool = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__: types.ModuleType = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

def SDL_FIND_BINARIES(libraries: list[str]) -> list[str]:
    """Find binaries of system libraries."""
    libraries = libraries + [f"{library}d" for library in libraries]
    binaries = [f"./{file}" if SDL_SYSTEM in ["Windows"] and not ("/" in file or "\\" in file) else file for library in libraries if (file := ctypes.util.find_library(library))]

    if SDL_SYSTEM in ["Darwin"] and SDL_ARCH in ["ARM64"] and os.path.exists(path := "/opt/Homebrew/lib"):
        binaries += [file for library in libraries for pattern in SDL_BINARY_PATTERNS if os.path.exists(file := os.path.join(path, pattern.format(library)))]

    return binaries

def SDL_DOWNLOAD_BINARIES(path: str, system: str = SDL_SYSTEM, arch: str = SDL_ARCH) -> None:
    """Download specific SDL3 binaries to the given path."""
    assert system.capitalize() in ["Darwin", "Linux", "Windows"], "Unknown system."
    assert arch.upper() in ["AMD64", "ARM64"], "Unknown architecture."
    if not os.path.exists(path): os.makedirs(path)

    headers = {"Accept": "application/vnd.github+json"}

    if len(os.environ.get("SDL_GITHUB_TOKEN", "")) != 0:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    try:
        for release in requests.get("https://api.github.com/repos/Aermoss/PySDL3-Build/releases", headers = headers).json():
            if release["draft"] or release["prerelease"]:
                continue

            for asset in release["assets"]:
                if asset["name"] != f"{system.capitalize()}-{arch.upper()}-{release['tag_name']}.zip":
                    continue

                with requests.get(asset["browser_download_url"], headers = headers, stream = True) as response:
                    assert response.status_code == 200, f"failed to get binaries from github, status: {response.status_code}."
                    size, current = int(response.headers.get("content-length", 0)), 0

                    with open(os.path.join(path, asset["name"]), "wb") as file:
                        for chunk in response.iter_content(chunk_size = 8192):
                            if chunk: file.write(chunk); current += len(chunk)
                            print("\33[32m", f"info: downloading '{asset['browser_download_url']}'... {current / size * 100:.1f}% ({current / (1024 ** 2):.2f}/{size / (1024 ** 2):.2f} MB).", "\33[0m", sep = "", end = "\r", flush = True)

                        print(flush = True)

                    data = {
                        "arch": arch, "system": system, "target": f"v{__version__}",
                        "version": release["tag_name"], "url": asset["browser_download_url"],
                        "created": asset["created_at"], "updated": asset["updated_at"],
                        "uploader": asset["uploader"]["login"], "files": [],
                        "repair": True, "find": True
                    }

                    with zipfile.ZipFile(os.path.join(path, asset["name"]), "r") as ref:
                        for name in ref.namelist():
                            data["files"].append(f"./{name}")

                            if os.path.exists(os.path.join(path, name)):
                                os.remove(os.path.join(path, name))

                        ref.extractall(path)

                    with open(os.path.join(path, "metadata.json"), "w") as file:
                        json.dump(data, file, indent = 4)

                    os.remove(os.path.join(path, asset["name"]))
                    return
                
    except requests.RequestException as exc:
        print("\33[31m", f"error: failed to download binaries: {str(exc).lower()}", "\33[0m", sep = "", flush = True)

if not __initialized__:
    if int(os.environ.get("SDL_CHECK_VERSION", str(int(not __frozen__)))) > 0:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if packaging.version.parse(__version__) < packaging.version.parse(version):
                print("\33[35m", f"warning: you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).", "\33[0m", sep = "", flush = True)

        except requests.RequestException:
            ...

    functions, binaryMap = {i: {} for i in SDL_BINARY_VAR_MAP_INV}, {}
    binaryData, missing = {"system": SDL_SYSTEM, "arch": SDL_ARCH, "files": []}, None
    binaryPath = os.environ.get("SDL_BINARY_PATH", os.path.join(os.path.dirname(__file__), "bin"))
    absPath = lambda path: path if os.path.isabs(path) else os.path.abspath(os.path.join(binaryPath, path))
    if not os.path.exists(binaryPath): os.makedirs(binaryPath)

    if int(os.environ.get("SDL_DISABLE_METADATA", "0")) > 0:
        for root, _, files in os.walk(binaryPath):
            for file in files:
                if (file.endswith(".dll") and SDL_SYSTEM in ["Windows"]) \
                or ((file.endswith(".dylib") or ".framework" in file) and SDL_SYSTEM in ["Darwin"]) \
                or (".so" in file and SDL_SYSTEM in ["Linux"]):
                    binaryData["files"].append(os.path.join(root, file))

    elif "metadata.json" in (files := os.listdir(binaryPath)):
        with open(os.path.join(binaryPath, "metadata.json"), "r") as file:
            missing, binaryData = True, json.load(file)
            binaryData["files"] = [absPath(i) for i in binaryData["files"]]

        if packaging.version.parse(__version__) > packaging.version.parse(binaryData.get("target", __version__)):
            print("\33[35m", f"warning: incompatible target version detected: '{binaryData['target']}', current: 'v{__version__}'.", "\33[0m", sep = "", flush = True)

        elif binaryData["system"].lower() != SDL_SYSTEM.lower() or binaryData["arch"].lower() != SDL_ARCH.lower():
            print("\33[35m", f"warning: incompatible binary architecture and/or system detected: '{binaryData['system']} ({binaryData['arch']})'.", "\33[0m", sep = "", flush = True)
            binaryData["repair"] = True

            for i in binaryData["files"]:
                if os.path.exists(i): os.remove(i)

        else:
            if missing := [i for i in binaryData["files"] if not os.path.exists(i)]:
                print("\33[35m", "warning: missing binary file(s) detected: '", "', '".join(missing), "'.", "\33[0m", sep = "", flush = True)

    else:
        print("\33[35m", "warning: no metadata detected.", "\33[0m", sep = "", flush = True)
        missing = True

    if int(os.environ.get("SDL_DOWNLOAD_BINARIES", str(int(binaryData.get("repair", True))))) > 0 and missing:
        SDL_DOWNLOAD_BINARIES(binaryPath, SDL_SYSTEM, SDL_ARCH)

        with open(os.path.join(binaryPath, "metadata.json"), "r") as file:
            binaryData, missing = json.load(file), None
            binaryData["files"] = [absPath(i) for i in binaryData["files"]]

    if int(os.environ.get("SDL_FIND_BINARIES", str(int(binaryData.get("find", missing is None))))) > 0:
        binaryData["files"] += SDL_FIND_BINARIES(list(SDL_BINARY_VAR_MAP_INV.keys()))

    for binary in SDL_BINARY_VAR_MAP_INV:
        for path in binaryData["files"].copy():
            if (file := os.path.split(path)[1]).split(".")[0].endswith(binary) and os.path.exists(path):
                if (file.endswith(".dll") and SDL_SYSTEM in ["Windows"]) \
                or ((file.endswith(".dylib") or ".framework" in file) and SDL_SYSTEM in ["Darwin"]) \
                or (".so" in file and SDL_SYSTEM in ["Linux"]):
                    binaryMap[binary], functions[binary] = ctypes.CDLL(os.path.abspath(path)), {}
                    binaryData["files"].remove(path)
                    break

def SDL_ARRAY(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) -> tuple[ctypes.Array[typing.Any], int]:
    """Create a ctypes array."""
    return ((kwargs.get("type") or args[0].__class__) * len(args))(*args), len(args)

def SDL_DEREFERENCE(value: typing.Any) -> typing.Any:
    """Dereference a ctypes pointer or object."""
    if isinstance(value, ctypes._Pointer): return value.contents
    elif hasattr(value, "_obj"): return value._obj
    else: return value

def SDL_CACHE_FUNC(func: abc.Callable[..., typing.Any]) -> abc.Callable[..., typing.Any]:
    """Simple function cache decorator."""
    cache = {}

    def __inner__(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) -> typing.Any:
        _hash = hash((args, tuple(frozenset(sorted(kwargs.items())))))
        if _hash not in cache: cache.update({_hash: func(*args, **kwargs)})
        return cache.get(_hash, None)

    return __inner__

@SDL_CACHE_FUNC
def SDL_GET_BINARY_NAME(binary: ctypes.CDLL) -> str | None:
    """Get the name of an SDL3 binary."""
    return {v: k for k, v in __module__.binaryMap.items()}.get(binary, None)

def SDL_GET_BINARY(name: str) -> ctypes.CDLL | None:
    """Get an SDL3 binary by its name."""
    return __module__.binaryMap.get(name, None)

def SDL_NOT_IMPLEMENTED(name: str) -> abc.Callable[..., None]:
    return lambda *args, **kwargs: print("\33[31m", f"error: invoked an unimplemented function: '{name}'.", "\33[0m", sep = "", flush = True)

SDL_ENUM: typing.TypeAlias = ctypes.c_int
SDL_VA_LIST: typing.TypeAlias = ctypes.c_char_p

class SDL_FUNC:
    @classmethod
    def __class_getitem__(cls, key) -> typing.Any:
        """Create a new ctypes function definition."""

        if not __frozen__ and int(os.environ.get("SDL_DEBUG", "0")) > 0:
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 4, "Expected a tuple with length 4."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type) or key[1] is None, "Expected a type as the second argument."
            assert isinstance(key[2], list), "Expected a list as the third argument."
            assert ... not in key[2] or key[2].count(...) == 1, "Expected at most 1 '...' in the argument list."
            assert ... not in key[2] or key[2][-1] == ..., "Expected '...' at the end of the argument list."
            assert isinstance(key[3], str), "Expected a string as the fourth argument."
            assert key[3] in SDL_BINARY_VAR_MAP_INV, "Unknown binary."

        if binary := SDL_GET_BINARY(key[3]):
            func = getattr(binary, key[0], None)

        else:
            if int(os.environ.get("SDL_IGNORE_MISSING_FUNCTIONS", "0")) > 0:
                print("\33[35m", f"warning: function '{key[0]}' not found in binary: '{key[3]}'.", "\33[0m", sep = "", flush = True)

        if not binary or not func: func = SDL_NOT_IMPLEMENTED(key[0])
        func.restype, func.binary = key[1], binary

        if ... in key[2]:
            def __inner__(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) -> typing.Any:
                for arg in args[len(__inner__.func.argtypes):]:
                    if isinstance(arg, int): __inner__.func.argtypes += [ctypes.c_int]
                    elif isinstance(arg, float): __inner__.func.argtypes += [ctypes.c_float]
                    elif isinstance(arg, bytes): __inner__.func.argtypes += [ctypes.c_char_p]
                    elif isinstance(arg, bool): __inner__.func.argtypes += [ctypes.c_bool]
                    else: __inner__.func.argtypes += [arg.__class__]

                value = __inner__.func(*args, **kwargs)
                __inner__.func.argtypes = key[2][:-1]
                return value

            func.argtypes, func.vararg = key[2][:-1], True
            func, __inner__.func = __inner__, func

        else:
            func.argtypes, func.vararg = key[2], False

        __module__.functions[key[3]][key[0]] = func
        return func

class SDL_POINTER:
    @classmethod
    def __class_getitem__(cls, key) -> typing.Any:
        """Create a ctypes pointer type from a ctypes type."""

        if not __frozen__ and int(os.environ.get("SDL_DEBUG", "0")) > 0:
            assert not isinstance(key, tuple), "Expected a single argument, got a tuple."
            assert isinstance(key, type), "Expected a type as the first argument."

        return ctypes.POINTER(key)

class SDL_CAST:
    @classmethod
    def __class_getitem__(cls, key) -> typing.Any:
        """Cast a ctypes pointer to an another type."""

        if not __frozen__ and int(os.environ.get("SDL_DEBUG", "0")) > 0:
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 2, "Expected a tuple with length 2."
            assert isinstance(key[0], ctypes._Pointer), "Expected a pointer as the first argument."
            assert isinstance(key[1], type), "Expected a type as the second argument."

        return ctypes.cast(key[0], key[1])

class SDL_TYPE:
    @classmethod
    def __class_getitem__(cls, key) -> typing.Any:
        """Create a new type from a ctypes type."""

        if not __frozen__ and int(os.environ.get("SDL_DEBUG", "0")) > 0:
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 2, "Expected a tuple with length 2."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type), "Expected a type as the second argument."

        return type(key[0], (ctypes._SimpleCData, ), {"_type_": key[1]._type_})

class SDL_FUNC_TYPE:
    @classmethod
    def __class_getitem__(cls, key) -> typing.Any:
        """Create a new ctypes function type."""

        if not __frozen__ and int(os.environ.get("SDL_DEBUG", "0")) > 0:
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 3, "Expected a tuple with length 3."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type) or key[1] is None, "Expected a type as the second argument."
            assert isinstance(key[2], list), "Expected a list as the third argument."

        value = ctypes.CFUNCTYPE(key[1], *key[2])
        value.__name__ = key[0]; return value

async def SDL_GET_LATEST_RELEASES() -> dict[str, str]:
    """Get latest releases of SDL3 modules from their official github repositories."""
    session, releases, tasks = aiohttp.ClientSession(), {}, []
    headers = {"Accept": "application/vnd.github+json"}

    if "SDL_GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    for repo in SDL_REPOSITORIES:
        url = f"https://api.github.com/repos/libsdl-org/{repo}/releases"
        print("\33[32m", f"info: sending a request to '{url}'.", "\33[0m", sep = "", flush = True)
        tasks.append(asyncio.create_task(session.get(url, headers = headers, ssl = False)))

    responses = await asyncio.gather(*tasks)
    print("\33[32m", f"info: response gathering completed ({len(responses)} response(s)).", "\33[0m", sep = "", flush = True)

    for response, repo in zip(responses, SDL_REPOSITORIES):
        if response.status != 200:
            print("\33[35m", "warning: ", (await response.json())["message"].lower(), "\33[0m", sep = "", flush = True)
            if response.status == 403: await session.close(); return releases
            print("\33[35m", f"warning: failed to get latest releases of '{response.url}', skipping (status: {response.status}).", "\33[0m", sep = "", flush = True)
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

async def SDL_GET_FUNC_DESCRIPTIONS(funcs: list[tuple[str, str]], rst: bool = False) -> tuple[list[str], list[list[str]]]:
    """Get descriptions and arguments of SDL3 functions from the official SDL3 wiki."""
    session, tasks = aiohttp.ClientSession(), []

    for module, func in funcs:
        url = f"https://wiki.libsdl.org/{module}/{func}"
        print("\33[32m", f"info: sending a request to '{url}'.", "\33[0m", sep = "", flush = True)
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))
    
    responses = await asyncio.gather(*tasks)
    print("\33[32m", f"info: response gathering completed ({len(responses)} response(s)).", "\33[0m", sep = "", flush = True)
    descriptions, arguments = [], []

    for response in responses:
        if response.status != 200:
            print("\33[35m", f"warning: failed to get description of '{response.url}', skipping (status: {response.status}).", "\33[0m", sep = "", flush = True)
            descriptions.append(None)
            arguments.append(None)

        else:
            content = (await response.content.read()).decode()

            if "no such page" in content.lower():
                print("\33[35m", f"warning: no such page found for '{response.url}', skipping.", "\33[0m", sep = "", flush = True)
                descriptions.append(None)
                arguments.append(None)
                continue

            for a, b in zip(list(re.finditer(r"<p>", content)), list(re.finditer(r"</p>", content))):
                if content[a.end()] == "<":
                    continue

                if rst:
                    description = re.sub(r"<a href=\"([a-zA-Z0-9_]+)\">([a-zA-Z0-9_]+)</a>", r"\1", content[a.end():b.start()]) \
                        .replace("<em>", "*").replace("</em>", "*").replace("<code>", "``").replace("</code>", "``").replace("<strong>", "**").replace("</strong>", "**")

                else:
                    description = re.sub(r"<a href=\"([a-zA-Z0-9_]+)\">([a-zA-Z0-9_]+)</a>", rf"[\2]({'/'.join(str(response.url).split('/')[:-1])}/\1)", content[a.end():b.start()]) \
                        .replace("<em>", "").replace("</em>", "").replace("<code>", "`").replace("</code>", "`").replace("<strong>", "").replace("</strong>", "")
                
                descriptions.append(description)
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

def SDL_GENERATE_DOCS(modules: list[str] = list(SDL_BINARY_VAR_MAP_INV.keys()), rst: bool = False) -> str:
    """Generate type hints and documentation for SDL3 functions."""

    __index, (descriptions, arguments) = -1, \
        asyncio.run(SDL_GET_FUNC_DESCRIPTIONS([(module, func) for module in modules for func in __module__.functions[module]], rst))

    for module in modules:
        for func in __module__.functions[module]:
            if (_ := __module__.functions[module][func]).__name__ == "__inner__": _ = _.func
            _.__doc__ = (descriptions[__index := __index + 1], arguments[__index])

    result = "" if rst else f"\"\"\"\n# This file is auto-generated, do not modify it.\nmeta = "
    if not rst: result += f"{{\"target\": \"v{__version__}\", \"system\": \"{SDL_SYSTEM}\"}}\n\"\"\"\n\n"
    result += f"from {'sdl3' if rst else ''}.SDL import *\n\n"
    result += f"from {'sdl3' if rst else ''}.__init__ import {'' if rst else 'raw, '}ctypes, typing, SDL_POINTER\n\n"
    types, definitions = set(), ""

    def SDL_GET_NAME(i):
        if i is None: return "None"
        if i.__name__.startswith("LP_"): types.add(i.__name__)
        if i.__name__.startswith("c_"): return f"ctypes.{i.__name__}"
        else: return i.__name__

    for index, module in enumerate(modules):
        if len(__module__.functions[module]) == 0: continue
        if not rst: definitions += f"# {SDL_BINARY_PATTERNS[SDL_SYSTEM][0].format(module)} implementation.\n\n"

        for _index, func in enumerate(__module__.functions[module]):
            if (_ := __module__.functions[module][func]).__name__ == "__inner__": _ = _.func
            vararg, restype, argtypes, (description, arguments) = _.vararg, _.restype, _.argtypes, _.__doc__
            assert arguments is None or (arguments is not None and len(arguments) == len(argtypes)), f"argument count mismatch for 'https://wiki.libsdl.org/{module}/{func}'."
            arguments = [f"{'_' if arguments is None or arguments[i] in keyword.kwlist else ''}{i if arguments is None else arguments[i]}" for i in range(len(argtypes))]
            definitions += f"def {func}({', '.join([f'{arg}: {SDL_GET_NAME(type)}' for arg, type in zip(arguments, argtypes)] + (['*args: list[typing.Any]'] if vararg else []))}) -> {SDL_GET_NAME(restype)}:\n"
            if not rst or description is not None: definitions += f"{' ' * 4}\"\"\"\n"
            if description is not None: definitions += f"    {description}\n"
            if not rst: definitions += f"\n{' ' * 4}https://wiki.libsdl.org/{module}/{func}\n"
            if not rst or description is not None: definitions += f"{' ' * 4}\"\"\""
            if not rst: definitions += f"\n{' ' * 4}return raw.{func}({', '.join(arguments + (['*args'] if vararg else []))})"
            elif description is None: definitions += f"\n{' ' * 4}..."

            if _index != len(__module__.functions[module]) - 1:
                definitions += "\n\n"

        if index != len(modules) - 1 and len(__module__.functions[modules[index + 1]]) != 0:
            definitions += "\n\n"

    for i in types:
        count, func = i.count("LP_"), i.replace("LP_", "")
        result += f"{i}: typing.TypeAlias = {'SDL_POINTER[' * count}{'ctypes.' if func.startswith('c_') else ''}{func}{']' * count}\n"

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
        print("\33[31m", f"error: failed to get docs from github: {str(exc).lower()}.", "\33[0m", sep = "", flush = True)

    return SDL_GENERATE_DOCS().encode("utf-8")

if not __initialized__ and int(os.environ.get("SDL_CTYPES_ALIAS_FIX", "0")) > 0:
    for i in dir(ctypes):
        if i.startswith("c_") and getattr(ctypes, i).__name__ != i and hasattr(getattr(ctypes, i), "_type_"):
            setattr(ctypes, i, SDL_TYPE[i, getattr(ctypes, i)])

from sdl3.SDL import *

if __doc_generator__:
    import sdl3.SDL as raw

SDL_VERSIONNUM_STRING: abc.Callable[[int], str] = lambda num: \
    f"{SDL_VERSIONNUM_MAJOR(num)}.{SDL_VERSIONNUM_MINOR(num)}.{SDL_VERSIONNUM_MICRO(num)}"

if not __initialized__:
    if int(os.environ.get("SDL_CHECK_BINARY_VERSION", "1")) > 0:
        for binary, left, right in zip(SDL_BINARY_VAR_MAP.values(), [SDL_GetVersion(), IMG_Version(), Mix_Version(), TTF_Version(), RTF_Version(), SDLNet_Version()], [SDL_VERSION, SDL_IMAGE_VERSION, SDL_MIXER_VERSION, SDL_TTF_VERSION, SDL_RTF_VERSION, SDL_NET_VERSION]):
            if left != right: print("\33[35m", f"warning: version mismatch with binary: '{SDL_BINARY_PATTERNS[SDL_SYSTEM][0].format(binary)}' (expected: {SDL_VERSIONNUM_STRING(right)}, got: {SDL_VERSIONNUM_STRING(left)}).", "\33[0m", sep = "", flush = True)

    if __doc_generator__:
        if not os.path.exists(__doc_file__):
            with open(__doc_file__, "wb") as file:
                file.write(SDL_GET_OR_GENERATE_DOCS())

        from .__doc__ import *
        try: exec(getattr(__doc__, "__doc__"), data := {})
        except SyntaxError: data = None

        if not data or data["meta"]["target"] != f"v{__version__}" or data["meta"]["system"] != SDL_SYSTEM:
            with open(__doc_file__, "wb") as file:
                file.write(SDL_GET_OR_GENERATE_DOCS())

            del sys.modules["sdl3.__doc__"]
            print("\33[35m", f"warning: reloading module: 'sdl3.__doc__'.", "\33[0m", sep = "", flush = True)
            from .__doc__ import *

    else:
        if os.path.exists(__doc_file__):
            os.remove(__doc_file__)