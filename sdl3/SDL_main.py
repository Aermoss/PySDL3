from .__init__ import sys, ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_init import SDL_AppResult, \
    SDL_AppInit_func, SDL_AppIterate_func, SDL_AppEvent_func, SDL_AppQuit_func

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_main_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p))

SDL_FUNC("SDL_SetMainReady", None)

SDL_FUNC("SDL_RunApp", ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), SDL_main_func, ctypes.c_void_p)
SDL_FUNC("SDL_EnterAppMainCallbacks", ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), SDL_AppInit_func, SDL_AppIterate_func, SDL_AppEvent_func, SDL_AppQuit_func)

if "win32" in sys.platform:
    SDL_FUNC("SDL_RegisterApp", ctypes.c_bool, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_void_p)
    SDL_FUNC("SDL_UnregisterApp", None)