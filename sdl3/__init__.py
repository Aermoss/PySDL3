import sys, os, ctypes, _ctypes

if "PYSDL3_DISABLE_DOCS" not in os.environ:
    os.environ["PYSDL3_DISABLE_DOCS"] = "0"

__disable_docs__ = 0 < int(os.environ.get("PYSDL3_DISABLE_DOCS"))
__docs_file__ = os.path.join(os.path.dirname(__file__), "__docs__.py")

__initialized__ = __name__.split(".")[0] in sys.modules if "." in __name__ else False
__module__ = sys.modules[__name__.split(".")[0] if "." in __name__ else __name__]

if not __initialized__:
    binaryPath = os.path.join(os.path.dirname(__file__), "bin")
    dll = ctypes.windll.LoadLibrary(os.path.join(binaryPath, "SDL3.dll"))
    functions = {}

else:
    binaryPath, dll, functions = \
        __module__.binaryPath, __module__.dll, __module__.functions

def SDL_FUNC(name, retType, *args):
    func = getattr(__module__.dll, name)
    func.restype, func.argtypes = retType, args
    if __disable_docs__: setattr(__module__, name, func)
    __module__.functions[name] = func

from .SDL import *

if not __initialized__ and not __disable_docs__:
    with open(__docs_file__, "w") as file:
        result = "from .SDL import *\n\n"
        result += "from .__init__ import ctypes, dll\n\n"
        definitions, types = "", set()

        for index, name in enumerate(functions.keys()):
            retType, args = functions[name].restype, functions[name].argtypes

            def getName(i):
                if i is None: return "None"
                name = i.__name__.replace("CFunctionType", "_CFuncPtr")
                if "SDL_" in name or "LP_" in name: types.add(name); return name
                else: return f"ctypes.{name}"

            definitions += f"def {name}({", ".join([f"_{index}: {getName(i)}" for index, i in enumerate(args)])}) -> {getName(retType)}:\n"
            definitions += f"    \"\"\"This function is auto-generated.\"\"\"\n"
            definitions += f"    return dll.{name}({", ".join([f"_{index}" for index, i in enumerate(args)])})"

            if index != len(functions.keys()) - 1:
                definitions += "\n\n"

        for i in types:
            result += f"class {i}(ctypes._Pointer):\n"
            result += "    \"\"\"This class is auto-generated.\"\"\"\n\n"

        file.write(result + definitions)

    from .__docs__ import *

else:
    if os.path.exists(__docs_file__):
        os.remove(__docs_file__)