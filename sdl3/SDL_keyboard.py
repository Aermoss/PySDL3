from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID
from .SDL_keycode import SDL_Keycode, SDL_Keymod
from .SDL_scancode import SDL_Scancode
from .SDL_video import SDL_Window
from .SDL_rect import SDL_Rect

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_KeyboardID = ctypes.c_uint32

SDL_FUNC("SDL_HasKeyboard", ctypes.c_bool)
SDL_FUNC("SDL_GetKeyboards", ctypes.POINTER(SDL_KeyboardID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetKeyboardNameForID", ctypes.c_char_p, SDL_KeyboardID)
SDL_FUNC("SDL_GetKeyboardFocus", ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetKeyboardState", ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_ResetKeyboard", None)
SDL_FUNC("SDL_GetModState", SDL_Keymod)
SDL_FUNC("SDL_SetModState", None, SDL_Keymod)
SDL_FUNC("SDL_GetKeyFromScancode", SDL_Keycode, SDL_Scancode, SDL_Keymod, ctypes.c_bool)
SDL_FUNC("SDL_GetScancodeFromKey", SDL_Scancode, SDL_Keycode, ctypes.POINTER(SDL_Keymod))
SDL_FUNC("SDL_SetScancodeName", ctypes.c_bool, SDL_Scancode, ctypes.c_char_p)
SDL_FUNC("SDL_GetScancodeName", ctypes.c_char_p, SDL_Scancode)
SDL_FUNC("SDL_GetScancodeFromName", SDL_Scancode, ctypes.c_char_p)
SDL_FUNC("SDL_GetKeyName", ctypes.c_char_p, SDL_Keycode)
SDL_FUNC("SDL_GetKeyFromName", SDL_Keycode, ctypes.c_char_p)

SDL_FUNC("SDL_StartTextInput", ctypes.c_bool, ctypes.POINTER(SDL_Window))

SDL_TextInputType = ctypes.c_int

SDL_TEXTINPUT_TYPE_TEXT = 0
SDL_TEXTINPUT_TYPE_TEXT_NAME = 1
SDL_TEXTINPUT_TYPE_TEXT_EMAIL = 2
SDL_TEXTINPUT_TYPE_TEXT_USERNAME = 3
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_HIDDEN = 4
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_VISIBLE = 5
SDL_TEXTINPUT_TYPE_NUMBER = 6
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_HIDDEN = 7
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_VISIBLE = 8

SDL_Capitalization = ctypes.c_int

SDL_CAPITALIZE_NONE = 0
SDL_CAPITALIZE_SENTENCES = 1
SDL_CAPITALIZE_WORDS = 2
SDL_CAPITALIZE_LETTERS = 3

SDL_FUNC("SDL_StartTextInputWithProperties", ctypes.c_bool, ctypes.POINTER(SDL_Window), SDL_PropertiesID)

SDL_PROP_TEXTINPUT_TYPE_NUMBER = "SDL.textinput.type".encode()
SDL_PROP_TEXTINPUT_CAPITALIZATION_NUMBER = "SDL.textinput.capitalization".encode()
SDL_PROP_TEXTINPUT_AUTOCORRECT_BOOLEAN = "SDL.textinput.autocorrect".encode()
SDL_PROP_TEXTINPUT_MULTILINE_BOOLEAN = "SDL.textinput.multiline".encode()
SDL_PROP_TEXTINPUT_ANDROID_INPUTTYPE_NUMBER = "SDL.textinput.android.inputtype".encode()

SDL_FUNC("SDL_TextInputActive", ctypes.c_bool, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_StopTextInput", ctypes.c_bool, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_ClearComposition", ctypes.c_bool, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_SetTextInputArea", ctypes.c_bool, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Rect), ctypes.c_int)
SDL_FUNC("SDL_GetTextInputArea", ctypes.c_bool, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Rect), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_HasScreenKeyboardSupport", ctypes.c_bool)
SDL_FUNC("SDL_ScreenKeyboardShown", ctypes.c_bool, ctypes.POINTER(SDL_Window))