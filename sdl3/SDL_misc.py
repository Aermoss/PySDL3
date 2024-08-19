from .__init__ import ctypes, SDL_FUNC

SDL_FUNC("SDL_OpenURL", ctypes.c_int, ctypes.c_char_p)