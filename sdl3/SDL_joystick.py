from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_sensor import SDL_SensorType
from .SDL_properties import SDL_PropertiesID
from .SDL_power import SDL_PowerState
from .SDL_guid import SDL_GUID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Joystick(ctypes.c_void_p):
    ...

SDL_JoystickID = ctypes.c_uint32

SDL_JoystickType = ctypes.c_int

SDL_JOYSTICK_TYPE_UNKNOWN = 0
SDL_JOYSTICK_TYPE_GAMEPAD = 1
SDL_JOYSTICK_TYPE_WHEEL = 2
SDL_JOYSTICK_TYPE_ARCADE_STICK = 3
SDL_JOYSTICK_TYPE_FLIGHT_STICK = 4
SDL_JOYSTICK_TYPE_DANCE_PAD = 5
SDL_JOYSTICK_TYPE_GUITAR = 6
SDL_JOYSTICK_TYPE_DRUM_KIT = 7
SDL_JOYSTICK_TYPE_ARCADE_PAD = 8
SDL_JOYSTICK_TYPE_THROTTLE = 9
SDL_JOYSTICK_TYPE_COUNT = 10

SDL_JoystickConnectionState = ctypes.c_int

SDL_JOYSTICK_CONNECTION_INVALID = -1
SDL_JOYSTICK_CONNECTION_UNKNOWN = 0
SDL_JOYSTICK_CONNECTION_WIRED = 1
SDL_JOYSTICK_CONNECTION_WIRELESS = 2

SDL_JOYSTICK_AXIS_MAX = 32767
SDL_JOYSTICK_AXIS_MIN = -32768

SDL_FUNC("SDL_LockJoysticks", None)
SDL_FUNC("SDL_UnlockJoysticks", None)
SDL_FUNC("SDL_HasJoystick", ctypes.c_bool)
SDL_FUNC("SDL_GetJoysticks", ctypes.POINTER(SDL_JoystickID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetJoystickNameForID", ctypes.c_char_p, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickPathForID", ctypes.c_char_p, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickPlayerIndexForID", ctypes.c_int, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickGUIDForID", SDL_GUID, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickVendorForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickProductForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickProductVersionForID", ctypes.c_uint16, SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickTypeForID", SDL_JoystickType, SDL_JoystickID)
SDL_FUNC("SDL_OpenJoystick", ctypes.POINTER(SDL_Joystick), SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickFromID", ctypes.POINTER(SDL_Joystick), SDL_JoystickID)
SDL_FUNC("SDL_GetJoystickFromPlayerIndex", ctypes.POINTER(SDL_Joystick), ctypes.c_int)

class SDL_VirtualJoystickTouchpadDesc(ctypes.Structure):
    _fields_ = [
        ("nfingers", ctypes.c_uint16),
        ("padding", ctypes.c_uint16 * 3)
    ]

class SDL_VirtualJoystickSensorDesc(ctypes.Structure):
    _fields_ = [
        ("type", SDL_SensorType),
        ("rate", ctypes.c_float)
    ]

class SDL_VirtualJoystickDesc(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("type", ctypes.c_uint16),
        ("padding", ctypes.c_uint16),
        ("vendor_id", ctypes.c_uint16),
        ("product_id", ctypes.c_uint16),
        ("naxes", ctypes.c_uint16),
        ("nbuttons", ctypes.c_uint16),
        ("nballs", ctypes.c_uint16),
        ("nhats", ctypes.c_uint16),
        ("ntouchpads", ctypes.c_uint16),
        ("nsensors", ctypes.c_uint16),
        ("padding2", ctypes.c_uint16 * 2),
        ("button_mask", ctypes.c_uint32),
        ("axis_mask", ctypes.c_uint32),
        ("name", ctypes.c_char_p),
        ("touchpads", ctypes.POINTER(SDL_VirtualJoystickTouchpadDesc)),
        ("sensors", ctypes.POINTER(SDL_VirtualJoystickSensorDesc)),
        ("userdata", ctypes.c_void_p),
        ("Update", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
        ("SetPlayerIndex", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)),
        ("Rumble", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint16, ctypes.c_uint16)),
        ("RumbleTriggers", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint16, ctypes.c_uint16)),
        ("SetLED", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)),
        ("SendEffect", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)),
        ("SetSensorsEnabled", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_bool)),
        ("Cleanup", ctypes.CFUNCTYPE(None, ctypes.c_void_p))
    ]

