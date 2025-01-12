from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_guid import SDL_GUID
from .SDL_power import SDL_PowerState
from .SDL_sensor import SDL_SensorType
from .SDL_iostream import SDL_IOStream
from .SDL_properties import SDL_PropertiesID
from .SDL_joystick import SDL_Joystick, SDL_JoystickID, SDL_JoystickConnectionState, \
    SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN, SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN, \
    SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN, SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN, \
    SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Gamepad(ctypes.c_void_p):
    ...

SDL_GamepadType = ctypes.c_int

SDL_GAMEPAD_TYPE_UNKNOWN = 0
SDL_GAMEPAD_TYPE_STANDARD = 1
SDL_GAMEPAD_TYPE_XBOX360 = 2
SDL_GAMEPAD_TYPE_XBOXONE = 3
SDL_GAMEPAD_TYPE_PS3 = 4
SDL_GAMEPAD_TYPE_PS4 = 5
SDL_GAMEPAD_TYPE_PS5 = 6
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_PRO = 7
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_LEFT = 8
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT = 9
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_PAIR = 10
SDL_GAMEPAD_TYPE_COUNT = 11

SDL_GamepadButton = ctypes.c_int

SDL_GAMEPAD_BUTTON_INVALID = -1
SDL_GAMEPAD_BUTTON_SOUTH = 0
SDL_GAMEPAD_BUTTON_EAST = 1
SDL_GAMEPAD_BUTTON_WEST = 2
SDL_GAMEPAD_BUTTON_NORTH = 3
SDL_GAMEPAD_BUTTON_BACK = 4
SDL_GAMEPAD_BUTTON_GUIDE = 5
SDL_GAMEPAD_BUTTON_START = 6
SDL_GAMEPAD_BUTTON_LEFT_STICK = 7
SDL_GAMEPAD_BUTTON_RIGHT_STICK = 8
SDL_GAMEPAD_BUTTON_LEFT_SHOULDER = 9
SDL_GAMEPAD_BUTTON_RIGHT_SHOULDER = 10
SDL_GAMEPAD_BUTTON_DPAD_UP = 11
SDL_GAMEPAD_BUTTON_DPAD_DOWN = 12
SDL_GAMEPAD_BUTTON_DPAD_LEFT = 13
SDL_GAMEPAD_BUTTON_DPAD_RIGHT = 14
SDL_GAMEPAD_BUTTON_MISC1 = 15
SDL_GAMEPAD_BUTTON_RIGHT_PADDLE1 = 16
SDL_GAMEPAD_BUTTON_LEFT_PADDLE1 = 17
SDL_GAMEPAD_BUTTON_RIGHT_PADDLE2 = 18
SDL_GAMEPAD_BUTTON_LEFT_PADDLE2 = 19
SDL_GAMEPAD_BUTTON_TOUCHPAD = 20
SDL_GAMEPAD_BUTTON_MISC2 = 21
SDL_GAMEPAD_BUTTON_MISC3 = 22
SDL_GAMEPAD_BUTTON_MISC4 = 23
SDL_GAMEPAD_BUTTON_MISC5 = 24
SDL_GAMEPAD_BUTTON_MISC6 = 25
SDL_GAMEPAD_BUTTON_COUNT = 26

SDL_GamepadButtonLabel = ctypes.c_int

SDL_GAMEPAD_BUTTON_LABEL_UNKNOWN = 0
SDL_GAMEPAD_BUTTON_LABEL_A = 1
SDL_GAMEPAD_BUTTON_LABEL_B = 2
SDL_GAMEPAD_BUTTON_LABEL_X = 3
SDL_GAMEPAD_BUTTON_LABEL_Y = 4
SDL_GAMEPAD_BUTTON_LABEL_CROSS = 5
SDL_GAMEPAD_BUTTON_LABEL_CIRCLE = 6
SDL_GAMEPAD_BUTTON_LABEL_SQUARE = 7
SDL_GAMEPAD_BUTTON_LABEL_TRIANGLE = 8

SDL_GamepadAxis = ctypes.c_int

