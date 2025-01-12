from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_stdinc import SDL_Time

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_FUNC("SDL_GetBasePath", ctypes.c_char_p)
SDL_FUNC("SDL_GetPrefPath", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)

SDL_Folder = ctypes.c_int

SDL_FOLDER_HOME = 0
SDL_FOLDER_DESKTOP = 1
SDL_FOLDER_DOCUMENTS = 2
SDL_FOLDER_DOWNLOADS = 3
SDL_FOLDER_MUSIC = 4
SDL_FOLDER_PICTURES = 5
SDL_FOLDER_PUBLICSHARE = 6
SDL_FOLDER_SAVEDGAMES = 7
SDL_FOLDER_SCREENSHOTS = 8
SDL_FOLDER_TEMPLATES = 9
SDL_FOLDER_VIDEOS = 10
SDL_FOLDER_COUNT = 11

SDL_FUNC("SDL_GetUserFolder", ctypes.c_char_p, SDL_Folder)

SDL_PathType = ctypes.c_int

SDL_PATHTYPE_NONE = 0
SDL_PATHTYPE_FILE = 1
SDL_PATHTYPE_DIRECTORY = 2
SDL_PATHTYPE_OTHER = 3

class SDL_PathInfo(ctypes.Structure):
    _fields_ = [
        ("type", SDL_PathType),
        ("size", ctypes.c_uint64),
        ("create_time", SDL_Time),
        ("modify_time", SDL_Time),
        ("access_time", SDL_Time)
    ]

SDL_GlobFlags = ctypes.c_uint32

SDL_GLOB_CASEINSENSITIVE = 1 << 0

SDL_FUNC("SDL_CreateDirectory", ctypes.c_bool, ctypes.c_char_p)

SDL_EnumerationResult = ctypes.c_int

SDL_ENUM_CONTINUE = 0
SDL_ENUM_SUCCESS = 1
SDL_ENUM_FAILURE = 2

SDL_EnumerateDirectoryCallback = ctypes.CFUNCTYPE(SDL_EnumerationResult, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)

SDL_FUNC("SDL_EnumerateDirectory", ctypes.c_bool, ctypes.c_char_p, SDL_EnumerateDirectoryCallback, ctypes.c_void_p)
SDL_FUNC("SDL_RemovePath", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("SDL_RenamePath", ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_CopyFile", ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_GetPathInfo", ctypes.c_bool, ctypes.c_char_p, ctypes.POINTER(SDL_PathInfo))
SDL_FUNC("SDL_GlobDirectory", ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(SDL_GlobFlags), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetCurrentDirectory", ctypes.c_char_p)