SDL_FUNC("SDL_AttachVirtualJoystick", SDL_JoystickID, ctypes.POINTER(SDL_VirtualJoystickDesc))
SDL_FUNC("SDL_DetachVirtualJoystick", ctypes.c_bool, SDL_JoystickID)
SDL_FUNC("SDL_IsJoystickVirtual", ctypes.c_bool, SDL_JoystickID)
SDL_FUNC("SDL_SetJoystickVirtualAxis", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.c_int16)
SDL_FUNC("SDL_SetJoystickVirtualBall", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.c_int16, ctypes.c_int16)
SDL_FUNC("SDL_SetJoystickVirtualButton", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.c_uint8)
SDL_FUNC("SDL_SetJoystickVirtualHat", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.c_uint8)
SDL_FUNC("SDL_SetJoystickVirtualTouchpad", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.c_int, ctypes.c_uint8, ctypes.c_float, ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_SendJoystickVirtualSensorData", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), SDL_SensorType, ctypes.c_uint64, ctypes.POINTER(ctypes.c_float), ctypes.c_int)
SDL_FUNC("SDL_GetJoystickProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Joystick))

SDL_PROP_JOYSTICK_CAP_MONO_LED_BOOLEAN = "SDL.joystick.cap.mono_led".encode()
SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN = "SDL.joystick.cap.rgb_led".encode()
SDL_PROP_JOYSTICK_CAP_PLAYER_LED_BOOLEAN = "SDL.joystick.cap.player_led".encode()
SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN = "SDL.joystick.cap.rumble".encode()
SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN = "SDL.joystick.cap.trigger_rumble".encode()

SDL_FUNC("SDL_GetJoystickName", ctypes.c_char_p, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickPath", ctypes.c_char_p, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickPlayerIndex", ctypes.c_int, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_SetJoystickPlayerIndex", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int)
SDL_FUNC("SDL_GetJoystickGUID", SDL_GUID, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickVendor", ctypes.c_uint16, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickProduct", ctypes.c_uint16, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickProductVersion", ctypes.c_uint16, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickFirmwareVersion", ctypes.c_uint16, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickSerial", ctypes.c_char_p, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickType", SDL_JoystickType, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickGUIDInfo", None, SDL_GUID, ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint16))
SDL_FUNC("SDL_JoystickConnected", ctypes.c_bool, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickID", SDL_JoystickID, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetNumJoystickAxes", ctypes.c_int, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetNumJoystickBalls", ctypes.c_int, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetNumJoystickHats", ctypes.c_int, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetNumJoystickButtons", ctypes.c_int, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_SetJoystickEventsEnabled", None, ctypes.c_bool)
SDL_FUNC("SDL_JoystickEventsEnabled", ctypes.c_bool)
SDL_FUNC("SDL_UpdateJoysticks", None)
SDL_FUNC("SDL_GetJoystickAxis", ctypes.c_int16, ctypes.POINTER(SDL_Joystick), ctypes.c_int)
SDL_FUNC("SDL_GetJoystickAxisInitialState", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.POINTER(ctypes.c_int16))
SDL_FUNC("SDL_GetJoystickBall", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetJoystickHat", ctypes.c_uint8, ctypes.POINTER(SDL_Joystick), ctypes.c_int)

SDL_HAT_CENTERED = 0x00
SDL_HAT_UP = 0x01
SDL_HAT_RIGHT = 0x02
SDL_HAT_DOWN = 0x04
SDL_HAT_LEFT = 0x08
SDL_HAT_RIGHTUP = SDL_HAT_RIGHT | SDL_HAT_UP
SDL_HAT_RIGHTDOWN = SDL_HAT_RIGHT | SDL_HAT_DOWN
SDL_HAT_LEFTUP = SDL_HAT_LEFT | SDL_HAT_UP
SDL_HAT_LEFTDOWN = SDL_HAT_LEFT | SDL_HAT_DOWN

SDL_FUNC("SDL_GetJoystickButton", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_int)
SDL_FUNC("SDL_RumbleJoystick", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)
SDL_FUNC("SDL_RumbleJoystickTriggers", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)
SDL_FUNC("SDL_SetJoystickLED", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("SDL_SendJoystickEffect", ctypes.c_bool, ctypes.POINTER(SDL_Joystick), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_CloseJoystick", None, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickConnectionState", SDL_JoystickConnectionState, ctypes.POINTER(SDL_Joystick))
SDL_FUNC("SDL_GetJoystickPowerInfo", SDL_PowerState, ctypes.POINTER(SDL_Joystick), ctypes.POINTER(ctypes.c_int))