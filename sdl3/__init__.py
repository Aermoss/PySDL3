import ctypes, sys, os

BINARY_PATH = os.path.join(os.path.dirname(__file__), "bin")
SDL_DLL = ctypes.CDLL(os.path.join(BINARY_PATH, "SDL3.dll"))

def SDL_FUNC(name, restype, *args):
    func = getattr(SDL_DLL, name)
    func.restype, func.argtypes = restype, args
    setattr(sys.modules[__name__.split(".")[0]], name, func)

from .SDL import *