from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_video import SDL_Window

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MessageBoxFlags = ctypes.c_uint32

SDL_MESSAGEBOX_ERROR = 0x00000010
SDL_MESSAGEBOX_WARNING = 0x00000020
SDL_MESSAGEBOX_INFORMATION = 0x00000040
SDL_MESSAGEBOX_BUTTONS_LEFT_TO_RIGHT = 0x00000080
SDL_MESSAGEBOX_BUTTONS_RIGHT_TO_LEFT = 0x00000100

SDL_MessageBoxButtonFlags = ctypes.c_uint32

SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 0x00000001
SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 0x00000002

class SDL_MessageBoxButtonData(ctypes.Structure):
    _fields_ = [
        ("flags", SDL_MessageBoxButtonFlags),
        ("buttonID", ctypes.c_int),
        ("text", ctypes.c_char_p)
    ]

class SDL_MessageBoxColor(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_uint8),
        ("g", ctypes.c_uint8),
        ("b", ctypes.c_uint8)
    ]

SDL_MessageBoxColorType = ctypes.c_int

SDL_MESSAGEBOX_COLOR_BACKGROUND = 0
SDL_MESSAGEBOX_COLOR_TEXT = 1
SDL_MESSAGEBOX_COLOR_BUTTON_BORDER = 2
SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND = 3
SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED = 4
SDL_MESSAGEBOX_COLOR_COUNT = 5

class SDL_MessageBoxColorScheme(ctypes.Structure):
    _fields_ = [
        ("colors", SDL_MessageBoxColor * SDL_MESSAGEBOX_COLOR_COUNT)
    ]

class SDL_MessageBoxData(ctypes.Structure):
    _fields_ = [
        ("flags", SDL_MessageBoxFlags),
        ("window", ctypes.POINTER(SDL_Window)),
        ("title", ctypes.c_char_p),
        ("message", ctypes.c_char_p),
        ("numbuttons", ctypes.c_int),
        ("buttons", ctypes.POINTER(SDL_MessageBoxButtonData)),
        ("colorScheme", ctypes.POINTER(SDL_MessageBoxColorScheme))
    ]

SDL_FUNC("SDL_ShowMessageBox", ctypes.c_bool, ctypes.POINTER(SDL_MessageBoxData), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_ShowSimpleMessageBox", ctypes.c_bool, SDL_MessageBoxFlags, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(SDL_Window))