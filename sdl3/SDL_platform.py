from .__init__ import ctypes, SDL_FUNC

SDL_FUNC("SDL_GetPlatform", ctypes.c_char_p)