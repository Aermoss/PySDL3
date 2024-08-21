from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_MUTEX_TIMEDOUT = 1

class SDL_Mutex(ctypes.Structure):
    ...

SDL_FUNC("SDL_CreateMutex", ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_LockMutex", None, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_TryLockMutex", ctypes.c_int, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_UnlockMutex", None, ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_DestroyMutex", None, ctypes.POINTER(SDL_Mutex))

class SDL_RWLock(ctypes.Structure):
    ...

SDL_RWLOCK_TIMEDOUT = SDL_MUTEX_TIMEDOUT

SDL_FUNC("SDL_CreateRWLock", ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_LockRWLockForReading", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_LockRWLockForWriting", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_TryLockRWLockForReading", ctypes.c_int, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_TryLockRWLockForWriting", ctypes.c_int, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_UnlockRWLock", None, ctypes.POINTER(SDL_RWLock))
SDL_FUNC("SDL_DestroyRWLock", None, ctypes.POINTER(SDL_RWLock))

class SDL_Semaphore(ctypes.Structure):
    ...

SDL_FUNC("SDL_CreateSemaphore", ctypes.POINTER(SDL_Semaphore), ctypes.c_uint32)
SDL_FUNC("SDL_DestroySemaphore", None, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_WaitSemaphore", ctypes.c_int, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_TryWaitSemaphore", ctypes.c_int, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_WaitSemaphoreTimeout", ctypes.c_int, ctypes.POINTER(SDL_Semaphore), ctypes.c_int32)
SDL_FUNC("SDL_SignalSemaphore", ctypes.c_int, ctypes.POINTER(SDL_Semaphore))
SDL_FUNC("SDL_GetSemaphoreValue", ctypes.c_uint32, ctypes.POINTER(SDL_Semaphore))

class SDL_Condition(ctypes.Structure):
    ...

SDL_FUNC("SDL_CreateCondition", ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_DestroyCondition", None, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_SignalCondition", ctypes.c_int, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_BroadcastCondition", ctypes.c_int, ctypes.POINTER(SDL_Condition))
SDL_FUNC("SDL_WaitCondition", ctypes.c_int, ctypes.POINTER(SDL_Condition), ctypes.POINTER(SDL_Mutex))
SDL_FUNC("SDL_WaitConditionTimeout", ctypes.c_int, ctypes.POINTER(SDL_Condition), ctypes.POINTER(SDL_Mutex), ctypes.c_int32)