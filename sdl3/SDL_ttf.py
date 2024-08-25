from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_GET_DLL, SDL_TTF_DLL, SDL_DLL

from .SDL_pixels import SDL_Color
from .SDL_surface import SDL_Surface
from .SDL_iostream import SDL_IOStream
from .SDL_version import SDL_VERSIONNUM

SDL_SET_CURRENT_DLL(SDL_TTF_DLL)

SDL_TTF_MAJOR_VERSION = 3
SDL_TTF_MINOR_VERSION = 0
SDL_TTF_MICRO_VERSION = 0

SDL_TTF_VERSION = \
    SDL_VERSIONNUM(SDL_TTF_MAJOR_VERSION, SDL_TTF_MINOR_VERSION, SDL_TTF_MICRO_VERSION)

SDL_TTF_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_TTF_MAJOR_VERSION >= x) and \
    (SDL_TTF_MAJOR_VERSION > x or SDL_TTF_MINOR_VERSION >= y) and \
    (SDL_TTF_MAJOR_VERSION > x or SDL_TTF_MINOR_VERSION > y or SDL_TTF_MICRO_VERSION >= z)

SDL_FUNC("TTF_Version", ctypes.c_int)
SDL_FUNC("TTF_GetFreeTypeVersion", None, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetHarfBuzzVersion", None, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

UNICODE_BOM_NATIVE = 0xFEFF
UNICODE_BOM_SWAPPED = 0xFFFE

SDL_FUNC("TTF_ByteSwappedUNICODE", None, ctypes.c_bool)

class TTF_Font(ctypes.c_void_p):
    ...

SDL_FUNC("TTF_Init", ctypes.c_int)
SDL_FUNC("TTF_OpenFont", ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("TTF_OpenFontIndex", ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int, ctypes.c_long)
SDL_FUNC("TTF_OpenFontIO", ctypes.POINTER(TTF_Font), ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.c_int)
SDL_FUNC("TTF_OpenFontIndexIO", ctypes.POINTER(TTF_Font), ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.c_int, ctypes.c_long)
SDL_FUNC("TTF_OpenFontDPI", ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int, ctypes.c_uint, ctypes.c_uint)
SDL_FUNC("TTF_OpenFontIndexDPI", ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int, ctypes.c_long, ctypes.c_uint, ctypes.c_uint)
SDL_FUNC("TTF_OpenFontDPIIO", ctypes.POINTER(TTF_Font), ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.c_int, ctypes.c_uint, ctypes.c_uint)
SDL_FUNC("TTF_OpenFontIndexDPIIO", ctypes.POINTER(TTF_Font), ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.c_int, ctypes.c_long, ctypes.c_uint, ctypes.c_uint)
SDL_FUNC("TTF_SetFontSize", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_SetFontSizeDPI", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_int, ctypes.c_uint, ctypes.c_uint)

TTF_STYLE_NORMAL = 0x00
TTF_STYLE_BOLD = 0x01
TTF_STYLE_ITALIC = 0x02
TTF_STYLE_UNDERLINE = 0x04
TTF_STYLE_STRIKETHROUGH = 0x08

SDL_FUNC("TTF_GetFontStyle", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontStyle", None, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_GetFontOutline", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontOutline", None, ctypes.POINTER(TTF_Font), ctypes.c_int)

TTF_HINTING_NORMAL = 0
TTF_HINTING_LIGHT = 1
TTF_HINTING_MONO = 2
TTF_HINTING_NONE = 3
TTF_HINTING_LIGHT_SUBPIXEL = 4

SDL_FUNC("TTF_GetFontHinting", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontHinting", None, ctypes.POINTER(TTF_Font), ctypes.c_int)

TTF_WRAPPED_ALIGN_LEFT = 0
TTF_WRAPPED_ALIGN_CENTER = 1
TTF_WRAPPED_ALIGN_RIGHT = 2

SDL_FUNC("TTF_GetFontWrappedAlign", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontWrappedAlign", None, ctypes.POINTER(TTF_Font), ctypes.c_int)

SDL_FUNC("TTF_FontHeight", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontAscent", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontDescent", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontLineSkip", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontKerning", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontKerning", None, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_FontFaces", ctypes.c_long, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontFaceIsFixedWidth", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontFaceFamilyName", ctypes.c_char_p, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontFaceStyleName", ctypes.c_char_p, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GlyphIsProvided", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint16)
SDL_FUNC("TTF_GlyphIsProvided32", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint32)
SDL_FUNC("TTF_GlyphMetrics", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint16, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GlyphMetrics32", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint32, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_SizeText", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_SizeUTF8", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_SizeUNICODE", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_MeasureText", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_MeasureUTF8", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_MeasureUNICODE", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_RenderText_Solid", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color)
SDL_FUNC("TTF_RenderUTF8_Solid", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color)
SDL_FUNC("TTF_RenderUNICODE_Solid", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color)
SDL_FUNC("TTF_RenderText_Solid_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUTF8_Solid_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUNICODE_Solid_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderGlyph_Solid", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint16, SDL_Color)
SDL_FUNC("TTF_RenderGlyph32_Solid", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color)
SDL_FUNC("TTF_RenderText_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderUTF8_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderUNICODE_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_Shaded_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUTF8_Shaded_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUNICODE_Shaded_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderGlyph_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint16, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderGlyph32_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color)
SDL_FUNC("TTF_RenderUTF8_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color)
SDL_FUNC("TTF_RenderUNICODE_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color)
SDL_FUNC("TTF_RenderText_Blended_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUTF8_Blended_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUNICODE_Blended_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderGlyph_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint16, SDL_Color)
SDL_FUNC("TTF_RenderGlyph32_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color)
SDL_FUNC("TTF_RenderText_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderUTF8_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderUNICODE_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_LCD_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUTF8_LCD_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderUNICODE_LCD_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_uint16), SDL_Color, SDL_Color, ctypes.c_uint32)
SDL_FUNC("TTF_RenderGlyph_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint16, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderGlyph32_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color)

TTF_RenderText = lambda font, text, fg, bg: \
    SDL_GET_DLL(SDL_TTF_DLL).TTF_RenderText_Shaded(font, text, fg, bg)

TTF_RenderUTF8 = lambda font, text, fg, bg: \
    SDL_GET_DLL(SDL_TTF_DLL).TTF_RenderUTF8_Shaded(font, text, fg, bg)

TTF_RenderUNICODE = lambda font, text, fg, bg: \
    SDL_GET_DLL(SDL_TTF_DLL).TTF_RenderUNICODE_Shaded(font, text, fg, bg)

SDL_FUNC("TTF_CloseFont", None, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_Quit", None)
SDL_FUNC("TTF_WasInit", ctypes.c_int)
SDL_FUNC("TTF_GetFontKerningSizeGlyphs", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint16, ctypes.c_uint16)
SDL_FUNC("TTF_GetFontKerningSizeGlyphs32", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("TTF_SetFontSDF", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_bool)
SDL_FUNC("TTF_GetFontSDF", ctypes.c_bool, ctypes.POINTER(TTF_Font))

TTF_SetError = SDL_GET_DLL(SDL_DLL).SDL_SetError
TTF_GetError = SDL_GET_DLL(SDL_DLL).SDL_GetError

TTF_Direction = ctypes.c_int

TTF_DIRECTION_LTR = 0
TTF_DIRECTION_RTL = 1
TTF_DIRECTION_TTB = 2
TTF_DIRECTION_BTT = 3

SDL_FUNC("TTF_SetFontDirection", ctypes.c_int, ctypes.POINTER(TTF_Font), TTF_Direction)
SDL_FUNC("TTF_SetFontScriptName", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p)
SDL_FUNC("TTF_SetFontLanguage", ctypes.c_int, ctypes.POINTER(TTF_Font), ctypes.c_char_p)
SDL_FUNC("TTF_IsFontScalable", ctypes.c_bool, ctypes.POINTER(TTF_Font))