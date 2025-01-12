from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_FUNC("SDL_SetError", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("SDL_SetErrorV", ctypes.c_bool, ctypes.c_char_p, ctypes.c_void_p)
SDL_FUNC("SDL_OutOfMemory", ctypes.c_bool)
SDL_FUNC("SDL_GetError", ctypes.c_char_p)
SDL_FUNC("SDL_ClearError", ctypes.c_bool)

def SDL_Unsupported() -> ctypes.c_int:
    return SDL_GET_BINARY(SDL_BINARY).SDL_SetError("That operation is not supported".encode())

def SDL_InvalidParamError(param: ctypes.c_char_p) -> ctypes.c_int:
    if isinstance(param, bytes): param = param.decode()
    return SDL_GET_BINARY(SDL_BINARY).SDL_SetError(f"Parameter '{param}' is invalid".encode())