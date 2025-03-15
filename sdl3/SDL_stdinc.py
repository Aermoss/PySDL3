from .__init__ import ctypes, typing, abc, SDL_POINTER, SDL_FUNC_TYPE, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_arraysize = lambda array: ctypes.sizeof(array) // ctypes.sizeof(array[0])

SDL_FALSE, SDL_TRUE = False, True

SDL_bool: typing.TypeAlias = SDL_TYPE["SDL_bool", ctypes.c_bool]

Sint8: typing.TypeAlias = SDL_TYPE["Sint8", ctypes.c_int8]

SDL_MAX_SINT8, SDL_MIN_SINT8 = 0x7F, ~0X7F

Uint8: typing.TypeAlias = SDL_TYPE["Uint8", ctypes.c_uint8]

SDL_MAX_UINT8, SDL_MIN_UINT8 = 0xFF, 0X00

Sint16: typing.TypeAlias = SDL_TYPE["Sint16", ctypes.c_int16]

SDL_MAX_SINT16, SDL_MIN_SINT16 = 0x7FFF, ~0X7FFF

Uint16: typing.TypeAlias = SDL_TYPE["Uint16", ctypes.c_uint16]

SDL_MAX_UINT16, SDL_MIN_UINT16 = 0xFFFF, 0X0000

Sint32: typing.TypeAlias = SDL_TYPE["Sint32", ctypes.c_int32]

SDL_MAX_SINT32, SDL_MIN_SINT32 = 0x7FFFFFFF, ~0X7FFFFFFF

Uint32: typing.TypeAlias = SDL_TYPE["Uint32", ctypes.c_uint32]

SDL_MAX_UINT32, SDL_MIN_UINT32 = 0xFFFFFFFF, 0X00000000

Sint64: typing.TypeAlias = SDL_TYPE["Sint64", ctypes.c_int64]

SDL_MAX_SINT64, SDL_MIN_SINT64 = 0x7FFFFFFFFFFFFFFF, ~0X7FFFFFFFFFFFFFFF

Uint64: typing.TypeAlias = SDL_TYPE["Uint64", ctypes.c_uint64]

SDL_MAX_UINT64, SDL_MIN_UINT64 = 0xFFFFFFFFFFFFFFFF, 0X0000000000000000

SDL_Time: typing.TypeAlias = SDL_TYPE["SDL_Time", Sint64]

SDL_MAX_TIME, SDL_MIN_TIME = SDL_MAX_SINT64, SDL_MIN_SINT64

SDL_FLT_EPSILON = 1.1920928955078125e-07

SDL_malloc: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_malloc", ctypes.c_void_p, [ctypes.c_size_t]]
SDL_calloc: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_calloc", ctypes.c_void_p, [ctypes.c_size_t, ctypes.c_size_t]]
SDL_realloc: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_realloc", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_size_t]]
SDL_free: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_free", None, [ctypes.c_void_p]]

SDL_malloc_func: typing.TypeAlias = SDL_FUNC_TYPE["SDL_malloc_func", ctypes.c_void_p, [ctypes.c_size_t]]
SDL_calloc_func: typing.TypeAlias = SDL_FUNC_TYPE["SDL_calloc_func", ctypes.c_void_p, [ctypes.c_size_t, ctypes.c_size_t]]
SDL_realloc_func: typing.TypeAlias = SDL_FUNC_TYPE["SDL_realloc_func", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_size_t]]
SDL_free_func: typing.TypeAlias = SDL_FUNC_TYPE["SDL_free_func", None, [ctypes.c_void_p]]

SDL_GetOriginalMemoryFunctions: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetOriginalMemoryFunctions", None, [SDL_POINTER[SDL_malloc_func], SDL_POINTER[SDL_calloc_func], SDL_POINTER[SDL_realloc_func], SDL_POINTER[SDL_free_func]]]
SDL_GetMemoryFunctions: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetMemoryFunctions", None, [SDL_POINTER[SDL_malloc_func], SDL_POINTER[SDL_calloc_func], SDL_POINTER[SDL_realloc_func], SDL_POINTER[SDL_free_func]]]
SDL_SetMemoryFunctions: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetMemoryFunctions", ctypes.c_bool, [SDL_malloc_func, SDL_calloc_func, SDL_realloc_func, SDL_free_func]]

