from .__init__ import os, inspect, ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_ASSERT_LEVEL = 2
SDL_NULL_WHILE_LOOP_CONDITION = 0

SDL_AssertState = ctypes.c_int

SDL_ASSERTION_RETRY = 0
SDL_ASSERTION_BREAK = 1
SDL_ASSERTION_ABORT = 2
SDL_ASSERTION_IGNORE = 3
SDL_ASSERTION_ALWAYS_IGNORE = 4

SDL_AssertData = ctypes.c_void_p

class SDL_AssertData(ctypes.Structure):
    _fields_ = [
        ("always_ignore", ctypes.c_bool),
        ("trigger_count", ctypes.c_uint),
        ("condition", ctypes.c_char_p),
        ("filename", ctypes.c_char_p),
        ("linenum", ctypes.c_int),
        ("function", ctypes.c_char_p),
        ("next", ctypes.POINTER(SDL_AssertData))
    ]

SDL_FUNC("SDL_ReportAssertion", SDL_AssertState, ctypes.POINTER(SDL_AssertData), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)

SDL_TriggerBreakpoint = lambda: breakpoint()
SDL_AssertBreakpoint = lambda: SDL_TriggerBreakpoint()

def SDL_disabled_assert(condition: ctypes.c_bool) -> None:
    ...

def SDL_enabled_assert(condition: ctypes.c_bool) -> None:
    while not condition:
        current = inspect.currentframe()
        
        while "assert" in current.f_code.co_name or ("<lambda>" in current.f_code.co_name):
            current = current.f_back

        data = SDL_AssertData()
        data.condition = "<condition>".encode()
        state = SDL_GET_BINARY(SDL_BINARY).SDL_ReportAssertion \
            (ctypes.byref(data), current.f_code.co_name.encode(), os.path.split(current.f_code.co_filename)[-1].encode(), current.f_lineno)

        if state in [SDL_ASSERTION_RETRY]:
            continue

        if state in [SDL_ASSERTION_BREAK]:
            return SDL_AssertBreakpoint()

match SDL_ASSERT_LEVEL:
    case 0:
        SDL_assert = lambda condition: SDL_disabled_assert(condition)
        SDL_assert_release = lambda condition: SDL_disabled_assert(condition)
        SDL_assert_paranoid = lambda condition: SDL_disabled_assert(condition)

    case 1:
        SDL_assert = lambda condition: SDL_disabled_assert(condition)
        SDL_assert_release = lambda condition: SDL_enabled_assert(condition)
        SDL_assert_paranoid = lambda condition: SDL_disabled_assert(condition)

    case 2:
        SDL_assert = lambda condition: SDL_enabled_assert(condition)
        SDL_assert_release = lambda condition: SDL_enabled_assert(condition)
        SDL_assert_paranoid = lambda condition: SDL_disabled_assert(condition)

    case 3:
        SDL_assert = lambda condition: SDL_enabled_assert(condition)
        SDL_assert_release = lambda condition: SDL_enabled_assert(condition)
        SDL_assert_paranoid = lambda condition: SDL_enabled_assert(condition)

    case _:
        SDL_enabled_assert(False)

SDL_assert_always = lambda condition: SDL_enabled_assert(condition)
SDL_AssertionHandler = ctypes.CFUNCTYPE(SDL_AssertState, ctypes.POINTER(SDL_AssertData), ctypes.c_void_p)

SDL_FUNC("SDL_SetAssertionHandler", None, SDL_AssertionHandler, ctypes.c_void_p)
SDL_FUNC("SDL_GetDefaultAssertionHandler", SDL_AssertionHandler)
SDL_FUNC("SDL_GetAssertionHandler", SDL_AssertionHandler, ctypes.POINTER(ctypes.c_void_p))
SDL_FUNC("SDL_GetAssertionReport", ctypes.POINTER(SDL_AssertData))
SDL_FUNC("SDL_ResetAssertionReport", None)