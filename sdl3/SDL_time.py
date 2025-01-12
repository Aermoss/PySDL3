from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_stdinc import SDL_Time

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_DateTime(ctypes.Structure):
    _fields_ = [
        ("year", ctypes.c_int),
        ("month", ctypes.c_int),
        ("day", ctypes.c_int),
        ("hour", ctypes.c_int),
        ("minute", ctypes.c_int),
        ("second", ctypes.c_int),
        ("nanosecond", ctypes.c_int),
        ("day_of_week", ctypes.c_int),
        ("utc_offset", ctypes.c_int)
    ]

SDL_DateFormat = ctypes.c_int

SDL_DATE_FORMAT_YYYYMMDD = 0
SDL_DATE_FORMAT_DDMMYYYY = 1
SDL_DATE_FORMAT_MMDDYYYY = 2 

SDL_TimeFormat = ctypes.c_int

SDL_TIME_FORMAT_24HR = 0
SDL_TIME_FORMAT_12HR = 1

SDL_FUNC("SDL_GetDateTimeLocalePreferences", ctypes.c_bool, ctypes.POINTER(SDL_DateFormat), ctypes.POINTER(SDL_TimeFormat))
SDL_FUNC("SDL_GetCurrentTime", ctypes.c_bool, ctypes.POINTER(SDL_Time))
SDL_FUNC("SDL_TimeToDateTime", ctypes.c_bool, SDL_Time, ctypes.POINTER(SDL_DateTime), ctypes.c_bool)
SDL_FUNC("SDL_DateTimeToTime", ctypes.c_bool, ctypes.POINTER(SDL_DateTime), ctypes.POINTER(SDL_Time))
SDL_FUNC("SDL_TimeToWindows", None, SDL_Time, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_TimeFromWindows", SDL_Time, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_GetDaysInMonth", ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetDayOfYear", ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetDayOfWeek", ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)