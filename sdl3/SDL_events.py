from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_video import SDL_Window, SDL_WindowID, SDL_DisplayID
from .SDL_sensor import SDL_SensorID
from .SDL_joystick import SDL_JoystickID
from .SDL_keyboard import SDL_KeyboardID
from .SDL_keycode import SDL_Keycode, SDL_Keymod
from .SDL_scancode import SDL_Scancode
from .SDL_mouse import SDL_MouseID, SDL_MouseWheelDirection, SDL_MouseButtonFlags
from .SDL_power import SDL_PowerState
from .SDL_audio import SDL_AudioDeviceID
from .SDL_camera import SDL_CameraID
from .SDL_pen import SDL_PenID, SDL_PenInputFlags, SDL_PenAxis
from .SDL_touch import SDL_TouchID, SDL_FingerID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_EventType = ctypes.c_int

SDL_EVENT_FIRST = 0x0
SDL_EVENT_QUIT = 0x100
SDL_EVENT_TERMINATING = 0x101
SDL_EVENT_LOW_MEMORY = 0x102
SDL_EVENT_WILL_ENTER_BACKGROUND = 0x103
SDL_EVENT_DID_ENTER_BACKGROUND = 0x104
SDL_EVENT_WILL_ENTER_FOREGROUND = 0x105
SDL_EVENT_DID_ENTER_FOREGROUND = 0x106
SDL_EVENT_LOCALE_CHANGED = 0x107
SDL_EVENT_SYSTEM_THEME_CHANGED = 0x108

SDL_EVENT_DISPLAY_ORIENTATION = 0x151
SDL_EVENT_DISPLAY_ADDED = 0x152
SDL_EVENT_DISPLAY_REMOVED = 0x153
SDL_EVENT_DISPLAY_MOVED = 0x154
SDL_EVENT_DISPLAY_DESKTOP_MODE_CHANGED = 0x155
SDL_EVENT_DISPLAY_CURRENT_MODE_CHANGED = 0x156
SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED = 0x157
SDL_EVENT_DISPLAY_FIRST = SDL_EVENT_DISPLAY_ORIENTATION
SDL_EVENT_DISPLAY_LAST = SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED

SDL_EVENT_WINDOW_SHOWN = 0x202
SDL_EVENT_WINDOW_HIDDEN = 0x203
SDL_EVENT_WINDOW_EXPOSED = 0x204
SDL_EVENT_WINDOW_MOVED = 0x205
SDL_EVENT_WINDOW_RESIZED = 0x206
SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED = 0x207
SDL_EVENT_WINDOW_METAL_VIEW_RESIZED = 0x208
SDL_EVENT_WINDOW_MINIMIZED = 0x209
SDL_EVENT_WINDOW_MAXIMIZED = 0x20A
SDL_EVENT_WINDOW_RESTORED = 0x20B
SDL_EVENT_WINDOW_MOUSE_ENTER = 0x20C
SDL_EVENT_WINDOW_MOUSE_LEAVE = 0x20D
SDL_EVENT_WINDOW_FOCUS_GAINED = 0x20E
SDL_EVENT_WINDOW_FOCUS_LOST = 0x20F
SDL_EVENT_WINDOW_CLOSE_REQUESTED = 0x210
SDL_EVENT_WINDOW_HIT_TEST = 0x211
SDL_EVENT_WINDOW_ICCPROF_CHANGED = 0x212
SDL_EVENT_WINDOW_DISPLAY_CHANGED = 0x213
SDL_EVENT_WINDOW_DISPLAY_SCALE_CHANGED = 0x214
SDL_EVENT_WINDOW_SAFE_AREA_CHANGED = 0x215
SDL_EVENT_WINDOW_OCCLUDED = 0x216
SDL_EVENT_WINDOW_ENTER_FULLSCREEN = 0x217
SDL_EVENT_WINDOW_LEAVE_FULLSCREEN = 0x218
SDL_EVENT_WINDOW_DESTROYED = 0x219

SDL_EVENT_WINDOW_HDR_STATE_CHANGED = 0x21A
SDL_EVENT_WINDOW_FIRST = SDL_EVENT_WINDOW_SHOWN
SDL_EVENT_WINDOW_LAST = SDL_EVENT_WINDOW_HDR_STATE_CHANGED

SDL_EVENT_KEY_DOWN = 0x300
SDL_EVENT_KEY_UP = 0x301
SDL_EVENT_TEXT_EDITING = 0x302
SDL_EVENT_TEXT_INPUT = 0x303
SDL_EVENT_KEYMAP_CHANGED = 0x304

