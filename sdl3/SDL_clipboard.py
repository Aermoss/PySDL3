from .__init__ import ctypes, typing, SDL_POINTER, SDL_FUNC_TYPE, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_FUNC("SDL_SetClipboardText", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("SDL_GetClipboardText", ctypes.c_char_p)
SDL_FUNC("SDL_HasClipboardText", ctypes.c_bool)

SDL_FUNC("SDL_SetPrimarySelectionText", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("SDL_GetPrimarySelectionText", ctypes.c_char_p)
SDL_FUNC("SDL_HasPrimarySelectionText", ctypes.c_bool)

SDL_ClipboardDataCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_ClipboardDataCallback", ctypes.c_void_p, ctypes.c_char_p, SDL_POINTER[ctypes.c_size_t]]
SDL_ClipboardCleanupCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_ClipboardCleanupCallback", None, ctypes.c_void_p]

SDL_FUNC("SDL_SetClipboardData", ctypes.c_bool, SDL_ClipboardDataCallback, SDL_ClipboardCleanupCallback, ctypes.c_void_p, SDL_POINTER[ctypes.c_char_p], ctypes.c_size_t)
SDL_FUNC("SDL_ClearClipboardData", ctypes.c_bool)
SDL_FUNC("SDL_GetClipboardData", ctypes.c_void_p, ctypes.c_char_p, SDL_POINTER[ctypes.c_size_t])
SDL_FUNC("SDL_HasClipboardData", ctypes.c_bool, ctypes.c_char_p)