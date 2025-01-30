from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

from .SDL_atomic import SDL_AtomicInt
from .SDL_stdinc import SDL_FunctionPointer
from .SDL_properties import SDL_PropertiesID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Thread(ctypes.c_void_p):
    ...

SDL_ThreadID = ctypes.c_uint64
SDL_TLSID = SDL_AtomicInt

SDL_ThreadPriority = ctypes.c_int

SDL_THREAD_PRIORITY_LOW = 0
SDL_THREAD_PRIORITY_NORMAL = 1
SDL_THREAD_PRIORITY_HIGH = 2
SDL_THREAD_PRIORITY_TIME_CRITICAL = 3

SDL_ThreadState = ctypes.c_int

SDL_THREAD_UNKNOWN = 0
SDL_THREAD_ALIVE = 1
SDL_THREAD_DETACHED = 2
SDL_THREAD_COMPLETE = 3

SDL_ThreadFunction = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

SDL_BeginThreadFunction = SDL_FunctionPointer(0)
SDL_EndThreadFunction = SDL_FunctionPointer(0)

SDL_FUNC("SDL_CreateThreadRuntime", ctypes.POINTER(SDL_Thread), SDL_ThreadFunction, ctypes.c_char_p, ctypes.c_void_p, SDL_FunctionPointer, SDL_FunctionPointer)
SDL_FUNC("SDL_CreateThreadWithPropertiesRuntime", ctypes.POINTER(SDL_Thread), SDL_PropertiesID, SDL_FunctionPointer, SDL_FunctionPointer)

SDL_CreateThread = lambda fn, name, data: \
    SDL_GET_BINARY(SDL_BINARY).SDL_CreateThreadRuntime(fn, name, data, SDL_BeginThreadFunction, SDL_EndThreadFunction)

SDL_CreateThreadWithProperties = lambda props: \
    SDL_GET_BINARY(SDL_BINARY).SDL_CreateThreadWithPropertiesRuntime(props, SDL_BeginThreadFunction, SDL_EndThreadFunction)

SDL_PROP_THREAD_CREATE_ENTRY_FUNCTION_POINTER = "SDL.thread.create.entry_function".encode()
SDL_PROP_THREAD_CREATE_NAME_STRING = "SDL.thread.create.name".encode()
SDL_PROP_THREAD_CREATE_USERDATA_POINTER = "SDL.thread.create.userdata".encode()
SDL_PROP_THREAD_CREATE_STACKSIZE_NUMBER = "SDL.thread.create.stacksize".encode()

SDL_FUNC("SDL_GetThreadName", ctypes.c_char_p, ctypes.POINTER(SDL_Thread))
SDL_FUNC("SDL_GetCurrentThreadID", SDL_ThreadID)
SDL_FUNC("SDL_GetThreadID", SDL_ThreadID, ctypes.POINTER(SDL_Thread))
SDL_FUNC("SDL_SetCurrentThreadPriority", ctypes.c_bool, SDL_ThreadPriority)
SDL_FUNC("SDL_WaitThread", None, ctypes.POINTER(SDL_Thread), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetThreadState", SDL_ThreadState, ctypes.POINTER(SDL_Thread))
SDL_FUNC("SDL_DetachThread", None, ctypes.POINTER(SDL_Thread))
SDL_FUNC("SDL_GetTLS", ctypes.c_void_p, ctypes.POINTER(SDL_TLSID))

SDL_TLSDestructorCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

SDL_FUNC("SDL_SetTLS", ctypes.c_bool, ctypes.POINTER(SDL_TLSID), ctypes.c_void_p, SDL_TLSDestructorCallback)
SDL_FUNC("SDL_CleanupTLS", None)