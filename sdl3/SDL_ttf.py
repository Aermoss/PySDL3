from .__init__ import ctypes, typing, abc, SDL_PLATFORM_SPECIFIC, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_TTF_BINARY

from .SDL_pixels import SDL_Color
from .SDL_gpu import SDL_GPUDevice, SDL_GPUTexture
from .SDL_properties import SDL_PropertiesID
from .SDL_render import SDL_Renderer
from .SDL_surface import SDL_Surface
from .SDL_iostream import SDL_IOStream
from .SDL_version import SDL_VERSIONNUM
from .SDL_rect import SDL_Rect, SDL_FPoint

SDL_SET_CURRENT_BINARY(SDL_TTF_BINARY)

SDL_TTF_MAJOR_VERSION = 3
SDL_TTF_MINOR_VERSION = 2
SDL_TTF_MICRO_VERSION = 0

SDL_TTF_VERSION = \
    SDL_VERSIONNUM(SDL_TTF_MAJOR_VERSION, SDL_TTF_MINOR_VERSION, SDL_TTF_MICRO_VERSION)

SDL_TTF_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_TTF_MAJOR_VERSION >= x) and \
    (SDL_TTF_MAJOR_VERSION > x or SDL_TTF_MINOR_VERSION >= y) and \
    (SDL_TTF_MAJOR_VERSION > x or SDL_TTF_MINOR_VERSION > y or SDL_TTF_MICRO_VERSION >= z)

TTF_Version: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_Version", ctypes.c_int, []]
TTF_GetFreeTypeVersion: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFreeTypeVersion", None, [SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]
TTF_GetHarfBuzzVersion: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetHarfBuzzVersion", None, [SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]

class TTF_Font(ctypes.c_void_p):
    ...

TTF_Init: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_Init", ctypes.c_int, []]
TTF_OpenFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_OpenFont", SDL_POINTER[TTF_Font], [ctypes.c_char_p, ctypes.c_float]]
TTF_OpenFontIO: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_OpenFontIO", SDL_POINTER[TTF_Font], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_float]]
TTF_OpenFontWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_OpenFontWithProperties", SDL_POINTER[TTF_Font], [SDL_PropertiesID]]

TTF_PROP_FONT_CREATE_FILENAME_STRING = "SDL_ttf.font.create.filename".encode()
TTF_PROP_FONT_CREATE_IOSTREAM_POINTER = "SDL_ttf.font.create.iostream".encode()
TTF_PROP_FONT_CREATE_IOSTREAM_OFFSET_NUMBER = "SDL_ttf.font.create.iostream.offset".encode()
TTF_PROP_FONT_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN = "SDL_ttf.font.create.iostream.autoclose".encode()
TTF_PROP_FONT_CREATE_SIZE_FLOAT = "SDL_ttf.font.create.size".encode()
TTF_PROP_FONT_CREATE_FACE_NUMBER = "SDL_ttf.font.create.face".encode()
TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER = "SDL_ttf.font.create.hdpi".encode()
TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER = "SDL_ttf.font.create.vdpi".encode()
TTF_PROP_FONT_CREATE_EXISTING_FONT = "SDL_ttf.font.create.existing_font"

TTF_CopyFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CopyFont", SDL_POINTER[TTF_Font], [SDL_POINTER[TTF_Font]]]

TTF_GetFontProperties: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontProperties", SDL_PropertiesID, [SDL_POINTER[TTF_Font]]]

TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER = "SDL_ttf.font.outline.line_cap".encode()
TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER = "SDL_ttf.font.outline.line_join".encode()
TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER = "SDL_ttf.font.outline.miter_limit".encode()

TTF_GetFontGeneration: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontGeneration", ctypes.c_uint32, [SDL_POINTER[TTF_Font]]]

TTF_AddFallbackFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_AddFallbackFont", ctypes.c_bool, [SDL_POINTER[TTF_Font], SDL_POINTER[TTF_Font]]]
TTF_RemoveFallbackFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RemoveFallbackFont", None, [SDL_POINTER[TTF_Font], SDL_POINTER[TTF_Font]]]
TTF_ClearFallbackFonts: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_ClearFallbackFonts", None, [SDL_POINTER[TTF_Font]]]

