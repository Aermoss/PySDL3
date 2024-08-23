from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_video import SDL_Window

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_MetalView = ctypes.c_void_p

SDL_FUNC("SDL_Metal_CreateView", SDL_MetalView, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_Metal_DestroyView", None, SDL_MetalView)
SDL_FUNC("SDL_Metal_GetLayer", ctypes.c_void_p, SDL_MetalView)