SDL_aligned_alloc: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_aligned_alloc", ctypes.c_void_p, [ctypes.c_size_t, ctypes.c_size_t]]
SDL_aligned_free: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_aligned_free", None, [ctypes.c_void_p]]

SDL_GetNumAllocations: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetNumAllocations", ctypes.c_int, []]

class SDL_Environment(ctypes.c_void_p):
    ...

SDL_GetEnvironment: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetEnvironment", SDL_POINTER[SDL_Environment], []]
SDL_CreateEnvironment: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CreateEnvironment", SDL_POINTER[SDL_Environment], [ctypes.c_bool]]
SDL_GetEnvironmentVariable: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetEnvironmentVariable", ctypes.c_char_p, [SDL_POINTER[SDL_Environment], ctypes.c_char_p]]
SDL_GetEnvironmentVariables: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetEnvironmentVariables", SDL_POINTER[ctypes.c_char_p], [SDL_POINTER[SDL_Environment]]]
SDL_SetEnvironmentVariable: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetEnvironmentVariable", ctypes.c_bool, [SDL_POINTER[SDL_Environment], ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]]
SDL_UnsetEnvironmentVariable: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UnsetEnvironmentVariable", ctypes.c_bool, [SDL_POINTER[SDL_Environment], ctypes.c_char_p]]
SDL_DestroyEnvironment: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DestroyEnvironment", None, [SDL_POINTER[SDL_Environment]]]

SDL_getenv: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_getenv", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_getenv_unsafe: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_getenv_unsafe", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_setenv_unsafe: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_setenv_unsafe", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]]
SDL_unsetenv_unsafe: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_unsetenv_unsafe", ctypes.c_int, [ctypes.c_char_p]]

SDL_CompareCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_CompareCallback", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p]]

SDL_qsort: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_qsort", None, [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback]]
SDL_bsearch: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_bsearch", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback]]

SDL_CompareCallback_r: typing.TypeAlias = SDL_FUNC_TYPE["SDL_CompareCallback_r", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]]

SDL_qsort_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_qsort_r", None, [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback_r, ctypes.c_void_p]]
SDL_bsearch_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_bsearch_r", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, SDL_CompareCallback_r, ctypes.c_void_p]]

SDL_abs: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_abs", ctypes.c_int, [ctypes.c_int]]

SDL_min = lambda x, y: x if x < y else y
SDL_max = lambda x, y: x if x > y else y
SDL_clamp = lambda x, a, b: a if x < a else (b if x > b else x)

SDL_isalpha: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isalpha", ctypes.c_int, [ctypes.c_int]]
SDL_isalnum: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isalnum", ctypes.c_int, [ctypes.c_int]]
SDL_isblank: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isblank", ctypes.c_int, [ctypes.c_int]]
SDL_iscntrl: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_iscntrl", ctypes.c_int, [ctypes.c_int]]
SDL_isdigit: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isdigit", ctypes.c_int, [ctypes.c_int]]
SDL_isxdigit: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isxdigit", ctypes.c_int, [ctypes.c_int]]
SDL_ispunct: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ispunct", ctypes.c_int, [ctypes.c_int]]
SDL_isspace: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isspace", ctypes.c_int, [ctypes.c_int]]
SDL_isupper: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isupper", ctypes.c_int, [ctypes.c_int]]
SDL_islower: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_islower", ctypes.c_int, [ctypes.c_int]]
SDL_isprint: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isprint", ctypes.c_int, [ctypes.c_int]]
SDL_isgraph: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isgraph", ctypes.c_int, [ctypes.c_int]]
SDL_toupper: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_toupper", ctypes.c_int, [ctypes.c_int]]
SDL_tolower: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_tolower", ctypes.c_int, [ctypes.c_int]]

SDL_crc16: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_crc16", ctypes.c_uint16, [ctypes.c_uint16, ctypes.c_void_p, ctypes.c_size_t]]
SDL_crc32: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_crc32", ctypes.c_uint32, [ctypes.c_uint32, ctypes.c_void_p, ctypes.c_size_t]]
SDL_murmur3_32: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_murmur3_32", ctypes.c_uint32, [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_uint32]]

