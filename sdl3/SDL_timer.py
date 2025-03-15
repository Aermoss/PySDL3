from .__init__ import ctypes, typing, abc, SDL_FUNC_TYPE, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MS_PER_SECOND = 1000
SDL_US_PER_SECOND = 1000000
SDL_NS_PER_SECOND = 1000000000
SDL_NS_PER_MS = 1000000
SDL_NS_PER_US = 1000

SDL_SECONDS_TO_NS = lambda s: s * SDL_NS_PER_SECOND
SDL_NS_TO_SECONDS = lambda ns: ns / SDL_NS_PER_SECOND
SDL_MS_TO_NS = lambda ms: ms * SDL_NS_PER_MS
SDL_NS_TO_MS = lambda ns: ns / SDL_NS_PER_MS
SDL_US_TO_NS = lambda us: us * SDL_NS_PER_US
SDL_NS_TO_US = lambda ns: ns / SDL_NS_PER_US

SDL_GetTicks: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTicks", ctypes.c_uint64, []]
SDL_GetTicksNS: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTicksNS", ctypes.c_uint64, []]
SDL_GetPerformanceCounter: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPerformanceCounter", ctypes.c_uint64, []]
SDL_GetPerformanceFrequency: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPerformanceFrequency", ctypes.c_uint64, []]
SDL_Delay: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_Delay", None, [ctypes.c_uint32]]
SDL_DelayNS: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DelayNS", None, [ctypes.c_uint64]]
SDL_DelayPrecise: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DelayPrecise", None, [ctypes.c_uint64]]

SDL_TimerID: typing.TypeAlias = SDL_TYPE["SDL_TimerID", ctypes.c_uint32]
SDL_TimerCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_TimerCallback", ctypes.c_uint32, [ctypes.c_void_p, SDL_TimerID, ctypes.c_uint32]]

SDL_AddTimer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_AddTimer", SDL_TimerID, [ctypes.c_uint32, SDL_TimerCallback, ctypes.c_void_p]]

SDL_NSTimerCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_NSTimerCallback", ctypes.c_uint64, [ctypes.c_void_p, SDL_TimerID, ctypes.c_uint64]]

SDL_AddTimerNS: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_AddTimerNS", SDL_TimerID, [ctypes.c_uint64, SDL_NSTimerCallback, ctypes.c_void_p]]
SDL_RemoveTimer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_RemoveTimer", ctypes.c_bool, [SDL_TimerID]]