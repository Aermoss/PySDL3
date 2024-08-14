from .__init__ import ctypes, SDL_FUNC

SDL_InitFlags = ctypes.c_uint32

SDL_INIT_TIMER = 0x00000001
SDL_INIT_AUDIO = 0x00000010
SDL_INIT_VIDEO = 0x00000020
SDL_INIT_JOYSTICK = 0x00000200
SDL_INIT_HAPTIC = 0x00001000
SDL_INIT_GAMEPAD = 0x00002000
SDL_INIT_EVENTS = 0x00004000
SDL_INIT_SENSOR = 0x00008000
SDL_INIT_CAMERA = 0x00010000

SDL_FUNC("SDL_Init", ctypes.c_int, SDL_InitFlags)
SDL_FUNC("SDL_InitSubSystem", ctypes.c_int, SDL_InitFlags)
SDL_FUNC("SDL_QuitSubSystem", None, SDL_InitFlags)
SDL_FUNC("SDL_WasInit", SDL_InitFlags, SDL_InitFlags)
SDL_FUNC("SDL_Quit", None)

SDL_FUNC("SDL_SetAppMetadata", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_SetAppMetadataProperty", ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

SDL_PROP_APP_METADATA_NAME_STRING = "SDL.app.metadata.name"
SDL_PROP_APP_METADATA_VERSION_STRING = "SDL.app.metadata.version"
SDL_PROP_APP_METADATA_IDENTIFIER_STRING = "SDL.app.metadata.identifier"
SDL_PROP_APP_METADATA_CREATOR_STRING = "SDL.app.metadata.creator"
SDL_PROP_APP_METADATA_COPYRIGHT_STRING = "SDL.app.metadata.copyright"
SDL_PROP_APP_METADATA_URL_STRING = "SDL.app.metadata.url"
SDL_PROP_APP_METADATA_TYPE_STRING = "SDL.app.metadata.type"

SDL_FUNC("SDL_GetAppMetadataProperty", ctypes.c_char_p, ctypes.c_char_p)