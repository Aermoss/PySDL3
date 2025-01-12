from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from.SDL_atomic import SDL_AtomicInt
from .SDL_thread import SDL_ThreadID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_MUTEX_TIMEDOUT = 1

class SDL_Mutex(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_CreateMutex", ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_LockMutex", None, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_TryLockMutex", ctypes.c_bool, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_UnlockMutex", None, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_DestroyMutex", None, ctypes.POINTER(SDL_Mutex))

class SDL_RWLock(ctypes.c_void_p):
    ...

SDL_RWLOCK_TIMEDOUT = SDL_MUTEX_TIMEDOUT

SDL_FUNC("SDL_CreateRWLock", ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_LockRWLockForReading", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_LockRWLockForWriting", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_TryLockRWLockForReading", ctypes.c_bool, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_TryLockRWLockForWriting", ctypes.c_bool, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_UnlockRWLock", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_DestroyRWLock", None, ctypes.POINTER(SDL_RWLock))

class SDL_Semaphore(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_CreateSemaphore", ctypes.POINTER(SDL_Semaphore), ctypes.c_uint32)
SDL_FUNC("SDL_DestroySemaphore", None, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_WaitSemaphore", None, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_TryWaitSemaphore", ctypes.c_bool, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_WaitSemaphoreTimeout", ctypes.c_bool, ctypes.POINTER(SDL_Semaphore), ctypes.c_int32)
SDL_FUNC("SDL_SignalSemaphore", None, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_GetSemaphoreValue", ctypes.c_uint32, ctypes.POINTER(SDL_Semaphore))

class SDL_Condition(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_CreateCondition", ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_DestroyCondition", None, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_SignalCondition", None, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_BroadcastCondition", None, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_WaitCondition", None, ctypes.POINTER(SDL_Condition), ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_WaitConditionTimeout", ctypes.c_bool, ctypes.POINTER(SDL_Condition), ctypes.POINTER(SDL_Mutex), ctypes.c_int32)

SDL_InitStatus = ctypes.c_int

SDL_INIT_STATUS_UNINITIALIZED = 0
SDL_INIT_STATUS_INITIALIZING = 1
SDL_INIT_STATUS_INITIALIZED = 2
SDL_INIT_STATUS_UNINITIALIZING = 3

class SDL_InitState(ctypes.Structure):
    _fields_ = [
        ("status", SDL_AtomicInt),
        ("error", SDL_ThreadID),
        ("reserved", ctypes.c_void_p)
    ]

SDL_FUNC("SDL_ShouldInit", ctypes.c_bool, ctypes.POINTER(SDL_InitState))
SDL_FUNC("SDL_ShouldQuit", ctypes.c_bool, ctypes.POINTER(SDL_InitState))

SDL_FUNC("SDL_SetInitialized", None, ctypes.POINTER(SDL_InitState), ctypes.c_bool)