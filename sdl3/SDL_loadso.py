from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_stdinc import SDL_FunctionPointer

SDL_SET_CURRENT_DLL(SDL_DLL)

class SDL_SharedObject(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_LoadObject", ctypes.POINTER(SDL_SharedObject), ctypes.c_char_p)
SDL_FUNC("SDL_LoadFunction", SDL_FunctionPointer, ctypes.POINTER(SDL_SharedObject), ctypes.c_char_p)
SDL_FUNC("SDL_UnloadObject", None, ctypes.POINTER(SDL_SharedObject))