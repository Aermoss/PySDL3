from .__init__ import ctypes, typing, abc, \
    SDL_POINTER, SDL_ENUM, SDL_FUNC, SDL_TYPE, SDL_BINARY

from .SDL_stdinc import SDL_FOURCC
from .SDL_endian import SDL_BYTEORDER, SDL_BIG_ENDIAN

SDL_ALPHA_OPAQUE, SDL_ALPHA_TRANSPARENT_FLOAT = 255, 1.0
SDL_ALPHA_TRANSPARENT, SDL_ALPHA_OPAQUE_FLOAT = 0, 0.0

SDL_PixelType: typing.TypeAlias = SDL_TYPE["SDL_PixelType", SDL_ENUM]

SDL_PIXELTYPE_UNKNOWN, SDL_PIXELTYPE_INDEX1, SDL_PIXELTYPE_INDEX4, SDL_PIXELTYPE_INDEX8, SDL_PIXELTYPE_PACKED8, SDL_PIXELTYPE_PACKED16, SDL_PIXELTYPE_PACKED32, \
    SDL_PIXELTYPE_ARRAYU8, SDL_PIXELTYPE_ARRAYU16, SDL_PIXELTYPE_ARRAYU32, SDL_PIXELTYPE_ARRAYF16, SDL_PIXELTYPE_ARRAYF32, SDL_PIXELTYPE_INDEX2 = range(13)

SDL_BitmapOrder: typing.TypeAlias = SDL_TYPE["SDL_BitmapOrder", SDL_ENUM]

SDL_BITMAPORDER_NONE, SDL_BITMAPORDER_4321, SDL_BITMAPORDER_1234 = range(3)

SDL_PackedOrder: typing.TypeAlias = SDL_TYPE["SDL_PackedOrder", SDL_ENUM]

SDL_PACKEDORDER_NONE, SDL_PACKEDORDER_XRGB, SDL_PACKEDORDER_RGBX, SDL_PACKEDORDER_ARGB, SDL_PACKEDORDER_RGBA, \
    SDL_PACKEDORDER_XBGR, SDL_PACKEDORDER_BGRX, SDL_PACKEDORDER_ABGR, SDL_PACKEDORDER_BGRA = range(9)

SDL_ArrayOrder: typing.TypeAlias = SDL_TYPE["SDL_ArrayOrder", SDL_ENUM]

SDL_ARRAYORDER_NONE, SDL_ARRAYORDER_RGB, SDL_ARRAYORDER_RGBA, SDL_ARRAYORDER_ARGB, \
    SDL_ARRAYORDER_BGR, SDL_ARRAYORDER_BGRA, SDL_ARRAYORDER_ABGR = range(7)

SDL_PackedLayout: typing.TypeAlias = SDL_TYPE["SDL_PackedLayout", SDL_ENUM]

SDL_PACKEDLAYOUT_NONE, SDL_PACKEDLAYOUT_332, SDL_PACKEDLAYOUT_4444, SDL_PACKEDLAYOUT_1555, SDL_PACKEDLAYOUT_5551, SDL_PACKEDLAYOUT_565, \
    SDL_PACKEDLAYOUT_8888, SDL_PACKEDLAYOUT_2101010, SDL_PACKEDLAYOUT_1010102 = range(9)

def SDL_DEFINE_PIXELFORMAT(ptype: int, order: int, layout: int, bits: int, pbytes: int) -> int:
    return (1 << 28) | (ptype << 24) | (order << 20) | (layout << 16) | (bits << 8) | (pbytes << 0)

SDL_DEFINE_PIXELFOURCC: abc.Callable[[int, int, int, int], int] = SDL_FOURCC
SDL_ISPIXELFORMAT_FOURCC: abc.Callable[..., bool] = lambda format: format and SDL_PIXELFLAG(format) != 1

