from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID
from .SDL_surface import SDL_FlipMode
from .SDL_video import SDL_Window
from .SDL_pixels import SDL_FColor
from .SDL_rect import SDL_Rect

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_GPUDevice(ctypes.c_void_p):
    ...

class SDL_GPUBuffer(ctypes.c_void_p):
    ...

class SDL_GPUTransferBuffer(ctypes.c_void_p):
    ...

class SDL_GPUTexture(ctypes.c_void_p):
    ...

class SDL_GPUSampler(ctypes.c_void_p):
    ...

class SDL_GPUShader(ctypes.c_void_p):
    ...

class SDL_GPUComputePipeline(ctypes.c_void_p):
    ...

class SDL_GPUGraphicsPipeline(ctypes.c_void_p):
    ...

class SDL_GPUCommandBuffer(ctypes.c_void_p):
    ...

class SDL_GPURenderPass(ctypes.c_void_p):
    ...

class SDL_GPUComputePass(ctypes.c_void_p):
    ...

class SDL_GPUCopyPass(ctypes.c_void_p):
    ...

class SDL_GPUFence(ctypes.c_void_p):
    ...

SDL_GPUPrimitiveType = ctypes.c_int

SDL_GPU_PRIMITIVETYPE_TRIANGLELIST = 0
SDL_GPU_PRIMITIVETYPE_TRIANGLESTRIP = 1
SDL_GPU_PRIMITIVETYPE_LINELIST = 2
SDL_GPU_PRIMITIVETYPE_LINESTRIP = 3
SDL_GPU_PRIMITIVETYPE_POINTLIST = 4

SDL_GPULoadOp = ctypes.c_int

SDL_GPU_LOADOP_LOAD = 0
SDL_GPU_LOADOP_CLEAR = 1
SDL_GPU_LOADOP_DONT_CARE = 2

SDL_GPUStoreOp = ctypes.c_int

SDL_GPU_STOREOP_STORE = 0
SDL_GPU_STOREOP_DONT_CARE = 1
SDL_GPU_STOREOP_RESOLVE = 2
SDL_GPU_STOREOP_RESOLVE_AND_STORE = 3

SDL_GPUIndexElementSize = ctypes.c_int

SDL_GPU_INDEXELEMENTSIZE_16BIT = 0
SDL_GPU_INDEXELEMENTSIZE_32BIT = 1

SDL_GPUTextureFormat = ctypes.c_int

SDL_GPU_TEXTUREFORMAT_INVALID = 0

SDL_GPU_TEXTUREFORMAT_A8_UNORM = 1
SDL_GPU_TEXTUREFORMAT_R8_UNORM = 2
SDL_GPU_TEXTUREFORMAT_R8G8_UNORM = 3
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM = 4
SDL_GPU_TEXTUREFORMAT_R16_UNORM = 5
SDL_GPU_TEXTUREFORMAT_R16G16_UNORM = 6
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UNORM = 7
SDL_GPU_TEXTUREFORMAT_R10G10B10A2_UNORM = 8
SDL_GPU_TEXTUREFORMAT_B5G6R5_UNORM = 9
SDL_GPU_TEXTUREFORMAT_B5G5R5A1_UNORM = 10
SDL_GPU_TEXTUREFORMAT_B4G4R4A4_UNORM = 11
SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM = 12
SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM = 13
SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM = 14
SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM = 15
SDL_GPU_TEXTUREFORMAT_BC4_R_UNORM = 16
SDL_GPU_TEXTUREFORMAT_BC5_RG_UNORM = 17
SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM = 18

SDL_GPU_TEXTUREFORMAT_BC6H_RGB_FLOAT = 19
SDL_GPU_TEXTUREFORMAT_BC6H_RGB_UFLOAT = 20

SDL_GPU_TEXTUREFORMAT_R8_SNORM = 21
SDL_GPU_TEXTUREFORMAT_R8G8_SNORM = 22
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_SNORM = 23
SDL_GPU_TEXTUREFORMAT_R16_SNORM = 24
SDL_GPU_TEXTUREFORMAT_R16G16_SNORM = 25
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_SNORM = 26

SDL_GPU_TEXTUREFORMAT_R16_FLOAT = 27
SDL_GPU_TEXTUREFORMAT_R16G16_FLOAT = 28
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_FLOAT = 29
SDL_GPU_TEXTUREFORMAT_R32_FLOAT = 30
SDL_GPU_TEXTUREFORMAT_R32G32_FLOAT = 31
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_FLOAT = 32

SDL_GPU_TEXTUREFORMAT_R11G11B10_UFLOAT = 33

SDL_GPU_TEXTUREFORMAT_R8_UINT = 34
SDL_GPU_TEXTUREFORMAT_R8G8_UINT = 35
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UINT = 36
SDL_GPU_TEXTUREFORMAT_R16_UINT = 37
SDL_GPU_TEXTUREFORMAT_R16G16_UINT = 38
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UINT = 39
SDL_GPU_TEXTUREFORMAT_R32_UINT = 40
SDL_GPU_TEXTUREFORMAT_R32G32_UINT = 41
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_UINT = 42

SDL_GPU_TEXTUREFORMAT_R8_INT = 43
SDL_GPU_TEXTUREFORMAT_R8G8_INT = 44
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_INT = 45
SDL_GPU_TEXTUREFORMAT_R16_INT = 46
SDL_GPU_TEXTUREFORMAT_R16G16_INT = 47
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_INT = 48
SDL_GPU_TEXTUREFORMAT_R32_INT = 49
SDL_GPU_TEXTUREFORMAT_R32G32_INT = 50
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_INT = 51

SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM_SRGB = 52
SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM_SRGB = 53

SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM_SRGB = 54
SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM_SRGB = 55
SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM_SRGB = 56
SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM_SRGB = 57

SDL_GPU_TEXTUREFORMAT_D16_UNORM = 58
SDL_GPU_TEXTUREFORMAT_D24_UNORM = 59
SDL_GPU_TEXTUREFORMAT_D32_FLOAT = 60
SDL_GPU_TEXTUREFORMAT_D24_UNORM_S8_UINT = 61
SDL_GPU_TEXTUREFORMAT_D32_FLOAT_S8_UINT = 62

SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM = 63
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM = 64
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM = 65
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM = 66
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM = 67
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM = 68
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM = 69
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM = 70
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM = 71
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM = 72
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM = 73
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM = 74
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM = 75
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM = 76

SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM_SRGB = 77
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM_SRGB = 78
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM_SRGB = 79
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM_SRGB = 80
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM_SRGB = 81
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM_SRGB = 82
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM_SRGB = 83
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM_SRGB = 84
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM_SRGB = 85
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM_SRGB = 86
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM_SRGB = 87
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM_SRGB = 88
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM_SRGB = 89
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM_SRGB = 90

SDL_GPU_TEXTUREFORMAT_ASTC_4x4_FLOAT = 91
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_FLOAT = 92
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_FLOAT = 93
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_FLOAT = 94
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_FLOAT = 95
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_FLOAT = 96
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_FLOAT = 97
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_FLOAT = 98
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_FLOAT = 99
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_FLOAT = 100
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_FLOAT = 101
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_FLOAT = 102
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_FLOAT = 103
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_FLOAT = 104

SDL_GPUTextureUsageFlags = ctypes.c_uint32

SDL_GPU_TEXTUREUSAGE_SAMPLER = 1 << 0
SDL_GPU_TEXTUREUSAGE_COLOR_TARGET = 1 << 1
SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET = 1 << 2
SDL_GPU_TEXTUREUSAGE_GRAPHICS_STORAGE_READ = 1 << 3
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ = 1 << 4
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE = 1 << 5
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE = 1 << 6

SDL_GPUTextureType = ctypes.c_int

SDL_GPU_TEXTURETYPE_2D = 0
SDL_GPU_TEXTURETYPE_2D_ARRAY = 1
SDL_GPU_TEXTURETYPE_3D = 2
SDL_GPU_TEXTURETYPE_CUBE = 3
SDL_GPU_TEXTURETYPE_CUBE_ARRAY = 4

SDL_GPUSampleCount = ctypes.c_int

SDL_GPU_SAMPLECOUNT_1 = 0
SDL_GPU_SAMPLECOUNT_2 = 1
SDL_GPU_SAMPLECOUNT_4 = 2
SDL_GPU_SAMPLECOUNT_8 = 3

SDL_GPUCubeMapFace = ctypes.c_int

SDL_GPU_CUBEMAPFACE_POSITIVEX = 0
SDL_GPU_CUBEMAPFACE_NEGATIVEX = 1
SDL_GPU_CUBEMAPFACE_POSITIVEY = 2
SDL_GPU_CUBEMAPFACE_NEGATIVEY = 3
SDL_GPU_CUBEMAPFACE_POSITIVEZ = 4
SDL_GPU_CUBEMAPFACE_NEGATIVEZ = 5

SDL_GPUBufferUsageFlags = ctypes.c_uint32

SDL_GPU_BUFFERUSAGE_VERTEX = 1 << 0
SDL_GPU_BUFFERUSAGE_INDEX = 1 << 1
SDL_GPU_BUFFERUSAGE_INDIRECT = 1 << 2
SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ = 1 << 3
SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ = 1 << 4
SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE = 1 << 5

SDL_GPUTransferBufferUsage = ctypes.c_int

SDL_GPU_TRANSFERBUFFERUSAGE_UPLOAD = 0
SDL_GPU_TRANSFERBUFFERUSAGE_DOWNLOAD = 1

SDL_GPUShaderStage = ctypes.c_int

SDL_GPU_SHADERSTAGE_VERTEX = 0
SDL_GPU_SHADERSTAGE_FRAGMENT = 1

SDL_GPUShaderFormat = ctypes.c_uint32

SDL_GPU_SHADERFORMAT_INVALID = 0
SDL_GPU_SHADERFORMAT_PRIVATE = 1 << 0
SDL_GPU_SHADERFORMAT_SPIRV = 1 << 1
SDL_GPU_SHADERFORMAT_DXBC = 1 << 2
SDL_GPU_SHADERFORMAT_DXIL = 1 << 3
SDL_GPU_SHADERFORMAT_MSL = 1 << 4
SDL_GPU_SHADERFORMAT_METALLIB = 1 << 5

SDL_GPUVertexElementFormat = ctypes.c_int

SDL_GPU_VERTEXELEMENTFORMAT_INVALID = 0

SDL_GPU_VERTEXELEMENTFORMAT_INT = 1
SDL_GPU_VERTEXELEMENTFORMAT_INT2 = 2
SDL_GPU_VERTEXELEMENTFORMAT_INT3 = 3
SDL_GPU_VERTEXELEMENTFORMAT_INT4 = 4

