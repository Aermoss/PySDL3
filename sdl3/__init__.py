"""A pure Python wrapper for SDL3."""

__version__ = "0.9.10b0"

import os, sys, requests, ctypes, ctypes.util, platform, collections.abc as abc, \
    keyword, packaging.version, asyncio, aiohttp, zipfile, typing, types, json, re

SDL_BINARY, SDL_IMAGE_BINARY, SDL_MIXER_BINARY, SDL_TTF_BINARY, SDL_RTF_BINARY, SDL_NET_BINARY, SDL_SHADERCROSS_BINARY, \
    *SDL_MODULES = ["SDL3", "SDL3_image", "SDL3_mixer", "SDL3_ttf", "SDL3_rtf", "SDL3_net", "SDL3_shadercross"] * 2

def SDL_FORMAT_ARCH(arch: str) -> str:
    """Format the architecture string."""
    if arch.lower() in ["x64", "x86_64", "amd64"]: return "AMD64"
    if arch.lower() in ["aarch64", "arm64"]: return "ARM64"
    assert False, "Unknown architecture."

SDL_SYSTEM, SDL_ARCH = platform.system(), SDL_FORMAT_ARCH(platform.machine())
SDL_BINARY_EXTENSIONS, SDL_BINARY_PATTERNS = {"Windows": ["dll"], "Darwin": ["dylib"], "Linux": ["so"]}, \
    {"Windows": ["{}.dll"], "Darwin": ["lib{}.dylib", "{0}.framework/{0}", "{0}.framework/Versions/Current/{0}"], "Linux": ["lib{}.so"]}

def SDL_PLATFORM_SPECIFIC(system: list[str] | None = None, arch: list[str] | None = None) -> bool:
    """Check if the current platform is inside the given platforms."""
    if int(os.environ.get("SDL_PLATFORM_AGNOSTIC", "0")) > 0: return True
    return (not system or SDL_SYSTEM in system) and (not arch or SDL_ARCH in arch)

__release__: bool = not int(os.environ.get("SDL_DEBUG", "0")) > 0
__frozen__: bool = getattr(sys, "frozen", False) or getattr(sys, "_MEIPASS", None) is not None

__doc_file__: str = os.path.join(os.path.dirname(__file__), "__doc__.py")
__doc_generator__: int = int(os.environ.get("SDL_DOC_GENERATOR", "0" if __frozen__ else "1")) > 0

__initialized__: bool = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__: types.ModuleType = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

class SDL_LOGGER:
    Info, Warning, Error = range(3)
    __level__: int = int(os.environ.get("SDL_LOG_LEVEL", "0"))
    __colors__: dict[int, str] = {Info: "\33[32m", Warning: "\33[35m", Error: "\33[31m"}
    __names__: dict[int, str] = {Info: "Info", Warning: "Warning", Error: "Error"}

    @classmethod
    def Log(cls, level: int, message: str | None = None, end: str | None = "\n") -> None:
        """Log a message at a specific level."""
        assert level in [cls.Error, cls.Warning, cls.Info], "Unknown log level."
        if cls.__level__ is None or level < cls.__level__: return

        if message is not None:
            sys.stdout.write(f"{cls.__colors__[level]}{cls.__names__[level]}: {message}\33[0m")

        if end is not None:
            sys.stdout.write(end)

        sys.stdout.flush()

def SDL_FIND_BINARIES(libraries: list[str]) -> list[str]:
    """Search for binaries in the system libraries."""
    libraries = libraries + [f"{library}d" for library in libraries]
    binaries = [(f"./{file}" if SDL_SYSTEM in ["Windows"] and not ("/" in file or "\\" in file) else file) for library in libraries if (file := ctypes.util.find_library(library))]

    if SDL_SYSTEM in ["Darwin"] and SDL_ARCH in ["ARM64"] and os.path.exists(path := "/opt/Homebrew/lib"):
        binaries += [file for library in libraries for pattern in SDL_BINARY_PATTERNS[SDL_SYSTEM] if os.path.exists(file := os.path.join(path, pattern.format(library)))]

    return binaries

