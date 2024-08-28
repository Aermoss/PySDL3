from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_DLL

from .SDL_endian import SDL_BYTEORDER, SDL_BIG_ENDIAN

SDL_SET_CURRENT_DLL(SDL_DLL)

SDL_ALPHA_OPAQUE = 255
SDL_ALPHA_TRANSPARENT = 0

SDL_PixelType = ctypes.c_int

SDL_PIXELTYPE_UNKNOWN = 0
SDL_PIXELTYPE_INDEX1 = 1
SDL_PIXELTYPE_INDEX4 = 2
SDL_PIXELTYPE_INDEX8 = 3
SDL_PIXELTYPE_PACKED8 = 4
SDL_PIXELTYPE_PACKED16 = 5
SDL_PIXELTYPE_PACKED32 = 6
SDL_PIXELTYPE_ARRAYU8 = 7
SDL_PIXELTYPE_ARRAYU16 = 8
SDL_PIXELTYPE_ARRAYU32 = 9
SDL_PIXELTYPE_ARRAYF16 = 10
SDL_PIXELTYPE_ARRAYF32 = 11
SDL_PIXELTYPE_INDEX2 = 12

SDL_BitmapOrder = ctypes.c_int

SDL_BITMAPORDER_NONE = 0
SDL_BITMAPORDER_4321 = 1
SDL_BITMAPORDER_1234 = 2

SDL_PackedOrder = ctypes.c_int

SDL_PACKEDORDER_NONE = 0
SDL_PACKEDORDER_XRGB = 1
SDL_PACKEDORDER_RGBX = 2
SDL_PACKEDORDER_ARGB = 3
SDL_PACKEDORDER_RGBA = 4
SDL_PACKEDORDER_XBGR = 5
SDL_PACKEDORDER_BGRX = 6
SDL_PACKEDORDER_ABGR = 7
SDL_PACKEDORDER_BGRA = 8

SDL_ArrayOrder = ctypes.c_int

SDL_ARRAYORDER_NONE = 0
SDL_ARRAYORDER_RGB = 1
SDL_ARRAYORDER_RGBA = 2
SDL_ARRAYORDER_ARGB = 3
SDL_ARRAYORDER_BGR = 4
SDL_ARRAYORDER_BGRA = 5
SDL_ARRAYORDER_ABGR = 6

SDL_PackedLayout = ctypes.c_int

SDL_PACKEDLAYOUT_NONE = 0
SDL_PACKEDLAYOUT_332 = 1
SDL_PACKEDLAYOUT_4444 = 2
SDL_PACKEDLAYOUT_1555 = 3
SDL_PACKEDLAYOUT_5551 = 4
SDL_PACKEDLAYOUT_565 = 5
SDL_PACKEDLAYOUT_8888 = 6
SDL_PACKEDLAYOUT_2101010 = 7
SDL_PACKEDLAYOUT_1010102 = 8

def SDL_FOURCC(a, b, c, d):
    return (ord(a) << 0) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)

def SDL_DEFINE_PIXELFORMAT(ptype, order, layout, bits, pbytes):
    return (1 << 28) | (ptype << 24) | (order << 20) | (layout << 16) | (bits << 8) | (pbytes << 0)

SDL_DEFINE_PIXELFOURCC = SDL_FOURCC
SDL_PIXELFLAG = lambda x: (x >> 28) & 0x0F
SDL_PIXELTYPE = lambda x: (x >> 24) & 0x0F
SDL_PIXELORDER = lambda x: (x >> 20) & 0x0F
SDL_PIXELLAYOUT = lambda x: (x >> 16) & 0x0F
SDL_BITSPERPIXEL = lambda x: (x >> 8) & 0xFF
SDL_ISPIXELFORMAT_FOURCC = lambda fmt: ((fmt) and (SDL_PIXELFLAG(fmt) != 1))