SDL_PIXELFLAG: abc.Callable[..., int] = lambda x: (x >> 28) & 0x0F
SDL_PIXELTYPE: abc.Callable[..., int] = lambda x: (x >> 24) & 0x0F
SDL_PIXELORDER: abc.Callable[..., int] = lambda x: (x >> 20) & 0x0F
SDL_PIXELLAYOUT: abc.Callable[..., int] = lambda x: (x >> 16) & 0x0F
SDL_BITSPERPIXEL: abc.Callable[..., int] = lambda x: (x >> 8) & 0xFF

def SDL_BYTESPERPIXEL(x: int) -> int:
    if not SDL_ISPIXELFORMAT_FOURCC(x): return (x >> 0) & 0xFF
    else: return 2 if x in (SDL_PIXELFORMAT_YUY2, SDL_PIXELFORMAT_UYVY, SDL_PIXELFORMAT_YVYU, SDL_PIXELFORMAT_P010) else 1

def SDL_ISPIXELFORMAT_INDEXED(format: int) -> bool:
    return not SDL_ISPIXELFORMAT_FOURCC(format) and (SDL_PIXELTYPE(format) in [SDL_PIXELTYPE_INDEX1, SDL_PIXELTYPE_INDEX2, SDL_PIXELTYPE_INDEX4, SDL_PIXELTYPE_INDEX8])

def SDL_ISPIXELFORMAT_PACKED(format: int) -> bool:
    return not SDL_ISPIXELFORMAT_FOURCC(format) and (SDL_PIXELTYPE(format) in [SDL_PIXELTYPE_PACKED8, SDL_PIXELTYPE_PACKED16, SDL_PIXELTYPE_PACKED32])

def SDL_ISPIXELFORMAT_ARRAY(format: int) -> bool:
    return not SDL_ISPIXELFORMAT_FOURCC(format) and SDL_PIXELTYPE(format) in [SDL_PIXELTYPE_ARRAYU8, SDL_PIXELTYPE_ARRAYU16, SDL_PIXELTYPE_ARRAYU32, SDL_PIXELTYPE_ARRAYF16, SDL_PIXELTYPE_ARRAYF32]

def SDL_ISPIXELFORMAT_10BIT(format: int) -> bool:
    return not SDL_ISPIXELFORMAT_FOURCC(format) and (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_PACKED32 and SDL_PIXELLAYOUT(format) == SDL_PACKEDLAYOUT_2101010)

def SDL_ISPIXELFORMAT_FLOAT(format: int) -> bool:
    return not SDL_ISPIXELFORMAT_FOURCC(format) and (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_ARRAYF16 or SDL_PIXELTYPE(format) == SDL_PIXELTYPE_ARRAYF32)

def SDL_ISPIXELFORMAT_ALPHA(format: int) -> bool:
    return SDL_ISPIXELFORMAT_PACKED(format) and (SDL_PIXELORDER(format) in [SDL_PACKEDORDER_ARGB, SDL_PACKEDORDER_RGBA, SDL_PACKEDORDER_ABGR, SDL_PACKEDORDER_BGRA]) \
        or SDL_ISPIXELFORMAT_ARRAY(format) and (SDL_PIXELORDER(format) in [SDL_ARRAYORDER_ARGB, SDL_ARRAYORDER_RGBA, SDL_ARRAYORDER_ABGR, SDL_ARRAYORDER_BGRA])

SDL_PixelFormat: typing.TypeAlias = SDL_TYPE["SDL_PixelFormat", SDL_ENUM]

