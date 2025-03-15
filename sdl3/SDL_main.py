from .__init__ import ctypes, typing, abc, SDL_PLATFORM_SPECIFIC, SDL_POINTER, \
    SDL_FUNC, SDL_FUNC_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_init import SDL_AppInit_func, \
    SDL_AppIterate_func, SDL_AppEvent_func, SDL_AppQuit_func

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_main_func: typing.TypeAlias = SDL_FUNC_TYPE["SDL_main_func", ctypes.c_int, [ctypes.c_int, SDL_POINTER[ctypes.c_char_p]]]

SDL_SetMainReady: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetMainReady", None, []]

SDL_RunApp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_RunApp", ctypes.c_int, [ctypes.c_int, SDL_POINTER[ctypes.c_char_p], SDL_main_func, ctypes.c_void_p]]
SDL_EnterAppMainCallbacks: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_EnterAppMainCallbacks", ctypes.c_int, [ctypes.c_int, SDL_POINTER[ctypes.c_char_p], SDL_AppInit_func, SDL_AppIterate_func, SDL_AppEvent_func, SDL_AppQuit_func]]

if SDL_PLATFORM_SPECIFIC(system = ["Windows"]):
    SDL_RegisterApp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_RegisterApp", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_uint32, ctypes.c_void_p]]
    SDL_UnregisterApp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UnregisterApp", None, []]