SDL_EVENT_KEYBOARD_ADDED = 0x305
SDL_EVENT_KEYBOARD_REMOVED = 0x306
SDL_EVENT_TEXT_EDITING_CANDIDATES = 0x307

SDL_EVENT_MOUSE_MOTION = 0x400
SDL_EVENT_MOUSE_BUTTON_DOWN = 0x401
SDL_EVENT_MOUSE_BUTTON_UP = 0x402
SDL_EVENT_MOUSE_WHEEL = 0x403
SDL_EVENT_MOUSE_ADDED = 0x404
SDL_EVENT_MOUSE_REMOVED = 0x405

SDL_EVENT_JOYSTICK_AXIS_MOTION = 0x600
SDL_EVENT_JOYSTICK_BALL_MOTION = 0x601
SDL_EVENT_JOYSTICK_HAT_MOTION = 0x602
SDL_EVENT_JOYSTICK_BUTTON_DOWN = 0x603
SDL_EVENT_JOYSTICK_BUTTON_UP = 0x604
SDL_EVENT_JOYSTICK_ADDED = 0x605
SDL_EVENT_JOYSTICK_REMOVED = 0x606
SDL_EVENT_JOYSTICK_BATTERY_UPDATED = 0x607
SDL_EVENT_JOYSTICK_UPDATE_COMPLETE = 0x608

SDL_EVENT_GAMEPAD_AXIS_MOTION = 0x650
SDL_EVENT_GAMEPAD_BUTTON_DOWN = 0x651
SDL_EVENT_GAMEPAD_BUTTON_UP = 0x652
SDL_EVENT_GAMEPAD_ADDED = 0x653
SDL_EVENT_GAMEPAD_REMOVED = 0x654
SDL_EVENT_GAMEPAD_REMAPPED = 0x655
SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN = 0x656
SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION = 0x657
SDL_EVENT_GAMEPAD_TOUCHPAD_UP = 0x658
SDL_EVENT_GAMEPAD_SENSOR_UPDATE = 0x659
SDL_EVENT_GAMEPAD_UPDATE_COMPLETE = 0x65A
SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED = 0x65B

SDL_EVENT_FINGER_DOWN = 0x700
SDL_EVENT_FINGER_UP = 0x701
SDL_EVENT_FINGER_MOTION = 0x702
SDL_EVENT_FINGER_CANCELED = 0x703

SDL_EVENT_CLIPBOARD_UPDATE = 0x900

SDL_EVENT_DROP_FILE = 0x1000
SDL_EVENT_DROP_TEXT = 0x1001
SDL_EVENT_DROP_BEGIN = 0x1002
SDL_EVENT_DROP_COMPLETE = 0x1003
SDL_EVENT_DROP_POSITION = 0x1004

SDL_EVENT_AUDIO_DEVICE_ADDED = 0x1100
SDL_EVENT_AUDIO_DEVICE_REMOVED = 0x1101
SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED = 0x1102

SDL_EVENT_SENSOR_UPDATE = 0x1200

SDL_EVENT_PEN_PROXIMITY_IN = 0x1300
SDL_EVENT_PEN_PROXIMITY_OUT = 0x1301
SDL_EVENT_PEN_DOWN = 0x1302
SDL_EVENT_PEN_UP = 0x1303
SDL_EVENT_PEN_BUTTON_DOWN = 0x1304
SDL_EVENT_PEN_BUTTON_UP = 0x1305
SDL_EVENT_PEN_MOTION = 0x1306
SDL_EVENT_PEN_AXIS = 0x1307

SDL_EVENT_CAMERA_DEVICE_ADDED = 0x1400
SDL_EVENT_CAMERA_DEVICE_REMOVED = 0x1401
SDL_EVENT_CAMERA_DEVICE_APPROVED = 0x1402
SDL_EVENT_CAMERA_DEVICE_DENIED = 0x1403

SDL_EVENT_RENDER_TARGETS_RESET = 0x2000
SDL_EVENT_RENDER_DEVICE_RESET = 0x2001
SDL_EVENT_RENDER_DEVICE_LOST = 0x2002

SDL_EVENT_PRIVATE0 = 0x4000
SDL_EVENT_PRIVATE1 = 0x4001
SDL_EVENT_PRIVATE2 = 0x4002
SDL_EVENT_PRIVATE3 = 0x4003

SDL_EVENT_POLL_SENTINEL = 0x7F00
SDL_EVENT_USER = 0x8000
SDL_EVENT_LAST = 0xFFFF
SDL_EVENT_ENUM_PADDING = 0x7FFFFFFF

