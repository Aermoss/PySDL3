from .__init__ import sys, ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_video import SDL_DisplayID

SDL_SET_CURRENT_DLL(SDL_DLL)

if sys.platform in ["win32"]:
    import ctypes.wintypes as wintypes

    MSG = wintypes.tagMSG
    SDL_WindowsMessageHook = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(MSG))
    SDL_FUNC("SDL_SetWindowsMessageHook", None, SDL_WindowsMessageHook, ctypes.c_void_p)

    SDL_FUNC("SDL_GetDirect3D9AdapterIndex", ctypes.c_int, SDL_DisplayID)
    SDL_FUNC("SDL_GetDXGIOutputInfo", ctypes.c_bool, SDL_DisplayID, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

    class XEvent(ctypes.Union):
        ...

    SDL_X11EventHook = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(XEvent))
    SDL_FUNC("SDL_SetX11EventHook", None, SDL_X11EventHook, ctypes.c_void_p) 

if sys.platform in ["linux"]:
    SDL_FUNC("SDL_SetLinuxThreadPriority", ctypes.c_bool, ctypes.c_int64, ctypes.c_int)
    SDL_FUNC("SDL_SetLinuxThreadPriorityAndPolicy", ctypes.c_bool, ctypes.c_int64, ctypes.c_int, ctypes.c_int)

SDL_FUNC("SDL_IsTablet", ctypes.c_bool)
SDL_FUNC("SDL_OnApplicationWillTerminate", None)
SDL_FUNC("SDL_OnApplicationDidReceiveMemoryWarning", None)
SDL_FUNC("SDL_OnApplicationWillEnterBackground", None)
SDL_FUNC("SDL_OnApplicationDidEnterBackground", None)
SDL_FUNC("SDL_OnApplicationWillEnterForeground", None)
SDL_FUNC("SDL_OnApplicationDidEnterForeground", None)