from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_video import SDL_Window
from .SDL_surface import SDL_Surface

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MouseID = ctypes.c_uint32

class SDL_Cursor(ctypes.c_void_p):
    ...

SDL_SystemCursor = ctypes.c_int

SDL_SYSTEM_CURSOR_DEFAULT = 0
SDL_SYSTEM_CURSOR_TEXT = 1
SDL_SYSTEM_CURSOR_WAIT = 2
SDL_SYSTEM_CURSOR_CROSSHAIR = 3
SDL_SYSTEM_CURSOR_PROGRESS = 4
SDL_SYSTEM_CURSOR_NWSE_RESIZE = 5
SDL_SYSTEM_CURSOR_NESW_RESIZE = 6
SDL_SYSTEM_CURSOR_EW_RESIZE = 7
SDL_SYSTEM_CURSOR_NS_RESIZE = 8
SDL_SYSTEM_CURSOR_MOVE = 9
SDL_SYSTEM_CURSOR_NOT_ALLOWED = 10
SDL_SYSTEM_CURSOR_POINTER = 11
SDL_SYSTEM_CURSOR_NW_RESIZE = 12
SDL_SYSTEM_CURSOR_N_RESIZE = 13
SDL_SYSTEM_CURSOR_NE_RESIZE = 14
SDL_SYSTEM_CURSOR_E_RESIZE = 15
SDL_SYSTEM_CURSOR_SE_RESIZE = 16
SDL_SYSTEM_CURSOR_S_RESIZE = 17
SDL_SYSTEM_CURSOR_SW_RESIZE = 18
SDL_SYSTEM_CURSOR_W_RESIZE = 19
SDL_SYSTEM_CURSOR_COUNT = 20

SDL_MouseWheelDirection = ctypes.c_int

SDL_MOUSEWHEEL_NORMAL = 0
SDL_MOUSEWHEEL_FLIPPED = 1

SDL_MouseButtonFlags = ctypes.c_uint32

SDL_BUTTON_LEFT = 1
SDL_BUTTON_MIDDLE = 2
SDL_BUTTON_RIGHT = 3
SDL_BUTTON_X1 = 4
SDL_BUTTON_X2 = 5

SDL_BUTTON_MASK = lambda x: 1 << (x - 1)
SDL_BUTTON_LMASK = SDL_BUTTON_MASK(SDL_BUTTON_LEFT)
SDL_BUTTON_MMASK = SDL_BUTTON_MASK(SDL_BUTTON_MIDDLE)
SDL_BUTTON_RMASK = SDL_BUTTON_MASK(SDL_BUTTON_RIGHT)
SDL_BUTTON_X1MASK = SDL_BUTTON_MASK(SDL_BUTTON_X1)
SDL_BUTTON_X2MASK = SDL_BUTTON_MASK(SDL_BUTTON_X2)

SDL_FUNC("SDL_HasMouse", ctypes.c_bool)
SDL_FUNC("SDL_GetMice", ctypes.POINTER(SDL_MouseID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetMouseNameForID", ctypes.c_char_p, SDL_MouseID)
SDL_FUNC("SDL_GetMouseFocus", ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetMouseState", SDL_MouseButtonFlags, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_GetGlobalMouseState", SDL_MouseButtonFlags, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_GetRelativeMouseState", SDL_MouseButtonFlags, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_WarpMouseInWindow", None, ctypes.POINTER(SDL_Window), ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_WarpMouseGlobal", ctypes.c_bool, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_SetWindowRelativeMouseMode", ctypes.c_bool, ctypes.POINTER(SDL_Window), ctypes.c_bool)
SDL_FUNC("SDL_GetWindowRelativeMouseMode", ctypes.c_bool, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_CaptureMouse", ctypes.c_bool, ctypes.c_bool)

SDL_FUNC("SDL_CreateCursor", ctypes.POINTER(SDL_Cursor), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_CreateColorCursor", ctypes.POINTER(SDL_Cursor), ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_CreateSystemCursor", ctypes.POINTER(SDL_Cursor), SDL_SystemCursor)
SDL_FUNC("SDL_SetCursor", ctypes.c_bool, ctypes.POINTER(SDL_Cursor))
SDL_FUNC("SDL_GetCursor", ctypes.POINTER(SDL_Cursor))
SDL_FUNC("SDL_GetDefaultCursor", ctypes.POINTER(SDL_Cursor))
SDL_FUNC("SDL_DestroyCursor", None, ctypes.POINTER(SDL_Cursor))
SDL_FUNC("SDL_ShowCursor", ctypes.c_bool)
SDL_FUNC("SDL_HideCursor", ctypes.c_bool)
SDL_FUNC("SDL_CursorVisible", ctypes.c_bool)