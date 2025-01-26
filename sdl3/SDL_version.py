from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MAJOR_VERSION = 3
SDL_MINOR_VERSION = 2
SDL_MICRO_VERSION = 1

SDL_VERSIONNUM = lambda major, minor, patch: \
    major * 1000000 + minor * 1000 + patch

SDL_VERSIONNUM_MAJOR = lambda version: int(version / 1000000)
SDL_VERSIONNUM_MINOR = lambda version: int(version / 1000) % 1000
SDL_VERSIONNUM_MICRO = lambda version: version % 1000

SDL_VERSION = SDL_VERSIONNUM(SDL_MAJOR_VERSION, SDL_MINOR_VERSION, SDL_MICRO_VERSION)
SDL_VERSION_ATLEAST = lambda x, y, z: SDL_VERSION >= SDL_VERSIONNUM(x, y, z)

SDL_FUNC("SDL_GetVersion", ctypes.c_int)
SDL_FUNC("SDL_GetRevision", ctypes.c_char_p)