def SDL_DOWNLOAD_BINARIES(path: str, system: str = SDL_SYSTEM, arch: str = SDL_ARCH) -> bool | None:
    """Download specific SDL3 binaries to the given path."""
    assert system.capitalize() in ["Darwin", "Linux", "Windows"], "Unknown system."
    assert arch.upper() in ["AMD64", "ARM64"], "Unknown architecture."
    if not os.path.exists(path): os.makedirs(path)

    headers = {"Accept": "application/vnd.github+json"}

    if len(os.environ.get("SDL_GITHUB_TOKEN", "")) != 0:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    try:
        for release in (_ := requests.get("https://api.github.com/repos/Aermoss/PySDL3-Build/releases", headers = headers).json()):
            if isinstance(release, str):
                SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to download binaries: {_[release]}")
                return False

            if release["draft"] or release["prerelease"]:
                continue

            for asset in release["assets"]:
                if asset["name"] != f"{system.capitalize()}-{arch.upper()}-{release['tag_name']}.zip":
                    continue

                with requests.get(asset["browser_download_url"], headers = headers, stream = True) as response:
                    if response.status_code != 200:
                        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to download binaries, status: {response.status_code} ({response.reason}).")
                        return False

                    size, current = int(response.headers.get("content-length", 0)), 0

                    with open(os.path.join(path, asset["name"]), "wb") as file:
                        for chunk in response.iter_content(chunk_size = 8192):
                            if chunk: file.write(chunk); current += len(chunk)
                            SDL_LOGGER.Log(SDL_LOGGER.Info, f"Downloading '{asset['browser_download_url']}'... {current / size * 100:.1f}% ({current / (1024 ** 2):.2f}/{size / (1024 ** 2):.2f} MB).", end = "\r")

                        SDL_LOGGER.Log(SDL_LOGGER.Info, end = "\n")

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
                    return True

            SDL_LOGGER.Log(SDL_LOGGER.Error, "Failed to download binaries, no binaries found.")
            return False

    except requests.RequestException as exc:
        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to download binaries: {exc}.")
        return False

def SDL_CHECK_BINARY_NAME(name: str) -> bool:
    """Check if the given name is a valid binary name in the current system."""

    if len(_ := name.split(".")) > 1:
        return _[1] in SDL_BINARY_EXTENSIONS[SDL_SYSTEM]

    else:
        return SDL_SYSTEM in ["Darwin"]