TTF_SetFontSize: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontSize", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_float]]
TTF_SetFontSizeDPI: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontSizeDPI", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_float, ctypes.c_int, ctypes.c_int]]

TTF_GetFontSize: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontSize", ctypes.c_float, [SDL_POINTER[TTF_Font]]]
TTF_GetFontDPI: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontDPI", ctypes.c_bool, [SDL_POINTER[TTF_Font], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]

TTF_FontStyleFlags: typing.TypeAlias = SDL_TYPE["TTF_FontStyleFlags", ctypes.c_uint32]

TTF_STYLE_NORMAL = 0x00
TTF_STYLE_BOLD = 0x01
TTF_STYLE_ITALIC = 0x02
TTF_STYLE_UNDERLINE = 0x04
TTF_STYLE_STRIKETHROUGH = 0x08

TTF_SetFontStyle: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontStyle", None, [SDL_POINTER[TTF_Font], TTF_FontStyleFlags]]
TTF_GetFontStyle: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontStyle", TTF_FontStyleFlags, [SDL_POINTER[TTF_Font]]]
TTF_SetFontOutline: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontOutline", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_int]]
TTF_GetFontOutline: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontOutline", ctypes.c_int, [SDL_POINTER[TTF_Font]]]

TTF_HintingFlags: typing.TypeAlias = SDL_TYPE["TTF_HintingFlags", ctypes.c_int]

TTF_HINTING_NORMAL = 0
TTF_HINTING_LIGHT = 1
TTF_HINTING_MONO = 2
TTF_HINTING_NONE = 3
TTF_HINTING_LIGHT_SUBPIXEL = 4

TTF_SetFontHinting: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontHinting", None, [SDL_POINTER[TTF_Font], TTF_HintingFlags]]
TTF_GetNumFontFaces: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetNumFontFaces", ctypes.c_int, [SDL_POINTER[TTF_Font]]]
TTF_GetFontHinting: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontHinting", TTF_HintingFlags, [SDL_POINTER[TTF_Font]]]

TTF_SetFontSDF: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontSDF", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_bool]]
TTF_GetFontSDF: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontSDF", ctypes.c_bool, [SDL_POINTER[TTF_Font]]]

TTF_HorizontalAlignment: typing.TypeAlias = SDL_TYPE["TTF_HorizontalAlignment", ctypes.c_int]

TTF_HORIZONTAL_ALIGN_INVALID = -1
TTF_HORIZONTAL_ALIGN_LEFT = 0
TTF_HORIZONTAL_ALIGN_CENTER = 1
TTF_HORIZONTAL_ALIGN_RIGHT = 2

TTF_SetFontWrapAlignment: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontWrapAlignment", None, [SDL_POINTER[TTF_Font], TTF_HorizontalAlignment]]
TTF_GetFontWrapAlignment: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontWrapAlignment", TTF_HorizontalAlignment, [SDL_POINTER[TTF_Font]]]

TTF_GetFontHeight: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontHeight", ctypes.c_int, [SDL_POINTER[TTF_Font]]]
TTF_GetFontAscent: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontAscent", ctypes.c_int, [SDL_POINTER[TTF_Font]]]
TTF_GetFontDescent: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontDescent", ctypes.c_int, [SDL_POINTER[TTF_Font]]]

TTF_SetFontLineSkip: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontLineSkip", None, [SDL_POINTER[TTF_Font], ctypes.c_int]]
TTF_GetFontLineSkip: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontLineSkip", ctypes.c_int, [SDL_POINTER[TTF_Font]]]

TTF_SetFontKerning: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontKerning", None, [SDL_POINTER[TTF_Font], ctypes.c_bool]]
TTF_GetFontKerning: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontKerning", ctypes.c_bool, [SDL_POINTER[TTF_Font]]]

TTF_FontIsFixedWidth: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_FontIsFixedWidth", ctypes.c_bool, [SDL_POINTER[TTF_Font]]]
TTF_FontIsScalable: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_FontIsScalable", ctypes.c_bool, [SDL_POINTER[TTF_Font]]]

