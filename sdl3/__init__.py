"""A pure Python wrapper for SDL3."""

__version__ = "0.7.0a3"

import sys, os, requests, ctypes, platform, atexit, inspect, array

SDL_DLL, SDL_IMAGE_DLL, SDL_MIXER_DLL, SDL_NET_DLL, SDL_RTF_DLL, SDL_TTF_DLL = \
    "SDL3", "SDL3_image", "SDL3_mixer", "SDL3_net", "SDL3_rtf", "SDL3_ttf"

SDL_DLL_VAR_MAP = {}

for i in locals().copy():
    if i.startswith("SDL_") and i.endswith("_DLL"):
        SDL_DLL_VAR_MAP[i] = locals()[i]

SDL_DLL_VAR_MAP_INV = {v: k for k, v in SDL_DLL_VAR_MAP.items()}

for key in ["PYSDL3_DISABLE_DOCS", "PYSDL3_DISABLE_CHECK_VERSION", "PYSDL3_ENABLE_INSTANCE_TRACKING", "PYSDL3_ENABLE_FORCE_CLOSE"]:
    if key not in os.environ:
        os.environ[key] = "0"

__docs__ = not 0 < int(os.environ.get("PYSDL3_DISABLE_DOCS"))
__check_version__ = not 0 < int(os.environ.get("PYSDL3_DISABLE_CHECK_VERSION"))
__instance_tracking__ = 0 < int(os.environ.get("PYSDL3_ENABLE_INSTANCE_TRACKING"))
__force_close__ = 0 < int(os.environ.get("PYSDL3_ENABLE_FORCE_CLOSE"))
__docs_file__ = os.path.join(os.path.dirname(__file__), "__docs__.py")

if __force_close__:
    def SDL_EXIT(code):
        atexit._run_exitfuncs()
        os._exit(code)

    sys.exit = SDL_EXIT

__initialized__ = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__ = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]
__loader__ = ctypes.CDLL if sys.platform not in ["win32"] else ctypes.WinDLL
__platform__ = "windows-x86_64" if sys.platform in ["win32"] \
    else ("linux-aarch64" if platform.machine() in ["aarch64"] else "linux-x86_64")

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
    if __check_version__:
        try:
            version = requests.get(f"https://pypi.org/pypi/PySDL3/json", timeout = 0.5).json()["info"]["version"]

            if __version__ != version:
                SDL_SET_TEXT_ATTR(13)
                print(f"you are using an older version of pysdl3 (current: {__version__}, lastest: {version}).", flush = True)
                SDL_SET_TEXT_ATTR(7)
                
        except:
            ...

    functions, instances, dllMap, dll = {}, {}, {}, None
    binaryPath = os.path.join(os.path.dirname(__file__), "bin")

    for key, value in SDL_DLL_VAR_MAP.items():
        if __platform__ in ["linux-aarch64"] and key in [SDL_TTF_DLL, SDL_RTF_DLL]:
            continue

        dllMap[value], functions[value] = \
            __loader__(os.path.join(binaryPath, __platform__, ("{}.dll" if sys.platform in ["win32"] else "lib{}.so").format(value))), {}

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
    dll = SDL_GET_CURRENT_DLL(); func = getattr(dll, name)
    func.__dll__, func.restype, func.argtypes = dll, retType, args
    if not __docs__: setattr(__module__, name, func)
    __module__.functions[SDL_GET_DLL_NAME(dll)][name] = func

if __instance_tracking__:
    if not __initialized__ and not __docs__:
        SDL_SET_TEXT_ATTR(13)
        print("instance tracker needs type hint generation system to work.", flush = True)
        SDL_SET_TEXT_ATTR(7)

    @atexit.register
    def SDL_CHECK_INSTANCES():
        if __module__.instances is not None:

            for i in __module__.instances:
                if len(__module__.instances[i]) != 0:
                    SDL_SET_TEXT_ATTR(13)

                    print(len(__module__.instances[i]), f"instance{'s' if len(__module__.instances[i]) > 1 else ''} of", i, \
                        f"{'are' if len(__module__.instances[i]) > 1 else 'is'} not destroyed.", flush = True)
                    
                    SDL_SET_TEXT_ATTR(7)

            __module__.instances = None

    def SDL_INSTANCE_TRACKER_REGISTER(name, func, *args):
        if name not in __module__.instances:
            __module__.instances[name] = []

        value = func(*args)

        if isinstance(value, ctypes._Pointer):
            __module__.instances[name].append(value)

        return value

    def SDL_INSTANCE_TRACKER_UNREGISTER(name, func, *args):
        value = func(*args)

        if name in __module__.instances:
            if len(args) != 0 and isinstance(args[0], ctypes._Pointer) and args[0] in __module__.instances[name]:
                __module__.instances[name].remove(args[0])

        return value

from .SDL import *

if not __initialized__ and __docs__:
    result = "from .SDL import *\n\n"
    result += f"from .__init__ import ctypes, SDL_GET_DLL, {'SDL_INSTANCE_TRACKER_REGISTER, SDL_INSTANCE_TRACKER_UNREGISTER, ' if __instance_tracking__ else ''}\\\n"
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
            
            createState, destroyState, renderState, freeState, closeState, loadState, openState = \
                "Create" in name, "Destroy" in name, "Render" in name and "Renderer" not in name, "Free" in name, "Close" in name, "Load" in name, "Open" in name and "Show" not in name
            
            if renderState and retType:
                if "Surface" not in retType.__name__:
                    renderState = False
            
            definitions += f"def {name}({', '.join([f'_{index}: {getName(i)}' for index, i in enumerate(args)])}) -> {getName(retType)}:\n"
            definitions += f"    \"\"\"This function is auto-generated.\"\"\"\n"

            if (createState or destroyState or renderState or freeState or closeState or loadState or openState) and __instance_tracking__:
                keyword = {createState: "Create", destroyState: "Destroy", renderState: "Render", freeState: "Free", closeState: "Close", loadState: "Load", openState: "Open"}[True]
                _name = name[name.find(keyword) + len(keyword):]

                for i in ["With", "From"]:
                    if i in _name:
                        _name = _name[:_name.find(i)]

                if "_" in _name:
                    _name = _name.split("_")[0]

                if (renderState or loadState or openState) and retType:
                    if retType.__name__.startswith("LP_"):
                        _name = retType.__name__.split("_")[-1]
                    
                definitions += f"    return {'SDL_INSTANCE_TRACKER_REGISTER' if (createState or renderState or loadState or openState) else 'SDL_INSTANCE_TRACKER_UNREGISTER'}" \
                    + f"(\"{_name}\", SDL_GET_DLL({SDL_DLL_VAR_MAP_INV[dll]}).{name}, {', '.join([f'_{index}' for index, i in enumerate(args)])})"

            else:
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