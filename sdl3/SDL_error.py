from .__init__ import ctypes, SDL_FUNC

SDL_FUNC("SDL_SetError", ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_OutOfMemory", ctypes.c_int)
SDL_FUNC("SDL_GetError", ctypes.c_char_p)
SDL_FUNC("SDL_ClearError", ctypes.c_int)

def SDL_Unsupported() -> int:
    return SDL_SetError("That operation is not supported".encode())

def SDL_InvalidParamError(param: str) -> int:
    return SDL_SetError(f"Parameter '{param}' is invalid".encode())