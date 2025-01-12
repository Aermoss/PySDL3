from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_mouse import SDL_MouseID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_TouchID = ctypes.c_uint64
SDL_FingerID = ctypes.c_uint64

SDL_TouchDeviceType = ctypes.c_int

SDL_TOUCH_DEVICE_INVALID = -1
SDL_TOUCH_DEVICE_DIRECT = 0
SDL_TOUCH_DEVICE_INDIRECT_ABSOLUTE = 1
SDL_TOUCH_DEVICE_INDIRECT_RELATIVE = 2

class SDL_Finger(ctypes.Structure):
    _fields_ = [
        ("id", SDL_FingerID),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("pressure", ctypes.c_float)
    ]

SDL_TOUCH_MOUSEID = SDL_MouseID(-1)
SDL_MOUSE_TOUCHID = SDL_TouchID(-1)

SDL_FUNC("SDL_GetTouchDevices", ctypes.POINTER(SDL_TouchID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetTouchDeviceName", ctypes.c_char_p, SDL_TouchID)
SDL_FUNC("SDL_GetTouchDeviceType", SDL_TouchDeviceType, SDL_TouchID)
SDL_FUNC("SDL_GetTouchFingers", ctypes.POINTER(ctypes.POINTER(SDL_Finger)), SDL_TouchID, ctypes.POINTER(ctypes.c_int))
