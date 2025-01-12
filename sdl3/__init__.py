"""A pure Python wrapper for SDL3."""

__version__ = "0.9.0b2"

import sys, os, requests, ctypes, platform, keyword, inspect, \
    asyncio, aiohttp, re, typing, array, atexit, packaging.version

SDL_BINARY, SDL_IMAGE_BINARY, SDL_MIXER_BINARY, SDL_NET_BINARY, SDL_RTF_BINARY, SDL_TTF_BINARY = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_net", "SDL3_rtf", "SDL3_ttf"

SDL_BINARY_VAR_MAP = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_BINARY"):
        SDL_BINARY_VAR_MAP[i] = locals()[i]

SDL_BINARY_VAR_MAP_INV = {value: key for key, value in SDL_BINARY_VAR_MAP.items()}
SDL_REPOSITORIES = {k.replace("3", ""): v for k, v in SDL_BINARY_VAR_MAP_INV.items()}

SDL_SYSTEM, SDL_ARCH = platform.system(), platform.machine().upper().replace("X86_64", "AMD64").replace("AARCH64", "ARM64")
SDL_BINARY_NAME_FORMAT = {"Darwin": "lib{}.dylib", "Linux": "lib{}.so", "Windows": "{}.dll"}

__doc_file__ = os.path.join(os.path.dirname(__file__), "__doc__.py")
__doc_generator__ = int(os.environ.get("SDL_DOC_GENERATOR", "1")) > 0

__initialized__ = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__ = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

def SDL_SET_TEXT_ATTR(color):
    if SDL_SYSTEM in ["Windows"]:
        consoleHandle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(consoleHandle, color)

    else:
        if color == 7:
            print("\u001b[39m", end = "", flush = True)

        elif color == 13:
            print("\u001b[35m", end = "", flush = True)

        elif color == 12:
            print("\u001b[31m", end = "", flush = True)

        else:
            ...

if not __initialized__:
    if int(os.environ.get("SDL_VERSION_CHECK", "1")) > 0:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if packaging.version.parse(__version__) < packaging.version.parse(version):
                SDL_SET_TEXT_ATTR(13)
                print(f"you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).", flush = True)
                SDL_SET_TEXT_ATTR(7)

        except:
            ...

    functions, instances, binaryMap, binary = {}, {}, {}, None
    binaryPath = os.path.join(os.path.dirname(__file__), "bin", f"{SDL_SYSTEM.lower()}-{SDL_ARCH.lower()}")

    for key, value in SDL_BINARY_VAR_MAP.items():
        functions[value], binaryMap[value] = {}, (ctypes.WinDLL if SDL_SYSTEM in ["Windows"] else ctypes.CDLL) \
            (os.path.join(binaryPath, SDL_BINARY_NAME_FORMAT[SDL_SYSTEM].format(value)))

def SDL_ARRAY(*args, **kwargs):
    return ((kwargs.get("type") or args[0].__class__) * len(args))(*args), len(args)

def SDL_DEREFERENCE(value):
    if isinstance(value, ctypes._Pointer): return value.contents
    elif hasattr(value, "_obj"): return value._obj
    else: return value

def SDL_FUNC_CACHE(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        else:
            cache[args] = func(*args)
            return cache[args]

    return wrapper

@SDL_FUNC_CACHE
def SDL_GET_BINARY_NAME(binary):
    return {v: k for k, v in __module__.binaryMap.items()}[binary]

def SDL_GET_BINARY(name):
    return __module__.binaryMap[name]

def SDL_SET_CURRENT_BINARY(name):
    __module__.binary = SDL_GET_BINARY(name)

def SDL_GET_CURRENT_BINARY():
    return __module__.binary

def SDL_GET_FUNCTION_BINARY(name):
    return __module__.functions[name].__binary__

def SDL_FUNC(name, retType, *args):
    func = getattr(binary := SDL_GET_CURRENT_BINARY(), name)
    func.__binary__, func.restype, func.argtypes = binary, retType, args
    if not __doc_generator__: setattr(__module__, name, func)
    __module__.functions[SDL_GET_BINARY_NAME(binary)][name] = func

async def SDL_GET_LATEST_RELEASES():
    session, releases, tasks = aiohttp.ClientSession(), {}, []

    for repo in SDL_REPOSITORIES:
        url = f"https://api.github.com/repos/libsdl-org/{repo}/releases"
        print(f"sending a request to \"{url}\".", flush = True)
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))

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