SDL_GPU_VERTEXELEMENTFORMAT_UINT = 5
SDL_GPU_VERTEXELEMENTFORMAT_UINT2 = 6
SDL_GPU_VERTEXELEMENTFORMAT_UINT3 = 7
SDL_GPU_VERTEXELEMENTFORMAT_UINT4 = 8

SDL_GPU_VERTEXELEMENTFORMAT_FLOAT = 9
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT2 = 10
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT3 = 11
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT4 = 12

SDL_GPU_VERTEXELEMENTFORMAT_BYTE2 = 13
SDL_GPU_VERTEXELEMENTFORMAT_BYTE4 = 14

SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2 = 15
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4 = 16

SDL_GPU_VERTEXELEMENTFORMAT_BYTE2_NORM = 17
SDL_GPU_VERTEXELEMENTFORMAT_BYTE4_NORM = 18

SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2_NORM = 19
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4_NORM = 20

SDL_GPU_VERTEXELEMENTFORMAT_SHORT2 = 21
SDL_GPU_VERTEXELEMENTFORMAT_SHORT4 = 22

SDL_GPU_VERTEXELEMENTFORMAT_USHORT2 = 23
SDL_GPU_VERTEXELEMENTFORMAT_USHORT4 = 24

SDL_GPU_VERTEXELEMENTFORMAT_SHORT2_NORM = 25
SDL_GPU_VERTEXELEMENTFORMAT_SHORT4_NORM = 26

SDL_GPU_VERTEXELEMENTFORMAT_USHORT2_NORM = 27
SDL_GPU_VERTEXELEMENTFORMAT_USHORT4_NORM = 28

SDL_GPU_VERTEXELEMENTFORMAT_HALF2 = 29
SDL_GPU_VERTEXELEMENTFORMAT_HALF4 = 30

SDL_GPUVertexInputRate = ctypes.c_int

SDL_GPU_VERTEXINPUTRATE_VERTEX = 0
SDL_GPU_VERTEXINPUTRATE_INSTANCE = 1

SDL_GPUFillMode = ctypes.c_int

SDL_GPU_FILLMODE_FILL = 0
SDL_GPU_FILLMODE_LINE = 1

SDL_GPUCullMode = ctypes.c_int

SDL_GPU_CULLMODE_NONE = 0
SDL_GPU_CULLMODE_FRONT = 1
SDL_GPU_CULLMODE_BACK = 2

SDL_GPUFrontFace = ctypes.c_int

SDL_GPU_FRONTFACE_COUNTER_CLOCKWISE = 0
SDL_GPU_FRONTFACE_CLOCKWISE = 1

SDL_GPUCompareOp = ctypes.c_int

SDL_GPU_COMPAREOP_INVALID = 0
SDL_GPU_COMPAREOP_NEVER = 1
SDL_GPU_COMPAREOP_LESS = 2
SDL_GPU_COMPAREOP_EQUAL = 3
SDL_GPU_COMPAREOP_LESS_OR_EQUAL = 4
SDL_GPU_COMPAREOP_GREATER = 5
SDL_GPU_COMPAREOP_NOT_EQUAL = 6
SDL_GPU_COMPAREOP_GREATER_OR_EQUAL = 7
SDL_GPU_COMPAREOP_ALWAYS = 8

SDL_GPUStencilOp = ctypes.c_int

SDL_GPU_STENCILOP_INVALID = 0
SDL_GPU_STENCILOP_KEEP = 1
SDL_GPU_STENCILOP_ZERO = 2
SDL_GPU_STENCILOP_REPLACE = 3
SDL_GPU_STENCILOP_INCREMENT_AND_CLAMP = 4
SDL_GPU_STENCILOP_DECREMENT_AND_CLAMP = 5
SDL_GPU_STENCILOP_INVERT = 6
SDL_GPU_STENCILOP_INCREMENT_AND_WRAP = 7
SDL_GPU_STENCILOP_DECREMENT_AND_WRAP = 8

SDL_GPUBlendOp = ctypes.c_int

SDL_GPU_BLENDOP_INVALID = 0
SDL_GPU_BLENDOP_ADD = 1
SDL_GPU_BLENDOP_SUBTRACT = 2
SDL_GPU_BLENDOP_REVERSE_SUBTRACT = 3
SDL_GPU_BLENDOP_MIN = 4
SDL_GPU_BLENDOP_MAX = 5

SDL_GPUBlendFactor = ctypes.c_int

SDL_GPU_BLENDFACTOR_INVALID = 0
SDL_GPU_BLENDFACTOR_ZERO = 1
SDL_GPU_BLENDFACTOR_ONE = 2
SDL_GPU_BLENDFACTOR_SRC_COLOR = 3
SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_COLOR = 4
SDL_GPU_BLENDFACTOR_DST_COLOR = 5
SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_COLOR = 6
SDL_GPU_BLENDFACTOR_SRC_ALPHA = 7
SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_ALPHA = 8
SDL_GPU_BLENDFACTOR_DST_ALPHA = 9
SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_ALPHA = 10
SDL_GPU_BLENDFACTOR_CONSTANT_COLOR = 11
SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR = 12
SDL_GPU_BLENDFACTOR_SRC_ALPHA_SATURATE = 13

SDL_GPUColorComponentFlags = ctypes.c_uint8

SDL_GPU_COLORCOMPONENT_R = 1 << 0
SDL_GPU_COLORCOMPONENT_G = 1 << 1
SDL_GPU_COLORCOMPONENT_B = 1 << 2
SDL_GPU_COLORCOMPONENT_A = 1 << 3

SDL_GPUFilter = ctypes.c_int

SDL_GPU_FILTER_NEAREST = 0
SDL_GPU_FILTER_LINEAR = 1

SDL_GPUSamplerMipmapMode = ctypes.c_int

SDL_GPU_SAMPLERMIPMAPMODE_NEAREST = 0
SDL_GPU_SAMPLERMIPMAPMODE_LINEAR = 1

SDL_GPUSamplerAddressMode = ctypes.c_int

SDL_GPU_SAMPLERADDRESSMODE_REPEAT = 0
SDL_GPU_SAMPLERADDRESSMODE_MIRRORED_REPEAT = 1
SDL_GPU_SAMPLERADDRESSMODE_CLAMP_TO_EDGE = 2

SDL_GPUPresentMode = ctypes.c_int

SDL_GPU_PRESENTMODE_VSYNC = 0
SDL_GPU_PRESENTMODE_IMMEDIATE = 1
SDL_GPU_PRESENTMODE_MAILBOX = 2

SDL_GPUSwapchainComposition = ctypes.c_int

SDL_GPU_SWAPCHAINCOMPOSITION_SDR = 0
SDL_GPU_SWAPCHAINCOMPOSITION_SDR_LINEAR = 1
SDL_GPU_SWAPCHAINCOMPOSITION_HDR_EXTENDED_LINEAR = 2
SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2084 = 3

class SDL_GPUViewport(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("w", ctypes.c_float),
        ("h", ctypes.c_float),
        ("min_depth", ctypes.c_float),
        ("max_depth", ctypes.c_float)
    ]

class SDL_GPUTextureTransferInfo(ctypes.Structure):
    _fields_ = [
        ("transfer_buffer", ctypes.POINTER(SDL_GPUTransferBuffer)),
        ("offset", ctypes.c_uint32),
        ("pixels_per_row", ctypes.c_uint32),
        ("rows_per_layer", ctypes.c_uint32)
    ]

class SDL_GPUTransferBufferLocation(ctypes.Structure):
    _fields_ = [
        ("transfer_buffer", ctypes.POINTER(SDL_GPUTransferBuffer)),
        ("offset", ctypes.c_uint32)
    ]

class SDL_GPUTextureLocation(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("z", ctypes.c_uint32)
    ]

class SDL_GPUTextureRegion(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("z", ctypes.c_uint32),
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32),
        ("d", ctypes.c_uint32)
    ]

class SDL_GPUBlitRegion(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("mip_level", ctypes.c_uint32),
        ("layer_or_depth_plane", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32)
    ]

class SDL_GPUBufferLocation(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.POINTER(SDL_GPUBuffer)),
        ("offset", ctypes.c_uint32)
    ]

class SDL_GPUBufferRegion(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.POINTER(SDL_GPUBuffer)),
        ("offset", ctypes.c_uint32),
        ("size", ctypes.c_uint32)
    ]

class SDL_GPUIndirectDrawCommand(ctypes.Structure):
    _fields_ = [
        ("num_vertices", ctypes.c_uint32),
        ("num_instances", ctypes.c_uint32),
        ("first_vertex", ctypes.c_uint32),
        ("first_instance", ctypes.c_uint32)
    ]

class SDL_GPUIndexedIndirectDrawCommand(ctypes.Structure):
    _fields_ = [
        ("num_indices", ctypes.c_uint32),
        ("num_instances", ctypes.c_uint32),
        ("first_index", ctypes.c_uint32),
        ("vertex_offset", ctypes.c_int32),
        ("first_instance", ctypes.c_uint32)
    ]

class SDL_GPUIndirectDispatchCommand(ctypes.Structure):
    _fields_ = [
        ("groupcount_x", ctypes.c_uint32),
        ("groupcount_y", ctypes.c_uint32),
        ("groupcount_z", ctypes.c_uint32)
    ]

class SDL_GPUSamplerCreateInfo(ctypes.Structure):
    _fields_ = [
        ("min_filter", SDL_GPUFilter),
        ("mag_filter", SDL_GPUFilter),
        ("mipmap_mode", SDL_GPUSamplerMipmapMode),
        ("address_mode_u", SDL_GPUSamplerAddressMode),
        ("address_mode_v", SDL_GPUSamplerAddressMode),
        ("address_mode_w", SDL_GPUSamplerAddressMode),
        ("mip_lod_bias", ctypes.c_float),
        ("max_anisotropy", ctypes.c_float),
        ("compare_op", SDL_GPUCompareOp),
        ("min_lod", ctypes.c_float),
        ("max_lod", ctypes.c_float),
        ("enable_anisotropy", ctypes.c_bool),
        ("enable_compare", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUVertexBufferDescription(ctypes.Structure):
    _fields_ = [
        ("slot", ctypes.c_uint32),
        ("pitch", ctypes.c_uint32),
        ("input_rate", SDL_GPUVertexInputRate),
        ("instance_step_rate", ctypes.c_uint32)
    ]

class SDL_GPUVertexAttribute(ctypes.Structure):
    _fields_ = [
        ("location", ctypes.c_uint32),
        ("buffer_slot", ctypes.c_uint32),
        ("format", SDL_GPUVertexElementFormat),
        ("offset", ctypes.c_uint32)
    ]

class SDL_GPUVertexInputState(ctypes.Structure):
    _fields_ = [
        ("vertex_buffer_descriptions", ctypes.POINTER(SDL_GPUVertexBufferDescription)),
        ("num_vertex_buffers", ctypes.c_uint32),
        ("vertex_attributes", ctypes.POINTER(SDL_GPUVertexAttribute)),
        ("num_vertex_attributes", ctypes.c_uint32)
    ]

class SDL_GPUStencilOpState(ctypes.Structure):
    _fields_ = [
        ("fail_op", SDL_GPUStencilOp),
        ("pass_op", SDL_GPUStencilOp),
        ("depth_fail_op", SDL_GPUStencilOp),
        ("compare_op", SDL_GPUCompareOp)
    ]

class SDL_GPUColorTargetBlendState(ctypes.Structure):
    _fields_ = [
        ("src_color_blendfactor", SDL_GPUBlendFactor),
        ("dst_color_blendfactor", SDL_GPUBlendFactor),
        ("color_blend_op", SDL_GPUBlendOp),
        ("src_alpha_blendfactor", SDL_GPUBlendFactor),
        ("dst_alpha_blendfactor", SDL_GPUBlendFactor),
        ("alpha_blend_op", SDL_GPUBlendOp),
        ("color_write_mask", SDL_GPUColorComponentFlags),
        ("enable_blend", ctypes.c_bool),
        ("enable_color_write_mask", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_GPUShaderCreateInfo(ctypes.Structure):
    _fields_ = [
        ("code_size", ctypes.c_size_t),
        ("code", ctypes.POINTER(ctypes.c_uint8)),
        ("entrypoint", ctypes.c_char_p),
        ("format", SDL_GPUShaderFormat),
        ("stage", SDL_GPUShaderStage),
        ("num_samplers", ctypes.c_uint32),
        ("num_storage_textures", ctypes.c_uint32),
        ("num_storage_buffers", ctypes.c_uint32),
        ("num_uniform_buffers", ctypes.c_uint32),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUTextureCreateInfo(ctypes.Structure):
    _fields_ = [
        ("type", SDL_GPUTextureType),
        ("format", SDL_GPUTextureFormat),
        ("usage", SDL_GPUTextureUsageFlags),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("layer_count_or_depth", ctypes.c_uint32),
        ("num_levels", ctypes.c_uint32),
        ("sample_count", SDL_GPUSampleCount),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ("usage", SDL_GPUBufferUsageFlags),
        ("size", ctypes.c_uint32),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUTransferBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ("usage", SDL_GPUTransferBufferUsage),
        ("size", ctypes.c_uint32),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPURasterizerState(ctypes.Structure):
    _fields_ = [
        ("fill_mode", SDL_GPUFillMode),
        ("cull_mode", SDL_GPUCullMode),
        ("front_face", SDL_GPUFrontFace),
        ("depth_bias_constant_factor", ctypes.c_float),
        ("depth_bias_clamp", ctypes.c_float),
        ("depth_bias_slope_factor", ctypes.c_float),
        ("enable_depth_bias", ctypes.c_bool),
        ("enable_depth_clip", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_GPUMultisampleState(ctypes.Structure):
    _fields_ = [
        ("sample_count", SDL_GPUSampleCount),
        ("sample_mask", ctypes.c_uint32),
        ("enable_mask", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_GPUDepthStencilState(ctypes.Structure):
    _fields_ = [
        ("compare_op", SDL_GPUCompareOp),
        ("back_stencil_state", SDL_GPUStencilOpState),
        ("front_stencil_state", SDL_GPUStencilOpState),
        ("compare_mask", ctypes.c_uint8),
        ("write_mask", ctypes.c_uint8),
        ("enable_depth_test", ctypes.c_bool),
        ("enable_depth_write", ctypes.c_bool),
        ("enable_stencil_test", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_GPUColorTargetDescription(ctypes.Structure):
    _fields_ = [
        ("format", SDL_GPUTextureFormat),
        ("blend_state", SDL_GPUColorTargetBlendState)
    ]

class SDL_GPUGraphicsPipelineTargetInfo(ctypes.Structure):
    _fields_ = [
        ("color_target_descriptions", ctypes.POINTER(SDL_GPUColorTargetDescription)),
        ("num_color_targets", ctypes.c_uint32),
        ("depth_stencil_format", SDL_GPUTextureFormat),
        ("has_depth_stencil_target", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_GPUGraphicsPipelineCreateInfo(ctypes.Structure):
    _fields_ = [
        ("vertex_shader", ctypes.POINTER(SDL_GPUShader)),
        ("fragment_shader", ctypes.POINTER(SDL_GPUShader)),
        ("vertex_input_state", SDL_GPUVertexInputState),
        ("primitive_type", SDL_GPUPrimitiveType),
        ("rasterizer_state", SDL_GPURasterizerState),
        ("multisample_state", SDL_GPUMultisampleState),
        ("depth_stencil_state", SDL_GPUDepthStencilState),
        ("target_info", SDL_GPUGraphicsPipelineTargetInfo),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUComputePipelineCreateInfo(ctypes.Structure):
    _fields_ = [
        ("code_size", ctypes.c_size_t),
        ("code", ctypes.POINTER(ctypes.c_uint8)),
        ("entrypoint", ctypes.c_char_p),
        ("format", SDL_GPUShaderFormat),
        ("num_samplers", ctypes.c_uint32),
        ("num_readonly_storage_textures", ctypes.c_uint32),
        ("num_readonly_storage_buffers", ctypes.c_uint32),
        ("num_readwrite_storage_textures", ctypes.c_uint32),
        ("num_readwrite_storage_buffers", ctypes.c_uint32),
        ("num_uniform_buffers", ctypes.c_uint32),
        ("threadcount_x", ctypes.c_uint32),
        ("threadcount_y", ctypes.c_uint32),
        ("threadcount_z", ctypes.c_uint32),
        ("props", SDL_PropertiesID)
    ]

class SDL_GPUColorTargetInfo(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("mip_level", ctypes.c_uint32),
        ("layer_or_depth_plane", ctypes.c_uint32),
        ("clear_color", SDL_FColor),
        ("load_op", SDL_GPULoadOp),
        ("store_op", SDL_GPUStoreOp),
        ("resolve_texture", ctypes.POINTER(SDL_GPUTexture)),
        ("resolve_mip_level", ctypes.c_uint32),
        ("resolve_layer", ctypes.c_uint32),
        ("cycle", ctypes.c_bool),
        ("cycle_resolve_texture", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_GPUDepthStencilTargetInfo(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("clear_depth", ctypes.c_float),
        ("load_op", SDL_GPULoadOp),
        ("store_op", SDL_GPUStoreOp),
        ("stencil_load_op", SDL_GPULoadOp),
        ("stencil_store_op", SDL_GPUStoreOp),
        ("cycle", ctypes.c_bool),
        ("clear_stencil", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_GPUBlitInfo(ctypes.Structure):
    _fields_ = [
        ("source", SDL_GPUBlitRegion),
        ("destination", SDL_GPUBlitRegion),
        ("load_op", SDL_GPULoadOp),
        ("clear_color", SDL_FColor),
        ("flip_mode", SDL_FlipMode),
        ("filter", SDL_GPUFilter),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_GPUBufferBinding(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.POINTER(SDL_GPUBuffer)),
        ("offset", ctypes.c_uint32)
    ]

class SDL_GPUTextureSamplerBinding(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("sampler", ctypes.POINTER(SDL_GPUSampler))
    ]

class SDL_GPUStorageBufferReadWriteBinding(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.POINTER(SDL_GPUBuffer)),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_GPUStorageTextureReadWriteBinding(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.POINTER(SDL_GPUTexture)),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

SDL_FUNC("SDL_GPUSupportsShaderFormats", ctypes.c_bool, SDL_GPUShaderFormat, ctypes.c_char_p)
SDL_FUNC("SDL_GPUSupportsProperties", ctypes.c_bool, SDL_PropertiesID)

SDL_FUNC("SDL_CreateGPUDevice", ctypes.POINTER(SDL_GPUDevice), SDL_GPUShaderFormat, ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("SDL_CreateGPUDeviceWithProperties", ctypes.POINTER(SDL_GPUDevice), SDL_PropertiesID)

SDL_PROP_GPU_DEVICE_CREATE_DEBUGMODE_BOOLEAN = "SDL.gpu.device.create.debugmode".encode()
SDL_PROP_GPU_DEVICE_CREATE_PREFERLOWPOWER_BOOLEAN = "SDL.gpu.device.create.preferlowpower".encode()
SDL_PROP_GPU_DEVICE_CREATE_NAME_STRING = "SDL.gpu.device.create.name".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_PRIVATE_BOOLEAN = "SDL.gpu.device.create.shaders.private".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_SPIRV_BOOLEAN = "SDL.gpu.device.create.shaders.spirv".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXBC_BOOLEAN = "SDL.gpu.device.create.shaders.dxbc".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_DXIL_BOOLEAN = "SDL.gpu.device.create.shaders.dxil".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_MSL_BOOLEAN = "SDL.gpu.device.create.shaders.msl".encode()
SDL_PROP_GPU_DEVICE_CREATE_SHADERS_METALLIB_BOOLEAN = "SDL.gpu.device.create.shaders.metallib".encode()
SDL_PROP_GPU_DEVICE_CREATE_D3D12_SEMANTIC_NAME_STRING = "SDL.gpu.device.create.d3d12.semantic".encode()

SDL_FUNC("SDL_DestroyGPUDevice", None, ctypes.POINTER(SDL_GPUDevice))

SDL_FUNC("SDL_GetNumGPUDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetGPUDriver", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_GetGPUDeviceDriver", ctypes.c_char_p, ctypes.POINTER(SDL_GPUDevice))
SDL_FUNC("SDL_GetGPUShaderFormats", SDL_GPUShaderFormat, ctypes.POINTER(SDL_GPUDevice))

SDL_FUNC("SDL_CreateGPUComputePipeline", ctypes.POINTER(SDL_GPUComputePipeline), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUComputePipelineCreateInfo))

SDL_PROP_GPU_COMPUTEPIPELINE_CREATE_NAME_STRING = "SDL.gpu.computepipeline.create.name".encode()

SDL_FUNC("SDL_CreateGPUGraphicsPipeline", ctypes.POINTER(SDL_GPUGraphicsPipeline), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUGraphicsPipelineCreateInfo))

SDL_PROP_GPU_GRAPHICSPIPELINE_CREATE_NAME_STRING = "SDL.gpu.graphicspipeline.create.name".encode()

SDL_FUNC("SDL_CreateGPUSampler", ctypes.POINTER(SDL_GPUSampler), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUSamplerCreateInfo))

SDL_PROP_GPU_SAMPLER_CREATE_NAME_STRING = "SDL.gpu.sampler.create.name".encode()

SDL_FUNC("SDL_CreateGPUShader", ctypes.POINTER(SDL_GPUShader), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUShaderCreateInfo))

SDL_PROP_GPU_SHADER_CREATE_NAME_STRING = "SDL.gpu.shader.create.name".encode()

SDL_FUNC("SDL_CreateGPUTexture", ctypes.POINTER(SDL_GPUTexture), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTextureCreateInfo))

SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_R_FLOAT = "SDL.gpu.texture.create.d3d12.clear.r".encode()
SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_G_FLOAT = "SDL.gpu.texture.create.d3d12.clear.g".encode()
SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_B_FLOAT = "SDL.gpu.texture.create.d3d12.clear.b".encode()
SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_A_FLOAT = "SDL.gpu.texture.create.d3d12.clear.a".encode()
SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_DEPTH_FLOAT = "SDL.gpu.texture.create.d3d12.clear.depth".encode()
SDL_PROP_GPU_TEXTURE_CREATE_D3D12_CLEAR_STENCIL_UINT8 = "SDL.gpu.texture.create.d3d12.clear.stencil".encode()
SDL_PROP_GPU_TEXTURE_CREATE_NAME_STRING = "SDL.gpu.texture.create.name".encode()

SDL_FUNC("SDL_CreateGPUBuffer", ctypes.POINTER(SDL_GPUBuffer), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUBufferCreateInfo))

SDL_PROP_GPU_BUFFER_CREATE_NAME_STRING = "SDL.gpu.buffer.create.name".encode()

SDL_FUNC("SDL_CreateGPUTransferBuffer", ctypes.POINTER(SDL_GPUTransferBuffer), ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTransferBufferCreateInfo))

SDL_PROP_GPU_TRANSFERBUFFER_CREATE_NAME_STRING = "SDL.gpu.transferbuffer.create.name".encode()

SDL_FUNC("SDL_SetGPUBufferName", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUBuffer), ctypes.c_char_p)
SDL_FUNC("SDL_SetGPUTextureName", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTexture), ctypes.c_char_p)

SDL_FUNC("SDL_InsertGPUDebugLabel", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.c_char_p)
SDL_FUNC("SDL_PushGPUDebugGroup", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.c_char_p)
SDL_FUNC("SDL_PopGPUDebugGroup", None, ctypes.POINTER(SDL_GPUCommandBuffer))

SDL_FUNC("SDL_ReleaseGPUTexture", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTexture))
SDL_FUNC("SDL_ReleaseGPUSampler", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUSampler))
SDL_FUNC("SDL_ReleaseGPUBuffer", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUBuffer))
SDL_FUNC("SDL_ReleaseGPUTransferBuffer", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTransferBuffer))
SDL_FUNC("SDL_ReleaseGPUComputePipeline", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUComputePipeline))
SDL_FUNC("SDL_ReleaseGPUShader", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUShader))
SDL_FUNC("SDL_ReleaseGPUGraphicsPipeline", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUGraphicsPipeline))

SDL_FUNC("SDL_AcquireGPUCommandBuffer", ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_GPUDevice))

SDL_FUNC("SDL_PushGPUVertexUniformData", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
SDL_FUNC("SDL_PushGPUFragmentUniformData", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
SDL_FUNC("SDL_PushGPUComputeUniformData", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)

SDL_FUNC("SDL_BeginGPURenderPass", ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_GPUColorTargetInfo), ctypes.c_uint32, ctypes.POINTER(SDL_GPUDepthStencilTargetInfo))
SDL_FUNC("SDL_BindGPUGraphicsPipeline", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUGraphicsPipeline))
SDL_FUNC("SDL_SetGPUViewport", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUViewport))
SDL_FUNC("SDL_SetGPUScissor", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_SetGPUBlendConstants", None, ctypes.POINTER(SDL_GPURenderPass), SDL_FColor)
SDL_FUNC("SDL_SetGPUStencilReference", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint8)
SDL_FUNC("SDL_BindGPUVertexBuffers", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUBufferBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUIndexBuffer", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUBufferBinding), SDL_GPUIndexElementSize)
SDL_FUNC("SDL_BindGPUVertexSamplers", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUTextureSamplerBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUVertexStorageTextures", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(ctypes.POINTER(SDL_GPUTexture)), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUVertexStorageBuffers", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUBufferBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUFragmentSamplers", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUTextureSamplerBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUFragmentStorageTextures", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(ctypes.POINTER(SDL_GPUTexture)), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUFragmentStorageBuffers", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUBufferBinding), ctypes.c_uint32)
SDL_FUNC("SDL_DrawGPUIndexedPrimitives", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint32)
SDL_FUNC("SDL_DrawGPUPrimitives", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_DrawGPUPrimitivesIndirect", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUBuffer), ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_DrawGPUIndexedPrimitivesIndirect", None, ctypes.POINTER(SDL_GPURenderPass), ctypes.POINTER(SDL_GPUBuffer), ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_EndGPURenderPass", None, ctypes.POINTER(SDL_GPURenderPass))

SDL_FUNC("SDL_BeginGPUComputePass", ctypes.POINTER(SDL_GPUComputePass), ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_GPUStorageTextureReadWriteBinding), ctypes.c_uint32, ctypes.POINTER(SDL_GPUStorageBufferReadWriteBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUComputePipeline", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.POINTER(SDL_GPUComputePipeline))
SDL_FUNC("SDL_BindGPUComputeSamplers", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUTextureSamplerBinding), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUComputeStorageTextures", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.c_uint32, ctypes.POINTER(ctypes.POINTER(SDL_GPUTexture)), ctypes.c_uint32)
SDL_FUNC("SDL_BindGPUComputeStorageBuffers", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.c_uint32, ctypes.POINTER(SDL_GPUBufferBinding), ctypes.c_uint32)
SDL_FUNC("SDL_DispatchGPUCompute", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_DispatchGPUComputeIndirect", None, ctypes.POINTER(SDL_GPUComputePass), ctypes.POINTER(SDL_GPUBuffer), ctypes.c_uint32)
SDL_FUNC("SDL_EndGPUComputePass", None, ctypes.POINTER(SDL_GPUComputePass))

SDL_FUNC("SDL_MapGPUTransferBuffer", ctypes.c_void_p, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTransferBuffer), ctypes.c_bool)
SDL_FUNC("SDL_UnmapGPUTransferBuffer", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUTransferBuffer))

SDL_FUNC("SDL_BeginGPUCopyPass", ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUCommandBuffer))
SDL_FUNC("SDL_UploadToGPUTexture", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUTextureTransferInfo), ctypes.POINTER(SDL_GPUTextureRegion), ctypes.c_bool)
SDL_FUNC("SDL_UploadToGPUBuffer", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUTransferBufferLocation), ctypes.POINTER(SDL_GPUBufferRegion), ctypes.c_bool)
SDL_FUNC("SDL_CopyGPUTextureToTexture", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUTextureLocation), ctypes.POINTER(SDL_GPUTextureLocation), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_bool)
SDL_FUNC("SDL_CopyGPUBufferToBuffer", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUBufferLocation), ctypes.POINTER(SDL_GPUBufferLocation), ctypes.c_uint32, ctypes.c_bool)
SDL_FUNC("SDL_DownloadFromGPUTexture", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUTextureRegion), ctypes.POINTER(SDL_GPUTextureTransferInfo))
SDL_FUNC("SDL_DownloadFromGPUBuffer", None, ctypes.POINTER(SDL_GPUCopyPass), ctypes.POINTER(SDL_GPUBufferRegion), ctypes.POINTER(SDL_GPUTransferBufferLocation))
SDL_FUNC("SDL_EndGPUCopyPass", None, ctypes.POINTER(SDL_GPUCopyPass))

SDL_FUNC("SDL_GenerateMipmapsForGPUTexture", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_GPUTexture))
SDL_FUNC("SDL_BlitGPUTexture", None, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_GPUBlitInfo))

SDL_FUNC("SDL_WindowSupportsGPUSwapchainComposition", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window), SDL_GPUSwapchainComposition)
SDL_FUNC("SDL_WindowSupportsGPUPresentMode", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window), SDL_GPUPresentMode)
SDL_FUNC("SDL_ClaimWindowForGPUDevice", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_ReleaseWindowFromGPUDevice", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_SetGPUSwapchainParameters", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window), SDL_GPUSwapchainComposition, SDL_GPUPresentMode)
SDL_FUNC("SDL_SetGPUAllowedFramesInFlight", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.c_uint32)
SDL_FUNC("SDL_GetGPUSwapchainTextureFormat", SDL_GPUTextureFormat, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_AcquireGPUSwapchainTexture", ctypes.c_bool, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.POINTER(SDL_GPUTexture)), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_WaitForGPUSwapchain", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_WaitAndAcquireGPUSwapchainTexture", ctypes.c_bool, ctypes.POINTER(SDL_GPUCommandBuffer), ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.POINTER(SDL_GPUTexture)), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32))

SDL_FUNC("SDL_SubmitGPUCommandBuffer", ctypes.c_bool, ctypes.POINTER(SDL_GPUCommandBuffer))
SDL_FUNC("SDL_SubmitGPUCommandBufferAndAcquireFence", ctypes.POINTER(SDL_GPUFence), ctypes.POINTER(SDL_GPUCommandBuffer))
SDL_FUNC("SDL_CancelGPUCommandBuffer", ctypes.c_bool, ctypes.POINTER(SDL_GPUCommandBuffer))

SDL_FUNC("SDL_WaitForGPUIdle", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice))
SDL_FUNC("SDL_WaitForGPUFences", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.c_bool, ctypes.POINTER(ctypes.POINTER(SDL_GPUFence)), ctypes.c_uint32)

SDL_FUNC("SDL_QueryGPUFence", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUFence))
SDL_FUNC("SDL_ReleaseGPUFence", None, ctypes.POINTER(SDL_GPUDevice), ctypes.POINTER(SDL_GPUFence))

SDL_FUNC("SDL_GPUTextureFormatTexelBlockSize", ctypes.c_uint32, SDL_GPUTextureFormat)
SDL_FUNC("SDL_GPUTextureSupportsFormat", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), SDL_GPUTextureFormat, SDL_GPUTextureType, SDL_GPUTextureUsageFlags)
SDL_FUNC("SDL_GPUTextureSupportsSampleCount", ctypes.c_bool, ctypes.POINTER(SDL_GPUDevice), SDL_GPUTextureFormat, SDL_GPUSampleCount)
SDL_FUNC("SDL_CalculateGPUTextureFormatSize", ctypes.c_uint32, SDL_GPUTextureFormat, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)