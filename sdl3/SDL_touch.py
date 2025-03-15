from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_mouse import SDL_MouseID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_TouchID: typing.TypeAlias = SDL_TYPE["SDL_TouchID", ctypes.c_uint64]
SDL_FingerID: typing.TypeAlias = SDL_TYPE["SDL_FingerID", ctypes.c_uint64]

SDL_TouchDeviceType: typing.TypeAlias = SDL_TYPE["SDL_TouchDeviceType", ctypes.c_int]

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

SDL_GetTouchDevices: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTouchDevices", SDL_POINTER[SDL_TouchID], [SDL_POINTER[ctypes.c_int]]]
SDL_GetTouchDeviceName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTouchDeviceName", ctypes.c_char_p, [SDL_TouchID]]
SDL_GetTouchDeviceType: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTouchDeviceType", SDL_TouchDeviceType, [SDL_TouchID]]
SDL_GetTouchFingers: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetTouchFingers", SDL_POINTER[SDL_POINTER[SDL_Finger]], [SDL_TouchID, SDL_POINTER[ctypes.c_int]]]