SDL_memcpy: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_memcpy", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]]
SDL_memmove: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_memmove", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]]
SDL_memset: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_memset", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]]
SDL_memset4: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_memset4", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_size_t]]

SDL_zero = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(ctypes.byref(x), 0, ctypes.sizeof(x))
SDL_zerop = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(x, 0, ctypes.sizeof(x.contents))
SDL_zeroa = lambda x: SDL_GET_BINARY(SDL_BINARY).SDL_memset(x, 0, ctypes.sizeof(x))

SDL_memcmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_memcmp", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]]

SDL_wcslen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcslen", ctypes.c_size_t, [ctypes.c_wchar_p]]
SDL_wcsnlen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsnlen", ctypes.c_size_t, [ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcslcpy: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcslcpy", ctypes.c_size_t, [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcslcat: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcslcat", ctypes.c_size_t, [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcsdup: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsdup", ctypes.c_wchar_p, [ctypes.c_wchar_p]]
SDL_wcsstr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsstr", ctypes.c_wchar_p, [ctypes.c_wchar_p, ctypes.c_wchar_p]]
SDL_wcsnstr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsnstr", ctypes.c_wchar_p, [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcscmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcscmp", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_wchar_p]]
SDL_wcsncmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsncmp", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcscasecmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcscasecmp", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_wchar_p]]
SDL_wcsncasecmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcsncasecmp", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_size_t]]
SDL_wcstol: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_wcstol", ctypes.c_long, [ctypes.c_wchar_p, SDL_POINTER[ctypes.c_wchar_p], ctypes.c_int]]

SDL_strlen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strlen", ctypes.c_size_t, [ctypes.c_char_p]]
SDL_strnlen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strnlen", ctypes.c_size_t, [ctypes.c_char_p, ctypes.c_size_t]]
SDL_strlcpy: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strlcpy", ctypes.c_size_t, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]
SDL_utf8strlcpy: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_utf8strlcpy", ctypes.c_size_t, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]
SDL_strlcat: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strlcat", ctypes.c_size_t, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]
SDL_strdup: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strdup", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_strndup: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strndup", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_size_t]]
SDL_strrev: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strrev", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_strupr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strupr", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_strlwr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strlwr", ctypes.c_char_p, [ctypes.c_char_p]]
SDL_strchr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strchr", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_int]]
SDL_strrchr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strrchr", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_int]]
SDL_strstr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strstr", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_strnstr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strnstr", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]
SDL_strcasestr: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strcasestr", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_strtok_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtok_r", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p]]]
SDL_utf8strlen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_utf8strlen", ctypes.c_size_t, [ctypes.c_char_p]]
SDL_utf8strnlen: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_utf8strnlen", ctypes.c_size_t, [ctypes.c_char_p, ctypes.c_size_t]]

SDL_itoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_itoa", ctypes.c_char_p, [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]]
SDL_uitoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_uitoa", ctypes.c_char_p, [ctypes.c_uint, ctypes.c_char_p, ctypes.c_int]]
SDL_ltoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ltoa", ctypes.c_char_p, [ctypes.c_long, ctypes.c_char_p, ctypes.c_int]]
SDL_ultoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ultoa", ctypes.c_char_p, [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_int]]
SDL_lltoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_lltoa", ctypes.c_char_p, [ctypes.c_int64, ctypes.c_char_p, ctypes.c_int]]
SDL_ulltoa: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ulltoa", ctypes.c_char_p, [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_int]]

SDL_atoi: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atoi", ctypes.c_int, [ctypes.c_char_p]]
SDL_atof: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atof", ctypes.c_double, [ctypes.c_char_p]]
SDL_strtol: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtol", ctypes.c_long, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p], ctypes.c_int]]
SDL_strtoul: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtoul", ctypes.c_ulong, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p], ctypes.c_int]]
SDL_strtoll: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtoll", ctypes.c_int64, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p], ctypes.c_int]]
SDL_strtoull: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtoull", ctypes.c_uint64, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p], ctypes.c_int]]
SDL_strtod: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strtod", ctypes.c_double, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p]]]

SDL_strcmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strcmp", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_strncmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strncmp", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]
SDL_strcasecmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strcasecmp", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_strncasecmp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_strncasecmp", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]

