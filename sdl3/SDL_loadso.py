from .__init__ import ctypes, SDL_FUNC

from .SDL_stdinc import SDL_FunctionPointer

SDL_FUNC("SDL_LoadObject", ctypes.c_void_p, ctypes.c_char_p)
SDL_FUNC("SDL_LoadFunction", SDL_FunctionPointer, ctypes.c_void_p, ctypes.c_char_p)
SDL_FUNC("SDL_UnloadObject", None, ctypes.c_void_p)