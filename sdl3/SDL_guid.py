from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_GUID(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_uint8 * 16)
    ]

SDL_FUNC("SDL_GUIDToString", None, SDL_GUID, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_StringToGUID", SDL_GUID, ctypes.c_char_p)