"""A pure Python wrapper for SDL3."""

__version__ = "0.8.1b0"

import sys, os, requests, ctypes, platform, asyncio, aiohttp, re, inspect, array, atexit

SDL_DLL, SDL_IMAGE_DLL, SDL_MIXER_DLL, SDL_NET_DLL, SDL_RTF_DLL, SDL_TTF_DLL = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_net", "SDL3_rtf", "SDL3_ttf"

SDL_DLL_VAR_MAP = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_DLL"):
        SDL_DLL_VAR_MAP[i] = locals()[i]

SDL_DLL_VAR_MAP_INV = {value: key for key, value in SDL_DLL_VAR_MAP.items()}

__doc_file__ = os.path.join(os.path.dirname(__file__), "__doc__.py")
__doc_generator__ = int(os.environ.get("PYSDL3_DOC_GENERATOR", "1")) > 0

__initialized__ = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__ = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

def SDL_SET_TEXT_ATTR(color):
    if sys.platform in ["win32"]:
        console_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(console_handle, color)

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
    if int(os.environ.get("PYSDL3_VERSION_CHECK", "1")) > 0:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if __version__ != version:
                SDL_SET_TEXT_ATTR(13)
                print(f"you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).", flush = True)
                SDL_SET_TEXT_ATTR(7)

        except:
            ...

    functions, instances, dllMap, dll = {}, {}, {}, None
    binaryPath = os.path.join(os.path.dirname(__file__), "bin", f"{platform.system().lower()}-{platform.machine().lower().replace('x86_64', 'amd64').replace('aarch64', 'arm64')}")

    for key, value in SDL_DLL_VAR_MAP.items():
        functions[value], dllMap[value] = {}, (ctypes.WinDLL if "win32" in sys.platform else ctypes.CDLL) \
            (os.path.join(binaryPath, ("{}.dll" if "win32" in sys.platform else "lib{}.so").format(value)))

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
def SDL_GET_DLL_NAME(dll):
    return {v: k for k, v in __module__.dllMap.items()}[dll]

def SDL_GET_DLL(name):
    return __module__.dllMap[name]

def SDL_SET_CURRENT_DLL(name):
    __module__.dll = SDL_GET_DLL(name)

def SDL_GET_CURRENT_DLL():
    return __module__.dll

def SDL_GET_FUNCTION_DLL(name):
    return __module__.functions[name].__dll__

def SDL_FUNC(name, retType, *args):
    func = getattr(dll := SDL_GET_CURRENT_DLL(), name)
    func.__dll__, func.restype, func.argtypes = dll, retType, args
    if not __doc_generator__: setattr(__module__, name, func)
    __module__.functions[SDL_GET_DLL_NAME(dll)][name] = func

async def SDL_GET_DESCRIPTIONS(urls):
    session, tasks = aiohttp.ClientSession(), []

    for url in urls:
        print(f"sending a request to \"{url}\".\n", end = "", flush = True)
        tasks.append(asyncio.create_task(session.get(url, ssl = False)))
    
    responses = await asyncio.gather(*tasks)
    print(f"response gathering completed ({len(responses)} response(s)).\n", end = "", flush = True)
    descriptions = []

    for response in responses:
        if response.status != 200:
            print(f"failed to get description of \"{response.url}\", skipping (status: {response.status}).\n", end = "", flush = True)
            descriptions.append(None)

        else:
            content = (await response.content.read()).decode()

            for a, b in zip(list(re.finditer(r"<p>", content)), list(re.finditer(r"</p>", content))):
                if content[a.end()] == "<": continue
                description = re.sub(r"<a href=\"([a-zA-Z0-9_]+)\">([a-zA-Z0-9_]+)</a>", rf"[\2]({'/'.join(str(response.url).split('/')[:-1])}/\1)", content[a.end():b.start()])
                descriptions.append(description.replace("<em>", "").replace("</em>", "").replace("<code>", "`").replace("</code>", "`").replace("<strong>", "").replace("</strong>", ""))
                break

        response.close()

    await session.close()
    return descriptions

def SDL_GENERATE_DOCS():
    __index, descriptions = -1, \
        asyncio.run(SDL_GET_DESCRIPTIONS([f"https://wiki.libsdl.org/{module}/{name}" for module in __module__.functions for name in __module__.functions[module]]))

    for module in __module__.functions:
        for name in __module__.functions[module]:
            __module__.functions[module][name].__doc__ = descriptions[__index := __index + 1]

    result = "\"\"\"This file is auto-generated.\"\"\"\n\n"
    result += "from .SDL import *\n\n"
    result += f"from .__init__ import ctypes, SDL_GET_DLL, \\\n"
    result += f"    {', '.join(list(SDL_DLL_VAR_MAP.keys()))}\n\n"
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
        definitions += f"# {module}.dll implementation.\n\n"

        for _index, name in enumerate(__module__.functions[module]):
            retType, args = \
                __module__.functions[module][name].restype, __module__.functions[module][name].argtypes

            definitions += f"def {name}({', '.join([f'_{index}: {SDL_GET_NAME(i)}' for index, i in enumerate(args)])}) -> {SDL_GET_NAME(retType)}:\n"
            definitions += f"    \"\"\"\n"

            if __module__.functions[module][name].__doc__ is not None and "no such page" not in __module__.functions[module][name].__doc__.lower():
                definitions += f"    {__module__.functions[module][name].__doc__}\n"

            definitions += f"    https://wiki.libsdl.org/{module}/{name}\n"
            definitions += f"    \"\"\"\n"
            definitions += f"    return SDL_GET_DLL({SDL_DLL_VAR_MAP_INV[module]}).{name}({', '.join([f'_{index}' for index, i in enumerate(args)])})"

            if _index != len(__module__.functions[module]) - 1:
                definitions += "\n\n"

        if index != len(__module__.functions) - 1 and len(list(__module__.functions.values())[index + 1]) != 0:
            definitions += "\n\n"

    for i in types:
        count, name = i.count("LP_"), i.replace("LP_", "")
        result += f"class {i}({'ctypes.POINTER(' * count}{'ctypes.' if name.startswith('c_') else ''}{name}{')' * count}):\n"
        result += f"    ...\n\n"

    return result + definitions

from .SDL import *

if not __initialized__:
    if __doc_generator__:
        if not os.path.exists(__doc_file__):
            with open(__doc_file__, "w") as file:
                file.write(SDL_GENERATE_DOCS())

        from .__doc__ import *

    else:
        if os.path.exists(__doc_file__):
            os.remove(__doc_file__)