TTF_GetFontFamilyName: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontFamilyName", ctypes.c_char_p, [SDL_POINTER[TTF_Font]]]
TTF_GetFontStyleName: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontStyleName", ctypes.c_char_p, [SDL_POINTER[TTF_Font]]]

TTF_Direction: typing.TypeAlias = SDL_TYPE["TTF_Direction", ctypes.c_int]

TTF_DIRECTION_INVALID = 0
TTF_DIRECTION_LTR = 4
TTF_DIRECTION_RTL = 5
TTF_DIRECTION_TTB = 6
TTF_DIRECTION_BTT = 7

TTF_SetFontDirection: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontDirection", ctypes.c_bool, [SDL_POINTER[TTF_Font], TTF_Direction]]
TTF_GetFontDirection: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontDirection", TTF_Direction, [SDL_POINTER[TTF_Font]]]

TTF_StringToTag: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_StringToTag", ctypes.c_uint32, [ctypes.c_char_p]]
TTF_TagToString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_TagToString", None, [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_size_t]]

TTF_SetFontScript: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontScript", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_uint32]]
TTF_GetFontScript: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetFontScript", ctypes.c_uint32, [SDL_POINTER[TTF_Font]]]

TTF_GetGlyphScript: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGlyphScript", ctypes.c_uint32, [ctypes.c_uint32]]

TTF_SetFontLanguage: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetFontLanguage", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_char_p]]
TTF_FontHasGlyph: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_FontHasGlyph", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_uint32]]

TTF_ImageType: typing.TypeAlias = SDL_TYPE["TTF_ImageType", ctypes.c_int]

TTF_IMAGE_INVALID = 0
TTF_IMAGE_ALPHA = 1
TTF_IMAGE_COLOR = 2
TTF_IMAGE_SDF = 3

TTF_GetGlyphImage: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGlyphImage", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_POINTER[TTF_ImageType]]]
TTF_GetGlyphImageForIndex: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGlyphImageForIndex", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_POINTER[TTF_ImageType]]]
TTF_GetGlyphMetrics: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGlyphMetrics", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]
TTF_GetGlyphKerning: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGlyphKerning", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_uint32, ctypes.c_uint32, SDL_POINTER[ctypes.c_int]]]

TTF_GetStringSize: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetStringSize", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]
TTF_GetStringSizeWrapped: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetStringSizeWrapped", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]

TTF_MeasureString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_MeasureString", ctypes.c_bool, [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int, SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_size_t]]]

TTF_RenderText_Solid: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Solid", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color]]
TTF_RenderText_Solid_Wrapped: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Solid_Wrapped", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, ctypes.c_int]]
TTF_RenderGlyph_Solid: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderGlyph_Solid", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_Color]]

TTF_RenderText_Shaded: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Shaded", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color]]
TTF_RenderText_Shaded_Wrapped: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Shaded_Wrapped", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color, ctypes.c_int]]
TTF_RenderGlyph_Shaded: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderGlyph_Shaded", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_Color, SDL_Color]]

TTF_RenderText_Blended: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Blended", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color]]
TTF_RenderText_Blended_Wrapped: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_Blended_Wrapped", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, ctypes.c_int]]
TTF_RenderGlyph_Blended: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderGlyph_Blended", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_Color]]

TTF_RenderText_LCD: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_LCD", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color]]
TTF_RenderText_LCD_Wrapped: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderText_LCD_Wrapped", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color, ctypes.c_int]]
TTF_RenderGlyph_LCD: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_RenderGlyph_LCD", SDL_POINTER[SDL_Surface], [SDL_POINTER[TTF_Font], ctypes.c_uint32, SDL_Color, SDL_Color]]

class TTF_TextEngine(ctypes.c_void_p):
    ...

class TTF_TextData(ctypes.c_void_p):
    ...

class TTF_Text(ctypes.Structure):
    _fields_ = [
        ("text", ctypes.c_char_p),
        ("num_lines", ctypes.c_int),
        ("refcount", ctypes.c_int),
        ("internal", SDL_POINTER[TTF_TextData])
    ]

TTF_CreateSurfaceTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateSurfaceTextEngine", SDL_POINTER[TTF_TextEngine], []]
TTF_DrawSurfaceText: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DrawSurfaceText", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_int, SDL_POINTER[SDL_Surface]]]
TTF_DestroySurfaceTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DestroySurfaceTextEngine", None, [SDL_POINTER[TTF_TextEngine]]]

