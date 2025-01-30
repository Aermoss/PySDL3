from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_events import SDL_Event

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_InitFlags = ctypes.c_uint32

SDL_INIT_AUDIO = 0x00000010
SDL_INIT_VIDEO = 0x00000020
SDL_INIT_JOYSTICK = 0x00000200
SDL_INIT_HAPTIC = 0x00001000
SDL_INIT_GAMEPAD = 0x00002000
SDL_INIT_EVENTS = 0x00004000
SDL_INIT_SENSOR = 0x00008000
SDL_INIT_CAMERA = 0x00010000

SDL_AppResult = ctypes.c_int

SDL_APP_CONTINUE = 0
SDL_APP_SUCCESS = 1
SDL_APP_FAILURE = 2

SDL_AppInit_func = ctypes.CFUNCTYPE(SDL_AppResult, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.POINTER(ctypes.c_char_p))
SDL_AppIterate_func = ctypes.CFUNCTYPE(SDL_AppResult, ctypes.c_void_p)
SDL_AppEvent_func = ctypes.CFUNCTYPE(SDL_AppResult, ctypes.c_void_p, ctypes.POINTER(SDL_Event))
SDL_AppQuit_func = ctypes.CFUNCTYPE(None, ctypes.c_void_p, SDL_AppResult)

SDL_FUNC("SDL_Init", ctypes.c_bool, SDL_InitFlags)
SDL_FUNC("SDL_InitSubSystem", ctypes.c_bool, SDL_InitFlags)
SDL_FUNC("SDL_QuitSubSystem", None, SDL_InitFlags)
SDL_FUNC("SDL_WasInit", SDL_InitFlags, SDL_InitFlags)
SDL_FUNC("SDL_Quit", None)

SDL_FUNC("SDL_IsMainThread", ctypes.c_bool)
SDL_MainThreadCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
SDL_FUNC("SDL_RunOnMainThread", ctypes.c_bool, SDL_MainThreadCallback, ctypes.c_void_p, ctypes.c_bool)

SDL_FUNC("SDL_SetAppMetadata", ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_SetAppMetadataProperty", ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p)

SDL_PROP_APP_METADATA_NAME_STRING = "SDL.app.metadata.name".encode()
SDL_PROP_APP_METADATA_VERSION_STRING = "SDL.app.metadata.version".encode()
SDL_PROP_APP_METADATA_IDENTIFIER_STRING = "SDL.app.metadata.identifier".encode()
SDL_PROP_APP_METADATA_CREATOR_STRING = "SDL.app.metadata.creator".encode()
SDL_PROP_APP_METADATA_COPYRIGHT_STRING = "SDL.app.metadata.copyright".encode()
SDL_PROP_APP_METADATA_URL_STRING = "SDL.app.metadata.url".encode()
SDL_PROP_APP_METADATA_TYPE_STRING = "SDL.app.metadata.type".encode()

SDL_FUNC("SDL_GetAppMetadataProperty", ctypes.c_char_p, ctypes.c_char_p)