SDL_PIXELFORMAT_UNKNOWN: int = 0x00000000
SDL_PIXELFORMAT_INDEX1LSB: int = 0x11100100
SDL_PIXELFORMAT_INDEX1MSB: int = 0x11200100
SDL_PIXELFORMAT_INDEX2LSB: int = 0x1c100200
SDL_PIXELFORMAT_INDEX2MSB: int = 0x1c200200
SDL_PIXELFORMAT_INDEX4LSB: int = 0x12100400
SDL_PIXELFORMAT_INDEX4MSB: int = 0x12200400
SDL_PIXELFORMAT_INDEX8: int = 0x13000801
SDL_PIXELFORMAT_RGB332: int = 0x14110801
SDL_PIXELFORMAT_XRGB4444: int = 0x15120c02
SDL_PIXELFORMAT_XBGR4444: int = 0x15520c02
SDL_PIXELFORMAT_XRGB1555: int = 0x15130f02
SDL_PIXELFORMAT_XBGR1555: int = 0x15530f02
SDL_PIXELFORMAT_ARGB4444: int = 0x15321002
SDL_PIXELFORMAT_RGBA4444: int = 0x15421002
SDL_PIXELFORMAT_ABGR4444: int = 0x15721002
SDL_PIXELFORMAT_BGRA4444: int = 0x15821002
SDL_PIXELFORMAT_ARGB1555: int = 0x15331002
SDL_PIXELFORMAT_RGBA5551: int = 0x15441002
SDL_PIXELFORMAT_ABGR1555: int = 0x15731002
SDL_PIXELFORMAT_BGRA5551: int = 0x15841002
SDL_PIXELFORMAT_RGB565: int = 0x15151002
SDL_PIXELFORMAT_BGR565: int = 0x15551002
SDL_PIXELFORMAT_RGB24: int = 0x17101803
SDL_PIXELFORMAT_BGR24: int = 0x17401803
SDL_PIXELFORMAT_XRGB8888: int = 0x16161804
SDL_PIXELFORMAT_RGBX8888: int = 0x16261804
SDL_PIXELFORMAT_XBGR8888: int = 0x16561804
SDL_PIXELFORMAT_BGRX8888: int = 0x16661804
SDL_PIXELFORMAT_ARGB8888: int = 0x16362004
SDL_PIXELFORMAT_RGBA8888: int = 0x16462004
SDL_PIXELFORMAT_ABGR8888: int = 0x16762004
SDL_PIXELFORMAT_BGRA8888: int = 0x16862004
SDL_PIXELFORMAT_XRGB2101010: int = 0x16172004
SDL_PIXELFORMAT_XBGR2101010: int = 0x16572004
SDL_PIXELFORMAT_ARGB2101010: int = 0x16372004
SDL_PIXELFORMAT_ABGR2101010: int = 0x16772004
SDL_PIXELFORMAT_RGB48: int = 0x18103006
SDL_PIXELFORMAT_BGR48: int = 0x18403006
SDL_PIXELFORMAT_RGBA64: int = 0x18204008
SDL_PIXELFORMAT_ARGB64: int = 0x18304008
SDL_PIXELFORMAT_BGRA64: int = 0x18504008
SDL_PIXELFORMAT_ABGR64: int = 0x18604008
SDL_PIXELFORMAT_RGB48_FLOAT: int = 0x1a103006
SDL_PIXELFORMAT_BGR48_FLOAT: int = 0x1a403006
SDL_PIXELFORMAT_RGBA64_FLOAT: int = 0x1a204008
SDL_PIXELFORMAT_ARGB64_FLOAT: int = 0x1a304008
SDL_PIXELFORMAT_BGRA64_FLOAT: int = 0x1a504008
SDL_PIXELFORMAT_ABGR64_FLOAT: int = 0x1a604008
SDL_PIXELFORMAT_RGB96_FLOAT: int = 0x1b10600c
SDL_PIXELFORMAT_BGR96_FLOAT: int = 0x1b40600c
SDL_PIXELFORMAT_RGBA128_FLOAT: int = 0x1b208010
SDL_PIXELFORMAT_ARGB128_FLOAT: int = 0x1b308010
SDL_PIXELFORMAT_BGRA128_FLOAT: int = 0x1b508010
SDL_PIXELFORMAT_ABGR128_FLOAT: int = 0x1b608010
SDL_PIXELFORMAT_YV12: int = 0x32315659
SDL_PIXELFORMAT_IYUV: int = 0x56555949
SDL_PIXELFORMAT_YUY2: int = 0x32595559
SDL_PIXELFORMAT_UYVY: int = 0x59565955
SDL_PIXELFORMAT_YVYU: int = 0x55595659
SDL_PIXELFORMAT_NV12: int = 0x3231564e
SDL_PIXELFORMAT_NV21: int = 0x3132564e
SDL_PIXELFORMAT_P010: int = 0x30313050
SDL_PIXELFORMAT_EXTERNAL_OES: int = 0x2053454f
SDL_PIXELFORMAT_MJPG: int = 0x47504a4d

