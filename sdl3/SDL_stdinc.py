from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_arraysize = lambda array: ctypes.sizeof(array) // ctypes.sizeof(array[0])

SDL_FALSE = False
SDL_TRUE = True

SDL_bool = ctypes.c_bool

Sint8 = ctypes.c_int8
SDL_MAX_SINT8 = 0x7F
SDL_MIN_SINT8 = ~0X7F

Uint8 = ctypes.c_uint8
SDL_MAX_UINT8 = 0xFF
SDL_MIN_UINT8 = 0X00

Sint16 = ctypes.c_int16
SDL_MAX_SINT16 = 0x7FFF
SDL_MIN_SINT16 = ~0X7FFF

Uint16 = ctypes.c_uint16
SDL_MAX_UINT16 = 0xFFFF
SDL_MIN_UINT16 = 0X0000

Sint32 = ctypes.c_int32
SDL_MAX_SINT32 = 0x7FFFFFFF
SDL_MIN_SINT32 = ~0X7FFFFFFF

Uint32 = ctypes.c_uint32
SDL_MAX_UINT32 = 0xFFFFFFFF
SDL_MIN_UINT32 = 0X00000000

Sint64 = ctypes.c_int64
SDL_MAX_SINT64 = 0x7FFFFFFFFFFFFFFF
SDL_MIN_SINT64 = ~0X7FFFFFFFFFFFFFFF

Uint64 = ctypes.c_uint64
SDL_MAX_UINT64 = 0xFFFFFFFFFFFFFFFF
SDL_MIN_UINT64 = 0X0000000000000000

SDL_Time = Sint64
SDL_MAX_TIME = SDL_MAX_SINT64
SDL_MIN_TIME = SDL_MIN_SINT64

SDL_FLT_EPSILON = 1.1920928955078125e-07

SDL_FUNC("SDL_malloc", ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_calloc", ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t)
SDL_FUNC("SDL_realloc", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_free", None, ctypes.c_void_p)

SDL_malloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_size_t)
SDL_calloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t)
SDL_realloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
SDL_free_func = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

SDL_FUNC("SDL_GetOriginalMemoryFunctions", None, ctypes.POINTER(SDL_malloc_func), ctypes.POINTER(SDL_calloc_func), ctypes.POINTER(SDL_realloc_func), ctypes.POINTER(SDL_free_func))
SDL_FUNC("SDL_GetMemoryFunctions", None, ctypes.POINTER(SDL_malloc_func), ctypes.POINTER(SDL_calloc_func), ctypes.POINTER(SDL_realloc_func), ctypes.POINTER(SDL_free_func))
SDL_FUNC("SDL_SetMemoryFunctions", ctypes.c_bool, SDL_malloc_func, SDL_calloc_func, SDL_realloc_func, SDL_free_func)

SDL_FUNC("SDL_aligned_alloc", ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t)
SDL_FUNC("SDL_aligned_free", None, ctypes.c_void_p)

SDL_FUNC("SDL_GetNumAllocations", ctypes.c_int)