if not __initialized__:
    if int(os.environ.get("SDL_RELOAD_FIX", "1")) > 0:
        reloaded = False

        for module in sys.modules.copy():
            if module.startswith("sdl3."):
                del sys.modules[module]
                reloaded = True

        if "sdl3" in sys.modules and reloaded:
            del sys.modules["sdl3"]

    if int(os.environ.get("SDL_CHECK_VERSION", "0" if __frozen__ else "1")) > 0:
        try:
            version = requests.get("https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if packaging.version.parse(__version__) < packaging.version.parse(version):
                SDL_LOGGER.Log(SDL_LOGGER.Warning, f"You are using an older version of PySDL3 (current: {__version__}, latest: {version}).")

        except requests.RequestException:
            SDL_LOGGER.Log(SDL_LOGGER.Warning, "Failed to check for the latest version of PySDL3, please check manually.")

    functions, binaryMap = {module: {} for module in SDL_MODULES}, {}
    binaryData, missing = {"system": SDL_SYSTEM, "arch": SDL_ARCH, "files": []}, None
    binaryPath = os.environ.get("SDL_BINARY_PATH", os.path.join(os.path.dirname(__file__), "bin"))
    absPath = lambda path: path if os.path.isabs(path) else os.path.abspath(os.path.join(binaryPath, path))

    if not os.path.exists(binaryPath):
        try:
            os.makedirs(binaryPath)

        except OSError as exc:
            SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to create binary path: {exc}.")

    if int(os.environ.get("SDL_DISABLE_METADATA", "0")) > 0:
        if os.path.exists(binaryPath) and os.path.isdir(binaryPath):
            for root, _, files in os.walk(binaryPath):
                binaryData["files"] += [os.path.join(root, file) for file in files if SDL_CHECK_BINARY_NAME(file)]

        else:
            SDL_LOGGER.Log(SDL_LOGGER.Warning, "Binary path does not exist.")

    elif "metadata.json" in (files := os.listdir(binaryPath)):
        with open(os.path.join(binaryPath, "metadata.json"), "r") as file:
            binaryData, missing = json.load(file), True
            binaryData["files"] = [absPath(path) for path in binaryData["files"]]

        if packaging.version.parse(__version__) > packaging.version.parse(binaryData.get("target", __version__)):
            SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Incompatible target version detected: '{binaryData['target']}', current: 'v{__version__}'.")

        elif binaryData["system"].lower() != SDL_SYSTEM.lower() or binaryData["arch"].lower() != SDL_ARCH.lower():
            SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Incompatible binary architecture and/or system detected: '{binaryData['system']} ({binaryData['arch']})'.")
            binaryData["repair"] = True

            for path in binaryData["files"]:
                if os.path.exists(path): os.remove(path)

        else:
            if missing := [path for path in binaryData["files"] if not os.path.exists(path)]:
                SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Missing binary file(s) detected: '{', '.join(missing)}'.")

    else:
        SDL_LOGGER.Log(SDL_LOGGER.Warning, "No metadata detected.")
        missing = True

    if int(os.environ.get("SDL_DOWNLOAD_BINARIES", "1" if binaryData.get("repair", True) else "0")) > 0 and missing:
        if _ := SDL_DOWNLOAD_BINARIES(binaryPath, SDL_SYSTEM, SDL_ARCH):
            with open(os.path.join(binaryPath, "metadata.json"), "r") as file:
                binaryData, missing = json.load(file), None
                binaryData["files"] = [absPath(path) for path in binaryData["files"]]

    if int(os.environ.get("SDL_FIND_BINARIES", "1" if binaryData.get("find", missing is None) else "0")) > 0:
        binaryData["files"] += SDL_FIND_BINARIES(SDL_MODULES)

    for module in SDL_MODULES:
        for path in binaryData["files"]:
            if module in binaryMap:
                break

            if os.path.exists(path) and SDL_CHECK_BINARY_NAME(name := os.path.split(path)[1]):
                for _name in [module, f"{module}d"]:
                    if (name.split(".")[0] if "." in name else name).endswith(_name):
                        binaryMap[module] = ctypes.CDLL(os.path.abspath(path))

_CT = typing.TypeVar("_CT", bound = ctypes._SimpleCData)

def SDL_ARRAY(*values: _CT, _type: type[_CT] | None = None) -> tuple[ctypes.Array[_CT], int]:
    """Create a ctypes array from the given arguments."""
    return ((_type or type(values[0])) * len(values))(*values), len(values)

def SDL_DEREFERENCE(value: ctypes._Pointer) -> ctypes._SimpleCData:
    """Dereference a ctypes pointer or object."""
    if isinstance(value, ctypes._Pointer): return value.contents
    elif hasattr(value, "_obj"): return value._obj
    else: return value

def SDL_CACHE_FUNC(func: abc.Callable[..., typing.Any]) -> abc.Callable[..., typing.Any]:
    """Simple function cache decorator."""
    cache = {}

    def __inner__(*args, **kwargs) -> typing.Any:
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
    return lambda *args, **kwargs: \
        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Invoked an unimplemented function: '{name}'.")

class SDL_FUNC:
    def __class_getitem__(cls, key: tuple[str, type[ctypes._SimpleCData], list[type[ctypes._SimpleCData]], str]) -> ctypes._CFuncPtr | abc.Callable[..., None]:
        """Create a new ctypes function definition."""

        if not (__frozen__ or __release__):
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 4, "Expected a tuple with length 4."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type) or key[1] is None, "Expected a type as the second argument."
            assert isinstance(key[2], list), "Expected a list as the third argument."
            assert ... not in key[2] or key[2].count(...) == 1, "Expected at most 1 '...' in the argument list." # type: ignore
            assert ... not in key[2] or key[2][-1] == ..., "Expected '...' at the end of the argument list."
            assert isinstance(key[3], str), "Expected a string as the fourth argument."
            assert key[3] in SDL_MODULES, "Unknown binary."

        if binary := SDL_GET_BINARY(key[3]):
            func = getattr(binary, key[0], None)

            if not func and not int(os.environ.get("SDL_IGNORE_MISSING_FUNCTIONS", "1" if __frozen__ or __release__ else "0")) > 0:
                SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Function '{key[0]}' not found in binary: '{SDL_BINARY_PATTERNS[SDL_SYSTEM][0].format(key[3])}'.")

        if not binary or not func: func = SDL_NOT_IMPLEMENTED(key[0]) # type: ignore
        func.restype, func.binary = key[1], binary # type: ignore

        if ... in key[2]:
            def __inner__(*args, **kwargs) -> typing.Any:
                for arg in args[len(__inner__.func.argtypes):]: # type: ignore
                    if isinstance(arg, int): __inner__.func.argtypes += [ctypes.c_int] # type: ignore
                    elif isinstance(arg, float): __inner__.func.argtypes += [ctypes.c_float] # type: ignore
                    elif isinstance(arg, bytes): __inner__.func.argtypes += [ctypes.c_char_p] # type: ignore
                    elif isinstance(arg, bool): __inner__.func.argtypes += [ctypes.c_bool] # type: ignore
                    else: __inner__.func.argtypes += [arg.__class__] # type: ignore

                value = __inner__.func(*args, **kwargs) # type: ignore
                __inner__.func.argtypes = key[2][:-1] # type: ignore
                return value

            func.argtypes, func.vararg = key[2][:-1], True # type: ignore
            func, __inner__.func = __inner__, func # type: ignore

        else:
            func.argtypes, func.vararg = key[2], False # type: ignore

        __module__.functions[key[3]][key[0]] = func
        return func

class SDL_POINTER:
    def __class_getitem__(cls, key: type[ctypes._SimpleCData]) -> type[ctypes._Pointer]:
        """Create a ctypes pointer type from a ctypes type."""

        if not (__frozen__ or __release__):
            assert not isinstance(key, tuple), "Expected a single argument, got a tuple."
            assert isinstance(key, type), "Expected a type as the first argument."

        return ctypes.POINTER(key)

_T = typing.TypeVar("_T")

class SDL_CAST:
    def __class_getitem__(cls, key: tuple[typing.Any, type[_T]]) -> _T:
        """Cast a ctypes pointer to an another type."""

        if not (__frozen__ or __release__):
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 2, "Expected a tuple with length 2."
            assert isinstance(key[0], ctypes._Pointer), "Expected a pointer as the first argument."
            assert isinstance(key[1], type), "Expected a type as the second argument."

        return ctypes.cast(key[0], key[1]) # type: ignore