def SDL_BYTESPERPIXEL(x):
    if SDL_ISPIXELFORMAT_FOURCC(x):
        return 2 if x in (SDL_PIXELFORMAT_YUY2, SDL_PIXELFORMAT_UYVY, SDL_PIXELFORMAT_YVYU) else 1
        
    else:
        return ((x) >> 0) & 0xFF

def SDL_ISPIXELFORMAT_INDEXED(pformat):
    return not SDL_ISPIXELFORMAT_FOURCC(pformat) \
        and (SDL_PIXELTYPE(pformat) in [SDL_PIXELTYPE_INDEX1, SDL_PIXELTYPE_INDEX4, SDL_PIXELTYPE_INDEX8])

def SDL_ISPIXELFORMAT_PACKED(pformat):
    return not SDL_ISPIXELFORMAT_FOURCC(pformat) \
        and (SDL_PIXELTYPE(pformat) in [SDL_PIXELTYPE_PACKED8, SDL_PIXELTYPE_PACKED16, SDL_PIXELTYPE_PACKED32])

def SDL_ISPIXELFORMAT_ARRAY(pformat):
    return not SDL_ISPIXELFORMAT_FOURCC(pformat) \
        and (SDL_PIXELTYPE(pformat) in [SDL_PIXELTYPE_ARRAYU8, SDL_PIXELTYPE_ARRAYU16, SDL_PIXELTYPE_ARRAYU32, SDL_PIXELTYPE_ARRAYF16, SDL_PIXELTYPE_ARRAYF32])

def SDL_ISPIXELFORMAT_ALPHA(pformat):
    return SDL_ISPIXELFORMAT_PACKED(pformat) and (SDL_PIXELORDER(pformat) in [SDL_PACKEDORDER_ARGB, SDL_PACKEDORDER_RGBA, SDL_PACKEDORDER_ABGR, SDL_PACKEDORDER_BGRA]) \
        or SDL_ISPIXELFORMAT_ARRAY(pformat) and (SDL_PIXELORDER(pformat) in [SDL_ARRAYORDER_ARGB, SDL_ARRAYORDER_RGBA, SDL_ARRAYORDER_ABGR, SDL_ARRAYORDER_BGRA])

SDL_PixelFormat = ctypes.c_int

