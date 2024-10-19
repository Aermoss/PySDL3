from .__init__ import ctypes, sys, \
    SDL_FUNC, SDL_SET_CURRENT_DLL, SDL_GET_DLL, SDL_TTF_DLL, SDL_DLL

from .SDL_pixels import SDL_Color, SDL_FColor
from .SDL_properties import SDL_PropertiesID
from .SDL_render import SDL_Renderer
from .SDL_surface import SDL_Surface
from .SDL_iostream import SDL_IOStream
from .SDL_version import SDL_VERSIONNUM
from .SDL_rect import SDL_Rect

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

class TTF_Font(ctypes.c_void_p):
    ...

SDL_FUNC("TTF_Init", ctypes.c_int)
SDL_FUNC("TTF_OpenFont", ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_float)
SDL_FUNC("TTF_OpenFontIO", ctypes.POINTER(TTF_Font), ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.c_float)
SDL_FUNC("TTF_OpenFontWithProperties", ctypes.POINTER(TTF_Font), SDL_PropertiesID)

TTF_PROP_FONT_CREATE_FILENAME_STRING = "SDL_ttf.font.create.filename"
TTF_PROP_FONT_CREATE_IOSTREAM_POINTER = "SDL_ttf.font.create.iostream"
TTF_PROP_FONT_CREATE_IOSTREAM_OFFSET_NUMBER = "SDL_ttf.font.create.iostream.offset"
TTF_PROP_FONT_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN = "SDL_ttf.font.create.iostream.autoclose"
TTF_PROP_FONT_CREATE_SIZE_FLOAT = "SDL_ttf.font.create.size"
TTF_PROP_FONT_CREATE_FACE_NUMBER = "SDL_ttf.font.create.face"
TTF_PROP_FONT_CREATE_HORIZONTAL_DPI_NUMBER = "SDL_ttf.font.create.hdpi"
TTF_PROP_FONT_CREATE_VERTICAL_DPI_NUMBER = "SDL_ttf.font.create.vdpi"

SDL_FUNC("TTF_GetFontProperties", SDL_PropertiesID, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontGeneration", ctypes.c_uint32, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_SetFontSize", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_float)
SDL_FUNC("TTF_SetFontSizeDPI", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_float, ctypes.c_int, ctypes.c_int)

