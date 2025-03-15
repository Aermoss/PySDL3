from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_video import SDL_Window

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MetalView: typing.TypeAlias = SDL_TYPE["SDL_MetalView", ctypes.c_void_p]

SDL_Metal_CreateView: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_Metal_CreateView", SDL_MetalView, [SDL_POINTER[SDL_Window]]]
SDL_Metal_DestroyView: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_Metal_DestroyView", None, [SDL_MetalView]]
SDL_Metal_GetLayer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_Metal_GetLayer", ctypes.c_void_p, [SDL_MetalView]]