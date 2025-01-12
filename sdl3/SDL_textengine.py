from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_TTF_BINARY

from .SDL_mouse import SDL_MouseID
from .SDL_rect import SDL_Rect
from .SDL_properties import SDL_PropertiesID
from .SDL_ttf import TTF_Font, TTF_Text, TTF_SubString
from .SDL_pixels import SDL_FColor

SDL_SET_CURRENT_BINARY(SDL_TTF_BINARY)

TTF_DrawCommand = ctypes.c_int

TTF_DRAW_COMMAND_NOOP = 0
TTF_DRAW_COMMAND_FILL = 1
TTF_DRAW_COMMAND_COPY = 2

class TTF_FillOperation(ctypes.Structure):
    _fields_ = [
        ("cmd", TTF_DrawCommand),
        ("rect", SDL_Rect)
    ]

class TTF_CopyOperation(ctypes.Structure):
    _fields_ = [
        ("cmd", TTF_DrawCommand),
        ("text_offset", ctypes.c_int),
        ("glyph_index", ctypes.c_uint32),
        ("src", SDL_Rect),
        ("dst", SDL_Rect),
        ("reserved", ctypes.c_void_p)
    ]

class TTF_DrawOperation(ctypes.Union):
    _fields_ = [
        ("cmd", TTF_DrawCommand),
        ("fill", TTF_FillOperation),
        ("copy", TTF_CopyOperation)
    ]

class TTF_TextLayout(ctypes.c_void_p):
    ...

class TTF_TextEngine(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("userdata", ctypes.c_void_p),
        ("CreateText", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(TTF_Text))),
        ("DestroyText", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TTF_Text)))
    ]

class TTF_TextData(ctypes.Structure):
    _fields_ = [
        ("font", ctypes.POINTER(TTF_Font)),
        ("color", SDL_FColor),
        ("needs_layout_update", ctypes.c_bool),
        ("layout", ctypes.POINTER(TTF_TextLayout)),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("num_ops", ctypes.c_int),
        ("ops", ctypes.POINTER(TTF_DrawOperation)),
        ("num_clusters", ctypes.c_int),
        ("clusters", ctypes.POINTER(TTF_SubString)),
        ("props", SDL_PropertiesID),
        ("needs_engine_update", ctypes.c_bool),
        ("engine", TTF_TextEngine),
        ("engine_text", ctypes.c_void_p)
    ]