class SDL_TYPE:
    def __class_getitem__(cls, key: tuple[str, type[_T]]) -> type[_T]:
        """Create a new type from a ctypes type."""

        if not (__frozen__ or __release__):
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 2, "Expected a tuple with length 2."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type), "Expected a type as the second argument."

        if hasattr(key[1], "contents"):
            return type(key[0], (ctypes._Pointer, ), {"_type_": key[1]._type_, "contents": key[1].contents}) # type: ignore

        elif hasattr(key[1], "_fields_"):
            return type(key[0], (ctypes.Structure, ), {"_fields_": key[1]._fields_}) # type: ignore

        else:
            return type(key[0], (ctypes._SimpleCData, ), {"_type_": key[1]._type_}) # type: ignore

class SDL_FUNC_TYPE:
    def __class_getitem__(cls, key: tuple[str, type[ctypes._SimpleCData], list[type[ctypes._SimpleCData]]]) -> type[ctypes._CFuncPtr]:
        """Create a new ctypes function type."""

        if not (__frozen__ or __release__):
            assert isinstance(key, tuple), "Expected a tuple, got a single argument."
            assert len(key) == 3, "Expected a tuple with length 3."
            assert isinstance(key[0], str), "Expected a string as the first argument."
            assert isinstance(key[1], type) or key[1] is None, "Expected a type as the second argument."
            assert isinstance(key[2], list), "Expected a list as the third argument."

        _, ctypes._c_functype_cache = ctypes._c_functype_cache, {} # type: ignore
        value = ctypes.CFUNCTYPE(key[1], *key[2])
        value.__name__, ctypes._c_functype_cache = key[0], _ # type: ignore
        return value

SDL_ENUM: typing.TypeAlias = SDL_TYPE["SDL_ENUM", ctypes.c_int]
SDL_VA_LIST: typing.TypeAlias = SDL_TYPE["SDL_VA_LIST", ctypes.c_char_p]

def SDL_PARSE_ARGUMENTS(argc: ctypes.c_int, argv: SDL_POINTER[ctypes.c_char_p]) -> list[str]:
    return [argv[i].decode("utf-8") for i in range(argc.value)] # type: ignore

def SDL_PROCESS_DESCRIPTION(description: str, url: str | None = None, rst: bool = False) -> str:
    """Process HTML description."""

    return re.sub(r"<a href=\"([a-zA-Z0-9_]+)\">([a-zA-Z0-9_]+)</a>", r"\1" if rst or not url else rf"[\2]({'/'.join(url.split('/')[:-1])}/\1)", description) \
        .replace("</", "<").replace("<em>", "" if rst else "*").replace("<code>", "`" if rst else "``").replace("<strong>", "" if rst else "**")

async def SDL_GET_LATEST_RELEASES() -> dict[str, str]:
    """Get latest releases of SDL3 modules from their official github repositories."""
    session, releases, tasks = aiohttp.ClientSession(), {}, []
    headers = {"Accept": "application/vnd.github+json"}

    if "SDL_GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

    for module in SDL_MODULES:
        url = f"https://api.github.com/repos/libsdl-org/{module.replace('3', '')}/releases"
        tasks.append(asyncio.create_task(session.get(url, headers = headers, ssl = False)))
        SDL_LOGGER.Log(SDL_LOGGER.Info, f"Sending a request to '{url}'.")

    responses = await asyncio.gather(*tasks)
    SDL_LOGGER.Log(SDL_LOGGER.Info, f"Response gathering completed ({len(responses)} responses).")

    for response, module in zip(responses, SDL_MODULES):
        if response.status != 200:
            SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Failed to get latest release of '{response.url}', skipping (status: {response.status}).")
            releases[module.replace('3', '')] = None

        else:
            latestRelease = (None, None)

            for release in await response.json():
                score = packaging.version.parse(release["tag_name"].split("-")[1])

                if not latestRelease[0] or score > latestRelease[0]:
                    latestRelease = (score, release["tag_name"])

            releases[module.replace('3', '')] = latestRelease[1]

    await session.close()
    return releases

