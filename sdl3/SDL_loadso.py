from .__init__ import ctypes, SDL_POINTER, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_stdinc import SDL_FunctionPointer

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_SharedObject(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_LoadObject", SDL_POINTER[SDL_SharedObject], ctypes.c_char_p)
SDL_FUNC("SDL_LoadFunction", SDL_FunctionPointer, SDL_POINTER[SDL_SharedObject], ctypes.c_char_p)
SDL_FUNC("SDL_UnloadObject", None, SDL_POINTER[SDL_SharedObject])