class SDL_CommonEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64)
    ]

class SDL_DisplayEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("displayID", SDL_DisplayID),
        ("data1", ctypes.c_int32),
        ("data2", ctypes.c_int32)
    ]

class SDL_WindowEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("data1", ctypes.c_int32),
        ("data2", ctypes.c_int32)
    ]

class SDL_KeyboardDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_KeyboardID)
    ]

class SDL_KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_KeyboardID),
        ("scancode", SDL_Scancode),
        ("key", SDL_Keycode),
        ("mod", SDL_Keymod),
        ("raw", ctypes.c_uint16),
        ("down", ctypes.c_bool),
        ("repeat", ctypes.c_bool)
    ]

class SDL_TextEditingEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("text", ctypes.c_char_p),
        ("start", ctypes.c_int32),
        ("length", ctypes.c_int32)
    ]

class SDL_TextEditingCandidatesEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("candidates", ctypes.POINTER(ctypes.c_char_p)),
        ("num_candidates", ctypes.c_int32),
        ("selected_candidate", ctypes.c_int32),
        ("horizontal", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_TextInputEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("text", ctypes.c_char_p)
    ]

class SDL_MouseDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_MouseID)
    ]

class SDL_MouseMotionEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_MouseID),
        ("state", SDL_MouseButtonFlags),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("xrel", ctypes.c_float),
        ("yrel", ctypes.c_float)
    ]

class SDL_MouseButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_MouseID),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("clicks", ctypes.c_uint8),
        ("padding", ctypes.c_uint8),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float)
    ]

class SDL_MouseWheelEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_MouseID),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("direction", SDL_MouseWheelDirection),
        ("mouse_x", ctypes.c_float),
        ("mouse_y", ctypes.c_float)
    ]

class SDL_JoyAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_int16),
        ("padding4", ctypes.c_uint16)
    ]

class SDL_JoyBallEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("ball", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("xrel", ctypes.c_int16),
        ("yrel", ctypes.c_int16)
    ]

class SDL_JoyHatEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("hat", ctypes.c_uint8),
        ("value", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_JoyButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_JoyDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID)
    ]

class SDL_JoyBatteryEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("state", SDL_PowerState),
        ("percent", ctypes.c_int)
    ]

class SDL_GamepadAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_int16),
        ("padding4", ctypes.c_uint16)
    ]

class SDL_GamepadButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8)
    ]

class SDL_GamepadDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID)
    ]

class SDL_GamepadTouchpadEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("touchpad", ctypes.c_int32),
        ("finger", ctypes.c_int32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("pressure", ctypes.c_float)
    ]

class SDL_GamepadSensorEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_JoystickID),
        ("sensor", ctypes.c_int32),
        ("data", ctypes.c_float * 3),
        ("sensor_timestamp", ctypes.c_uint64)
    ]

class SDL_AudioDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_AudioDeviceID),
        ("recording", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8)
    ]

class SDL_CameraDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_CameraID)
    ]

class SDL_RenderEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID)
    ]

class SDL_TouchFingerEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("touchID", SDL_TouchID),
        ("fingerID", SDL_FingerID),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("dx", ctypes.c_float),
        ("dy", ctypes.c_float),
        ("pressure", ctypes.c_float),
        ("windowID", SDL_WindowID)
    ]

class SDL_PenProximityEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_PenID)
    ]

class SDL_PenMotionEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_PenID),
        ("pen_state", SDL_PenInputFlags),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float)
    ]

class SDL_PenTouchEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_PenID),
        ("pen_state", SDL_PenInputFlags),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("eraser", ctypes.c_bool),
        ("down", ctypes.c_bool)
    ]

class SDL_PenButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_PenID),
        ("pen_state", SDL_PenInputFlags),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool)
    ]

class SDL_PenAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("which", SDL_PenID),
        ("pen_state", SDL_PenInputFlags),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("axis", SDL_PenAxis),
        ("value", ctypes.c_float)
    ]

class SDL_DropEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("source", ctypes.c_char_p),
        ("data", ctypes.c_char_p)
    ]

class SDL_ClipboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("owner", ctypes.c_bool),
        ("num_mime_types", ctypes.c_int32),
        ("mime_types", ctypes.POINTER(ctypes.c_char_p))
    ]

class SDL_SensorEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", SDL_SensorID),
        ("data", ctypes.c_float * 6),
        ("sensor_timestamp", ctypes.c_uint64)
    ]

class SDL_QuitEvent(ctypes.Structure):
    _fields_ = [
        ("type", SDL_EventType),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64)
    ]