async def SDL_GET_FUNC_DESCRIPTIONS(funcs: list[tuple[str, str]], rst: bool = False) -> tuple[list[str], list[list[str]], list[str]]:
    """Get descriptions, arguments and return types of SDL3 functions from the official SDL3 wiki."""
    session, tasks = aiohttp.ClientSession(), []

    for module, func in funcs:
        url = f"https://wiki.libsdl.org/{module}/{func}"
        SDL_LOGGER.Log(SDL_LOGGER.Info, f"Sending a request to '{url}'.")
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))

    responses = await asyncio.gather(*tasks)
    SDL_LOGGER.Log(SDL_LOGGER.Info, f"Response gathering completed ({len(responses)} responses).")
    descriptions, arguments, returns = [], [], []

    for response in responses:
        if response.status != 200:
            SDL_LOGGER.Log(SDL_LOGGER.Warning, f"No such page: '{response.url}', skipping (status: {response.status}).")
            descriptions.append(None)
            arguments.append(None)
            returns.append(None)

        else:
            content = (await response.content.read()).decode()

            for a, b in zip(list(re.finditer(r"<p>", content)), list(re.finditer(r"</p>", content))):
                if content[a.end()] == "<": continue
                descriptions.append(SDL_PROCESS_DESCRIPTION(content[a.end():b.start()], str(response.url), rst))
                break

            for a, b in zip(list(re.finditer(r"<code([a-zA-Z0-9_=#\s\"\-]*)>", content)), list(re.finditer(r"</code>", content))):
                if "sourceCode c" not in content[a.start():a.end()]: continue
                text = re.sub(r"<(/)?([a-zA-Z0-9_=#\s\"\-]+)>", r"", content[a.end():b.start()]).split(";")[0]
                if "\n" in text: text = " ".join(text.split("\n"))
                returns.append(" ".join([i for i in text.split("(")[0].split(" ")[:-1] if i and i not in ["extern", "SDL_DECLSPEC"]]))
                text = text[text.index("(") + 1:text.index(")") + 1].replace(")", ",")[:-1]
                arguments.append({})

                for i in (text.split(", ") if "," in text else [text]) if text != "void" else []:
                    if i != "...": i = i.split(" ")
                    else: continue

                    arguments[-1][i[-1].replace("*", "")] = \
                        " ".join(i[:-1]) + "*" * i[-1].count("*")

                break

    await session.close()
    return descriptions, arguments, returns

async def SDL_GET_STRUCT_DESCRIPTIONS(structs: list[tuple[str, str]], rst: bool = False) -> tuple[list[str], list[dict[str, typing.Any]]]:
    """Get descriptions and members of SDL3 structures from the official SDL3 wiki."""
    session, tasks = aiohttp.ClientSession(), []

    for module, struct in structs:
        url = f"https://wiki.libsdl.org/{module}/{struct}"
        SDL_LOGGER.Log(SDL_LOGGER.Info, f"Sending a request to '{url}'.")
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))

    responses = await asyncio.gather(*tasks)
    SDL_LOGGER.Log(SDL_LOGGER.Info, f"Response gathering completed ({len(responses)} responses).")
    descriptions, members = [], []

    for response in responses:
        if response.status != 200:
            SDL_LOGGER.Log(SDL_LOGGER.Warning, f"No such page: '{response.url}', skipping (status: {response.status}).")
            descriptions.append(None)
            members.append(None)

        else:
            content = (await response.content.read()).decode()

            for a, b in zip(list(re.finditer(r"<p>", content)), list(re.finditer(r"</p>", content))):
                if content[a.end()] == "<": continue
                descriptions.append(SDL_PROCESS_DESCRIPTION(content[a.end():b.start()], str(response.url), rst))
                break

            for a, b in zip(list(re.finditer(r"<code([a-zA-Z0-9_=#\s\"\-]*)>", content)), list(re.finditer(r"</code>", content))):
                if "sourceCode c" not in content[a.start():a.end()]: continue
                text = re.sub(r"<(/)?([a-zA-Z0-9_=#\s\"\-]+)>", r"", content[a.end():b.start()])
                text, _ = re.sub(r"//.*", r"", re.sub(r"/\*[\s\S]*?\*/", r"", text)), text.split(" ")
                members.append({})

                for line in text.split("\n"):
                    if ";" not in line or "{" in line or "}" in line:
                        continue

                    line = line.split(";")[0].strip().replace(", ", ",")

                    if "SDLCALL" not in line:
                        count, line = line.count("*"), line.replace("*", "").split(" ")

                        for i in line[-1].split(",") if "," in line[-1] else [line[-1]]:
                            members[-1][i] = " ".join(line[:-1]) + "*" * count

                    else:
                        _ = line.replace("SDLCALL", "").split("(")
                        arguments, name = _[2].split(")")[0].strip(), _[1].split(")")[0].replace("*", "").strip()
                        members[-1][name] = {"return": _[0].strip(), "arguments": {}}

                        for i in arguments.split(",") if "," in arguments else [arguments]:
                            if i in ["...", "void"]: continue
                            count, i = i.count("*"), i.replace("*", "").split(" ")
                            members[-1][name]["arguments"][i[-1]] = " ".join(i[:-1]) + "*" * count

                break

    await session.close()
    return descriptions, members

def SDL_GET_MODULE_BY_NAME(name: str) -> str | None:
    """Get the module of an SDL3 function/structure by its name."""

    for prefix, module in sorted({"SDL": "SDL3", "IMG": "SDL3_image", "MIX": "SDL3_mixer", "TTF": "SDL3_ttf", "RTF": "SDL3_rtf", "NET": "SDL3_net", "SDL_ShaderCross": "SDL3_shadercross"}.items(), key = lambda x: -len(x[0])):
        if name.startswith(prefix): return module