SDL_PIXELFORMAT_UNKNOWN = 0x00000000
SDL_PIXELFORMAT_INDEX1LSB = 0x11100100
SDL_PIXELFORMAT_INDEX1MSB = 0x11200100
SDL_PIXELFORMAT_INDEX2LSB = 0x1c100200
SDL_PIXELFORMAT_INDEX2MSB = 0x1c200200
SDL_PIXELFORMAT_INDEX4LSB = 0x12100400
SDL_PIXELFORMAT_INDEX4MSB = 0x12200400
SDL_PIXELFORMAT_INDEX8 = 0x13000801
SDL_PIXELFORMAT_RGB332 = 0x14110801
SDL_PIXELFORMAT_XRGB4444 = 0x15120c02
SDL_PIXELFORMAT_XBGR4444 = 0x15520c02
SDL_PIXELFORMAT_XRGB1555 = 0x15130f02
SDL_PIXELFORMAT_XBGR1555 = 0x15530f02
SDL_PIXELFORMAT_ARGB4444 = 0x15321002
SDL_PIXELFORMAT_RGBA4444 = 0x15421002
SDL_PIXELFORMAT_ABGR4444 = 0x15721002
SDL_PIXELFORMAT_BGRA4444 = 0x15821002
SDL_PIXELFORMAT_ARGB1555 = 0x15331002
SDL_PIXELFORMAT_RGBA5551 = 0x15441002
SDL_PIXELFORMAT_ABGR1555 = 0x15731002
SDL_PIXELFORMAT_BGRA5551 = 0x15841002
SDL_PIXELFORMAT_RGB565 = 0x15151002
SDL_PIXELFORMAT_BGR565 = 0x15551002
SDL_PIXELFORMAT_RGB24 = 0x17101803
SDL_PIXELFORMAT_BGR24 = 0x17401803
SDL_PIXELFORMAT_XRGB8888 = 0x16161804
SDL_PIXELFORMAT_RGBX8888 = 0x16261804
SDL_PIXELFORMAT_XBGR8888 = 0x16561804
SDL_PIXELFORMAT_BGRX8888 = 0x16661804
SDL_PIXELFORMAT_ARGB8888 = 0x16362004
SDL_PIXELFORMAT_RGBA8888 = 0x16462004
SDL_PIXELFORMAT_ABGR8888 = 0x16762004
SDL_PIXELFORMAT_BGRA8888 = 0x16862004
SDL_PIXELFORMAT_XRGB2101010 = 0x16172004
SDL_PIXELFORMAT_XBGR2101010 = 0x16572004
SDL_PIXELFORMAT_ARGB2101010 = 0x16372004
SDL_PIXELFORMAT_ABGR2101010 = 0x16772004
SDL_PIXELFORMAT_RGB48 = 0x18103006
SDL_PIXELFORMAT_BGR48 = 0x18403006
SDL_PIXELFORMAT_RGBA64 = 0x18204008
SDL_PIXELFORMAT_ARGB64 = 0x18304008
SDL_PIXELFORMAT_BGRA64 = 0x18504008
SDL_PIXELFORMAT_ABGR64 = 0x18604008
SDL_PIXELFORMAT_RGB48_FLOAT = 0x1a103006
SDL_PIXELFORMAT_BGR48_FLOAT = 0x1a403006
SDL_PIXELFORMAT_RGBA64_FLOAT = 0x1a204008
SDL_PIXELFORMAT_ARGB64_FLOAT = 0x1a304008
SDL_PIXELFORMAT_BGRA64_FLOAT = 0x1a504008
SDL_PIXELFORMAT_ABGR64_FLOAT = 0x1a604008
SDL_PIXELFORMAT_RGB96_FLOAT = 0x1b10600c
SDL_PIXELFORMAT_BGR96_FLOAT = 0x1b40600c
SDL_PIXELFORMAT_RGBA128_FLOAT = 0x1b208010
SDL_PIXELFORMAT_ARGB128_FLOAT = 0x1b308010
SDL_PIXELFORMAT_BGRA128_FLOAT = 0x1b508010
SDL_PIXELFORMAT_ABGR128_FLOAT = 0x1b608010
SDL_PIXELFORMAT_YV12 = 0x32315659
SDL_PIXELFORMAT_IYUV = 0x56555949
SDL_PIXELFORMAT_YUY2 = 0x32595559
SDL_PIXELFORMAT_UYVY = 0x59565955
SDL_PIXELFORMAT_YVYU = 0x55595659
SDL_PIXELFORMAT_NV12 = 0x3231564e
SDL_PIXELFORMAT_NV21 = 0x3132564e
SDL_PIXELFORMAT_P010 = 0x30313050
SDL_PIXELFORMAT_EXTERNAL_OES = 0x2053454f

if SDL_BYTEORDER == SDL_BIG_ENDIAN:
    SDL_PIXELFORMAT_RGBA32 = SDL_PIXELFORMAT_RGBA8888
    SDL_PIXELFORMAT_ARGB32 = SDL_PIXELFORMAT_ARGB8888
    SDL_PIXELFORMAT_BGRA32 = SDL_PIXELFORMAT_BGRA8888
    SDL_PIXELFORMAT_ABGR32 = SDL_PIXELFORMAT_ABGR8888
    SDL_PIXELFORMAT_RGBX32 = SDL_PIXELFORMAT_RGBX8888
    SDL_PIXELFORMAT_XRGB32 = SDL_PIXELFORMAT_XRGB8888
    SDL_PIXELFORMAT_BGRX32 = SDL_PIXELFORMAT_BGRX8888
    SDL_PIXELFORMAT_XBGR32 = SDL_PIXELFORMAT_XBGR8888

