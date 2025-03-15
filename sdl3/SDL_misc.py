from .__init__ import ctypes, typing, abc, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_OpenURL: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_OpenURL", ctypes.c_bool, [ctypes.c_char_p]]