def SDL_PYTHONIZE_TYPE(type: str, name: str | None = None, globals: dict[str, typing.Any] = {}) -> str:
    """Pythonize C/C++ types."""
    array = (_ if str.isnumeric(_ := name.split("[")[1].split("]")[0]) else eval(_, globals)) if name is not None and name.count("[") == 1 and name.index("]") - name.index("[") != 1 else None
    type, count = type.replace("*", ""), type.count("*") + (0 if name is None or array is not None else name.count("["))

    if " " in type:
        type = " ".join([i for i in type.split(" ") if i and i not in ["const", "struct", "union", "enum", "SDLCALL"]])

    if type in (sdlTypes := {
        "Sint8": "ctypes.c_int8", "Uint8": "ctypes.c_uint8", "Sint16": "ctypes.c_int16", "Uint16": "ctypes.c_uint16",
        "Sint32": "ctypes.c_int32", "Uint32": "ctypes.c_uint32", "Sint64": "ctypes.c_int64", "Uint64": "ctypes.c_uint64"
    }): type = sdlTypes[type]

    if count and type in ["void", "char", "wchar_t"]:
        type, count = f"ctypes.c_{type.replace('_t', '')}_p", count - 1

    if type in (cTypes := {
        "int": "ctypes.c_int", "bool": "ctypes.c_bool", "float": "ctypes.c_float", "double": "ctypes.c_double",
        "char": "ctypes.c_char", "short": "ctypes.c_short", "long long": "ctypes.c_longlong", "long": "ctypes.c_long",
        "size_t": "ctypes.c_size_t", "ssize_t": "ctypes.c_ssize_t", "intptr_t": "ctypes.c_intptr_t", "uintptr_t": "ctypes.c_uintptr_t",
        "int8_t": "ctypes.c_int8", "uint8_t": "ctypes.c_uint8", "int16_t": "ctypes.c_int16", "uint16_t": "ctypes.c_uint16",
        "int32_t": "ctypes.c_int32", "uint32_t": "ctypes.c_uint32", "int64_t": "ctypes.c_int64", "uint64_t": "ctypes.c_uint64",
        "unsigned short": "ctypes.c_ushort", "unsigned long long": "ctypes.c_ulonglong", "unsigned long": "ctypes.c_ulong",
        "unsigned char": "ctypes.c_ubyte", "unsigned int": "ctypes.c_uint", "wchar_t": "ctypes.c_wchar", "va_list": "SDL_VA_LIST"
    }): type = cTypes[type]

    if not count and type in ["void"]: type = "None"
    if count and type.startswith("ctypes."): type = type.split(".")[1]
    return f"{'LP_' * count}{type}{'_Array_%s' % array if array else ''}"