if SDL_BYTEORDER == SDL_BIG_ENDIAN:
    SDL_PIXELFORMAT_RGBA32, SDL_PIXELFORMAT_ARGB32, SDL_PIXELFORMAT_BGRA32, SDL_PIXELFORMAT_ABGR32, SDL_PIXELFORMAT_RGBX32, SDL_PIXELFORMAT_XRGB32, SDL_PIXELFORMAT_BGRX32, SDL_PIXELFORMAT_XBGR32 = \
        SDL_PIXELFORMAT_RGBA8888, SDL_PIXELFORMAT_ARGB8888, SDL_PIXELFORMAT_BGRA8888, SDL_PIXELFORMAT_ABGR8888, SDL_PIXELFORMAT_RGBX8888, SDL_PIXELFORMAT_XRGB8888, SDL_PIXELFORMAT_BGRX8888, SDL_PIXELFORMAT_XBGR8888

else:
    SDL_PIXELFORMAT_RGBA32, SDL_PIXELFORMAT_ARGB32, SDL_PIXELFORMAT_BGRA32, SDL_PIXELFORMAT_ABGR32, SDL_PIXELFORMAT_RGBX32, SDL_PIXELFORMAT_XRGB32, SDL_PIXELFORMAT_BGRX32, SDL_PIXELFORMAT_XBGR32 = \
        SDL_PIXELFORMAT_ABGR8888, SDL_PIXELFORMAT_BGRA8888, SDL_PIXELFORMAT_ARGB8888, SDL_PIXELFORMAT_RGBA8888, SDL_PIXELFORMAT_XBGR8888, SDL_PIXELFORMAT_BGRX8888, SDL_PIXELFORMAT_XRGB8888, SDL_PIXELFORMAT_RGBX8888

SDL_ColorType: typing.TypeAlias = SDL_TYPE["SDL_ColorType", SDL_ENUM]

SDL_COLOR_TYPE_UNKNOWN, SDL_COLOR_TYPE_RGB, SDL_COLOR_TYPE_YCBCR = range(3)

SDL_ColorRange: typing.TypeAlias = SDL_TYPE["SDL_ColorRange", SDL_ENUM]

SDL_COLOR_RANGE_UNKOWN, SDL_COLOR_RANGE_LIMITED, SDL_COLOR_RANGE_FULL = range(3)

SDL_ColorPrimaries: typing.TypeAlias = SDL_TYPE["SDL_ColorPrimaries", SDL_ENUM]

SDL_COLOR_PRIMARIES_UNKNOWN, SDL_COLOR_PRIMARIES_BT709, SDL_COLOR_PRIMARIES_UNSPECIFIED, SDL_COLOR_PRIMARIES_BT470M, SDL_COLOR_PRIMARIES_BT470BG, \
    SDL_COLOR_PRIMARIES_BT601, SDL_COLOR_PRIMARIES_SMPTE240, SDL_COLOR_PRIMARIES_GENERIC_FILM, SDL_COLOR_PRIMARIES_BT2020, SDL_COLOR_PRIMARIES_XYZ , \
        SDL_COLOR_PRIMARIES_SMPTE431 , SDL_COLOR_PRIMARIES_SMPTE432 = range(12)

SDL_COLOR_PRIMARIES_EBU3213, SDL_COLOR_PRIMARIES_CUSTOM = 22, 31

