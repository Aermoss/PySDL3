import ctypes, sys, os

binaryPath = os.path.join(os.path.dirname(__file__), "bin")
dll = ctypes.windll.LoadLibrary(os.path.join(binaryPath, "SDL3.dll"))

def SDL_FUNC(name, restype, *args):
    func = getattr(dll, name)
    func.restype, func.argtypes = restype, args
    setattr(sys.modules[__name__.split(".")[0]], name, func)

from .SDL import *