def SDL_GENERATE_DOCS(modules: list[str] = SDL_MODULES, raw: types.ModuleType | None = None, rst: bool = False) -> str:
    """Generate type hints and docstring for SDL3 functions/structures using SDL3 wiki."""

    __index, (descriptions, arguments, returns) = -1, \
        asyncio.run(SDL_GET_FUNC_DESCRIPTIONS([(module, func) for module in modules for func in __module__.functions[module]], rst))

    for module in modules:
        for func in __module__.functions[module]:
            if (_ := __module__.functions[module][func]).__name__ == "__inner__": _ = _.func
            _.__doc__ = (descriptions[__index := __index + 1], arguments[__index], returns[__index])

    structs = False
    result = "" if rst else "\"\"\"\n# This file is auto-generated, do not modify it.\n__meta__ = "
    if not rst: result += f"{{\"target\": \"v{__version__}\", \"system\": \"{SDL_SYSTEM}\"}}\n\"\"\"\n\n"
    result += f"from {'sdl3' if rst else ''}.SDL import * # type: ignore\n"
    result += f"from {'sdl3' if rst else '.'} import {'' if rst else 'raw, '}SDL_POINTER"
    result += "\n\n" if rst or not structs else f", \\\n{' ' * 4}SDL_CLONE_METACLASS as SDL_CloneMeta\n\n"
    result += "import ctypes, typing\n\n"
    types, definitions = set(), ""

    def SDL_GET_FULL_NAME(type: type | None) -> str:
        if type is None: return "None"
        if type.__name__.startswith("LP_"): types.add(type.__name__)
        if type.__name__.startswith("c_"): return f"ctypes.{type.__name__}"
        else: return type.__name__

    if not rst and raw is not None and structs:
        structs = [(module, name) for name in dir(raw) if hasattr(getattr(raw, name), "_fields_") and not name.startswith("_") \
            and "_" in name and name not in ["SDL_GamepadBinding", "SDL_TLSID"] and (module := SDL_GET_MODULE_BY_NAME(name))]

        for (module, name), description, members in zip(structs, *asyncio.run(SDL_GET_STRUCT_DESCRIPTIONS(structs))):
            if not description or not members:
                continue

            if len(members) != len(_fields_ := getattr(raw, name)._fields_):
                SDL_LOGGER.Log(SDL_LOGGER.Error, f"Member count mismatch for https://wiki.libsdl.org/{module}/{name} (expected: {len(members)}, got: {len(_fields_)}).")

            for field, member in zip(_fields_, members):
                if field[0] != (_ := member.split("[")[0] if "[" in member else member):
                    SDL_LOGGER.Log(SDL_LOGGER.Error, f"Member name mismatch for https://wiki.libsdl.org/{module}/{name} (expected: {_}, got: {field[0]}).")

                if isinstance(members[member], dict):
                    if (left := SDL_GET_FULL_NAME(field[1]._restype_)) != (right := SDL_PYTHONIZE_TYPE(members[member]["return"], globals = raw.__dict__)):
                        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Member return type mismatch for https://wiki.libsdl.org/{module}/{name} (member: {_}, expected: {right}, got: {left}).")

                    for left, (_name, right) in zip(field[1]._argtypes_, members[member]["arguments"].items()):
                        if (_left := SDL_GET_FULL_NAME(left)) != (_right := SDL_PYTHONIZE_TYPE(right, _name, globals = raw.__dict__)):
                            SDL_LOGGER.Log(SDL_LOGGER.Error, f"Member argument type mismatch for https://wiki.libsdl.org/{module}/{name} (member: {_}, argument: {_name}, expected: {_right}, got: {_left}).")

                else:
                    if (left := SDL_GET_FULL_NAME(field[1])) != (right := SDL_PYTHONIZE_TYPE(members[member], member, globals = raw.__dict__)):
                        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Member type mismatch for https://wiki.libsdl.org/{module}/{name} (member: {member}, expected: {right}, got: {left}).")

            result += f"class {name}(metaclass = SDL_CloneMeta):\n{' ' * 4}\"\"\"{description}{'' if description.endswith('.') else '.'}\"\"\"\n\n"
            # result += f"{' ' * 4}def __init__({', '.join(["self"] + [f'{_[0]}: {SDL_GET_FULL_NAME(_[1])}' for _ in _fields_])}) -> None:\n"
            # result += f"{' ' * 8}super({name}, self).__init__()\n\n{' ' * 8}{', '.join([f'self.{_[0]}' for _ in _fields_])} = {', '.join([_[0] for _ in _fields_])}\n\n"

    for index, module in enumerate(modules):
        if len(__module__.functions[module]) == 0: continue
        if not rst: definitions += f"# {SDL_BINARY_PATTERNS[SDL_SYSTEM][0].format(module)} implementation.\n\n"

        for _index, func in enumerate(__module__.functions[module]):
            if (_ := __module__.functions[module][func]).__name__ == "__inner__": _ = _.func
            vararg, restype, argtypes, (description, arguments, _return) = _.vararg, _.restype, _.argtypes, _.__doc__

            if arguments is not None and len(arguments) != len(argtypes):
                SDL_LOGGER.Log(SDL_LOGGER.Error, f"Argument count mismatch for 'https://wiki.libsdl.org/{module}/{func}' (expected: {len(arguments)}, got: {len(argtypes)}).")

            if arguments is None:
                arguments = [f"_{i}" for i in range(len(argtypes))]

            else:
                for __index, i in enumerate(arguments):
                    if (left := SDL_PYTHONIZE_TYPE(arguments[i], i)) != (right := SDL_GET_FULL_NAME(argtypes[__index])):
                        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Argument type mismatch for 'https://wiki.libsdl.org/{module}/{func}' (argument: {i}, expected: {left}, got: {right}).")

                arguments = [f"{'_' if i in keyword.kwlist else ''}{i.replace('[', '').replace(']', '')}" for i in arguments]

            if _return is not None and (left := SDL_PYTHONIZE_TYPE(_return)) != (right := SDL_GET_FULL_NAME(restype)):
                SDL_LOGGER.Log(SDL_LOGGER.Error, f"Return type mismatch for 'https://wiki.libsdl.org/{module}/{func}' (expected: {left}, got: {right}).")

            definitions += f"def {func}({', '.join([f'{arg}: {SDL_GET_FULL_NAME(type)}' for arg, type in zip(arguments, argtypes)] + (['*args: typing.Any'] if vararg else []))}) -> {SDL_GET_FULL_NAME(restype)}:\n"

            if not rst or description is not None: definitions += f"{' ' * 4}\"\"\"\n"
            if description is not None: definitions += f"    {description}\n"
            if not rst: definitions += f"\n{' ' * 4}https://wiki.libsdl.org/{module}/{func}\n"
            if not rst or description is not None: definitions += f"{' ' * 4}\"\"\""
            if not rst: definitions += f"\n{' ' * 4}return raw.{func}({', '.join(arguments + (['*args'] if vararg else []))})"
            if rst and description is None: definitions += f"\n{' ' * 4}..."

            if _index != len(__module__.functions[module]) - 1:
                definitions += "\n\n"

        if index != len(modules) - 1 and len(__module__.functions[modules[index + 1]]) != 0:
            definitions += "\n\n"

    for i in types:
        count, func = i.count("LP_"), i.replace("LP_", "")
        result += f"{i}: typing.TypeAlias = {'SDL_POINTER[' * count}{'ctypes.' if func.startswith('c_') else ''}{func}{']' * count}\n"

    return f"{result}\n{definitions}"

