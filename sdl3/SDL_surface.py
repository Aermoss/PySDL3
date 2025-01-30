from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_pixels import SDL_PixelFormat, SDL_Colorspace, SDL_Palette
from .SDL_properties import SDL_PropertiesID
from .SDL_blendmode import SDL_BlendMode
from .SDL_iostream import SDL_IOStream
from .SDL_rect import SDL_Rect

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_SurfaceFlags = ctypes.c_uint32

SDL_SURFACE_PREALLOCATED = 0x00000001
SDL_SURFACE_LOCK_NEEDED = 0x00000002
SDL_SURFACE_LOCKED = 0x00000004
SDL_SURFACE_SIMD_ALIGNED = 0x00000008

SDL_MUSTLOCK = lambda s: (s.flags & SDL_SURFACE_LOCK_NEEDED) == SDL_SURFACE_LOCK_NEEDED

SDL_ScaleMode = ctypes.c_uint32

SDL_SCALEMODE_NEAREST = 0
SDL_SCALEMODE_LINEAR = 1

SDL_FlipMode = ctypes.c_uint32

SDL_FLIP_NONE = 0
SDL_FLIP_HORIZONTAL = 1
SDL_FLIP_VERTICAL = 2

class SDL_Surface(ctypes.Structure):
    _fields_ = [
        ("flags", SDL_SurfaceFlags),
        ("format", SDL_PixelFormat),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pitch", ctypes.c_int),
        ("pixels", ctypes.c_void_p),
        ("refcount", ctypes.c_int),
        ("reserved", ctypes.c_void_p)
    ]

SDL_FUNC("SDL_CreateSurface", ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, SDL_PixelFormat)
SDL_FUNC("SDL_CreateSurfaceFrom", ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, SDL_PixelFormat, ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_DestroySurface", None, ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_GetSurfaceProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Surface))

SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT = "SDL.surface.SDR_white_point".encode()
SDL_PROP_SURFACE_HDR_HEADROOM_FLOAT = "SDL.surface.HDR_headroom".encode()
SDL_PROP_SURFACE_TONEMAP_OPERATOR_STRING = "SDL.surface.tonemap".encode()

SDL_FUNC("SDL_SetSurfaceColorspace", ctypes.c_bool, ctypes.POINTER(SDL_Surface), SDL_Colorspace)
SDL_FUNC("SDL_GetSurfaceColorspace", SDL_Colorspace, ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_CreateSurfacePalette", ctypes.POINTER(SDL_Palette), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_SetSurfacePalette", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Palette))
SDL_FUNC("SDL_GetSurfacePalette", ctypes.POINTER(SDL_Palette), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_AddSurfaceAlternateImage", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_SurfaceHasAlternateImages", ctypes.c_bool, ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_GetSurfaceImages", ctypes.POINTER(ctypes.POINTER(SDL_Surface)), ctypes.POINTER(SDL_Surface), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_RemoveSurfaceAlternateImages", None, ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_LockSurface", ctypes.c_bool, ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_UnlockSurface", None, ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_LoadBMP_IO", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_IOStream), ctypes.c_bool)
SDL_FUNC("SDL_LoadBMP", ctypes.POINTER(SDL_Surface), ctypes.c_char_p)

SDL_FUNC("SDL_SaveBMP_IO", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_IOStream), ctypes.c_bool)
SDL_FUNC("SDL_SaveBMP", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_char_p)

SDL_FUNC("SDL_SetSurfaceRLE", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_bool)
SDL_FUNC("SDL_SurfaceHasRLE", ctypes.c_bool, ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_SetSurfaceColorKey", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_bool, ctypes.c_uint32)
SDL_FUNC("SDL_SurfaceHasColorKey", ctypes.c_bool, ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_GetSurfaceColorKey", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(ctypes.c_uint32))

SDL_FUNC("SDL_SetSurfaceColorMod", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_GetSurfaceColorMod", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))

SDL_FUNC("SDL_SetSurfaceAlphaMod", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_uint8)
SDL_FUNC("SDL_GetSurfaceAlphaMod", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(ctypes.c_uint8))

SDL_FUNC("SDL_SetSurfaceBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Surface), SDL_BlendMode)
SDL_FUNC("SDL_GetSurfaceBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_BlendMode))

SDL_FUNC("SDL_SetSurfaceClipRect", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetSurfaceClipRect", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_FlipSurface", ctypes.c_bool, ctypes.POINTER(SDL_Surface), SDL_FlipMode)
SDL_FUNC("SDL_DuplicateSurface", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_ScaleSurface", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, SDL_ScaleMode)

SDL_FUNC("SDL_ConvertSurface", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Surface), SDL_PixelFormat)
SDL_FUNC("SDL_ConvertSurfaceAndColorspace", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Surface), SDL_PixelFormat, ctypes.POINTER(SDL_Palette), SDL_Colorspace, SDL_PropertiesID)
SDL_FUNC("SDL_ConvertPixels", ctypes.c_bool, ctypes.c_int, ctypes.c_int, SDL_PixelFormat, ctypes.c_void_p, ctypes.c_int, SDL_PixelFormat, ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_ConvertPixelsAndColorspace", ctypes.c_bool, ctypes.c_int, ctypes.c_int, SDL_PixelFormat, SDL_Colorspace, SDL_PropertiesID, ctypes.c_void_p, ctypes.c_int, SDL_PixelFormat, SDL_Colorspace, SDL_PropertiesID, ctypes.c_void_p, ctypes.c_int)

SDL_FUNC("SDL_PremultiplyAlpha", ctypes.c_bool, ctypes.c_int, ctypes.c_int, SDL_PixelFormat, ctypes.c_void_p, ctypes.c_int, SDL_PixelFormat, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)
SDL_FUNC("SDL_PremultiplySurfaceAlpha", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_bool)

SDL_FUNC("SDL_ClearSurface", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)

SDL_FUNC("SDL_FillSurfaceRect", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.c_uint32)
SDL_FUNC("SDL_FillSurfaceRects", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.c_int, ctypes.c_uint32)

SDL_FUNC("SDL_BlitSurface", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_BlitSurfaceUnchecked", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_BlitSurfaceScaled", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), SDL_ScaleMode)
SDL_FUNC("SDL_BlitSurfaceUncheckedScaled", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), SDL_ScaleMode)
SDL_FUNC("SDL_BlitSurfaceTiled", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_BlitSurfaceTiledWithScale", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.c_float, SDL_ScaleMode, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_BlitSurface9Grid", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float, SDL_ScaleMode, ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_MapSurfaceRGB", ctypes.c_uint32, ctypes.POINTER(SDL_Surface), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_MapSurfaceRGBA", ctypes.c_uint32, ctypes.POINTER(SDL_Surface), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)

SDL_FUNC("SDL_ReadSurfacePixel", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_ReadSurfacePixelFloat", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_WriteSurfacePixel", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_WriteSurfacePixelFloat", ctypes.c_bool, ctypes.POINTER(SDL_Surface), ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)