SDL_INVALID_UNICODE_CODEPOINT = 0xFFFD

SDL_StepUTF8: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StepUTF8", ctypes.c_uint32, [SDL_POINTER[ctypes.c_char_p], SDL_POINTER[ctypes.c_size_t]]]
SDL_StepBackUTF8: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StepBackUTF8", ctypes.c_uint32, [ctypes.c_char_p, SDL_POINTER[ctypes.c_char_p]]]
SDL_UCS4ToUTF8: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UCS4ToUTF8", ctypes.c_char_p, [ctypes.c_uint32, ctypes.c_char_p]]

SDL_sscanf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_sscanf", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_vsscanf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_vsscanf", ctypes.c_int, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]]
SDL_snprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_snprintf", ctypes.c_int, [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p]]
SDL_swprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_swprintf", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_size_t, ctypes.c_wchar_p]]
SDL_vsnprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_vsnprintf", ctypes.c_int, [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_void_p]]
SDL_vswprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_vswprintf", ctypes.c_int, [ctypes.c_wchar_p, ctypes.c_size_t, ctypes.c_wchar_p, ctypes.c_void_p]]
SDL_asprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_asprintf", ctypes.c_int, [SDL_POINTER[ctypes.c_char_p], ctypes.c_char_p]]
SDL_vasprintf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_vasprintf", ctypes.c_int, [SDL_POINTER[ctypes.c_char_p], ctypes.c_char_p, ctypes.c_void_p]]

SDL_srand: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_srand", None, [ctypes.c_uint64]]
SDL_rand: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_rand", ctypes.c_int32, [ctypes.c_int64]]
SDL_randf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_randf", ctypes.c_float, []]
SDL_rand_bits: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_rand_bits", ctypes.c_uint32, []]
SDL_rand_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_rand_r", ctypes.c_int32, [SDL_POINTER[ctypes.c_uint64], ctypes.c_int32]]
SDL_randf_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_randf_r", ctypes.c_float, [SDL_POINTER[ctypes.c_uint64]]]
SDL_rand_bits_r: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_rand_bits_r", ctypes.c_uint32, [SDL_POINTER[ctypes.c_uint64]]]

SDL_PI_D = SDL_PI_F = 3.141592653589793238462643383279502884

