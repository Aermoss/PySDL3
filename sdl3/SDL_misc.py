from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_FUNC("SDL_OpenURL", ctypes.c_bool, ctypes.c_char_p)