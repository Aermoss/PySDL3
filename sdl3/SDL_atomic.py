from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_SpinLock: typing.TypeAlias = SDL_TYPE["SDL_SpinLock", ctypes.c_int]

SDL_TryLockSpinlock: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_TryLockSpinlock", ctypes.c_bool, [SDL_POINTER[SDL_SpinLock]]]
SDL_LockSpinlock: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_LockSpinlock", None, [SDL_POINTER[SDL_SpinLock]]]
SDL_UnlockSpinlock: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UnlockSpinlock", None, [SDL_POINTER[SDL_SpinLock]]]

SDL_MemoryBarrierReleaseFunction: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_MemoryBarrierReleaseFunction", None, []]
SDL_MemoryBarrierAcquireFunction: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_MemoryBarrierAcquireFunction", None, []]

class SDL_AtomicInt(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_int)
    ]

SDL_CompareAndSwapAtomicInt: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CompareAndSwapAtomicInt", ctypes.c_bool, [SDL_POINTER[SDL_AtomicInt], ctypes.c_int, ctypes.c_int]]
SDL_SetAtomicInt: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetAtomicInt", ctypes.c_int, [SDL_POINTER[SDL_AtomicInt], ctypes.c_int]]
SDL_GetAtomicInt: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetAtomicInt", ctypes.c_int, [SDL_POINTER[SDL_AtomicInt]]]
SDL_AddAtomicInt: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_AddAtomicInt", ctypes.c_int, [SDL_POINTER[SDL_AtomicInt], ctypes.c_int]]

class LP_SDL_AtomicInt(ctypes._Pointer):
    ...

def SDL_AtomicIncRef(a: LP_SDL_AtomicInt) -> ctypes.c_int:
    return SDL_GET_BINARY(SDL_BINARY).SDL_AddAtomicInt(a, 1)

def SDL_AtomicDecRef(a: LP_SDL_AtomicInt) -> ctypes.c_int:
    return SDL_GET_BINARY(SDL_BINARY).SDL_AddAtomicInt(a, -1) == 1

class SDL_AtomicU32(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_uint32)
    ]

SDL_CompareAndSwapAtomicU32: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CompareAndSwapAtomicU32", ctypes.c_bool, [SDL_POINTER[SDL_AtomicU32], ctypes.c_uint32, ctypes.c_uint32]]
SDL_SetAtomicU32: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetAtomicU32", ctypes.c_uint32, [SDL_POINTER[SDL_AtomicU32], ctypes.c_uint32]]
SDL_GetAtomicU32: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetAtomicU32", ctypes.c_uint32, [SDL_POINTER[SDL_AtomicU32]]]

SDL_CompareAndSwapAtomicPointer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CompareAndSwapAtomicPointer", ctypes.c_bool, [SDL_POINTER[ctypes.c_void_p], ctypes.c_void_p, ctypes.c_void_p]]
SDL_SetAtomicPointer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetAtomicPointer", ctypes.c_void_p, [SDL_POINTER[ctypes.c_void_p], ctypes.c_void_p]]
SDL_GetAtomicPointer: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetAtomicPointer", ctypes.c_void_p, [SDL_POINTER[ctypes.c_void_p]]]