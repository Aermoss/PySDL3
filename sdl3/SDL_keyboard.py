from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID
from .SDL_keycode import SDL_Keycode, SDL_Keymod
from .SDL_scancode import SDL_Scancode
from .SDL_video import SDL_Window
from .SDL_rect import SDL_Rect

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_KeyboardID: typing.TypeAlias = SDL_TYPE["SDL_KeyboardID", ctypes.c_uint32]

SDL_HasKeyboard: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_HasKeyboard", ctypes.c_bool, []]
SDL_GetKeyboards: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyboards", SDL_POINTER[SDL_KeyboardID], [SDL_POINTER[ctypes.c_int]]]
SDL_GetKeyboardNameForID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyboardNameForID", ctypes.c_char_p, [SDL_KeyboardID]]
SDL_GetKeyboardFocus: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyboardFocus", SDL_POINTER[SDL_Window], []]
SDL_GetKeyboardState: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyboardState", SDL_POINTER[ctypes.c_bool], [SDL_POINTER[ctypes.c_int]]]
SDL_ResetKeyboard: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ResetKeyboard", None, []]
SDL_GetModState: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetModState", SDL_Keymod, []]
SDL_SetModState: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetModState", None, [SDL_Keymod]]
SDL_GetKeyFromScancode: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyFromScancode", SDL_Keycode, [SDL_Scancode, SDL_Keymod, ctypes.c_bool]]
SDL_GetScancodeFromKey: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetScancodeFromKey", SDL_Scancode, [SDL_Keycode, SDL_POINTER[SDL_Keymod]]]
SDL_SetScancodeName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetScancodeName", ctypes.c_bool, [SDL_Scancode, ctypes.c_char_p]]
SDL_GetScancodeName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetScancodeName", ctypes.c_char_p, [SDL_Scancode]]
SDL_GetScancodeFromName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetScancodeFromName", SDL_Scancode, [ctypes.c_char_p]]
SDL_GetKeyName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyName", ctypes.c_char_p, [SDL_Keycode]]
SDL_GetKeyFromName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetKeyFromName", SDL_Keycode, [ctypes.c_char_p]]

SDL_StartTextInput: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StartTextInput", ctypes.c_bool, [SDL_POINTER[SDL_Window]]]

SDL_TextInputType: typing.TypeAlias = SDL_TYPE["SDL_TextInputType", ctypes.c_int]

SDL_TEXTINPUT_TYPE_TEXT = 0
SDL_TEXTINPUT_TYPE_TEXT_NAME = 1
SDL_TEXTINPUT_TYPE_TEXT_EMAIL = 2
SDL_TEXTINPUT_TYPE_TEXT_USERNAME = 3
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_HIDDEN = 4
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_VISIBLE = 5
SDL_TEXTINPUT_TYPE_NUMBER = 6
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_HIDDEN = 7
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_VISIBLE = 8

SDL_Capitalization: typing.TypeAlias = SDL_TYPE["SDL_Capitalization", ctypes.c_int]

SDL_CAPITALIZE_NONE = 0
SDL_CAPITALIZE_SENTENCES = 1
SDL_CAPITALIZE_WORDS = 2
SDL_CAPITALIZE_LETTERS = 3

SDL_StartTextInputWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StartTextInputWithProperties", ctypes.c_bool, [SDL_POINTER[SDL_Window], SDL_PropertiesID]]

SDL_PROP_TEXTINPUT_TYPE_NUMBER = "SDL.textinput.type".encode()
SDL_PROP_TEXTINPUT_CAPITALIZATION_NUMBER = "SDL.textinput.capitalization".encode()
SDL_PROP_TEXTINPUT_AUTOCORRECT_BOOLEAN = "SDL.textinput.autocorrect".encode()
SDL_PROP_TEXTINPUT_MULTILINE_BOOLEAN = "SDL.textinput.multiline".encode()
SDL_PROP_TEXTINPUT_ANDROID_INPUTTYPE_NUMBER = "SDL.textinput.android.inputtype".encode()

SDL_TextInputActive: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_TextInputActive", ctypes.c_bool, [SDL_POINTER[SDL_Window]]]
SDL_StopTextInput: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StopTextInput", ctypes.c_bool, [SDL_POINTER[SDL_Window]]]
SDL_ClearComposition: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ClearComposition", ctypes.c_bool, [SDL_POINTER[SDL_Window]]]
SDL_SetTextInputArea: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetTextInputArea", ctypes.c_bool, [SDL_POINTER[SDL_Window], SDL_POINTER[SDL_Rect], ctypes.c_int]]
SDL_GetTextInputArea: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTextInputArea", ctypes.c_bool, [SDL_POINTER[SDL_Window], SDL_POINTER[SDL_Rect], SDL_POINTER[ctypes.c_int]]]
SDL_HasScreenKeyboardSupport: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_HasScreenKeyboardSupport", ctypes.c_bool, []]
SDL_ScreenKeyboardShown: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ScreenKeyboardShown", ctypes.c_bool, [SDL_POINTER[SDL_Window]]]