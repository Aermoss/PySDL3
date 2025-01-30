from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_IOStatus = ctypes.c_uint32

SDL_IO_STATUS_READY = 0
SDL_IO_STATUS_ERROR = 1
SDL_IO_STATUS_EOF = 2
SDL_IO_STATUS_NOT_READY = 3
SDL_IO_STATUS_READONLY = 4
SDL_IO_STATUS_WRITEONLY = 5

SDL_IOWhence = ctypes.c_uint32

SDL_IO_SEEK_SET = 0
SDL_IO_SEEK_CUR = 1
SDL_IO_SEEK_END = 2

class SDL_IOStreamInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("size", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p)),
        ("seek", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p, ctypes.c_int64, SDL_IOWhence)),
        ("read", ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(SDL_IOStatus))),
        ("write", ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(SDL_IOStatus))),
        ("flush", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(SDL_IOStatus))),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p))
    ]

class SDL_IOStream(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_IOFromFile", ctypes.POINTER(SDL_IOStream), ctypes.c_char_p, ctypes.c_char_p)

SDL_PROP_IOSTREAM_WINDOWS_HANDLE_POINTER = "SDL.iostream.windows.handle".encode()
SDL_PROP_IOSTREAM_STDIO_FILE_POINTER = "SDL.iostream.stdio.file".encode()
SDL_PROP_IOSTREAM_FILE_DESCRIPTOR_NUMBER = "SDL.iostream.file_descriptor".encode()
SDL_PROP_IOSTREAM_ANDROID_AASSET_POINTER = "SDL.iostream.android.aasset".encode()

SDL_FUNC("SDL_IOFromMem", ctypes.POINTER(SDL_IOStream), ctypes.c_void_p, ctypes.c_size_t)

SDL_PROP_IOSTREAM_MEMORY_POINTER = "SDL.iostream.memory.base".encode()
SDL_PROP_IOSTREAM_MEMORY_SIZE_NUMBER = "SDL.iostream.memory.size".encode()

SDL_FUNC("SDL_IOFromConstMem", ctypes.POINTER(SDL_IOStream), ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_IOFromDynamicMem", ctypes.POINTER(SDL_IOStream))

SDL_PROP_IOSTREAM_DYNAMIC_MEMORY_POINTER = "SDL.iostream.dynamic.memory".encode()
SDL_PROP_IOSTREAM_DYNAMIC_CHUNKSIZE_NUMBER = "SDL.iostream.dynamic.chunksize".encode()

SDL_FUNC("SDL_OpenIO", ctypes.POINTER(SDL_IOStream), ctypes.POINTER(SDL_IOStreamInterface), ctypes.c_void_p)
SDL_FUNC("SDL_CloseIO", ctypes.c_bool, ctypes.POINTER(SDL_IOStream))

SDL_FUNC("SDL_GetIOProperties", SDL_PropertiesID, ctypes.POINTER(SDL_IOStream))
SDL_FUNC("SDL_GetIOStatus", SDL_IOStatus, ctypes.POINTER(SDL_IOStream))
SDL_FUNC("SDL_GetIOSize", ctypes.c_int64, ctypes.POINTER(SDL_IOStream))

SDL_FUNC("SDL_SeekIO", ctypes.c_int64, ctypes.POINTER(SDL_IOStream), ctypes.c_int64, SDL_IOWhence)
SDL_FUNC("SDL_TellIO", ctypes.c_int64, ctypes.POINTER(SDL_IOStream))
SDL_FUNC("SDL_ReadIO", ctypes.c_size_t, ctypes.POINTER(SDL_IOStream), ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_WriteIO", ctypes.c_size_t, ctypes.POINTER(SDL_IOStream), ctypes.c_void_p, ctypes.c_size_t)

SDL_FUNC("SDL_IOprintf", ctypes.c_size_t, ctypes.POINTER(SDL_IOStream), ctypes.c_char_p)
SDL_FUNC("SDL_IOvprintf", ctypes.c_size_t, ctypes.POINTER(SDL_IOStream), ctypes.c_char_p, ctypes.c_void_p)

SDL_FUNC("SDL_FlushIO", ctypes.c_bool, ctypes.POINTER(SDL_IOStream))

SDL_FUNC("SDL_LoadFile_IO", ctypes.c_void_p, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_size_t), ctypes.c_bool)
SDL_FUNC("SDL_LoadFile", ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t))

SDL_FUNC("SDL_SaveFile_IO", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_void_p), ctypes.c_size_t, ctypes.c_bool)
SDL_FUNC("SDL_SaveFile", ctypes.c_bool, ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_size_t)

SDL_FUNC("SDL_ReadU8", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_ReadS8", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int8))
SDL_FUNC("SDL_ReadU16LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint16))
SDL_FUNC("SDL_ReadS16LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int16))
SDL_FUNC("SDL_ReadU16BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint16))
SDL_FUNC("SDL_ReadS16BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int16))
SDL_FUNC("SDL_ReadU32LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_ReadS32LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int32))
SDL_FUNC("SDL_ReadU32BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_ReadS32BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int32))
SDL_FUNC("SDL_ReadU64LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint64))
SDL_FUNC("SDL_ReadS64LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int64))
SDL_FUNC("SDL_ReadU64BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_uint64))
SDL_FUNC("SDL_ReadS64BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.POINTER(ctypes.c_int64))

SDL_FUNC("SDL_WriteU8", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint8)
SDL_FUNC("SDL_WriteS8", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int8)
SDL_FUNC("SDL_WriteU16LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint16)
SDL_FUNC("SDL_WriteS16LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int16)
SDL_FUNC("SDL_WriteU16BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint16)
SDL_FUNC("SDL_WriteS16BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int16)
SDL_FUNC("SDL_WriteU32LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint32)
SDL_FUNC("SDL_WriteS32LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int32)
SDL_FUNC("SDL_WriteU32BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint32)
SDL_FUNC("SDL_WriteS32BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int32)
SDL_FUNC("SDL_WriteU64LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint64)
SDL_FUNC("SDL_WriteS64LE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int64)
SDL_FUNC("SDL_WriteU64BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_uint64)
SDL_FUNC("SDL_WriteS64BE", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_int64)