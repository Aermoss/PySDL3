from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_FUNC("SDL_GetPlatform", ctypes.c_char_p)