SDL_GAMEPAD_AXIS_INVALID = -1
SDL_GAMEPAD_AXIS_LEFTX = 0
SDL_GAMEPAD_AXIS_LEFTY = 1
SDL_GAMEPAD_AXIS_RIGHTX = 2
SDL_GAMEPAD_AXIS_RIGHTY = 3
SDL_GAMEPAD_AXIS_LEFT_TRIGGER = 4
SDL_GAMEPAD_AXIS_RIGHT_TRIGGER = 5
SDL_GAMEPAD_AXIS_COUNT = 6

SDL_GamepadBindingType = ctypes.c_int

SDL_GAMEPAD_BINDTYPE_NONE = 0
SDL_GAMEPAD_BINDTYPE_BUTTON = 1
SDL_GAMEPAD_BINDTYPE_AXIS = 2
SDL_GAMEPAD_BINDTYPE_HAT = 3

class _axis(ctypes.Structure):
    _fields_ = [
        ("axis", SDL_GamepadAxis),
        ("axis_min", ctypes.c_int),
        ("axis_max", ctypes.c_int)
    ]

class _hat(ctypes.Structure):
    _fields_ = [
        ("hat", ctypes.c_int),
        ("mask", ctypes.c_int)
    ]

class _input(ctypes.Union):
    _fields_ = [
        ("button", SDL_GamepadButton),
        ("axis", _axis),
        ("hat", _hat)
    ]

class _output(ctypes.Union):
    _fields_ = [
        ("button", SDL_GamepadButton),
        ("axis", _axis)
    ]

class SDL_GamepadBinding(ctypes.Structure):
    _fields_ = [
        ("input_type", SDL_GamepadBindingType),
        ("input", _input),
        ("output_type", SDL_GamepadBindingType),
        ("output", _output)
    ]

