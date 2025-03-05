from .__init__ import ctypes, typing, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_Keycode: typing.TypeAlias = ctypes.c_uint32

SDLK_EXTENDED_MASK = 1 << 29
SDLK_SCANCODE_MASK = 1 << 30
SDL_SCANCODE_TO_KEYCODE = lambda x: x | SDLK_SCANCODE_MASK
SDLK_UNKNOWN = 0x00000000
SDLK_RETURN = 0x0000000d
SDLK_ESCAPE = 0x0000001b
SDLK_BACKSPACE = 0x00000008
SDLK_TAB = 0x00000009
SDLK_SPACE = 0x00000020
SDLK_EXCLAIM = 0x00000021
SDLK_DBLAPOSTROPHE = 0x00000022
SDLK_HASH = 0x00000023
SDLK_DOLLAR = 0x00000024
SDLK_PERCENT = 0x00000025
SDLK_AMPERSAND = 0x00000026
SDLK_APOSTROPHE = 0x00000027
SDLK_LEFTPAREN = 0x00000028
SDLK_RIGHTPAREN = 0x00000029
SDLK_ASTERISK = 0x0000002a
SDLK_PLUS = 0x0000002b
SDLK_COMMA = 0x0000002c
SDLK_MINUS = 0x0000002d
SDLK_PERIOD = 0x0000002e
SDLK_SLASH = 0x0000002f
SDLK_0 = 0x00000030
SDLK_1 = 0x00000031
SDLK_2 = 0x00000032
SDLK_3 = 0x00000033
SDLK_4 = 0x00000034
SDLK_5 = 0x00000035
SDLK_6 = 0x00000036
SDLK_7 = 0x00000037
SDLK_8 = 0x00000038
SDLK_9 = 0x00000039
SDLK_COLON = 0x0000003a
SDLK_SEMICOLON = 0x0000003b
SDLK_LESS = 0x0000003c
SDLK_EQUALS = 0x0000003d
SDLK_GREATER = 0x0000003e
SDLK_QUESTION = 0x0000003f
SDLK_AT = 0x00000040
SDLK_LEFTBRACKET = 0x0000005b
SDLK_BACKSLASH = 0x0000005c
SDLK_RIGHTBRACKET = 0x0000005d
SDLK_CARET = 0x0000005e
SDLK_UNDERSCORE = 0x0000005f
SDLK_GRAVE = 0x00000060
SDLK_A = 0x00000061
SDLK_B = 0x00000062
SDLK_C = 0x00000063
SDLK_D = 0x00000064
SDLK_E = 0x00000065
SDLK_F = 0x00000066
SDLK_G = 0x00000067
SDLK_H = 0x00000068
SDLK_I = 0x00000069
SDLK_J = 0x0000006a
SDLK_K = 0x0000006b
SDLK_L = 0x0000006c
SDLK_M = 0x0000006d
SDLK_N = 0x0000006e
SDLK_O = 0x0000006f
SDLK_P = 0x00000070
SDLK_Q = 0x00000071
SDLK_R = 0x00000072
SDLK_S = 0x00000073
SDLK_T = 0x00000074
SDLK_U = 0x00000075
SDLK_V = 0x00000076
SDLK_W = 0x00000077
SDLK_X = 0x00000078
SDLK_Y = 0x00000079
SDLK_Z = 0x0000007a
SDLK_LEFTBRACE = 0x0000007b
SDLK_PIPE = 0x0000007c
SDLK_RIGHTBRACE = 0x0000007d
SDLK_TILDE = 0x0000007e
SDLK_DELETE = 0x0000007f
SDLK_PLUSMINUS = 0x000000b1
SDLK_CAPSLOCK = 0x40000039
SDLK_F1 = 0x4000003a
SDLK_F2 = 0x4000003b
SDLK_F3 = 0x4000003c
SDLK_F4 = 0x4000003d
SDLK_F5 = 0x4000003e
SDLK_F6 = 0x4000003f
SDLK_F7 = 0x40000040
SDLK_F8 = 0x40000041
SDLK_F9 = 0x40000042
SDLK_F10 = 0x40000043
SDLK_F11 = 0x40000044
SDLK_F12 = 0x40000045
SDLK_PRINTSCREEN = 0x40000046
SDLK_SCROLLLOCK = 0x40000047
SDLK_PAUSE = 0x40000048
SDLK_INSERT = 0x40000049
SDLK_HOME = 0x4000004a
SDLK_PAGEUP = 0x4000004b
SDLK_END = 0x4000004d
SDLK_PAGEDOWN = 0x4000004e
SDLK_RIGHT = 0x4000004f
SDLK_LEFT = 0x40000050
SDLK_DOWN = 0x40000051
SDLK_UP = 0x40000052
SDLK_NUMLOCKCLEAR = 0x40000053
SDLK_KP_DIVIDE = 0x40000054
SDLK_KP_MULTIPLY = 0x40000055
SDLK_KP_MINUS = 0x40000056
SDLK_KP_PLUS = 0x40000057
SDLK_KP_ENTER = 0x40000058
SDLK_KP_1 = 0x40000059
SDLK_KP_2 = 0x4000005a
SDLK_KP_3 = 0x4000005b
SDLK_KP_4 = 0x4000005c
SDLK_KP_5 = 0x4000005d
SDLK_KP_6 = 0x4000005e
SDLK_KP_7 = 0x4000005f
SDLK_KP_8 = 0x40000060
SDLK_KP_9 = 0x40000061
SDLK_KP_0 = 0x40000062
SDLK_KP_PERIOD = 0x40000063
SDLK_APPLICATION = 0x40000065
SDLK_POWER = 0x40000066
SDLK_KP_EQUALS = 0x40000067
SDLK_F13 = 0x40000068
SDLK_F14 = 0x40000069
SDLK_F15 = 0x4000006a
SDLK_F16 = 0x4000006b
SDLK_F17 = 0x4000006c
SDLK_F18 = 0x4000006d
SDLK_F19 = 0x4000006e
SDLK_F20 = 0x4000006f
SDLK_F21 = 0x40000070
SDLK_F22 = 0x40000071
SDLK_F23 = 0x40000072
SDLK_F24 = 0x40000073
SDLK_EXECUTE = 0x40000074
SDLK_HELP = 0x40000075
SDLK_MENU = 0x40000076
SDLK_SELECT = 0x40000077
SDLK_STOP = 0x40000078
SDLK_AGAIN = 0x40000079
SDLK_UNDO = 0x4000007a
SDLK_CUT = 0x4000007b
SDLK_COPY = 0x4000007c
SDLK_PASTE = 0x4000007d
SDLK_FIND = 0x4000007e
SDLK_MUTE = 0x4000007f
SDLK_VOLUMEUP = 0x40000080
SDLK_VOLUMEDOWN = 0x40000081
SDLK_KP_COMMA = 0x40000085
SDLK_KP_EQUALSAS400 = 0x40000086
SDLK_ALTERASE = 0x40000099
SDLK_SYSREQ = 0x4000009a
SDLK_CANCEL = 0x4000009b
SDLK_CLEAR = 0x4000009c
SDLK_PRIOR = 0x4000009d
SDLK_RETURN2 = 0x4000009e
SDLK_SEPARATOR = 0x4000009f
SDLK_OUT = 0x400000a0
SDLK_OPER = 0x400000a1
SDLK_CLEARAGAIN = 0x400000a2
SDLK_CRSEL = 0x400000a3
SDLK_EXSEL = 0x400000a4
SDLK_KP_00 = 0x400000b0
SDLK_KP_000 = 0x400000b1
SDLK_THOUSANDSSEPARATOR = 0x400000b2
SDLK_DECIMALSEPARATOR = 0x400000b3
SDLK_CURRENCYUNIT = 0x400000b4
SDLK_CURRENCYSUBUNIT = 0x400000b5
SDLK_KP_LEFTPAREN = 0x400000b6
SDLK_KP_RIGHTPAREN = 0x400000b7
SDLK_KP_LEFTBRACE = 0x400000b8
SDLK_KP_RIGHTBRACE = 0x400000b9
SDLK_KP_TAB = 0x400000ba
SDLK_KP_BACKSPACE = 0x400000bb
SDLK_KP_A = 0x400000bc
SDLK_KP_B = 0x400000bd
SDLK_KP_C = 0x400000be
SDLK_KP_D = 0x400000bf
SDLK_KP_E = 0x400000c0
SDLK_KP_F = 0x400000c1
SDLK_KP_XOR = 0x400000c2
SDLK_KP_POWER = 0x400000c3
SDLK_KP_PERCENT = 0x400000c4
SDLK_KP_LESS = 0x400000c5
SDLK_KP_GREATER = 0x400000c6
SDLK_KP_AMPERSAND = 0x400000c7
SDLK_KP_DBLAMPERSAND = 0x400000c8
SDLK_KP_VERTICALBAR = 0x400000c9
SDLK_KP_DBLVERTICALBAR = 0x400000ca
SDLK_KP_COLON = 0x400000cb
SDLK_KP_HASH = 0x400000cc
SDLK_KP_SPACE = 0x400000cd
SDLK_KP_AT = 0x400000ce
SDLK_KP_EXCLAM = 0x400000cf
SDLK_KP_MEMSTORE = 0x400000d0
SDLK_KP_MEMRECALL = 0x400000d1
SDLK_KP_MEMCLEAR = 0x400000d2
SDLK_KP_MEMADD = 0x400000d3
SDLK_KP_MEMSUBTRACT = 0x400000d4
SDLK_KP_MEMMULTIPLY = 0x400000d5
SDLK_KP_MEMDIVIDE = 0x400000d6
SDLK_KP_PLUSMINUS = 0x400000d7
SDLK_KP_CLEAR = 0x400000d8
SDLK_KP_CLEARENTRY = 0x400000d9
SDLK_KP_BINARY = 0x400000da
SDLK_KP_OCTAL = 0x400000db
SDLK_KP_DECIMAL = 0x400000dc
SDLK_KP_HEXADECIMAL = 0x400000dd
SDLK_LCTRL = 0x400000e0
SDLK_LSHIFT = 0x400000e1
SDLK_LALT = 0x400000e2
SDLK_LGUI = 0x400000e3
SDLK_RCTRL = 0x400000e4
SDLK_RSHIFT = 0x400000e5
SDLK_RALT = 0x400000e6
SDLK_RGUI = 0x400000e7
SDLK_MODE = 0x40000101
SDLK_SLEEP = 0x40000102
SDLK_WAKE = 0x40000103
SDLK_CHANNEL_INCREMENT = 0x40000104
SDLK_CHANNEL_DECREMENT = 0x40000105
SDLK_MEDIA_PLAY = 0x40000106
SDLK_MEDIA_PAUSE = 0x40000107
SDLK_MEDIA_RECORD = 0x40000108
SDLK_MEDIA_FAST_FORWARD = 0x40000109
SDLK_MEDIA_REWIND = 0x4000010a
SDLK_MEDIA_NEXT_TRACK = 0x4000010b
SDLK_MEDIA_PREVIOUS_TRACK = 0x4000010c
SDLK_MEDIA_STOP = 0x4000010d
SDLK_MEDIA_EJECT = 0x4000010e
SDLK_MEDIA_PLAY_PAUSE = 0x4000010f
SDLK_MEDIA_SELECT = 0x40000110
SDLK_AC_NEW = 0x40000111
SDLK_AC_OPEN = 0x40000112
SDLK_AC_CLOSE = 0x40000113
SDLK_AC_EXIT = 0x40000114
SDLK_AC_SAVE = 0x40000115
SDLK_AC_PRINT = 0x40000116
SDLK_AC_PROPERTIES = 0x40000117
SDLK_AC_SEARCH = 0x40000118
SDLK_AC_HOME = 0x40000119
SDLK_AC_BACK = 0x4000011a
SDLK_AC_FORWARD = 0x4000011b
SDLK_AC_STOP = 0x4000011c
SDLK_AC_REFRESH = 0x4000011d
SDLK_AC_BOOKMARKS = 0x4000011e
SDLK_SOFTLEFT = 0x4000011f
SDLK_SOFTRIGHT = 0x40000120
SDLK_CALL = 0x40000121
SDLK_ENDCALL = 0x40000122
SDLK_LEFT_TAB = 0x20000001
SDLK_LEVEL5_SHIFT = 0x20000002
SDLK_MULTI_KEY_COMPOSE = 0x20000003
SDLK_LMETA = 0x20000004
SDLK_RMETA = 0x20000005
SDLK_LHYPER = 0x20000006
SDLK_RHYPER = 0x20000007

SDL_Keymod: typing.TypeAlias = ctypes.c_uint16

SDL_KMOD_NONE = 0x0000
SDL_KMOD_LSHIFT = 0x0001
SDL_KMOD_RSHIFT = 0x0002
SDL_KMOD_LEVEL5 = 0x0004
SDL_KMOD_LCTRL = 0x0040
SDL_KMOD_RCTRL = 0x0080
SDL_KMOD_LALT = 0x0100
SDL_KMOD_RALT = 0x0200
SDL_KMOD_LGUI = 0x0400
SDL_KMOD_RGUI = 0x0800
SDL_KMOD_NUM = 0x1000
SDL_KMOD_CAPS = 0x2000
SDL_KMOD_MODE = 0x4000
SDL_KMOD_SCROLL = 0x8000
SDL_KMOD_CTRL = SDL_KMOD_LCTRL | SDL_KMOD_RCTRL
SDL_KMOD_SHIFT = SDL_KMOD_LSHIFT | SDL_KMOD_RSHIFT
SDL_KMOD_ALT = SDL_KMOD_LALT | SDL_KMOD_RALT
SDL_KMOD_GUI = SDL_KMOD_LGUI | SDL_KMOD_RGUI