SDL_FUNC("TTF_GetFontSize", ctypes.c_float, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontDPI", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

TTF_STYLE_NORMAL = 0x00
TTF_STYLE_BOLD = 0x01
TTF_STYLE_ITALIC = 0x02
TTF_STYLE_UNDERLINE = 0x04
TTF_STYLE_STRIKETHROUGH = 0x08

SDL_FUNC("TTF_SetFontStyle", None, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_GetFontStyle", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontOutline", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_GetFontOutline", ctypes.c_int, ctypes.POINTER(TTF_Font))

TTF_HINTING_NORMAL = 0
TTF_HINTING_LIGHT = 1
TTF_HINTING_MONO = 2
TTF_HINTING_NONE = 3
TTF_HINTING_LIGHT_SUBPIXEL = 4

SDL_FUNC("TTF_SetFontHinting", None, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_GetFontHinting", ctypes.c_int, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_SetFontSDF", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_bool)
SDL_FUNC("TTF_GetFontSDF", ctypes.c_bool, ctypes.POINTER(TTF_Font))

TTF_HorizontalAlignment = ctypes.c_int

TTF_HORIZONTAL_ALIGN_INVALID = -1
TTF_HORIZONTAL_ALIGN_LEFT = 0
TTF_HORIZONTAL_ALIGN_CENTER = 1
TTF_HORIZONTAL_ALIGN_RIGHT = 2

SDL_FUNC("TTF_SetFontWrapAlignment", None, ctypes.POINTER(TTF_Font), TTF_HorizontalAlignment)
SDL_FUNC("TTF_GetFontWrapAlignment", TTF_HorizontalAlignment, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_GetFontHeight", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontAscent", ctypes.c_int, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontDescent", ctypes.c_int, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_SetFontLineSkip", None, ctypes.POINTER(TTF_Font), ctypes.c_int)
SDL_FUNC("TTF_GetFontLineSkip", ctypes.c_int, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_SetFontKerning", None, ctypes.POINTER(TTF_Font), ctypes.c_bool)
SDL_FUNC("TTF_GetFontKerning", ctypes.c_bool, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_FontIsFixedWidth", ctypes.c_bool, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_FontIsScalable", ctypes.c_bool, ctypes.POINTER(TTF_Font))

SDL_FUNC("TTF_GetFontFamilyName", ctypes.c_char_p, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetFontStyleName", ctypes.c_char_p, ctypes.POINTER(TTF_Font))

TTF_Direction = ctypes.c_int

TTF_DIRECTION_LTR = 0
TTF_DIRECTION_RTL = 1
TTF_DIRECTION_TTB = 2
TTF_DIRECTION_BTT = 3

SDL_FUNC("TTF_SetFontDirection", ctypes.c_bool, ctypes.POINTER(TTF_Font), TTF_Direction)
SDL_FUNC("TTF_GetFontDirection", TTF_Direction, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_SetFontScript", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_char_p)
SDL_FUNC("TTF_GetGlyphScript", ctypes.c_bool, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("TTF_SetFontLanguage", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_char_p)
SDL_FUNC("TTF_FontHasGlyph", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_uint32)
SDL_FUNC("TTF_GetGlyphImage", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32)
SDL_FUNC("TTF_GetGlyphImageForIndex", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32)
SDL_FUNC("TTF_GetGlyphMetrics", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_uint32, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetGlyphKerning", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetStringSize", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetStringSizeWrapped", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_MeasureString", ctypes.c_bool, ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("TTF_RenderText_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_Shaded_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color, ctypes.c_int)
SDL_FUNC("TTF_RenderGlyph_Shaded", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color)
SDL_FUNC("TTF_RenderText_Blended_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color, ctypes.c_int)
SDL_FUNC("TTF_RenderGlyph_Blended", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color)
SDL_FUNC("TTF_RenderText_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color)
SDL_FUNC("TTF_RenderText_LCD_Wrapped", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, SDL_Color, SDL_Color, ctypes.c_int)
SDL_FUNC("TTF_RenderGlyph_LCD", ctypes.POINTER(SDL_Surface), ctypes.POINTER(TTF_Font), ctypes.c_uint32, SDL_Color, SDL_Color)

class TTF_TextEngine(ctypes.c_void_p):
    ...

class TTF_TextData(ctypes.c_void_p):
    ...

class TTF_Text(ctypes.Structure):
    _fields_ = [
        ("text", ctypes.c_char_p),
        ("color", SDL_FColor),
        ("num_lines", ctypes.c_int),
        ("refcount", ctypes.c_int),
        ("internal", ctypes.POINTER(TTF_TextData))
    ]

SDL_FUNC("TTF_CreateSurfaceTextEngine", ctypes.POINTER(TTF_TextEngine))
SDL_FUNC("TTF_DrawSurfaceText", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.c_int, ctypes.POINTER(SDL_Surface))
SDL_FUNC("TTF_DestroySurfaceTextEngine", None, ctypes.POINTER(TTF_TextEngine))
SDL_FUNC("TTF_CreateRendererTextEngine", ctypes.POINTER(TTF_TextEngine), ctypes.POINTER(SDL_Renderer))
SDL_FUNC("TTF_DrawRendererText", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_float, ctypes.c_float)
SDL_FUNC("TTF_DestroyRendererTextEngine", None, ctypes.POINTER(TTF_TextEngine))
SDL_FUNC("TTF_CreateText", ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_TextEngine), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("TTF_CreateText_Wrapped", ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_TextEngine), ctypes.POINTER(TTF_Font), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int)

if "win32" in sys.platform:
    # For some reason it gives an undefined symbol error on linux.
    SDL_FUNC("TTF_GetTextProperties", SDL_PropertiesID, ctypes.POINTER(TTF_Text))

SDL_FUNC("TTF_SetTextEngine", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_TextEngine))
SDL_FUNC("TTF_GetTextEngine", ctypes.POINTER(TTF_TextEngine), ctypes.POINTER(TTF_Text))
SDL_FUNC("TTF_SetTextFont", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_GetTextFont", ctypes.POINTER(TTF_Font), ctypes.POINTER(TTF_Text))
SDL_FUNC("TTF_SetTextString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("TTF_InsertTextString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("TTF_AppendTextString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("TTF_DeleteTextString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.c_int)
SDL_FUNC("TTF_SetTextWrapping", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_bool, ctypes.c_int)
SDL_FUNC("TTF_GetTextWrapping", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetTextSize", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

TTF_SubStringFlags = ctypes.c_uint32

TTF_SUBSTRING_TEXT_STARTD = 0x00000001  
TTF_SUBSTRING_LINE_STARTD = 0x00000002  
TTF_SUBSTRING_LINE_ENDD = 0x00000004  
TTF_SUBSTRING_TEXT_END = 0x00000008  

class TTF_SubString(ctypes.Structure):
    _fields_ = [
        ("flags", TTF_SubStringFlags),
        ("offset", ctypes.c_int),
        ("length", ctypes.c_int),
        ("line_index", ctypes.c_int),
        ("cluster_index", ctypes.c_int),
        ("rect", SDL_Rect)
    ]

SDL_FUNC("TTF_GetTextSubString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.POINTER(TTF_SubString))
SDL_FUNC("TTF_GetTextSubStringForLine", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.POINTER(TTF_SubString))
SDL_FUNC("TTF_GetTextSubStringsForRange", ctypes.POINTER(ctypes.POINTER(TTF_SubString)), ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
SDL_FUNC("TTF_GetTextSubStringForPoint", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.c_int, ctypes.c_int, ctypes.POINTER(TTF_SubString))
SDL_FUNC("TTF_GetPreviousTextSubString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_SubString), ctypes.POINTER(TTF_SubString))
SDL_FUNC("TTF_GetNextTextSubString", ctypes.c_bool, ctypes.POINTER(TTF_Text), ctypes.POINTER(TTF_SubString), ctypes.POINTER(TTF_SubString))
SDL_FUNC("TTF_UpdateText", None, ctypes.POINTER(TTF_Text))
SDL_FUNC("TTF_DestroyText", None, ctypes.POINTER(TTF_Text))

SDL_FUNC("TTF_CloseFont", None, ctypes.POINTER(TTF_Font))
SDL_FUNC("TTF_Quit", None)
SDL_FUNC("TTF_WasInit", ctypes.c_int)