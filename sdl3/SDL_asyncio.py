from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_AsyncIO(ctypes.c_void_p):
    ...

SDL_AsyncIOTaskType = ctypes.c_int

SDL_ASYNCIO_TASK_READ = 0
SDL_ASYNCIO_TASK_WRITE = 1
SDL_ASYNCIO_TASK_CLOSE = 2

SDL_AsyncIOResult = ctypes.c_int

SDL_ASYNCIO_COMPLETE = 0
SDL_ASYNCIO_FAILURE = 1
SDL_ASYNCIO_CANCELED = 2

class SDL_AsyncIOOutcome(ctypes.Structure):
    _fields_ = [
        ("asyncio", ctypes.POINTER(SDL_AsyncIO)),
        ("type", SDL_AsyncIOTaskType),
        ("result", SDL_AsyncIOResult),
        ("buffer", ctypes.c_void_p),
        ("offset", ctypes.c_uint64),
        ("bytes_requested", ctypes.c_uint64),
        ("bytes_transferred", ctypes.c_uint64),
        ("userdata", ctypes.c_void_p)
    ]

class SDL_AsyncIOQueue(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_AsyncIOFromFile", ctypes.POINTER(SDL_AsyncIO), ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_GetAsyncIOSize", ctypes.c_int64, ctypes.POINTER(SDL_AsyncIO))

SDL_FUNC("SDL_ReadAsyncIO", ctypes.c_bool, ctypes.POINTER(SDL_AsyncIO), ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.c_void_p)
SDL_FUNC("SDL_WriteAsyncIO", ctypes.c_bool, ctypes.POINTER(SDL_AsyncIO), ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.c_void_p)
SDL_FUNC("SDL_CloseAsyncIO", ctypes.c_bool, ctypes.POINTER(SDL_AsyncIO), ctypes.c_bool, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.c_void_p)

SDL_FUNC("SDL_CreateAsyncIOQueue", ctypes.POINTER(SDL_AsyncIOQueue))
SDL_FUNC("SDL_DestroyAsyncIOQueue", None, ctypes.POINTER(SDL_AsyncIOQueue))
SDL_FUNC("SDL_GetAsyncIOResult", ctypes.c_bool, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.POINTER(SDL_AsyncIOOutcome))
SDL_FUNC("SDL_WaitAsyncIOResult", ctypes.c_bool, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.POINTER(SDL_AsyncIOOutcome), ctypes.c_int32)
SDL_FUNC("SDL_SignalAsyncIOQueue", None, ctypes.POINTER(SDL_AsyncIOQueue))

SDL_FUNC("SDL_LoadFileAsync", ctypes.c_bool, ctypes.c_char_p, ctypes.POINTER(SDL_AsyncIOQueue), ctypes.c_void_p)