SDL_TransferCharacteristics: typing.TypeAlias = SDL_TYPE["SDL_TransferCharacteristics", SDL_ENUM]

SDL_TRANSFER_CHARACTERISTICS_UNKNOWN, SDL_TRANSFER_CHARACTERISTICS_BT709, SDL_TRANSFER_CHARACTERISTICS_UNSPECIFIED, SDL_TRANSFER_CHARACTERISTICS_GAMMA22, \
    SDL_TRANSFER_CHARACTERISTICS_GAMMA28, SDL_TRANSFER_CHARACTERISTICS_BT601, SDL_TRANSFER_CHARACTERISTICS_SMPTE240, SDL_TRANSFER_CHARACTERISTICS_LINEAR, SDL_TRANSFER_CHARACTERISTICS_LOG100, \
        SDL_TRANSFER_CHARACTERISTICS_LOG100_SQRT10, SDL_TRANSFER_CHARACTERISTICS_IEC61966, SDL_TRANSFER_CHARACTERISTICS_BT1361, SDL_TRANSFER_CHARACTERISTICS_SRGB, SDL_TRANSFER_CHARACTERISTICS_BT2020_10BIT, \
            SDL_TRANSFER_CHARACTERISTICS_BT2020_12BIT, SDL_TRANSFER_CHARACTERISTICS_PQ, SDL_TRANSFER_CHARACTERISTICS_SMPTE428, SDL_TRANSFER_CHARACTERISTICS_HLG = range(18)

SDL_TRANSFER_CHARACTERISTICS_CUSTOM: int = 31

SDL_MatrixCoefficients: typing.TypeAlias = SDL_TYPE["SDL_MatrixCoefficients", SDL_ENUM]

SDL_MATRIX_COEFFICIENTS_IDENTITY, SDL_MATRIX_COEFFICIENTS_BT709, SDL_MATRIX_COEFFICIENTS_UNSPECIFIED, SDL_MATRIX_COEFFICIENTS_FCC, \
    SDL_MATRIX_COEFFICIENTS_BT470BG, SDL_MATRIX_COEFFICIENTS_BT601, SDL_MATRIX_COEFFICIENTS_SMPTE240, SDL_MATRIX_COEFFICIENTS_YCGCO, \
        SDL_MATRIX_COEFFICIENTS_BT2020_NCL, SDL_MATRIX_COEFFICIENTS_BT2020_CL, SDL_MATRIX_COEFFICIENTS_SMPTE2085, SDL_MATRIX_COEFFICIENTS_CHROMA_DERIVED_NCL, \
            SDL_MATRIX_COEFFICIENTS_CHROMA_DERIVED_CL, SDL_MATRIX_COEFFICIENTS_ICTCP = range(14)

SDL_MATRIX_COEFFICIENTS_CUSTOM: int = 31

SDL_ChromaLocation: typing.TypeAlias = SDL_TYPE["SDL_ChromaLocation", SDL_ENUM]

SDL_CHROMA_LOCATION_NONE, SDL_CHROMA_LOCATION_LEFT, \
    SDL_CHROMA_LOCATION_CENTER, SDL_CHROMA_LOCATION_TOPLEFT = range(4)

SDL_Colorspace: typing.TypeAlias = SDL_TYPE["SDL_Colorspace", SDL_ENUM]

SDL_COLORSPACE_UNKNOWN: int = 0x00000000
SDL_COLORSPACE_SRGB: int = 0x120005a0
SDL_COLORSPACE_SRGB_LINEAR: int = 0x12000500
SDL_COLORSPACE_HDR10: int = 0x12002600
SDL_COLORSPACE_JPEG: int = 0x220004c6
SDL_COLORSPACE_BT601_LIMITED: int = 0x211018c6
SDL_COLORSPACE_BT601_FULL: int = 0x221018c6
SDL_COLORSPACE_BT709_LIMITED: int = 0x21100421
SDL_COLORSPACE_BT709_FULL: int = 0x22100421
SDL_COLORSPACE_BT2020_LIMITED: int = 0x21102609
SDL_COLORSPACE_BT2020_FULL: int = 0x22102609

