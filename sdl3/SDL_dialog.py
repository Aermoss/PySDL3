from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_video import SDL_Window
from .SDL_properties import SDL_PropertiesID

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

SDL_FileDialogType = ctypes.c_int

SDL_FILEDIALOG_OPENFILE = 0
SDL_FILEDIALOG_SAVEFILE = 1
SDL_FILEDIALOG_OPENFOLDER = 2

SDL_PROP_FILE_DIALOG_FILTERS_POINTER = "SDL.filedialog.filters"
SDL_PROP_FILE_DIALOG_NFILTERS_NUMBER = "SDL.filedialog.nfilters"
SDL_PROP_FILE_DIALOG_WINDOW_POINTER = "SDL.filedialog.window"
SDL_PROP_FILE_DIALOG_LOCATION_STRING = "SDL.filedialog.location"
SDL_PROP_FILE_DIALOG_MANY_BOOLEAN = "SDL.filedialog.many"
SDL_PROP_FILE_DIALOG_TITLE_STRING = "SDL.filedialog.title"
SDL_PROP_FILE_DIALOG_ACCEPT_STRING = "SDL.filedialog.accept"
SDL_PROP_FILE_DIALOG_CANCEL_STRING = "SDL.filedialog.cancel"

SDL_FUNC("SDL_ShowFileDialogWithProperties", None, SDL_FileDialogType, SDL_DialogFileCallback, ctypes.c_void_p, SDL_PropertiesID)