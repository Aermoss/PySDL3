from .__init__ import ctypes, typing, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_video import SDL_Window

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MetalView: typing.TypeAlias = SDL_TYPE["SDL_MetalView", ctypes.c_void_p]

SDL_FUNC("SDL_Metal_CreateView", SDL_MetalView, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_Metal_DestroyView", None, SDL_MetalView)
SDL_FUNC("SDL_Metal_GetLayer", ctypes.c_void_p, SDL_MetalView)