class SDL_Environment(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_GetEnvironment", ctypes.POINTER(SDL_Environment))
SDL_FUNC("SDL_CreateEnvironment", ctypes.POINTER(SDL_Environment), ctypes.c_bool)
SDL_FUNC("SDL_GetEnvironmentVariable", ctypes.c_char_p, ctypes.POINTER(SDL_Environment), ctypes.c_char_p)
SDL_FUNC("SDL_GetEnvironmentVariables", ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(SDL_Environment))
SDL_FUNC("SDL_SetEnvironmentVariable", ctypes.c_bool, ctypes.POINTER(SDL_Environment), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool)
SDL_FUNC("SDL_UnsetEnvironmentVariable", ctypes.c_bool, ctypes.POINTER(SDL_Environment), ctypes.c_char_p)
SDL_FUNC("SDL_DestroyEnvironment", None, ctypes.POINTER(SDL_Environment))

SDL_FUNC("SDL_getenv", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_getenv_unsafe", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_setenv_unsafe", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_unsetenv_unsafe", ctypes.c_int, ctypes.c_char_p)

SDL_CompareCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

SDL_FUNC("SDL_qsort", None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback)
SDL_FUNC("SDL_bsearch", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback)

SDL_CompareCallback_r = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

SDL_FUNC("SDL_qsort_r", None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback_r, ctypes.c_void_p)
SDL_FUNC("SDL_bsearch_r", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback_r, ctypes.c_void_p)

SDL_FUNC("SDL_abs", ctypes.c_int, ctypes.c_int)

SDL_min = lambda x, y: x if x < y else y
SDL_max = lambda x, y: x if x > y else y
SDL_clamp = lambda x, a, b: a if x < a else (b if x > b else x)

SDL_FUNC("SDL_isalpha", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isalnum", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isblank", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_iscntrl", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isdigit", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isxdigit", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_ispunct", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isspace", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isupper", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_islower", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isprint", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_isgraph", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_toupper", ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_tolower", ctypes.c_int, ctypes.c_int)

SDL_FUNC("SDL_crc16", ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_crc32", ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_murmur3_32", ctypes.c_uint32, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_uint32)

SDL_FUNC("SDL_memcpy", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_memmove", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
SDL_FUNC("SDL_memset", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t)
SDL_FUNC("SDL_memset4", ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_size_t)

SDL_zero = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(ctypes.byref(x), 0, ctypes.sizeof(x))
SDL_zerop = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(x, 0, ctypes.sizeof(x.contents))
SDL_zeroa = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(x, 0, ctypes.sizeof(x))

SDL_FUNC("SDL_memcmp", ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)

SDL_FUNC("SDL_wcslen", ctypes.c_size_t, ctypes.c_wchar_p)
SDL_FUNC("SDL_wcsnlen", ctypes.c_size_t, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcslcpy", ctypes.c_size_t, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcslcat", ctypes.c_size_t, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcsdup", ctypes.c_wchar_p, ctypes.c_wchar_p)
SDL_FUNC("SDL_wcsstr", ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p)
SDL_FUNC("SDL_wcsnstr", ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcscmp", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p)
SDL_FUNC("SDL_wcsncmp", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcscasecmp", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p)
SDL_FUNC("SDL_wcsncasecmp", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_wcstol", ctypes.c_long, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_wchar_p), ctypes.c_int)

SDL_FUNC("SDL_strlen", ctypes.c_size_t, ctypes.c_char_p)
SDL_FUNC("SDL_strnlen", ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strlcpy", ctypes.c_size_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_utf8strlcpy", ctypes.c_size_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strlcat", ctypes.c_size_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strdup", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strndup", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strrev", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strupr", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strlwr", ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strchr", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_strrchr", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_strstr", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strnstr", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strcasestr", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strtok_r", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p))
SDL_FUNC("SDL_utf8strlen", ctypes.c_size_t, ctypes.c_char_p)
SDL_FUNC("SDL_utf8strnlen", ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t)

SDL_FUNC("SDL_itoa", ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_uitoa", ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_ltoa", ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_ultoa", ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_lltoa", ctypes.c_char_p, ctypes.c_int64, ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_ulltoa", ctypes.c_char_p, ctypes.c_uint64, ctypes.c_char_p, ctypes.c_int)

SDL_FUNC("SDL_atoi", ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_atof", ctypes.c_double, ctypes.c_char_p)
SDL_FUNC("SDL_strtol", ctypes.c_long, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)
SDL_FUNC("SDL_strtoul", ctypes.c_ulong, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)
SDL_FUNC("SDL_strtoll", ctypes.c_int64, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)
SDL_FUNC("SDL_strtoull", ctypes.c_uint64, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int)
SDL_FUNC("SDL_strtod", ctypes.c_double, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p))

SDL_FUNC("SDL_strcmp", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strncmp", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)
SDL_FUNC("SDL_strcasecmp", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_strncasecmp", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)

SDL_INVALID_UNICODE_CODEPOINT = 0xFFFD

SDL_FUNC("SDL_StepUTF8", ctypes.c_uint32, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t))
SDL_FUNC("SDL_StepBackUTF8", ctypes.c_uint32, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p))
SDL_FUNC("SDL_UCS4ToUTF8", ctypes.c_char_p, ctypes.c_uint32, ctypes.c_char_p)

SDL_FUNC("SDL_sscanf", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_vsscanf", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)
SDL_FUNC("SDL_snprintf", ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p)
SDL_FUNC("SDL_swprintf", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_size_t, ctypes.c_wchar_p)
SDL_FUNC("SDL_vsnprintf", ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_void_p)
SDL_FUNC("SDL_vswprintf", ctypes.c_int, ctypes.c_wchar_p, ctypes.c_size_t, ctypes.c_wchar_p, ctypes.c_void_p)
SDL_FUNC("SDL_asprintf", ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p)
SDL_FUNC("SDL_vasprintf", ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_void_p)

SDL_FUNC("SDL_srand", None, ctypes.c_uint64)
SDL_FUNC("SDL_rand", ctypes.c_int32, ctypes.c_int64)
SDL_FUNC("SDL_randf", ctypes.c_float)
SDL_FUNC("SDL_rand_bits", ctypes.c_uint32)
SDL_FUNC("SDL_rand_r", ctypes.c_int32, ctypes.POINTER(ctypes.c_uint64), ctypes.c_int32)
SDL_FUNC("SDL_randf_r", ctypes.c_float, ctypes.POINTER(ctypes.c_uint64))
SDL_FUNC("SDL_rand_bits_r", ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint64))

SDL_PI_D = SDL_PI_F = 3.141592653589793238462643383279502884

SDL_FUNC("SDL_acos", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_acosf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_asin", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_asinf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_atan", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_atanf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_atan2", ctypes.c_double, ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_atan2f", ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_ceil", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_ceilf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_copysign", ctypes.c_double, ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_copysignf", ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_cos", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_cosf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_exp", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_expf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_fabs", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_fabsf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_floor", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_floorf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_trunc", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_truncf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_fmod", ctypes.c_double, ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_fmodf", ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_isinf", ctypes.c_int, ctypes.c_double)
SDL_FUNC("SDL_isinff", ctypes.c_int, ctypes.c_float)
SDL_FUNC("SDL_isnan", ctypes.c_int, ctypes.c_double)
SDL_FUNC("SDL_isnanf", ctypes.c_int, ctypes.c_float)
SDL_FUNC("SDL_log", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_logf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_log10", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_log10f", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_modf", ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double))
SDL_FUNC("SDL_modff", ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_pow", ctypes.c_double, ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_powf", ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_round", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_roundf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_lround", ctypes.c_long, ctypes.c_double)
SDL_FUNC("SDL_lroundf", ctypes.c_long, ctypes.c_float)
SDL_FUNC("SDL_scalbn", ctypes.c_double, ctypes.c_double, ctypes.c_int)
SDL_FUNC("SDL_scalbnf", ctypes.c_float, ctypes.c_float, ctypes.c_int)
SDL_FUNC("SDL_sin", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_sinf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_sqrt", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_sqrtf", ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_tan", ctypes.c_double, ctypes.c_double)
SDL_FUNC("SDL_tanf", ctypes.c_float, ctypes.c_float)

class SDL_iconv_t(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_iconv_open", SDL_iconv_t, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_iconv_close", ctypes.c_int, SDL_iconv_t)
SDL_FUNC("SDL_iconv", ctypes.c_size_t, SDL_iconv_t, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t))

SDL_ICONV_ERROR = -1
SDL_ICONV_E2BIG = -2
SDL_ICONV_EILSEQ = -3
SDL_ICONV_EINVAL = -4

SDL_FUNC("SDL_iconv_string", ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t)

SDL_iconv_utf8_locale = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_utf8_ucs2 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UCS-2".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_utf8_ucs4 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UCS-4".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_wchar_utf8 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UTF-8".encode(), "WCHAR_T".encode(), s.encode(), (SDL_GET_BINARY(SDL_BINARY).SDL_wcslen(s.encode()) + 1) * ctypes.sizeof(ctypes.c_wchar))

SDL_FunctionPointer = ctypes.CFUNCTYPE(None)