def SDL_GET_OR_GENERATE_DOCS(*args, **kwargs) -> bytes:
    """Get type hints and docstrings for SDL3 functions/structures from github or by generating them."""

    try:
        headers = {"Accept": "application/vnd.github+json"}

        if "SDL_GITHUB_TOKEN" in os.environ:
            headers["Authorization"] = f"Bearer {os.environ['SDL_GITHUB_TOKEN']}"

        for release in (_ := requests.get("https://api.github.com/repos/Aermoss/PySDL3/releases", headers = headers).json()):
            if isinstance(release, str):
                SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to get docs from github: {_[release]}")
                break

            if release["tag_name"] != f"v{__version__}":
                continue

            for asset in release["assets"]:
                if asset["name"] != f"{SDL_SYSTEM}-Docs.py":
                    continue

                with requests.get(asset["browser_download_url"], headers = headers, stream = True) as response:
                    if response.status_code != 200:
                        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to get docs from github, status: {response.status_code} ({response.reason}).")
                        break

                    return bytearray().join([chunk for chunk in response.iter_content(chunk_size = 8192) if chunk])

    except requests.RequestException as exc:
        SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to get docs from github: {exc}.")

    SDL_LOGGER.Log(SDL_LOGGER.Warning, "Generating docs... this may take a while.")
    return SDL_GENERATE_DOCS(*args, **kwargs).encode("utf-8")

if not __initialized__ and int(os.environ.get("SDL_CTYPES_ALIAS_FIX", "0" if __frozen__ or __release__ else "1")) > 0:
    for i in dir(ctypes):
        if i.startswith("c_") and getattr(ctypes, i).__name__ != i and hasattr(getattr(ctypes, i), "_type_"):
            setattr(ctypes, i, SDL_TYPE[i, getattr(ctypes, i)])

from sdl3.SDL import * # type: ignore

if __doc_generator__:
    import sdl3.SDL as raw # type: ignore

    class SDL_CLONE_METACLASS(type):
        """Simple clone metaclass."""

        def __new__(cls, name: str, _: typing.Any, attributes: dict[str, typing.Any]) -> typing.Any:
            _class = getattr(raw, name)

            for key, value in attributes.items():
                if key in ["__init__"]:
                    setattr(_class, key, value)

            return _class

SDL_VERSIONNUM_STRING: abc.Callable[[int], str] = lambda num: str(None).lower() if not num else \
    f"{SDL_VERSIONNUM_MAJOR(num)}.{SDL_VERSIONNUM_MINOR(num)}.{SDL_VERSIONNUM_MICRO(num)}"

if not __initialized__:
    if int(os.environ.get("SDL_CHECK_BINARY_VERSION", "1")) > 0:
        for module, left, right in zip(SDL_MODULES, [SDL_GetVersion, IMG_Version, MIX_Version, TTF_Version, RTF_Version, NET_Version], [SDL_VERSION, SDL_IMAGE_VERSION, SDL_MIXER_VERSION, SDL_TTF_VERSION, SDL_RTF_VERSION, SDL_NET_VERSION]):
            if module in __module__.binaryMap and (_ := left()) != right: SDL_LOGGER.Log(SDL_LOGGER.Warning, f"Version mismatch with binary: '{SDL_BINARY_PATTERNS[SDL_SYSTEM][0].format(module)}' (expected: {SDL_VERSIONNUM_STRING(right)}, got: {SDL_VERSIONNUM_STRING(_)}).")

    def SDL_TRY_WRITE_DOCS() -> bool | None:
        try:
            with open(__doc_file__, "wb") as file:
                file.write(SDL_GET_OR_GENERATE_DOCS(raw = raw))

            return True

        except OSError as exc:
            SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to write docs: {exc}.")

    if __doc_generator__ and (os.path.exists(__doc_file__) or SDL_TRY_WRITE_DOCS()):
        try:
            if "sdl3.__doc__" in sys.modules: del sys.modules["sdl3.__doc__"]
            from .__doc__ import * # type: ignore
            exec(getattr(sys.modules["sdl3.__doc__"], "__doc__"), data := {})

        except (SyntaxError, NameError, TypeError) as exc:
            import traceback
            traceback.print_exc()
            SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to read docs: {exc}.")
            data = None

        if os.path.exists(__doc_file__) and (not data or "__meta__" not in data or data["__meta__"]["target"] != f"v{__version__}" or data["__meta__"]["system"] != SDL_SYSTEM) and SDL_TRY_WRITE_DOCS():
            if "sdl3.__doc__" in sys.modules: del sys.modules["sdl3.__doc__"]
            SDL_LOGGER.Log(SDL_LOGGER.Warning, "Reloading module: 'sdl3.__doc__'...")
            from .__doc__ import * # type: ignore

    else:
        try:
            if not (__frozen__ or __release__):
                if os.path.exists(__doc_file__):
                    os.remove(__doc_file__)

        except PermissionError as exc:
            SDL_LOGGER.Log(SDL_LOGGER.Error, f"Failed to remove docs: {exc}.")
