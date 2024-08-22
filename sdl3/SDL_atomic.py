from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_GET_DLL, SDL_DLL

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_SpinLock = ctypes.c_int

SDL_FUNC("SDL_TryLockSpinlock", ctypes.c_bool, ctypes.POINTER(SDL_SpinLock))
SDL_FUNC("SDL_LockSpinlock", None, ctypes.POINTER(SDL_SpinLock))
SDL_FUNC("SDL_UnlockSpinlock", None, ctypes.POINTER(SDL_SpinLock))

SDL_FUNC("SDL_MemoryBarrierReleaseFunction", None)
SDL_FUNC("SDL_MemoryBarrierAcquireFunction", None)

class SDL_AtomicInt(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_int)
    ]

SDL_FUNC("SDL_AtomicCompareAndSwap", ctypes.c_bool, ctypes.POINTER(SDL_AtomicInt), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_AtomicSet", ctypes.c_int, ctypes.POINTER(SDL_AtomicInt), ctypes.c_int)
SDL_FUNC("SDL_AtomicGet", ctypes.c_int, ctypes.POINTER(SDL_AtomicInt))
SDL_FUNC("SDL_AtomicAdd", ctypes.c_int, ctypes.POINTER(SDL_AtomicInt), ctypes.c_int)

class LP_SDL_AtomicInt(ctypes._Pointer):
    ...

def SDL_AtomicIncRef(a: LP_SDL_AtomicInt) -> ctypes.c_int:
    return SDL_GET_DLL(SDL_DLL).SDL_AtomicAdd(a, 1)

def SDL_AtomicDecRef(a: LP_SDL_AtomicInt) -> ctypes.c_int:
    return SDL_GET_DLL(SDL_DLL).SDL_AtomicAdd(a, -1) == 1

SDL_FUNC("SDL_AtomicCompareAndSwapPointer", ctypes.c_bool, ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.c_void_p)
SDL_FUNC("SDL_AtomicSetPtr", ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p)
SDL_FUNC("SDL_AtomicGetPtr", ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))