async def SDL_GET_FUNCTION_DOCS(urls):
    session, tasks = aiohttp.ClientSession(), []

    for url in urls:
        print(f"sending a request to \"{url}\".\n", end = "", flush = True)
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))
    
    responses = await asyncio.gather(*tasks)
    print(f"response gathering completed ({len(responses)} response(s)).\n", end = "", flush = True)
    descriptions, arguments = [], []

    for response, url in zip(responses, urls):
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

def SDL_GENERATE_DOCS():
    __index, (descriptions, arguments) = -1, \
        asyncio.run(SDL_GET_FUNCTION_DOCS([f"https://wiki.libsdl.org/{module}/{name}" for module in __module__.functions for name in __module__.functions[module]]))

    for module in __module__.functions:
        for name in __module__.functions[module]:
            __index = __index + 1
            __module__.functions[module][name].__doc__ = \
                (descriptions[__index], arguments[__index])

    result = "\"\"\"This file is auto-generated.\"\"\"\n\n"
    result += "from .SDL import *\n\n"
    result += f"from .__init__ import ctypes, typing, SDL_GET_BINARY, \\\n"
    result += f"    {', '.join(list(SDL_BINARY_VAR_MAP.keys()))}\n\n"
    types, definitions = set(), ""

    def SDL_GET_NAME(i):
        if i is None: return "None"
        if "CFunctionType" in i.__name__:
            return "ctypes._Pointer"

        if "LP_" in i.__name__ or not i.__name__.startswith("c_"):
            if "LP_" in i.__name__:
                types.add(i.__name__)

            return i.__name__
        
        else:
            return f"ctypes.{i.__name__}"

    for index, module in enumerate(__module__.functions):
        if len(__module__.functions[module]) == 0: continue
        definitions += f"# {SDL_BINARY_NAME_FORMAT[platform.system()].format(module)} implementation.\n\n"

        for _index, name in enumerate(__module__.functions[module]):
            retType, argtypes, (description, arguments) = \
                __module__.functions[module][name].restype, __module__.functions[module][name].argtypes, __module__.functions[module][name].__doc__

            assert arguments is None or (arguments is not None and len(arguments) == len(argtypes)), f"argument count mismatch for 'https://wiki.libsdl.org/{module}/{name}'."
            arguments = [f"{'_' if arguments is None or arguments[i] in keyword.kwlist else ''}{i if arguments is None else arguments[i]}" for i in range(len(argtypes))]
            definitions += f"def {name}({', '.join([f'{arg}: {SDL_GET_NAME(type)}' for arg, type in zip(arguments, argtypes)])}) -> {SDL_GET_NAME(retType)}:\n"
            definitions += f"    \"\"\"\n"
            if description is not None: definitions += f"    {description}\n"
            definitions += f"    https://wiki.libsdl.org/{module}/{name}\n"
            definitions += f"    \"\"\"\n"
            definitions += f"    return SDL_GET_BINARY({SDL_BINARY_VAR_MAP_INV[module]}).{name}({', '.join(arguments)})"

            if _index != len(__module__.functions[module]) - 1:
                definitions += "\n\n"

        if index != len(__module__.functions) - 1 and len(list(__module__.functions.values())[index + 1]) != 0:
            definitions += "\n\n"

    for i in types:
        count, name = i.count("LP_"), i.replace("LP_", "")
        result += f"{i}: typing.TypeAlias = {'ctypes.POINTER(' * count}{'ctypes.' if name.startswith('c_') else ''}{name}{')' * count} # type: ignore\n"

    return f"{result}\n{definitions}"

def SDL_GET_OR_GENERATE_DOCS():
    for release in requests.get(f"https://api.github.com/repos/Aermoss/PySDL3/releases").json():
        if release["tag_name"] != __version__:
            continue

        for asset in release["assets"]:
            if asset["name"] != f"{SDL_SYSTEM.lower()}-docs.py": continue
            print(asset)
            return requests.get(asset["browser_download_url"]).text

    return SDL_GENERATE_DOCS()

from .SDL import *

if not __initialized__:
    if __doc_generator__:
        if not os.path.exists(__doc_file__):
            with open(__doc_file__, "w") as file:
                file.write(SDL_GET_OR_GENERATE_DOCS())

        from .__doc__ import *

    else:
        if os.path.exists(__doc_file__):
            os.remove(__doc_file__)