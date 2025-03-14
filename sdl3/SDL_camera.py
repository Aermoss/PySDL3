from .__init__ import ctypes, typing, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_pixels import SDL_PixelFormat, SDL_Colorspace
from .SDL_properties import SDL_PropertiesID
from .SDL_surface import SDL_Surface

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_CameraID: typing.TypeAlias = SDL_TYPE["SDL_CameraID", ctypes.c_uint32]

class SDL_Camera(ctypes.c_void_p):
    ...

class SDL_CameraSpec(ctypes.Structure):
    _fields_ = [
        ("format", SDL_POINTER[SDL_PixelFormat]),
        ("colorspace", SDL_Colorspace),
        ("width", ctypes.c_int),
        ("height", ctypes.c_int),
        ("framerate_numerator", ctypes.c_int),
        ("framerate_denominator", ctypes.c_int)
    ]

SDL_CameraPosition: typing.TypeAlias = SDL_TYPE["SDL_CameraPosition", ctypes.c_int]

SDL_CAMERA_POSITION_UNKNOWN = 0
SDL_CAMERA_POSITION_FRONT_FACING = 1
SDL_CAMERA_POSITION_BACK_FACING = 2

SDL_FUNC("SDL_GetNumCameraDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetCameraDriver", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_GetCurrentCameraDriver", ctypes.c_char_p)
SDL_FUNC("SDL_GetCameras", SDL_POINTER[SDL_CameraID], SDL_POINTER[ctypes.c_int])
SDL_FUNC("SDL_GetCameraSupportedFormats", SDL_POINTER[SDL_POINTER[SDL_CameraSpec]], SDL_CameraID, SDL_POINTER[ctypes.c_int])
SDL_FUNC("SDL_GetCameraName", ctypes.c_char_p, SDL_CameraID)
SDL_FUNC("SDL_GetCameraPosition", SDL_CameraPosition, SDL_CameraID)
SDL_FUNC("SDL_OpenCamera", SDL_POINTER[SDL_Camera], SDL_CameraID, SDL_POINTER[SDL_CameraSpec])
SDL_FUNC("SDL_GetCameraPermissionState", ctypes.c_int, SDL_POINTER[SDL_Camera])
SDL_FUNC("SDL_GetCameraID", SDL_CameraID, SDL_POINTER[SDL_Camera])
SDL_FUNC("SDL_GetCameraProperties", SDL_PropertiesID, SDL_POINTER[SDL_Camera])
SDL_FUNC("SDL_GetCameraFormat", ctypes.c_bool, SDL_POINTER[SDL_Camera], SDL_POINTER[SDL_CameraSpec])
SDL_FUNC("SDL_AcquireCameraFrame", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_Camera], SDL_POINTER[ctypes.c_int64])
SDL_FUNC("SDL_ReleaseCameraFrame", None, SDL_POINTER[SDL_Camera], SDL_POINTER[SDL_Surface])
SDL_FUNC("SDL_CloseCamera", None, SDL_POINTER[SDL_Camera])