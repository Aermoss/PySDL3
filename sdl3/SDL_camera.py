from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_pixels import SDL_PixelFormat, SDL_Colorspace
from .SDL_properties import SDL_PropertiesID
from .SDL_surface import SDL_Surface

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_CameraID = ctypes.c_uint32

class SDL_Camera(ctypes.c_void_p):
    ...

class SDL_CameraSpec(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.POINTER(SDL_PixelFormat)),
        ("colorspace", SDL_Colorspace),
        ("width", ctypes.c_int),
        ("height", ctypes.c_int),
        ("framerate_numerator", ctypes.c_int),
        ("framerate_denominator", ctypes.c_int)
    ]

SDL_CameraPosition = ctypes.c_int

SDL_CAMERA_POSITION_UNKNOWN = 0
SDL_CAMERA_POSITION_FRONT_FACING = 1
SDL_CAMERA_POSITION_BACK_FACING = 2

SDL_FUNC("SDL_GetNumCameraDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetCameraDriver", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_GetCurrentCameraDriver", ctypes.c_char_p)
SDL_FUNC("SDL_GetCameras", ctypes.POINTER(SDL_CameraID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetCameraSupportedFormats", ctypes.POINTER(ctypes.POINTER(SDL_CameraSpec)), SDL_CameraID, ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetCameraName", ctypes.c_char_p, SDL_CameraID)
SDL_FUNC("SDL_GetCameraPosition", SDL_CameraPosition, SDL_CameraID)
SDL_FUNC("SDL_OpenCamera", ctypes.POINTER(SDL_Camera), SDL_CameraID, ctypes.POINTER(SDL_CameraSpec))
SDL_FUNC("SDL_GetCameraPermissionState", ctypes.c_int, ctypes.POINTER(SDL_Camera))
SDL_FUNC("SDL_GetCameraID", SDL_CameraID, ctypes.POINTER(SDL_Camera))
SDL_FUNC("SDL_GetCameraProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Camera))
SDL_FUNC("SDL_GetCameraFormat", ctypes.c_bool, ctypes.POINTER(SDL_Camera), ctypes.POINTER(SDL_CameraSpec))
SDL_FUNC("SDL_AcquireCameraFrame", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Camera), ctypes.POINTER(ctypes.c_int64))
SDL_FUNC("SDL_ReleaseCameraFrame", None, ctypes.POINTER(SDL_Camera), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_CloseCamera", None, ctypes.POINTER(SDL_Camera))