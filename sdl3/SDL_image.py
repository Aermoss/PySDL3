import ctypes, typing, collections.abc as abc

from . import SDL_POINTER, SDL_FUNC, \
    SDL_IMAGE_BINARY, SDL_TYPE, SDL_ENUM
from .SDL_gpu import SDL_GPUTexture, SDL_GPUDevice, SDL_GPUCopyPass
from .SDL_surface import SDL_Surface
from .SDL_render import SDL_Texture, SDL_Renderer
from .SDL_iostream import SDL_IOStream
from .SDL_properties import SDL_PropertiesID
from .SDL_mouse import SDL_Cursor
from .SDL_version import SDL_VERSIONNUM

SDL_IMAGE_MAJOR_VERSION, SDL_IMAGE_MINOR_VERSION, SDL_IMAGE_MICRO_VERSION = 3, 4, 0
SDL_IMAGE_VERSION: int = SDL_VERSIONNUM(SDL_IMAGE_MAJOR_VERSION, SDL_IMAGE_MINOR_VERSION, SDL_IMAGE_MICRO_VERSION)

SDL_IMAGE_VERSION_ATLEAST: abc.Callable[[int, int, int], bool] = lambda x, y, z: \
    (SDL_IMAGE_MAJOR_VERSION >= x) and (SDL_IMAGE_MAJOR_VERSION > x or SDL_IMAGE_MINOR_VERSION >= y) and \
        (SDL_IMAGE_MAJOR_VERSION > x or SDL_IMAGE_MINOR_VERSION > y or SDL_IMAGE_MICRO_VERSION >= z)

IMG_Version: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_Version", ctypes.c_int, [], SDL_IMAGE_BINARY]

IMG_Load: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_Load", SDL_POINTER[SDL_Surface], [ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_Load_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_Load_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_LoadTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTyped_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]

IMG_LoadTexture: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTexture", SDL_POINTER[SDL_Texture], [SDL_POINTER[SDL_Renderer], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_LoadTexture_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTexture_IO", SDL_POINTER[SDL_Texture], [SDL_POINTER[SDL_Renderer], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_LoadTextureTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTextureTyped_IO", SDL_POINTER[SDL_Texture], [SDL_POINTER[SDL_Renderer], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]

IMG_LoadGPUTexture: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadGPUTexture", SDL_POINTER[SDL_GPUTexture], [SDL_POINTER[SDL_GPUDevice], SDL_POINTER[SDL_GPUCopyPass], ctypes.c_char_p, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]], SDL_IMAGE_BINARY]
IMG_LoadGPUTexture_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadGPUTexture_IO", SDL_POINTER[SDL_GPUTexture], [SDL_POINTER[SDL_GPUDevice], SDL_POINTER[SDL_GPUCopyPass], SDL_POINTER[SDL_IOStream], ctypes.c_bool, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]], SDL_IMAGE_BINARY]
IMG_LoadGPUTextureTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadGPUTextureTyped_IO", SDL_POINTER[SDL_GPUTexture], [SDL_POINTER[SDL_GPUDevice], SDL_POINTER[SDL_GPUCopyPass], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]], SDL_IMAGE_BINARY]

IMG_GetClipboardImage: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_GetClipboardImage", SDL_POINTER[SDL_Surface], [], SDL_IMAGE_BINARY]

IMG_isANI: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isANI", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isAVIF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isAVIF", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isCUR: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isCUR", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isBMP: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isBMP", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isGIF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isGIF", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isICO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isICO", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isJPG: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isJPG", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isJXL: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isJXL", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isLBM: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isLBM", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isPCX: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isPCX", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isPNG: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isPNG", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isPNM: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isPNM", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isQOI: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isQOI", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isSVG: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isSVG", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isTIF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isTIF", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isWEBP: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isWEBP", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isXCF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isXCF", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isXPM: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isXPM", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_isXV: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_isXV", ctypes.c_bool, [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]

IMG_LoadAVIF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAVIF_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadBMP_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadBMP_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadCUR_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadCUR_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadGIF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadGIF_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadICO_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadICO_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadJPG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadJPG_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadJXL_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadJXL_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadLBM_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadLBM_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadPCX_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadPCX_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadPNG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadPNG_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadPNM_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadPNM_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadQOI_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadQOI_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadSVG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadSVG_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadSizedSVG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadSizedSVG_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream], ctypes.c_int, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_LoadTGA_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTGA_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadTIF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadTIF_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadWEBP_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadWEBP_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadXCF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadXCF_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadXPM_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadXPM_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadXV_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadXV_IO", SDL_POINTER[SDL_Surface], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]

