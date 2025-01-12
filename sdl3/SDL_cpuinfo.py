from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_CACHELINE_SIZE = 128

SDL_FUNC("SDL_GetNumLogicalCPUCores", ctypes.c_int)
SDL_FUNC("SDL_GetCPUCacheLineSize", ctypes.c_int)

SDL_FUNC("SDL_HasAltiVec", ctypes.c_bool)
SDL_FUNC("SDL_HasMMX", ctypes.c_bool)
SDL_FUNC("SDL_HasSSE", ctypes.c_bool)
SDL_FUNC("SDL_HasSSE2", ctypes.c_bool)
SDL_FUNC("SDL_HasSSE3", ctypes.c_bool)
SDL_FUNC("SDL_HasSSE41", ctypes.c_bool)
SDL_FUNC("SDL_HasSSE42", ctypes.c_bool)
SDL_FUNC("SDL_HasAVX", ctypes.c_bool)
SDL_FUNC("SDL_HasAVX2", ctypes.c_bool)
SDL_FUNC("SDL_HasAVX512F", ctypes.c_bool)
SDL_FUNC("SDL_HasARMSIMD", ctypes.c_bool)
SDL_FUNC("SDL_HasNEON", ctypes.c_bool)
SDL_FUNC("SDL_HasLSX", ctypes.c_bool)
SDL_FUNC("SDL_HasLASX", ctypes.c_bool)

SDL_FUNC("SDL_GetSystemRAM", ctypes.c_int)
SDL_FUNC("SDL_GetSIMDAlignment", ctypes.c_size_t)