else:
    SDL_PIXELFORMAT_RGBA32 = SDL_PIXELFORMAT_ABGR8888
    SDL_PIXELFORMAT_ARGB32 = SDL_PIXELFORMAT_BGRA8888
    SDL_PIXELFORMAT_BGRA32 = SDL_PIXELFORMAT_ARGB8888
    SDL_PIXELFORMAT_ABGR32 = SDL_PIXELFORMAT_RGBA8888
    SDL_PIXELFORMAT_RGBX32 = SDL_PIXELFORMAT_XBGR8888
    SDL_PIXELFORMAT_XRGB32 = SDL_PIXELFORMAT_BGRX8888
    SDL_PIXELFORMAT_BGRX32 = SDL_PIXELFORMAT_XRGB8888
    SDL_PIXELFORMAT_XBGR32 = SDL_PIXELFORMAT_RGBX8888

SDL_ColorType = ctypes.c_int

SDL_COLOR_TYPE_UNKNOWN = 0
SDL_COLOR_TYPE_RGB = 1
SDL_COLOR_TYPE_YCBCR = 2

SDL_ColorRange = ctypes.c_int

SDL_COLOR_RANGE_UNKOWN = 0
SDL_COLOR_RANGE_LIMITED = 1
SDL_COLOR_RANGE_FULL = 2

SDL_ColorPrimaries = ctypes.c_int

SDL_COLOR_PRIMARIES_UNKNOWN = 0
SDL_COLOR_PRIMARIES_BT709 = 1
SDL_COLOR_PRIMARIES_UNSPECIFIED = 2
SDL_COLOR_PRIMARIES_BT470M = 4
SDL_COLOR_PRIMARIES_BT470BG = 5
SDL_COLOR_PRIMARIES_BT601 = 6
SDL_COLOR_PRIMARIES_SMPTE240 = 7
SDL_COLOR_PRIMARIES_GENERIC_FILM = 8
SDL_COLOR_PRIMARIES_BT2020 = 9
SDL_COLOR_PRIMARIES_XYZ = 10
SDL_COLOR_PRIMARIES_SMPTE431 = 11
SDL_COLOR_PRIMARIES_SMPTE432 = 12
SDL_COLOR_PRIMARIES_EBU3213 = 22
SDL_COLOR_PRIMARIES_CUSTOM = 31

SDL_TransferCharacteristics = ctypes.c_int

SDL_TRANSFER_CHARACTERISTICS_UNKNOWN = 0
SDL_TRANSFER_CHARACTERISTICS_BT709 = 1
SDL_TRANSFER_CHARACTERISTICS_UNSPECIFIED = 2
SDL_TRANSFER_CHARACTERISTICS_GAMMA22 = 4
SDL_TRANSFER_CHARACTERISTICS_GAMMA28 = 5
SDL_TRANSFER_CHARACTERISTICS_BT601 = 6
SDL_TRANSFER_CHARACTERISTICS_SMPTE240 = 7
SDL_TRANSFER_CHARACTERISTICS_LINEAR = 8
SDL_TRANSFER_CHARACTERISTICS_LOG100 = 9
SDL_TRANSFER_CHARACTERISTICS_LOG100_SQRT10 = 10
SDL_TRANSFER_CHARACTERISTICS_IEC61966 = 11
SDL_TRANSFER_CHARACTERISTICS_BT1361 = 12
SDL_TRANSFER_CHARACTERISTICS_SRGB = 13
SDL_TRANSFER_CHARACTERISTICS_BT2020_10BIT = 14
SDL_TRANSFER_CHARACTERISTICS_BT2020_12BIT = 15
SDL_TRANSFER_CHARACTERISTICS_PQ = 16
SDL_TRANSFER_CHARACTERISTICS_SMPTE428 = 17
SDL_TRANSFER_CHARACTERISTICS_HLG = 18
SDL_TRANSFER_CHARACTERISTICS_CUSTOM = 31

SDL_MatrixCoefficients = ctypes.c_int

