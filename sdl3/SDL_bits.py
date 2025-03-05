from .__init__ import ctypes

def SDL_HasExactlyOneBitSet32(x: ctypes.c_uint32) -> ctypes.c_bool:
    if x and not (x & (x - 1)): return ctypes.c_bool(1)
    else: return ctypes.c_bool(0)