TTF_CreateRendererTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateRendererTextEngine", SDL_POINTER[TTF_TextEngine], [SDL_POINTER[SDL_Renderer]]]
TTF_CreateRendererTextEngineWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateRendererTextEngineWithProperties", SDL_POINTER[TTF_TextEngine], [SDL_PropertiesID]]

TTF_PROP_RENDERER_TEXT_ENGINE_RENDERER = "SDL_ttf.renderer_text_engine.create.renderer"
TTF_PROP_RENDERER_TEXT_ENGINE_ATLAS_TEXTURE_SIZE = "SDL_ttf.renderer_text_engine.create.atlas_texture_size"

TTF_DrawRendererText: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DrawRendererText", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_float, ctypes.c_float]]
TTF_DestroyRendererTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DestroyRendererTextEngine", None, [SDL_POINTER[TTF_TextEngine]]]

TTF_CreateGPUTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateGPUTextEngine", SDL_POINTER[TTF_TextEngine], [SDL_POINTER[SDL_GPUDevice]]]
TTF_CreateGPUTextEngineWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateGPUTextEngineWithProperties", SDL_POINTER[TTF_TextEngine], [SDL_PropertiesID]]

TTF_PROP_GPU_TEXT_ENGINE_DEVICE = "SDL_ttf.gpu_text_engine.create.device"
TTF_PROP_GPU_TEXT_ENGINE_ATLAS_TEXTURE_SIZE = "SDL_ttf.gpu_text_engine.create.atlas_texture_size"

class TTF_GPUAtlasDrawSequence(ctypes.c_void_p):
    ...

class TTF_GPUAtlasDrawSequence(ctypes.Structure):
    _fields_ = [
        ("atlas_texture", SDL_POINTER[SDL_GPUTexture]),
        ("xy", SDL_POINTER[SDL_FPoint]),
        ("uv", SDL_POINTER[SDL_FPoint]),
        ("num_vertices", ctypes.c_int),
        ("indices", SDL_POINTER[ctypes.c_int]),
        ("num_indices", ctypes.c_int),
        ("image_type", TTF_ImageType),
        ("next", SDL_POINTER[TTF_GPUAtlasDrawSequence])
    ]

TTF_GetGPUTextDrawData: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGPUTextDrawData", SDL_POINTER[TTF_GPUAtlasDrawSequence], [SDL_POINTER[TTF_Text]]]
TTF_DestroyGPUTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DestroyGPUTextEngine", None, [SDL_POINTER[TTF_TextEngine]]]

TTF_GPUTextEngineWinding: typing.TypeAlias = SDL_TYPE["TTF_GPUTextEngineWinding", ctypes.c_int]

TTF_GPU_TEXTENGINE_WINDING_INVALID = -1,
TTF_GPU_TEXTENGINE_WINDING_CLOCKWISE = 0
TTF_GPU_TEXTENGINE_WINDING_COUNTER_CLOCKWISE = 1

TTF_SetGPUTextEngineWinding: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetGPUTextEngineWinding", None, [SDL_POINTER[TTF_TextEngine], TTF_GPUTextEngineWinding]]
TTF_GetGPUTextEngineWinding: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetGPUTextEngineWinding", TTF_GPUTextEngineWinding, [SDL_POINTER[TTF_TextEngine]]]

TTF_CreateText: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CreateText", SDL_POINTER[TTF_Text], [SDL_POINTER[TTF_TextEngine], SDL_POINTER[TTF_Font], ctypes.c_char_p, ctypes.c_size_t]]

if SDL_PLATFORM_SPECIFIC(system = ["Windows"]):
    TTF_GetTextProperties: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextProperties", SDL_PropertiesID, [SDL_POINTER[TTF_Text]]]

TTF_SetTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextEngine", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[TTF_TextEngine]]]
TTF_GetTextEngine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextEngine", SDL_POINTER[TTF_TextEngine], [SDL_POINTER[TTF_Text]]]

TTF_SetTextFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextFont", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[TTF_Font]]]
TTF_GetTextFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextFont", SDL_POINTER[TTF_Font], [SDL_POINTER[TTF_Text]]]