SDL_MATRIX_COEFFICIENTS_IDENTITY = 0
SDL_MATRIX_COEFFICIENTS_BT709 = 1
SDL_MATRIX_COEFFICIENTS_UNSPECIFIED = 2
SDL_MATRIX_COEFFICIENTS_FCC = 4
SDL_MATRIX_COEFFICIENTS_BT470BG = 5
SDL_MATRIX_COEFFICIENTS_BT601 = 6
SDL_MATRIX_COEFFICIENTS_SMPTE240 = 7
SDL_MATRIX_COEFFICIENTS_YCGCO = 8
SDL_MATRIX_COEFFICIENTS_BT2020_NCL = 9
SDL_MATRIX_COEFFICIENTS_BT2020_CL = 10
SDL_MATRIX_COEFFICIENTS_SMPTE2085 = 11
SDL_MATRIX_COEFFICIENTS_CHROMA_DERIVED_NCL = 12
SDL_MATRIX_COEFFICIENTS_CHROMA_DERIVED_CL = 13
SDL_MATRIX_COEFFICIENTS_ICTCP = 14
SDL_MATRIX_COEFFICIENTS_CUSTOM = 31

SDL_ChromaLocation = ctypes.c_int

SDL_CHROMA_LOCATION_NONE = 0
SDL_CHROMA_LOCATION_LEFT = 1
SDL_CHROMA_LOCATION_CENTER = 2
SDL_CHROMA_LOCATION_TOPLEFT = 3

SDL_Colorspace = ctypes.c_int

SDL_COLORSPACE_UNKNOWN = 0x00000000
SDL_COLORSPACE_SRGB = 0x120005a0
SDL_COLORSPACE_SRGB_LINEAR = 0x12000500
SDL_COLORSPACE_HDR10 = 0x12002600
SDL_COLORSPACE_JPEG = 0x220004c6
SDL_COLORSPACE_BT601_LIMITED = 0x211018c6
SDL_COLORSPACE_BT601_FULL = 0x221018c6
SDL_COLORSPACE_BT709_LIMITED = 0x21100421
SDL_COLORSPACE_BT709_FULL = 0x22100421
SDL_COLORSPACE_BT2020_LIMITED = 0x21102609
SDL_COLORSPACE_BT2020_FULL = 0x22102609

SDL_COLORSPACE_RGB_DEFAULT = SDL_COLORSPACE_SRGB
SDL_COLORSPACE_YUV_DEFAULT = SDL_COLORSPACE_JPEG

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
        ("colors", ctypes.POINTER(SDL_Color)),
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
        ("Ashift", ctypes.c_uint8),
        ("refcount", ctypes.c_int)
    ]

SDL_FUNC("SDL_GetPixelFormatName", ctypes.c_char_p, SDL_PixelFormat)
SDL_FUNC("SDL_GetMasksForPixelFormat", ctypes.c_bool, SDL_PixelFormat, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_GetPixelFormatForMasks", SDL_PixelFormat, ctypes.c_int32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_GetPixelFormatDetails", ctypes.POINTER(SDL_PixelFormatDetails), SDL_PixelFormat)
SDL_FUNC("SDL_CreatePalette", ctypes.POINTER(SDL_Palette), ctypes.c_int)
SDL_FUNC("SDL_SetPaletteColors", ctypes.c_bool, ctypes.POINTER(SDL_Palette), ctypes.POINTER(SDL_Color), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_DestroyPalette", None, ctypes.POINTER(SDL_Palette))
SDL_FUNC("SDL_MapRGB", ctypes.c_uint32, ctypes.POINTER(SDL_PixelFormatDetails), ctypes.POINTER(SDL_Palette), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_MapRGBA", ctypes.c_uint32, ctypes.POINTER(SDL_PixelFormatDetails), ctypes.POINTER(SDL_Palette), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_GetRGB", None, ctypes.c_uint32, ctypes.POINTER(SDL_PixelFormatDetails), ctypes.POINTER(SDL_Palette), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_GetRGBA", None, ctypes.c_uint32, ctypes.POINTER(SDL_PixelFormatDetails), ctypes.POINTER(SDL_Palette), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))