SDL_COLORSPACE_RGB_DEFAULT, SDL_COLORSPACE_YUV_DEFAULT = \
    SDL_COLORSPACE_SRGB, SDL_COLORSPACE_JPEG

class SDL_Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_uint8),
        ("g", ctypes.c_uint8),
        ("b", ctypes.c_uint8),
        ("a", ctypes.c_uint8)
    ]

class SDL_FColor(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float)
    ]

class SDL_Palette(ctypes.Structure):
    _fields_ = [
        ("ncolors", ctypes.c_int),
        ("colors", SDL_POINTER[SDL_Color]),
        ("version", ctypes.c_uint32),
        ("refcount", ctypes.c_int)
    ]

class SDL_PixelFormatDetails(ctypes.Structure):
    _fields_ = [
        ("format", SDL_PixelFormat),
        ("bits_per_pixel", ctypes.c_uint8),
        ("bytes_per_pixel", ctypes.c_uint8),
        ("padding", ctypes.c_uint8 * 2),
        ("Rmask", ctypes.c_uint32),
        ("Gmask", ctypes.c_uint32),
        ("Bmask", ctypes.c_uint32),
        ("Amask", ctypes.c_uint32),
        ("Rbits", ctypes.c_uint8),
        ("Gbits", ctypes.c_uint8),
        ("Bbits", ctypes.c_uint8),
        ("Abits", ctypes.c_uint8),
        ("Rshift", ctypes.c_uint8),
        ("Gshift", ctypes.c_uint8),
        ("Bshift", ctypes.c_uint8),
        ("Ashift", ctypes.c_uint8)
    ]

SDL_GetPixelFormatName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPixelFormatName", ctypes.c_char_p, [SDL_PixelFormat], SDL_BINARY]
SDL_GetMasksForPixelFormat: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetMasksForPixelFormat", ctypes.c_bool, [SDL_PixelFormat, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_uint32], SDL_POINTER[ctypes.c_uint32], SDL_POINTER[ctypes.c_uint32], SDL_POINTER[ctypes.c_uint32]], SDL_BINARY]
SDL_GetPixelFormatForMasks: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPixelFormatForMasks", SDL_PixelFormat, [ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32], SDL_BINARY]
SDL_GetPixelFormatDetails: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetPixelFormatDetails", SDL_POINTER[SDL_PixelFormatDetails], [SDL_PixelFormat], SDL_BINARY]
SDL_CreatePalette: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CreatePalette", SDL_POINTER[SDL_Palette], [ctypes.c_int], SDL_BINARY]
SDL_SetPaletteColors: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetPaletteColors", ctypes.c_bool, [SDL_POINTER[SDL_Palette], SDL_POINTER[SDL_Color], ctypes.c_int, ctypes.c_int], SDL_BINARY]
SDL_DestroyPalette: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DestroyPalette", None, [SDL_POINTER[SDL_Palette]], SDL_BINARY]
SDL_MapRGB: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_MapRGB", ctypes.c_uint32, [SDL_POINTER[SDL_PixelFormatDetails], SDL_POINTER[SDL_Palette], ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8], SDL_BINARY]
SDL_MapRGBA: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_MapRGBA", ctypes.c_uint32, [SDL_POINTER[SDL_PixelFormatDetails], SDL_POINTER[SDL_Palette], ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8], SDL_BINARY]
SDL_GetRGB: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetRGB", None, [ctypes.c_uint32, SDL_POINTER[SDL_PixelFormatDetails], SDL_POINTER[SDL_Palette], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8]], SDL_BINARY]
SDL_GetRGBA: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetRGBA", None, [ctypes.c_uint32, SDL_POINTER[SDL_PixelFormatDetails], SDL_POINTER[SDL_Palette], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8]], SDL_BINARY]