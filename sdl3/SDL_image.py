from .__init__ import ctypes, SDL_POINTER, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_IMAGE_BINARY

from .SDL_surface import SDL_Surface
from .SDL_render import SDL_Texture, SDL_Renderer
from .SDL_iostream import SDL_IOStream
from .SDL_version import SDL_VERSIONNUM

SDL_SET_CURRENT_BINARY(SDL_IMAGE_BINARY)

SDL_IMAGE_MAJOR_VERSION = 3
SDL_IMAGE_MINOR_VERSION = 2
SDL_IMAGE_MICRO_VERSION = 4

SDL_IMAGE_VERSION = \
    SDL_VERSIONNUM(SDL_IMAGE_MAJOR_VERSION, SDL_IMAGE_MINOR_VERSION, SDL_IMAGE_MICRO_VERSION)

SDL_IMAGE_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_IMAGE_MAJOR_VERSION >= x) and \
    (SDL_IMAGE_MAJOR_VERSION > x or SDL_IMAGE_MINOR_VERSION >= y) and \
    (SDL_IMAGE_MAJOR_VERSION > x or SDL_IMAGE_MINOR_VERSION > y or SDL_IMAGE_MICRO_VERSION >= z)

SDL_FUNC("IMG_Version", ctypes.c_int)

SDL_FUNC("IMG_LoadTyped_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("IMG_Load", SDL_POINTER[SDL_Surface], ctypes.c_char_p)
SDL_FUNC("IMG_Load_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool)

SDL_FUNC("IMG_LoadTexture", SDL_POINTER[SDL_Texture], SDL_POINTER[SDL_Renderer], ctypes.c_char_p)
SDL_FUNC("IMG_LoadTexture_IO", SDL_POINTER[SDL_Texture], SDL_POINTER[SDL_Renderer], SDL_POINTER[SDL_IOStream], ctypes.c_bool)
SDL_FUNC("IMG_LoadTextureTyped_IO", SDL_POINTER[SDL_Texture], SDL_POINTER[SDL_Renderer], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p)

SDL_FUNC("IMG_isAVIF", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isICO", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isCUR", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isBMP", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isGIF", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isJPG", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isJXL", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isLBM", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isPCX", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isPNG", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isPNM", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isSVG", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isQOI", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isTIF", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isXCF", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isXPM", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isXV", ctypes.c_bool, SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_isWEBP", ctypes.c_bool, SDL_POINTER[SDL_IOStream])

SDL_FUNC("IMG_LoadAVIF_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadICO_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadCUR_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadBMP_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadGIF_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadJPG_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadJXL_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadLBM_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadPCX_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadPNG_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadPNM_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadSVG_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadQOI_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadTGA_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadTIF_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadXCF_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadXPM_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadXV_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadWEBP_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadSizedSVG_IO", SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_int, ctypes.c_int)

SDL_FUNC("IMG_ReadXPMFromArray", SDL_POINTER[SDL_Surface], SDL_POINTER[ctypes.c_char_p])
SDL_FUNC("IMG_ReadXPMFromArrayToRGB888", SDL_POINTER[SDL_Surface], SDL_POINTER[ctypes.c_char_p])

SDL_FUNC("IMG_SaveAVIF", ctypes.c_bool, SDL_POINTER[SDL_Surface], ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("IMG_SaveAVIF_IO", ctypes.c_bool, SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int)
SDL_FUNC("IMG_SavePNG", ctypes.c_bool, SDL_POINTER[SDL_Surface], ctypes.c_char_p)
SDL_FUNC("IMG_SavePNG_IO", ctypes.c_bool, SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool)
SDL_FUNC("IMG_SaveJPG", ctypes.c_bool, SDL_POINTER[SDL_Surface], ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("IMG_SaveJPG_IO", ctypes.c_bool, SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int)

class IMG_Animation(ctypes.Structure):
    _fields_ = [
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("count", ctypes.c_int),
        ("frames", SDL_POINTER[SDL_POINTER[SDL_Surface]]),
        ("delays", SDL_POINTER[ctypes.c_int])
    ]

SDL_FUNC("IMG_LoadAnimation", SDL_POINTER[IMG_Animation], ctypes.c_char_p)
SDL_FUNC("IMG_LoadAnimation_IO", SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool)
SDL_FUNC("IMG_LoadAnimationTyped_IO", SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("IMG_FreeAnimation", None, SDL_POINTER[IMG_Animation])
SDL_FUNC("IMG_LoadGIFAnimation_IO", SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream])
SDL_FUNC("IMG_LoadWEBPAnimation_IO", SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream])