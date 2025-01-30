from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_events import SDL_Event
from .SDL_rect import SDL_Point, SDL_FPoint, SDL_Rect, SDL_FRect
from .SDL_pixels import SDL_Color, SDL_FColor, SDL_PixelFormat
from .SDL_surface import SDL_Surface, SDL_ScaleMode, SDL_FlipMode
from .SDL_video import SDL_Window, SDL_WindowFlags
from .SDL_properties import SDL_PropertiesID
from .SDL_blendmode import SDL_BlendMode

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_SOFTWARE_RENDERER = "software".encode()

class SDL_Vertex(ctypes.Structure):
    _fields_ = [
        ("position", SDL_FPoint),
        ("color", SDL_Color),
        ("tex_coord", SDL_FPoint)
    ]

SDL_TextureAccess = ctypes.c_int

SDL_TEXTUREACCESS_STATIC = 0
SDL_TEXTUREACCESS_STREAMING = 1
SDL_TEXTUREACCESS_TARGET = 2

SDL_RendererLogicalPresentation = ctypes.c_int

SDL_LOGICAL_PRESENTATION_DISABLED = 0
SDL_LOGICAL_PRESENTATION_STRETCH = 1
SDL_LOGICAL_PRESENTATION_LETTERBOX = 2
SDL_LOGICAL_PRESENTATION_OVERSCAN = 3
SDL_LOGICAL_PRESENTATION_INTEGER_SCALE = 4

class SDL_Renderer(ctypes.c_void_p):
    ...

class SDL_Texture(ctypes.Structure):
    _fields_ = [
        ("format", SDL_PixelFormat),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("refcount", ctypes.c_int)
    ]

SDL_FUNC("SDL_GetNumRenderDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetRenderDriver", ctypes.c_char_p, ctypes.c_int)

SDL_FUNC("SDL_CreateWindowAndRenderer", ctypes.c_bool, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, SDL_WindowFlags, ctypes.POINTER(ctypes.POINTER(SDL_Window)), ctypes.POINTER(ctypes.POINTER(SDL_Renderer)))
SDL_FUNC("SDL_CreateRenderer", ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Window), ctypes.c_char_p)
SDL_FUNC("SDL_CreateRendererWithProperties", ctypes.POINTER(SDL_Renderer), SDL_PropertiesID)

SDL_PROP_RENDERER_CREATE_NAME_STRING = "SDL.renderer.create.name".encode()
SDL_PROP_RENDERER_CREATE_WINDOW_POINTER = "SDL.renderer.create.window".encode()
SDL_PROP_RENDERER_CREATE_SURFACE_POINTER = "SDL.renderer.create.surface".encode()
SDL_PROP_RENDERER_CREATE_OUTPUT_COLORSPACE_NUMBER = "SDL.renderer.create.output_colorspace".encode()
SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_NUMBER = "SDL.renderer.create.present_vsync".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_INSTANCE_POINTER = "SDL.renderer.create.vulkan.instance".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_SURFACE_NUMBER = "SDL.renderer.create.vulkan.surface".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_PHYSICAL_DEVICE_POINTER = "SDL.renderer.create.vulkan.physical_device".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_DEVICE_POINTER = "SDL.renderer.create.vulkan.device".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER = "SDL.renderer.create.vulkan.graphics_queue_family_index".encode()
SDL_PROP_RENDERER_CREATE_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER = "SDL.renderer.create.vulkan.present_queue_family_index".encode()

SDL_FUNC("SDL_CreateSoftwareRenderer", ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_GetRenderer", ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetRenderWindow", ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Renderer))
SDL_FUNC("SDL_GetRendererName", ctypes.c_char_p, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_GetRendererProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Renderer))

SDL_PROP_RENDERER_NAME_STRING = "SDL.renderer.name".encode()
SDL_PROP_RENDERER_WINDOW_POINTER = "SDL.renderer.window".encode()
SDL_PROP_RENDERER_SURFACE_POINTER = "SDL.renderer.surface".encode()
SDL_PROP_RENDERER_VSYNC_NUMBER = "SDL.renderer.vsync".encode()
SDL_PROP_RENDERER_MAX_TEXTURE_SIZE_NUMBER = "SDL.renderer.max_texture_size".encode()
SDL_PROP_RENDERER_TEXTURE_FORMATS_POINTER = "SDL.renderer.texture_formats".encode()
SDL_PROP_RENDERER_OUTPUT_COLORSPACE_NUMBER = "SDL.renderer.output_colorspace".encode()
SDL_PROP_RENDERER_HDR_ENABLED_BOOLEAN = "SDL.renderer.HDR_enabled".encode()
SDL_PROP_RENDERER_SDR_WHITE_POINT_FLOAT = "SDL.renderer.SDR_white_point".encode()
SDL_PROP_RENDERER_HDR_HEADROOM_FLOAT = "SDL.renderer.HDR_headroom".encode()
SDL_PROP_RENDERER_D3D9_DEVICE_POINTER = "SDL.renderer.d3d9.device".encode()
SDL_PROP_RENDERER_D3D11_DEVICE_POINTER = "SDL.renderer.d3d11.device".encode()
SDL_PROP_RENDERER_D3D11_SWAPCHAIN_POINTER = "SDL.renderer.d3d11.swap_chain".encode()
SDL_PROP_RENDERER_D3D12_DEVICE_POINTER = "SDL.renderer.d3d12.device".encode()
SDL_PROP_RENDERER_D3D12_SWAPCHAIN_POINTER = "SDL.renderer.d3d12.swap_chain".encode()
SDL_PROP_RENDERER_D3D12_COMMAND_QUEUE_POINTER = "SDL.renderer.d3d12.command_queue".encode()
SDL_PROP_RENDERER_VULKAN_INSTANCE_POINTER = "SDL.renderer.vulkan.instance".encode()
SDL_PROP_RENDERER_VULKAN_SURFACE_NUMBER = "SDL.renderer.vulkan.surface".encode()
SDL_PROP_RENDERER_VULKAN_PHYSICAL_DEVICE_POINTER = "SDL.renderer.vulkan.physical_device".encode()
SDL_PROP_RENDERER_VULKAN_DEVICE_POINTER = "SDL.renderer.vulkan.device".encode()
SDL_PROP_RENDERER_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER = "SDL.renderer.vulkan.graphics_queue_family_index".encode()
SDL_PROP_RENDERER_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER = "SDL.renderer.vulkan.present_queue_family_index".encode()
SDL_PROP_RENDERER_VULKAN_SWAPCHAIN_IMAGE_COUNT_NUMBER = "SDL.renderer.vulkan.swapchain_image_count".encode()
SDL_PROP_RENDERER_GPU_DEVICE_POINTER = "SDL.renderer.gpu.device".encode()

SDL_FUNC("SDL_GetRenderOutputSize", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetCurrentRenderOutputSize", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_CreateTexture", ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Renderer), SDL_PixelFormat, SDL_TextureAccess, ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_CreateTextureFromSurface", ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_CreateTextureWithProperties", ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Renderer), SDL_PropertiesID)

SDL_PROP_TEXTURE_CREATE_COLORSPACE_NUMBER = "SDL.texture.create.colorspace".encode()
SDL_PROP_TEXTURE_CREATE_FORMAT_NUMBER = "SDL.texture.create.format".encode()
SDL_PROP_TEXTURE_CREATE_ACCESS_NUMBER = "SDL.texture.create.access".encode()
SDL_PROP_TEXTURE_CREATE_WIDTH_NUMBER = "SDL.texture.create.width".encode()
SDL_PROP_TEXTURE_CREATE_HEIGHT_NUMBER = "SDL.texture.create.height".encode()
SDL_PROP_TEXTURE_CREATE_SDR_WHITE_POINT_FLOAT = "SDL.texture.create.SDR_white_point".encode()
SDL_PROP_TEXTURE_CREATE_HDR_HEADROOM_FLOAT = "SDL.texture.create.HDR_headroom".encode()
SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_POINTER = "SDL.texture.create.d3d11.texture".encode()
SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_U_POINTER = "SDL.texture.create.d3d11.texture_u".encode()
SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_V_POINTER = "SDL.texture.create.d3d11.texture_v".encode()
SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_POINTER = "SDL.texture.create.d3d12.texture".encode()
SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_U_POINTER = "SDL.texture.create.d3d12.texture_u".encode()
SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_V_POINTER = "SDL.texture.create.d3d12.texture_v".encode()
SDL_PROP_TEXTURE_CREATE_METAL_PIXELBUFFER_POINTER = "SDL.texture.create.metal.pixelbuffer".encode()
SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_NUMBER = "SDL.texture.create.opengl.texture".encode()
SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_UV_NUMBER = "SDL.texture.create.opengl.texture_uv".encode()
SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_U_NUMBER = "SDL.texture.create.opengl.texture_u".encode()
SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_V_NUMBER = "SDL.texture.create.opengl.texture_v".encode()
SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_NUMBER = "SDL.texture.create.opengles2.texture".encode()
SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_UV_NUMBER = "SDL.texture.create.opengles2.texture_uv".encode()
SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_U_NUMBER = "SDL.texture.create.opengles2.texture_u".encode()
SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_V_NUMBER = "SDL.texture.create.opengles2.texture_v".encode()
SDL_PROP_TEXTURE_CREATE_VULKAN_TEXTURE_NUMBER = "SDL.texture.create.vulkan.texture".encode()

SDL_FUNC("SDL_GetTextureProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Texture))

SDL_PROP_TEXTURE_COLORSPACE_NUMBER = "SDL.texture.colorspace".encode()
SDL_PROP_TEXTURE_FORMAT_NUMBER = "SDL.texture.format".encode()
SDL_PROP_TEXTURE_ACCESS_NUMBER = "SDL.texture.access".encode()
SDL_PROP_TEXTURE_WIDTH_NUMBER = "SDL.texture.width".encode()
SDL_PROP_TEXTURE_HEIGHT_NUMBER = "SDL.texture.height".encode()
SDL_PROP_TEXTURE_SDR_WHITE_POINT_FLOAT = "SDL.texture.SDR_white_point".encode()
SDL_PROP_TEXTURE_HDR_HEADROOM_FLOAT = "SDL.texture.HDR_headroom".encode()
SDL_PROP_TEXTURE_D3D11_TEXTURE_POINTER = "SDL.texture.d3d11.texture".encode()
SDL_PROP_TEXTURE_D3D11_TEXTURE_U_POINTER = "SDL.texture.d3d11.texture_u".encode()
SDL_PROP_TEXTURE_D3D11_TEXTURE_V_POINTER = "SDL.texture.d3d11.texture_v".encode()
SDL_PROP_TEXTURE_D3D12_TEXTURE_POINTER = "SDL.texture.d3d12.texture".encode()
SDL_PROP_TEXTURE_D3D12_TEXTURE_U_POINTER = "SDL.texture.d3d12.texture_u".encode()
SDL_PROP_TEXTURE_D3D12_TEXTURE_V_POINTER = "SDL.texture.d3d12.texture_v".encode()
SDL_PROP_TEXTURE_OPENGL_TEXTURE_NUMBER = "SDL.texture.opengl.texture".encode()
SDL_PROP_TEXTURE_OPENGL_TEXTURE_UV_NUMBER = "SDL.texture.opengl.texture_uv".encode()
SDL_PROP_TEXTURE_OPENGL_TEXTURE_U_NUMBER = "SDL.texture.opengl.texture_u".encode()
SDL_PROP_TEXTURE_OPENGL_TEXTURE_V_NUMBER = "SDL.texture.opengl.texture_v".encode()
SDL_PROP_TEXTURE_OPENGL_TEXTURE_TARGET_NUMBER = "SDL.texture.opengl.target".encode()
SDL_PROP_TEXTURE_OPENGL_TEX_W_FLOAT = "SDL.texture.opengl.tex_w".encode()
SDL_PROP_TEXTURE_OPENGL_TEX_H_FLOAT = "SDL.texture.opengl.tex_h".encode()
SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_NUMBER = "SDL.texture.opengles2.texture".encode()
SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_UV_NUMBER = "SDL.texture.opengles2.texture_uv".encode()
SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_U_NUMBER = "SDL.texture.opengles2.texture_u".encode()
SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_V_NUMBER = "SDL.texture.opengles2.texture_v".encode()
SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_TARGET_NUMBER = "SDL.texture.opengles2.target".encode()
SDL_PROP_TEXTURE_VULKAN_TEXTURE_NUMBER = "SDL.texture.vulkan.texture".encode()

SDL_FUNC("SDL_GetRendererFromTexture", ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture))
SDL_FUNC("SDL_GetTextureSize", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetTextureColorMod", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_SetTextureColorModFloat", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.c_float, ctypes.c_float, ctypes.c_float)

SDL_FUNC("SDL_GetTextureColorMod", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_GetTextureColorModFloat", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetTextureAlphaMod", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.c_uint8)
SDL_FUNC("SDL_SetTextureAlphaModFloat", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.c_float)

SDL_FUNC("SDL_GetTextureAlphaMod", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_GetTextureAlphaModFloat", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetTextureBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Texture), SDL_BlendMode)
SDL_FUNC("SDL_GetTextureBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_BlendMode))

SDL_FUNC("SDL_SetTextureScaleMode", ctypes.c_bool, ctypes.POINTER(SDL_Texture), SDL_ScaleMode)
SDL_FUNC("SDL_GetTextureScaleMode", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_ScaleMode))

SDL_FUNC("SDL_UpdateTexture", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Rect), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_UpdateYUVTexture", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Rect), ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_UpdateNVTexture", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Rect), ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)

SDL_FUNC("SDL_LockTexture", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Rect), ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_LockTextureToSurface", ctypes.c_bool, ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Rect), ctypes.POINTER(ctypes.POINTER(SDL_Surface)))
SDL_FUNC("SDL_UnlockTexture", None, ctypes.POINTER(SDL_Texture))

SDL_FUNC("SDL_SetRenderTarget", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture))
SDL_FUNC("SDL_GetRenderTarget", ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_SetRenderLogicalPresentation", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_int, ctypes.c_int, SDL_RendererLogicalPresentation)
SDL_FUNC("SDL_GetRenderLogicalPresentation", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(SDL_RendererLogicalPresentation))
SDL_FUNC("SDL_GetRenderLogicalPresentationRect", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_RenderCoordinatesFromWindow", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_RenderCoordinatesToWindow", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_ConvertEventToRenderCoordinates", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Event))

SDL_FUNC("SDL_SetRenderViewport", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRenderViewport", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_RenderViewportSet", ctypes.c_bool, ctypes.POINTER(SDL_Renderer))
SDL_FUNC("SDL_GetRenderSafeArea", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_SetRenderClipRect", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetRenderClipRect", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_RenderClipEnabled", ctypes.c_bool, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_SetRenderScale", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_GetRenderScale", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetRenderDrawColor", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_SetRenderDrawColorFloat", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)

SDL_FUNC("SDL_GetRenderDrawColor", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("SDL_GetRenderDrawColorFloat", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetRenderColorScale", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float)
SDL_FUNC("SDL_GetRenderColorScale", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_SetRenderDrawBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), SDL_BlendMode)
SDL_FUNC("SDL_GetRenderDrawBlendMode", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_BlendMode))

SDL_FUNC("SDL_RenderClear", ctypes.c_bool, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_RenderPoint", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_RenderPoints", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FPoint), ctypes.c_int)

SDL_FUNC("SDL_RenderLine", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_RenderLines", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FPoint), ctypes.c_int)

SDL_FUNC("SDL_RenderRect", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_RenderRects", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FRect), ctypes.c_int)

SDL_FUNC("SDL_RenderFillRect", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_RenderFillRects", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_FRect), ctypes.c_int)

SDL_FUNC("SDL_RenderTexture", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_RenderTextureRotated", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect), ctypes.c_double, ctypes.POINTER(SDL_FPoint), SDL_FlipMode)
SDL_FUNC("SDL_RenderTextureAffine", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FPoint), ctypes.POINTER(SDL_FPoint), ctypes.POINTER(SDL_FPoint))
SDL_FUNC("SDL_RenderTextureTiled", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_FRect), ctypes.c_float, ctypes.POINTER(SDL_FRect))
SDL_FUNC("SDL_RenderTexture9Grid", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_FRect), ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(SDL_FRect))

SDL_FUNC("SDL_RenderGeometry", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(SDL_Vertex), ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int)
SDL_FUNC("SDL_RenderGeometryRaw", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Texture), ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(SDL_FColor), ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)

SDL_FUNC("SDL_RenderReadPixels", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Renderer), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_RenderPresent", ctypes.c_bool, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_DestroyTexture", None, ctypes.POINTER(SDL_Texture))
SDL_FUNC("SDL_DestroyRenderer", None, ctypes.POINTER(SDL_Renderer))
SDL_FUNC("SDL_FlushRenderer", ctypes.c_bool, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_GetRenderMetalLayer", ctypes.c_void_p, ctypes.POINTER(SDL_Renderer))
SDL_FUNC("SDL_GetRenderMetalCommandEncoder", ctypes.c_void_p, ctypes.POINTER(SDL_Renderer))

SDL_FUNC("SDL_AddVulkanRenderSemaphores", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_uint32, ctypes.c_int64, ctypes.c_int64)

SDL_FUNC("SDL_SetRenderVSync", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_int)

SDL_RENDERER_VSYNC_DISABLED = 0
SDL_RENDERER_VSYNC_ADAPTIVE = -1

SDL_FUNC("SDL_GetRenderVSync", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.POINTER(ctypes.c_int))

SDL_DEBUG_TEXT_FONT_CHARACTER_SIZE = 8

SDL_FUNC("SDL_RenderDebugText", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.c_char_p)
SDL_FUNC("SDL_RenderDebugTextFormat", ctypes.c_bool, ctypes.POINTER(SDL_Renderer), ctypes.c_float, ctypes.c_float, ctypes.c_char_p)