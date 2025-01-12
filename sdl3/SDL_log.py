from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_LogCategory = ctypes.c_int

SDL_LOG_CATEGORY_APPLICATION = 0
SDL_LOG_CATEGORY_ERROR = 1
SDL_LOG_CATEGORY_ASSERT = 2
SDL_LOG_CATEGORY_SYSTEM = 3
SDL_LOG_CATEGORY_AUDIO = 4
SDL_LOG_CATEGORY_VIDEO = 5
SDL_LOG_CATEGORY_RENDER = 6
SDL_LOG_CATEGORY_INPUT = 7
SDL_LOG_CATEGORY_TEST = 8
SDL_LOG_CATEGORY_GPU = 9
SDL_LOG_CATEGORY_RESERVED1 = 10
SDL_LOG_CATEGORY_RESERVED2 = 11
SDL_LOG_CATEGORY_RESERVED3 = 12
SDL_LOG_CATEGORY_RESERVED4 = 13
SDL_LOG_CATEGORY_RESERVED5 = 14
SDL_LOG_CATEGORY_RESERVED6 = 15
SDL_LOG_CATEGORY_RESERVED7 = 16
SDL_LOG_CATEGORY_RESERVED8  = 17
SDL_LOG_CATEGORY_RESERVED9 = 18
SDL_LOG_CATEGORY_RESERVED10 = 19
SDL_LOG_CATEGORY_CUSTOM = 20

SDL_LogPriority = ctypes.c_int

SDL_LOG_PRIORITY_INVALID = 0
SDL_LOG_PRIORITY_TRACE = 1
SDL_LOG_PRIORITY_VERBOSE = 2
SDL_LOG_PRIORITY_DEBUG = 3
SDL_LOG_PRIORITY_INFO = 4
SDL_LOG_PRIORITY_WARN = 5
SDL_LOG_PRIORITY_ERROR = 6
SDL_LOG_PRIORITY_CRITICAL = 7
SDL_LOG_PRIORITY_COUNT = 8

SDL_FUNC("SDL_SetLogPriorities", None, SDL_LogPriority)
SDL_FUNC("SDL_SetLogPriority", None, ctypes.c_int, SDL_LogPriority)
SDL_FUNC("SDL_GetLogPriority", SDL_LogPriority, ctypes.c_int)
SDL_FUNC("SDL_ResetLogPriorities", None)
SDL_FUNC("SDL_SetLogPriorityPrefix", ctypes.c_bool, SDL_LogPriority, ctypes.c_char_p)

SDL_FUNC("SDL_Log", None, ctypes.c_char_p)
SDL_FUNC("SDL_LogTrace", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogVerbose", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogDebug", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogInfo", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogWarn", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogError", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogCritical", None, ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_LogMessage", None, ctypes.c_int, SDL_LogPriority, ctypes.c_char_p)
SDL_FUNC("SDL_LogMessageV", None, ctypes.c_int, SDL_LogPriority, ctypes.c_char_p, ctypes.c_char_p)

SDL_LogOutputFunction = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int, SDL_LogPriority, ctypes.c_char_p)

SDL_FUNC("SDL_GetDefaultLogOutputFunction", SDL_LogOutputFunction)
SDL_FUNC("SDL_GetLogOutputFunction", None, ctypes.POINTER(SDL_LogOutputFunction), ctypes.POINTER(ctypes.c_void_p))
SDL_FUNC("SDL_SetLogOutputFunction", None, SDL_LogOutputFunction, ctypes.c_void_p)