class SDL_UserEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", SDL_WindowID),
        ("code", ctypes.c_int32),
        ("data1", ctypes.c_void_p),
        ("data2", ctypes.c_void_p)
    ]

class SDL_Event(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("common", SDL_CommonEvent),
        ("display", SDL_DisplayEvent),
        ("window", SDL_WindowEvent),
        ("kdevice", SDL_KeyboardDeviceEvent),
        ("key", SDL_KeyboardEvent),
        ("edit", SDL_TextEditingEvent),
        ("edit_candidates", SDL_TextEditingCandidatesEvent),
        ("text", SDL_TextInputEvent),
        ("mdevice", SDL_MouseDeviceEvent),
        ("motion", SDL_MouseMotionEvent),
        ("button", SDL_MouseButtonEvent),
        ("wheel", SDL_MouseWheelEvent),
        ("jdevice", SDL_JoyDeviceEvent),
        ("jaxis", SDL_JoyAxisEvent),
        ("jball", SDL_JoyBallEvent),
        ("jhat", SDL_JoyHatEvent),
        ("jbutton", SDL_JoyButtonEvent),
        ("jbattery", SDL_JoyBatteryEvent),
        ("gdevice", SDL_GamepadDeviceEvent),
        ("gaxis", SDL_GamepadAxisEvent),
        ("gbutton", SDL_GamepadButtonEvent),
        ("gtouchpad", SDL_GamepadTouchpadEvent),
        ("gsensor", SDL_GamepadSensorEvent),
        ("adevice", SDL_AudioDeviceEvent),
        ("cdevice", SDL_CameraDeviceEvent),
        ("sensor", SDL_SensorEvent),
        ("quit", SDL_QuitEvent),
        ("user", SDL_UserEvent),
        ("tfinger", SDL_TouchFingerEvent),
        ("pproximity", SDL_PenProximityEvent),
        ("ptouch", SDL_PenTouchEvent),
        ("pmotion", SDL_PenMotionEvent),
        ("pbutton", SDL_PenButtonEvent),
        ("paxis", SDL_PenAxisEvent),
        ("render", SDL_RenderEvent),
        ("drop", SDL_DropEvent),
        ("clipboard", SDL_ClipboardEvent),
        ("padding", ctypes.c_uint8 * 128)
    ]

SDL_FUNC("SDL_PumpEvents", None)

SDL_EventAction = ctypes.c_int

SDL_ADDEVENT = 0
SDL_PEEKEVENT = 1
SDL_GETEVENT = 2

SDL_FUNC("SDL_PeepEvents", ctypes.c_int, ctypes.POINTER(SDL_Event), ctypes.c_int, SDL_EventAction, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_HasEvent", ctypes.c_bool, ctypes.c_uint32)
SDL_FUNC("SDL_HasEvents", ctypes.c_bool, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_FlushEvent", None, ctypes.c_uint32)
SDL_FUNC("SDL_FlushEvents", None, ctypes.c_uint32, ctypes.c_uint32)
SDL_FUNC("SDL_PollEvent", ctypes.c_bool, ctypes.POINTER(SDL_Event))
SDL_FUNC("SDL_WaitEvent", ctypes.c_bool, ctypes.POINTER(SDL_Event))
SDL_FUNC("SDL_WaitEventTimeout", ctypes.c_bool, ctypes.POINTER(SDL_Event), ctypes.c_int32)
SDL_FUNC("SDL_PushEvent", ctypes.c_bool, ctypes.POINTER(SDL_Event))

SDL_EventFilter = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(SDL_Event))

SDL_FUNC("SDL_SetEventFilter", None, SDL_EventFilter, ctypes.c_void_p)
SDL_FUNC("SDL_GetEventFilter", ctypes.c_bool, ctypes.POINTER(SDL_EventFilter), ctypes.POINTER(ctypes.c_void_p))
SDL_FUNC("SDL_AddEventWatch", ctypes.c_bool, SDL_EventFilter, ctypes.c_void_p)
SDL_FUNC("SDL_RemoveEventWatch", None, SDL_EventFilter, ctypes.c_void_p)
SDL_FUNC("SDL_FilterEvents", None, SDL_EventFilter, ctypes.c_void_p)
SDL_FUNC("SDL_SetEventEnabled", None, ctypes.c_uint32, ctypes.c_bool)
SDL_FUNC("SDL_EventEnabled", ctypes.c_bool, ctypes.c_uint32)
SDL_FUNC("SDL_RegisterEvents", ctypes.c_uint32, ctypes.c_int)
SDL_FUNC("SDL_GetWindowFromEvent", ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Event))