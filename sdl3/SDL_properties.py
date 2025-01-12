from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_PropertiesID = ctypes.c_uint32
SDL_PropertyType = ctypes.c_int

SDL_PROPERTY_TYPE_INVALID = 0
SDL_PROPERTY_TYPE_POINTER = 1
SDL_PROPERTY_TYPE_STRING = 2
SDL_PROPERTY_TYPE_NUMBER = 3
SDL_PROPERTY_TYPE_FLOAT = 4
SDL_PROPERTY_TYPE_BOOLEAN = 5

SDL_FUNC("SDL_GetGlobalProperties", SDL_PropertiesID)
SDL_FUNC("SDL_CreateProperties", SDL_PropertiesID)
SDL_FUNC("SDL_CopyProperties", ctypes.c_bool, SDL_PropertiesID, SDL_PropertiesID)
SDL_FUNC("SDL_LockProperties", ctypes.c_bool, SDL_PropertiesID)
SDL_FUNC("SDL_UnlockProperties", None, SDL_PropertiesID)

SDL_CleanupPropertyCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

SDL_FUNC("SDL_SetPointerPropertyWithCleanup", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_void_p, SDL_CleanupPropertyCallback, ctypes.c_void_p)
SDL_FUNC("SDL_SetPointerProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_void_p)
SDL_FUNC("SDL_SetStringProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_SetNumberProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_int64)
SDL_FUNC("SDL_SetFloatProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_float)
SDL_FUNC("SDL_SetBooleanProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_bool)
SDL_FUNC("SDL_HasProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p)
SDL_FUNC("SDL_GetPropertyType", SDL_PropertyType, SDL_PropertiesID, ctypes.c_char_p)
SDL_FUNC("SDL_GetPointerProperty", ctypes.c_void_p, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_void_p)
SDL_FUNC("SDL_GetStringProperty", ctypes.c_char_p, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_char_p)
SDL_FUNC("SDL_GetNumberProperty", ctypes.c_int64, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_int64)
SDL_FUNC("SDL_GetFloatProperty", ctypes.c_float, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_float)
SDL_FUNC("SDL_GetBooleanProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p, ctypes.c_bool)
SDL_FUNC("SDL_ClearProperty", ctypes.c_bool, SDL_PropertiesID, ctypes.c_char_p)

SDL_EnumeratePropertiesCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, SDL_PropertiesID, ctypes.c_char_p)

SDL_FUNC("SDL_EnumerateProperties", ctypes.c_bool, SDL_PropertiesID, SDL_EnumeratePropertiesCallback, ctypes.c_void_p)
SDL_FUNC("SDL_DestroyProperties", None, SDL_PropertiesID)