SDL_FUNC("SDL_AddGamepadMapping", ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_AddGamepadMappingsFromIO", ctypes.c_int, ctypes.POINTER(SDL_IOStream), ctypes.c_bool)
SDL_FUNC("SDL_AddGamepadMappingsFromFile", ctypes.c_int, ctypes.c_char_p)
SDL_FUNC("SDL_ReloadGamepadMappings", ctypes.c_bool)
SDL_FUNC("SDL_GetGamepadMappings", ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetGamepadMappingForGUID", ctypes.c_char_p, SDL_GUID)
SDL_FUNC("SDL_GetGamepadMapping", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_SetGamepadMapping", ctypes.c_bool, SDL_JoystickID, ctypes.c_char_p)
SDL_FUNC("SDL_HasGamepad", ctypes.c_bool)
SDL_FUNC("SDL_GetGamepads", ctypes.POINTER(SDL_JoystickID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_IsGamepad", ctypes.c_bool, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadNameForID", ctypes.c_char_p, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadPathForID", ctypes.c_char_p, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadPlayerIndexForID", ctypes.c_int, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadGUIDForID", SDL_GUID, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadVendorForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadProductForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadProductVersionForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadTypeForID", SDL_GamepadType, SDL_JoystickID)
SDL_FUNC("SDL_GetRealGamepadTypeForID", SDL_GamepadType, SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadMappingForID", ctypes.c_char_p, SDL_JoystickID)
SDL_FUNC("SDL_OpenGamepad", ctypes.POINTER(SDL_Gamepad), SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadFromID", ctypes.POINTER(SDL_Gamepad), SDL_JoystickID)
SDL_FUNC("SDL_GetGamepadFromPlayerIndex", ctypes.POINTER(SDL_Gamepad), ctypes.c_int)
SDL_FUNC("SDL_GetGamepadProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Gamepad))

SDL_PROP_GAMEPAD_CAP_MONO_LED_BOOLEAN = SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN
SDL_PROP_GAMEPAD_CAP_RGB_LED_BOOLEAN = SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN
SDL_PROP_GAMEPAD_CAP_PLAYER_LED_BOOLEAN = SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN
SDL_PROP_GAMEPAD_CAP_RUMBLE_BOOLEAN = SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN
SDL_PROP_GAMEPAD_CAP_TRIGGER_RUMBLE_BOOLEAN = SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN

SDL_FUNC("SDL_GetGamepadID", SDL_JoystickID, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadName", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadPath", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadType", SDL_GamepadType, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetRealGamepadType", SDL_GamepadType, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadPlayerIndex", ctypes.c_int, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_SetGamepadPlayerIndex", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_int)
SDL_FUNC("SDL_GetGamepadVendor", ctypes.c_uint16, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadProduct", ctypes.c_uint16, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadProductVersion", ctypes.c_uint16, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadFirmwareVersion", ctypes.c_uint16, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadSerial", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadSteamHandle", ctypes.c_uint64, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadConnectionState", SDL_JoystickConnectionState, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadPowerInfo", SDL_PowerState, ctypes.POINTER(SDL_Gamepad), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GamepadConnected", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetGamepadJoystick", ctypes.POINTER(SDL_Joystick), ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_SetGamepadEventsEnabled", None, ctypes.c_bool)
SDL_FUNC("SDL_GamepadEventsEnabled", ctypes.c_bool)
SDL_FUNC("SDL_GetGamepadBindings", ctypes.POINTER(ctypes.POINTER(SDL_GamepadBinding)), ctypes.POINTER(SDL_Gamepad), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_UpdateGamepads", None)
SDL_FUNC("SDL_GetGamepadTypeFromString", SDL_GamepadType, ctypes.c_char_p)
SDL_FUNC("SDL_GetGamepadStringForType", ctypes.c_char_p, SDL_GamepadType)
SDL_FUNC("SDL_GetGamepadAxisFromString", SDL_GamepadAxis, ctypes.c_char_p)
SDL_FUNC("SDL_GetGamepadStringForAxis", ctypes.c_char_p, SDL_GamepadAxis)
SDL_FUNC("SDL_GamepadHasAxis", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_GamepadAxis)
SDL_FUNC("SDL_GetGamepadAxis", ctypes.c_int16, ctypes.POINTER(SDL_Gamepad), SDL_GamepadAxis)
SDL_FUNC("SDL_GetGamepadButtonFromString", SDL_GamepadButton, ctypes.c_char_p)
SDL_FUNC("SDL_GetGamepadStringForButton", ctypes.c_char_p, SDL_GamepadButton)
SDL_FUNC("SDL_GamepadHasButton", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_GamepadButton)
SDL_FUNC("SDL_GetGamepadButton", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_GamepadButton)
SDL_FUNC("SDL_GetGamepadButtonLabelForType", SDL_GamepadButtonLabel, SDL_GamepadType, SDL_GamepadButton)
SDL_FUNC("SDL_GetGamepadButtonLabel", SDL_GamepadButtonLabel, ctypes.POINTER(SDL_Gamepad), SDL_GamepadButton)
SDL_FUNC("SDL_GetNumGamepadTouchpads", ctypes.c_int, ctypes.POINTER(SDL_Gamepad))
SDL_FUNC("SDL_GetNumGamepadTouchpadFingers", ctypes.c_int, ctypes.POINTER(SDL_Gamepad), ctypes.c_int)
SDL_FUNC("SDL_GetGamepadTouchpadFinger", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))
SDL_FUNC("SDL_GamepadHasSensor", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_SensorType)
SDL_FUNC("SDL_SetGamepadSensorEnabled", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_SensorType, ctypes.c_bool)
SDL_FUNC("SDL_GamepadSensorEnabled", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_SensorType)
SDL_FUNC("SDL_GetGamepadSensorDataRate", ctypes.c_float, ctypes.POINTER(SDL_Gamepad), SDL_SensorType)
SDL_FUNC("SDL_GetGamepadSensorData", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), SDL_SensorType, ctypes.POINTER(ctypes.c_float), ctypes.c_int)
SDL_FUNC("SDL_RumbleGamepad", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)
SDL_FUNC("SDL_RumbleGamepadTriggers", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)
SDL_FUNC("SDL_SetGamepadLED", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_SendGamepadEffect", ctypes.c_bool, ctypes.POINTER(SDL_Gamepad), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_CloseGamepad", None, ctypes.POINTER(SDL_Gamepad))

SDL_FUNC("SDL_GetGamepadAppleSFSymbolsNameForButton", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad), SDL_GamepadButton)
SDL_FUNC("SDL_GetGamepadAppleSFSymbolsNameForAxis", ctypes.c_char_p, ctypes.POINTER(SDL_Gamepad), SDL_GamepadAxis)