TTF_SetTextDirection: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextDirection", ctypes.c_bool, [SDL_POINTER[TTF_Text], TTF_Direction]]
TTF_GetTextDirection: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextDirection", TTF_Direction, [SDL_POINTER[TTF_Text]]]

TTF_SetTextScript: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextScript", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_uint32]]
TTF_GetTextScript: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextScript", ctypes.c_uint32, [SDL_POINTER[TTF_Text]]]

TTF_SetTextColor: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextColor", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]]
TTF_SetTextColorFloat: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextColorFloat", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]]

TTF_GetTextColor: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextColor", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8], SDL_POINTER[ctypes.c_uint8]]]
TTF_GetTextColorFloat: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextColorFloat", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[ctypes.c_float], SDL_POINTER[ctypes.c_float], SDL_POINTER[ctypes.c_float], SDL_POINTER[ctypes.c_float]]]

TTF_SetTextPosition: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextPosition", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_int]]
TTF_GetTextPosition: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextPosition", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]

TTF_SetTextWrapWidth: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextWrapWidth", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int]]
TTF_GetTextWrapWidth: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextWrapWidth", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[ctypes.c_int]]]

TTF_SetTextWrapWhitespaceVisible: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextWrapWhitespaceVisible", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_bool]]
TTF_TextWrapWhitespaceVisible: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_TextWrapWhitespaceVisible", ctypes.c_bool, [SDL_POINTER[TTF_Text]]]

TTF_SetTextString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_SetTextString", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_char_p, ctypes.c_size_t]]
TTF_InsertTextString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_InsertTextString", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]]
TTF_AppendTextString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_AppendTextString", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_char_p, ctypes.c_size_t]]
TTF_DeleteTextString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DeleteTextString", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_int]]

TTF_GetTextSize: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextSize", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[ctypes.c_int], SDL_POINTER[ctypes.c_int]]]

TTF_SubStringFlags: typing.TypeAlias = SDL_TYPE["TTF_SubStringFlags", ctypes.c_uint32]

TTF_SUBSTRING_DIRECTION_MASK = 0x000000FF
TTF_SUBSTRING_TEXT_START = 0x00000100
TTF_SUBSTRING_LINE_START = 0x00000200
TTF_SUBSTRING_LINE_END = 0x00000400
TTF_SUBSTRING_TEXT_END = 0x00000800

class TTF_SubString(ctypes.Structure):
    _fields_ = [
        ("flags", TTF_SubStringFlags),
        ("offset", ctypes.c_int),
        ("length", ctypes.c_int),
        ("line_index", ctypes.c_int),
        ("cluster_index", ctypes.c_int),
        ("rect", SDL_Rect)
    ]

TTF_GetTextSubString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextSubString", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, SDL_POINTER[TTF_SubString]]]
TTF_GetTextSubStringForLine: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextSubStringForLine", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, SDL_POINTER[TTF_SubString]]]
TTF_GetTextSubStringsForRange: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextSubStringsForRange", SDL_POINTER[SDL_POINTER[TTF_SubString]], [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_int, SDL_POINTER[ctypes.c_int]]]
TTF_GetTextSubStringForPoint: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetTextSubStringForPoint", ctypes.c_bool, [SDL_POINTER[TTF_Text], ctypes.c_int, ctypes.c_int, SDL_POINTER[TTF_SubString]]]
TTF_GetPreviousTextSubString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetPreviousTextSubString", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[TTF_SubString], SDL_POINTER[TTF_SubString]]]
TTF_GetNextTextSubString: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_GetNextTextSubString", ctypes.c_bool, [SDL_POINTER[TTF_Text], SDL_POINTER[TTF_SubString], SDL_POINTER[TTF_SubString]]]
TTF_UpdateText: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_UpdateText", None, [SDL_POINTER[TTF_Text]]]
TTF_DestroyText: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_DestroyText", None, [SDL_POINTER[TTF_Text]]]

TTF_CloseFont: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_CloseFont", None, [SDL_POINTER[TTF_Font]]]
TTF_Quit: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_Quit", None, []]
TTF_WasInit: abc.Callable[..., typing.Any] = SDL_FUNC["TTF_WasInit", ctypes.c_int, []]