IMG_ReadXPMFromArray: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_ReadXPMFromArray", SDL_POINTER[SDL_Surface], [SDL_POINTER[ctypes.c_char_p]], SDL_IMAGE_BINARY]
IMG_ReadXPMFromArrayToRGB888: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_ReadXPMFromArrayToRGB888", SDL_POINTER[SDL_Surface], [SDL_POINTER[ctypes.c_char_p]], SDL_IMAGE_BINARY]

IMG_Save: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_Save", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveTyped_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveAVIF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAVIF", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_SaveAVIF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAVIF_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_SaveBMP: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveBMP", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveBMP_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveBMP_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveCUR: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveCUR", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveCUR_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveCUR_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveGIF: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveGIF", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveGIF_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveGIF_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveICO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveICO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveICO_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveICO_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveJPG: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveJPG", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_SaveJPG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveJPG_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_SavePNG: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SavePNG", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SavePNG_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SavePNG_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveTGA: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveTGA", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveTGA_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveTGA_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveWEBP: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveWEBP", ctypes.c_bool, [SDL_POINTER[SDL_Surface], ctypes.c_char_p, ctypes.c_float], SDL_IMAGE_BINARY]
IMG_SaveWEBP_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveWEBP_IO", ctypes.c_bool, [SDL_POINTER[SDL_Surface], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_float], SDL_IMAGE_BINARY]

class IMG_Animation(ctypes.Structure):
    _fields_ = [
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("count", ctypes.c_int),
        ("frames", SDL_POINTER[SDL_POINTER[SDL_Surface]]),
        ("delays", SDL_POINTER[ctypes.c_int])
    ]

IMG_LoadAnimation: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAnimation", SDL_POINTER[IMG_Animation], [ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_LoadAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_LoadAnimationTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAnimationTyped_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]

IMG_LoadANIAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadANIAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadAPNGAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAPNGAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadAVIFAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadAVIFAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadGIFAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadGIFAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]
IMG_LoadWEBPAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_LoadWEBPAnimation_IO", SDL_POINTER[IMG_Animation], [SDL_POINTER[SDL_IOStream]], SDL_IMAGE_BINARY]

IMG_SaveAnimation: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAnimation", ctypes.c_bool, [SDL_POINTER[IMG_Animation], ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveAnimationTyped_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAnimationTyped_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_SaveANIAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveANIAnimation_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveAPNGAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAPNGAnimation_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveAVIFAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveAVIFAnimation_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int], SDL_IMAGE_BINARY]
IMG_SaveGIFAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveGIFAnimation_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_IMAGE_BINARY]
IMG_SaveWEBPAnimation_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_SaveWEBPAnimation_IO", ctypes.c_bool, [SDL_POINTER[IMG_Animation], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_int], SDL_IMAGE_BINARY]

IMG_CreateAnimatedCursor: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimatedCursor", SDL_POINTER[SDL_Cursor], [SDL_POINTER[IMG_Animation], ctypes.c_int, ctypes.c_int], SDL_IMAGE_BINARY]

IMG_FreeAnimation: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_FreeAnimation", None, [SDL_POINTER[IMG_Animation]], SDL_IMAGE_BINARY]

class IMG_AnimationEncoder(ctypes.c_void_p):
    ...

IMG_CreateAnimationEncoder: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationEncoder", SDL_POINTER[IMG_AnimationEncoder], [ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_CreateAnimationEncoder_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationEncoder_IO", SDL_POINTER[IMG_AnimationEncoder], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_CreateAnimationEncoderWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationEncoderWithProperties", SDL_POINTER[IMG_AnimationEncoder], [SDL_PropertiesID], SDL_IMAGE_BINARY]

IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING: bytes = "SDL_image.animation_encoder.create.filename".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER: bytes = "SDL_image.animation_encoder.create.iostream".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN: bytes = "SDL_image.animation_encoder.create.iostream.autoclose".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_TYPE_STRING: bytes = "SDL_image.animation_encoder.create.type".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_QUALITY_NUMBER: bytes = "SDL_image.animation_encoder.create.quality".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_NUMERATOR_NUMBER: bytes = "SDL_image.animation_encoder.create.timebase.numerator".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER: bytes = "SDL_image.animation_encoder.create.timebase.denominator".encode()

IMG_PROP_ANIMATION_ENCODER_CREATE_AVIF_MAX_THREADS_NUMBER: bytes = "SDL_image.animation_encoder.create.avif.max_threads".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_AVIF_KEYFRAME_INTERVAL_NUMBER: bytes = "SDL_image.animation_encoder.create.avif.keyframe_interval".encode()
IMG_PROP_ANIMATION_ENCODER_CREATE_GIF_USE_LUT_BOOLEAN: bytes = "SDL_image.animation_encoder.create.gif.use_lut".encode()

