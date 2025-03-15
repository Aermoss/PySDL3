from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_PowerState: typing.TypeAlias = SDL_TYPE["SDL_PowerState", ctypes.c_int]

SDL_POWERSTATE_ERROR = -1
SDL_POWERSTATE_UNKNOWN = 0
SDL_POWERSTATE_ON_BATTERY = 1
SDL_POWERSTATE_NO_BATTERY = 2
SDL_POWERSTATE_CHARGING = 3
SDL_POWERSTATE_CHARGED = 4

SDL_GetPowerInfo: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPowerInfo", SDL_PowerState, [SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]