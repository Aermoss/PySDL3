"""A pure Python wrapper for SDL3."""

__version__ = "0.7.0a0"

import sys, os, requests, ctypes, platform, inspect, array

if "PYSDL3_DISABLE_CHECK_VERSION" not in os.environ:
    os.environ["PYSDL3_DISABLE_CHECK_VERSION"] = "0"

SDL_DLL, SDL_IMAGE_DLL, SDL_MIXER_DLL, SDL_NET_DLL, SDL_RTF_DLL, SDL_TTF_DLL = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_net", "SDL3_rtf", "SDL3_ttf"

SDL_DLL_VAR_MAP = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_DLL"):
        SDL_DLL_VAR_MAP[i] = locals()[i]

SDL_DLL_VAR_MAP_INV = {v: k for k, v in SDL_DLL_VAR_MAP.items()}

if "PYSDL3_DISABLE_DOCS" not in os.environ:
    os.environ["PYSDL3_DISABLE_DOCS"] = "0"

__disable_docs__ = 0 < int(os.environ.get("PYSDL3_DISABLE_DOCS"))
__disable_check_version__ = 0 < int(os.environ.get("PYSDL3_DISABLE_CHECK_VERSION"))
__docs_file__ = os.path.join(os.path.dirname(__file__), "__docs__.py")

__initialized__ = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__ = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]
__loader__ = ctypes.CDLL if sys.platform not in ["win32"] else ctypes.WinDLL
__binary_folder__ = "windows-x86_64" if sys.platform in ["win32"] \
    else ("linux-aarch64" if platform.machine() in ["aarch64"] else "linux-x86_64")

def SDL_SET_TEXT_ATTR(color):
    if sys.platform in ["win32"]:
        console_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(console_handle, color)

    else:
        if color == 7:
            print("\u001b[0m", end = "", flush = True)

        elif color == 13:
            print("\u001b[31;1m", end = "", flush = True)

        elif color == 12:
            print("\u001b[31m", end = "", flush = True)

        else:
            ...

if not __initialized__:
    if not __disable_check_version__:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if __version__ != version:
                SDL_SET_TEXT_ATTR(13)
                print(f"you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).")
                SDL_SET_TEXT_ATTR(7)
                
        except:
            ...

    functions, dllMap, dll = {}, {}, None
    binaryPath = os.path.join(os.path.dirname(__file__), "bin")

    for key, value in SDL_DLL_VAR_MAP.items():
        if __binary_folder__ in ["linux-aarch64"] and key in [SDL_TTF_DLL, SDL_RTF_DLL]:
            continue

        dllMap[value], functions[value] = \
            __loader__(os.path.join(binaryPath, __binary_folder__, ("{}.dll" if sys.platform in ["win32"] else "lib{}.so").format(value))), {}

else:
    functions, dllMap, dll, binaryPath = \
        __module__.functions, __module__.dllMap, __module__.dll, __module__.binaryPath

def SDL_DEREFERENCE(value):
    if isinstance(value, ctypes._Pointer):
        return value.contents
    
    elif hasattr(value, "_obj"):
        return value._obj
    
    else:
        return value

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
    return {v: k for k, v in dllMap.items()}[dll]
        
def SDL_GET_DLL(name):
    return dllMap[name]

def SDL_SET_CURRENT_DLL(name):
    __module__.dll = SDL_GET_DLL(name)
    
def SDL_GET_CURRENT_DLL():
    return __module__.dll

def SDL_GET_FUNCTION_DLL(name):
    return __module__.functions[name].__dll__

def SDL_FUNC(name, retType, *args):
    dll = SDL_GET_CURRENT_DLL(); func = getattr(dll, name)
    func.__dll__, func.restype, func.argtypes = dll, retType, args
    if __disable_docs__: setattr(__module__, name, func)
    __module__.functions[SDL_GET_DLL_NAME(dll)][name] = func

from .SDL import *

if not __initialized__ and not __disable_docs__:
    result = "from .SDL import *\n\n"
    result += f"from .__init__ import ctypes, SDL_GET_DLL, \\\n"
    result += f"    {', '.join(list(SDL_DLL_VAR_MAP.keys()))}\n\n"
    types, definitions = set(), ""

    def getName(i):
        if i is None: return "None"
        if "CFunctionType" in i.__name__:
            return "ctypes._Pointer"

        if "LP_" in i.__name__ or not i.__name__.startswith("c_"):
            if "LP_" in i.__name__:
                types.add(i.__name__)

            return i.__name__
        
        else:
            return f"ctypes.{i.__name__}"

    for index, dll in enumerate(__module__.functions):
        if len(__module__.functions[dll]) == 0: continue
        definitions += f"# {dll}.dll implementation.\n\n"

        for _index, name in enumerate(__module__.functions[dll]):
            retType, args = \
                __module__.functions[dll][name].restype, __module__.functions[dll][name].argtypes

            definitions += f"def {name}({', '.join([f'_{index}: {getName(i)}' for index, i in enumerate(args)])}) -> {getName(retType)}:\n"
            definitions += f"    \"\"\"This function is auto-generated.\"\"\"\n"
            definitions += f"    return SDL_GET_DLL({SDL_DLL_VAR_MAP_INV[dll]}).{name}({', '.join([f'_{index}' for index, i in enumerate(args)])})"

            if _index != len(__module__.functions[dll]) - 1:
                definitions += "\n\n"

        if index != len(__module__.functions) - 1 and len(list(__module__.functions.values())[index + 1]) != 0:
            definitions += "\n\n"

    for i in types:
        count, name = i.count("LP_"), i.replace("LP_", "")
        result += f"class {i}({'ctypes.POINTER(' * count}{'ctypes.' if name.startswith('c_') else ''}{name}{')' * count}):\n"
        result += f"    \"\"\"This class is auto-generated.\"\"\"\n\n"

    with open(__docs_file__, "w") as file:
        file.write(result + definitions)

    from .__docs__ import *

else:
    if os.path.exists(__docs_file__):
        os.remove(__docs_file__)