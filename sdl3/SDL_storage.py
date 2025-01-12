from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_filesystem import SDL_EnumerateDirectoryCallback, SDL_PathInfo, SDL_GlobFlags
from .SDL_properties import SDL_PropertiesID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_StorageInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        ("ready", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        ("enumerate", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, SDL_EnumerateDirectoryCallback, ctypes.c_void_p)),
        ("info", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(SDL_PathInfo))),
        ("read_file", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)),
        ("write_file", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)),
        ("mkdir", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        ("remove", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        ("rename", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)),
        ("copy", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)),
        ("space_remaining", ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_void_p))
    ]

class SDL_Storage(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_OpenTitleStorage", ctypes.POINTER(SDL_Storage), ctypes.c_char_p, SDL_PropertiesID)
SDL_FUNC("SDL_OpenUserStorage", ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_char_p, SDL_PropertiesID)
SDL_FUNC("SDL_OpenFileStorage", ctypes.POINTER(SDL_Storage), ctypes.c_char_p)
SDL_FUNC("SDL_OpenStorage", ctypes.POINTER(SDL_Storage), ctypes.POINTER(SDL_StorageInterface), ctypes.c_void_p)
SDL_FUNC("SDL_CloseStorage", ctypes.c_bool, ctypes.POINTER(SDL_Storage))
SDL_FUNC("SDL_StorageReady", ctypes.c_bool, ctypes.POINTER(SDL_Storage))
SDL_FUNC("SDL_GetStorageFileSize", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint64))
SDL_FUNC("SDL_ReadStorageFile", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)
SDL_FUNC("SDL_WriteStorageFile", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)
SDL_FUNC("SDL_CreateStorageDirectory", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p)
SDL_FUNC("SDL_EnumerateStorageDirectory", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, SDL_EnumerateDirectoryCallback, ctypes.c_void_p)
SDL_FUNC("SDL_RemoveStoragePath", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p)
SDL_FUNC("SDL_RenameStoragePath", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_CopyStorageFile", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_GetStoragePathInfo", ctypes.c_bool, ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.POINTER(SDL_PathInfo))
SDL_FUNC("SDL_GetStorageSpaceRemaining", ctypes.c_uint64, ctypes.POINTER(SDL_Storage))
SDL_FUNC("SDL_GlobStorageDirectory", ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(SDL_Storage), ctypes.c_char_p, ctypes.c_char_p, SDL_GlobFlags, ctypes.POINTER(ctypes.c_int))