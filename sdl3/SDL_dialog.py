from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_video import SDL_Window

SDL_SET_CURRENT_DLL(SDL_DLL)

class SDL_DialogFileFilter(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("pattern", ctypes.c_char_p)
    ]

SDL_DialogFileCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)

SDL_FUNC("SDL_ShowOpenFileDialog", None, SDL_DialogFileCallback, ctypes.c_void_p, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_DialogFileFilter), ctypes.c_int, ctypes.c_char_p, ctypes.c_bool)
SDL_FUNC("SDL_ShowSaveFileDialog", None, SDL_DialogFileCallback, ctypes.c_void_p, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_DialogFileFilter), ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_ShowOpenFolderDialog", None, SDL_DialogFileCallback, ctypes.c_void_p, ctypes.POINTER(SDL_Window), ctypes.c_char_p, ctypes.c_bool)