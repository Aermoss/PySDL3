from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_RTF_BINARY, SDL_BINARY

from .SDL_pixels import SDL_Color
from .SDL_render import SDL_Renderer, SDL_Texture
from .SDL_version import SDL_VERSIONNUM
from .SDL_iostream import SDL_IOStream
from .SDL_rect import SDL_Rect

SDL_SET_CURRENT_BINARY(SDL_RTF_BINARY)

SDL_RTF_MAJOR_VERSION = 3
SDL_RTF_MINOR_VERSION = 0
SDL_RTF_MICRO_VERSION = 0

SDL_RTF_VERSION = \
    SDL_VERSIONNUM(SDL_RTF_MAJOR_VERSION, SDL_RTF_MINOR_VERSION, SDL_RTF_MICRO_VERSION)

SDL_RTF_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_RTF_MAJOR_VERSION >= x) and \
    (SDL_RTF_MAJOR_VERSION > x or SDL_RTF_MINOR_VERSION >= y) and \
    (SDL_RTF_MAJOR_VERSION > x or SDL_RTF_MINOR_VERSION > y or SDL_RTF_MICRO_VERSION >= z)

SDL_FUNC("RTF_Version", ctypes.c_int)

class RTF_Context(ctypes.c_void_p):
    ...

RTF_FontFamily = ctypes.c_int

RTF_FontDefault = 0
RTF_FontRoman = 1
RTF_FontSwiss = 2
RTF_FontModern = 3
RTF_FontScript = 4
RTF_FontDecor = 5
RTF_FontTech = 6
RTF_FontBidi = 7

RTF_FontStyle = ctypes.c_int

RTF_FontNormal = 0x00
RTF_FontBold = 0x01
RTF_FontItalic = 0x02
RTF_FontUnderline = 0x04

RTF_FONT_ENGINE_VERSION = 1

class RTF_FontEngine(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_int),
        ("CreateFont", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p, RTF_FontFamily, ctypes.c_int, ctypes.c_int, ctypes.c_int)),
        ("GetLineSpacing", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)),
        ("GetCharacterOffsets", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int)),
        ("RenderText", ctypes.CFUNCTYPE(ctypes.POINTER(SDL_Texture), ctypes.c_void_p, ctypes.POINTER(SDL_Renderer), ctypes.c_char_p, SDL_Color)),
        ("FreeFont", ctypes.CFUNCTYPE(None, ctypes.c_void_p))
    ]

SDL_FUNC("RTF_CreateContext", ctypes.POINTER(RTF_Context), ctypes.POINTER(SDL_Renderer), ctypes.POINTER(RTF_FontEngine))
SDL_FUNC("RTF_Load", ctypes.c_int, ctypes.POINTER(RTF_Context), ctypes.c_char_p)
SDL_FUNC("RTF_Load_IO", ctypes.c_int, ctypes.POINTER(RTF_Context), ctypes.POINTER(SDL_IOStream), ctypes.c_int)
SDL_FUNC("RTF_GetTitle", ctypes.c_char_p, ctypes.POINTER(RTF_Context))
SDL_FUNC("RTF_GetSubject", ctypes.c_char_p, ctypes.POINTER(RTF_Context))
SDL_FUNC("RTF_GetAuthor", ctypes.c_char_p, ctypes.POINTER(RTF_Context))
SDL_FUNC("RTF_GetHeight", ctypes.c_int, ctypes.POINTER(RTF_Context), ctypes.c_int)
SDL_FUNC("RTF_Render", None, ctypes.POINTER(RTF_Context), ctypes.POINTER(SDL_Rect), ctypes.c_int)
SDL_FUNC("RTF_FreeContext", None, ctypes.POINTER(RTF_Context))

RTF_SetError = SDL_GET_BINARY(SDL_BINARY).SDL_SetError
RTF_GetError = SDL_GET_BINARY(SDL_BINARY).SDL_GetError