IMG_AddAnimationEncoderFrame: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_AddAnimationEncoderFrame", ctypes.c_bool, [SDL_POINTER[IMG_AnimationEncoder], SDL_POINTER[SDL_Surface], ctypes.c_uint64], SDL_IMAGE_BINARY]
IMG_CloseAnimationEncoder: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CloseAnimationEncoder", ctypes.c_bool, [SDL_POINTER[IMG_AnimationEncoder]], SDL_IMAGE_BINARY]

IMG_AnimationDecoderStatus: typing.TypeAlias = SDL_TYPE["IMG_AnimationDecoderStatus", SDL_ENUM]

IMG_DECODER_STATUS_INVALID, IMG_DECODER_STATUS_OK, IMG_DECODER_STATUS_FAILED, IMG_DECODER_STATUS_COMPLETE = range(-1, 3)

class IMG_AnimationDecoder(ctypes.c_void_p):
    ...

IMG_CreateAnimationDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationDecoder", SDL_POINTER[IMG_AnimationDecoder], [ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_CreateAnimationDecoder_IO: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationDecoder_IO", SDL_POINTER[IMG_AnimationDecoder], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_char_p], SDL_IMAGE_BINARY]
IMG_CreateAnimationDecoderWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CreateAnimationDecoderWithProperties", SDL_POINTER[IMG_AnimationDecoder], [SDL_PropertiesID], SDL_IMAGE_BINARY]

IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING: bytes = "SDL_image.animation_decoder.create.filename".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER: bytes = "SDL_image.animation_decoder.create.iostream".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN: bytes = "SDL_image.animation_decoder.create.iostream.autoclose".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_TYPE_STRING: bytes = "SDL_image.animation_decoder.create.type".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_NUMERATOR_NUMBER: bytes = "SDL_image.animation_decoder.create.timebase.numerator".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER: bytes = "SDL_image.animation_decoder.create.timebase.denominator".encode()

IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_MAX_THREADS_NUMBER: bytes = "SDL_image.animation_decoder.create.avif.max_threads".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_ALLOW_INCREMENTAL_BOOLEAN: bytes = "SDL_image.animation_decoder.create.avif.allow_incremental".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_ALLOW_PROGRESSIVE_BOOLEAN: bytes = "SDL_image.animation_decoder.create.avif.allow_progressive".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_GIF_TRANSPARENT_COLOR_INDEX_NUMBER: bytes = "SDL_image.animation_encoder.create.gif.transparent_color_index".encode()
IMG_PROP_ANIMATION_DECODER_CREATE_GIF_NUM_COLORS_NUMBER: bytes = "SDL_image.animation_encoder.create.gif.num_colors".encode()

IMG_GetAnimationDecoderProperties: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_GetAnimationDecoderProperties", SDL_PropertiesID, [SDL_POINTER[IMG_AnimationDecoder]], SDL_IMAGE_BINARY]

IMG_PROP_METADATA_IGNORE_PROPS_BOOLEAN: bytes = "SDL_image.metadata.ignore_props".encode()
IMG_PROP_METADATA_DESCRIPTION_STRING: bytes = "SDL_image.metadata.description".encode()
IMG_PROP_METADATA_COPYRIGHT_STRING: bytes = "SDL_image.metadata.copyright".encode()
IMG_PROP_METADATA_TITLE_STRING: bytes = "SDL_image.metadata.title".encode()
IMG_PROP_METADATA_AUTHOR_STRING: bytes = "SDL_image.metadata.author".encode()
IMG_PROP_METADATA_CREATION_TIME_STRING: bytes = "SDL_image.metadata.creation_time".encode()
IMG_PROP_METADATA_FRAME_COUNT_NUMBER: bytes = "SDL_image.metadata.frame_count".encode()
IMG_PROP_METADATA_LOOP_COUNT_NUMBER: bytes = "SDL_image.metadata.loop_count".encode()

IMG_GetAnimationDecoderFrame: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_GetAnimationDecoderFrame", ctypes.c_bool, [SDL_POINTER[IMG_AnimationDecoder], SDL_POINTER[SDL_POINTER[SDL_Surface]], SDL_POINTER[ctypes.c_uint64]], SDL_IMAGE_BINARY]
IMG_GetAnimationDecoderStatus: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_GetAnimationDecoderStatus", IMG_AnimationDecoderStatus, [SDL_POINTER[IMG_AnimationDecoder]], SDL_IMAGE_BINARY]
IMG_ResetAnimationDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_ResetAnimationDecoder", ctypes.c_bool, [SDL_POINTER[IMG_AnimationDecoder]], SDL_IMAGE_BINARY]
IMG_CloseAnimationDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["IMG_CloseAnimationDecoder", ctypes.c_bool, [SDL_POINTER[IMG_AnimationDecoder]], SDL_IMAGE_BINARY]