SDL_acos: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_acos", ctypes.c_double, [ctypes.c_double]]
SDL_acosf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_acosf", ctypes.c_float, [ctypes.c_float]]
SDL_asin: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_asin", ctypes.c_double, [ctypes.c_double]]
SDL_asinf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_asinf", ctypes.c_float, [ctypes.c_float]]
SDL_atan: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atan", ctypes.c_double, [ctypes.c_double]]
SDL_atanf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atanf", ctypes.c_float, [ctypes.c_float]]
SDL_atan2: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atan2", ctypes.c_double, [ctypes.c_double, ctypes.c_double]]
SDL_atan2f: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_atan2f", ctypes.c_float, [ctypes.c_float, ctypes.c_float]]
SDL_ceil: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ceil", ctypes.c_double, [ctypes.c_double]]
SDL_ceilf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ceilf", ctypes.c_float, [ctypes.c_float]]
SDL_copysign: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_copysign", ctypes.c_double, [ctypes.c_double, ctypes.c_double]]
SDL_copysignf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_copysignf", ctypes.c_float, [ctypes.c_float, ctypes.c_float]]
SDL_cos: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_cos", ctypes.c_double, [ctypes.c_double]]
SDL_cosf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_cosf", ctypes.c_float, [ctypes.c_float]]
SDL_exp: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_exp", ctypes.c_double, [ctypes.c_double]]
SDL_expf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_expf", ctypes.c_float, [ctypes.c_float]]
SDL_fabs: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_fabs", ctypes.c_double, [ctypes.c_double]]
SDL_fabsf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_fabsf", ctypes.c_float, [ctypes.c_float]]
SDL_floor: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_floor", ctypes.c_double, [ctypes.c_double]]
SDL_floorf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_floorf", ctypes.c_float, [ctypes.c_float]]
SDL_trunc: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_trunc", ctypes.c_double, [ctypes.c_double]]
SDL_truncf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_truncf", ctypes.c_float, [ctypes.c_float]]
SDL_fmod: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_fmod", ctypes.c_double, [ctypes.c_double, ctypes.c_double]]
SDL_fmodf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_fmodf", ctypes.c_float, [ctypes.c_float, ctypes.c_float]]
SDL_isinf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isinf", ctypes.c_int, [ctypes.c_double]]
SDL_isinff: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isinff", ctypes.c_int, [ctypes.c_float]]
SDL_isnan: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isnan", ctypes.c_int, [ctypes.c_double]]
SDL_isnanf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_isnanf", ctypes.c_int, [ctypes.c_float]]
SDL_log: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_log", ctypes.c_double, [ctypes.c_double]]
SDL_logf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_logf", ctypes.c_float, [ctypes.c_float]]
SDL_log10: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_log10", ctypes.c_double, [ctypes.c_double]]
SDL_log10f: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_log10f", ctypes.c_float, [ctypes.c_float]]
SDL_modf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_modf", ctypes.c_double, [ctypes.c_double, SDL_POINTER[ctypes.c_double]]]
SDL_modff: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_modff", ctypes.c_float, [ctypes.c_float, SDL_POINTER[ctypes.c_float]]]
SDL_pow: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_pow", ctypes.c_double, [ctypes.c_double, ctypes.c_double]]
SDL_powf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_powf", ctypes.c_float, [ctypes.c_float, ctypes.c_float]]
SDL_round: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_round", ctypes.c_double, [ctypes.c_double]]
SDL_roundf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_roundf", ctypes.c_float, [ctypes.c_float]]
SDL_lround: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_lround", ctypes.c_long, [ctypes.c_double]]
SDL_lroundf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_lroundf", ctypes.c_long, [ctypes.c_float]]
SDL_scalbn: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_scalbn", ctypes.c_double, [ctypes.c_double, ctypes.c_int]]
SDL_scalbnf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_scalbnf", ctypes.c_float, [ctypes.c_float, ctypes.c_int]]
SDL_sin: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_sin", ctypes.c_double, [ctypes.c_double]]
SDL_sinf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_sinf", ctypes.c_float, [ctypes.c_float]]
SDL_sqrt: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_sqrt", ctypes.c_double, [ctypes.c_double]]
SDL_sqrtf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_sqrtf", ctypes.c_float, [ctypes.c_float]]
SDL_tan: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_tan", ctypes.c_double, [ctypes.c_double]]
SDL_tanf: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_tanf", ctypes.c_float, [ctypes.c_float]]

class SDL_iconv_t(ctypes.c_void_p):
    ...

SDL_iconv_open: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_iconv_open", SDL_iconv_t, [ctypes.c_char_p, ctypes.c_char_p]]
SDL_iconv_close: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_iconv_close", ctypes.c_int, [SDL_iconv_t]]
SDL_iconv: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_iconv", ctypes.c_size_t, [SDL_iconv_t, SDL_POINTER[ctypes.c_char_p], SDL_POINTER[ctypes.c_size_t], SDL_POINTER[ctypes.c_char_p], SDL_POINTER[ctypes.c_size_t]]]

SDL_ICONV_ERROR, SDL_ICONV_E2BIG, SDL_ICONV_EILSEQ, \
    SDL_ICONV_EINVAL = -1, -2, -3, -4

SDL_iconv_string: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_iconv_string", ctypes.c_char_p, [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]]

SDL_iconv_utf8_locale = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_utf8_ucs2 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UCS-2".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_utf8_ucs4 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UCS-4".encode(), "UTF-8".encode(), s.encode(), SDL_GET_BINARY(SDL_BINARY).SDL_strlen(s.encode()) + 1)

SDL_iconv_wchar_utf8 = lambda s: \
    SDL_GET_BINARY(SDL_BINARY).SDL_iconv_string("UTF-8".encode(), "WCHAR_T".encode(), s.encode(), (SDL_GET_BINARY(SDL_BINARY).SDL_wcslen(s.encode()) + 1) * ctypes.sizeof(ctypes.c_wchar))

SDL_FunctionPointer: typing.TypeAlias = SDL_FUNC_TYPE["SDL_FunctionPointer", None, []]