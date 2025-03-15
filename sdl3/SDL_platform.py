from .__init__ import ctypes, typing, abc, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_GetPlatform: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPlatform", ctypes.c_char_p, []]