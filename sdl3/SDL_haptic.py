from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_joystick import SDL_Joystick

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Haptic(ctypes.c_void_p):
    ...

SDL_HAPTIC_CONSTANT = 1 << 0
SDL_HAPTIC_SINE = 1 << 1
SDL_HAPTIC_SQUARE = 1 << 2
SDL_HAPTIC_TRIANGLE = 1 << 3
SDL_HAPTIC_SAWTOOTHUP = 1 << 4
SDL_HAPTIC_SAWTOOTHDOWN = 1 << 5
SDL_HAPTIC_RAMP = 1 << 6
SDL_HAPTIC_SPRING = 1 << 7
SDL_HAPTIC_DAMPER = 1 << 8
SDL_HAPTIC_INERTIA = 1 << 9
SDL_HAPTIC_FRICTION = 1 << 10
SDL_HAPTIC_LEFTRIGHT = 1 << 11
SDL_HAPTIC_RESERVED1 = 1 << 12
SDL_HAPTIC_RESERVED2 = 1 << 13
SDL_HAPTIC_RESERVED3 = 1 << 14
SDL_HAPTIC_CUSTOM = 1 << 15
SDL_HAPTIC_GAIN = 1 << 16
SDL_HAPTIC_AUTOCENTER = 1 << 17
SDL_HAPTIC_STATUS = 1 << 18
SDL_HAPTIC_PAUSE = 1 << 19

SDL_HAPTIC_POLAR = 0
SDL_HAPTIC_CARTESIAN = 1
SDL_HAPTIC_SPHERICAL = 2
SDL_HAPTIC_STEERING_AXIS = 3

SDL_HAPTIC_INFINITY = 4294967295

class SDL_HapticDirection(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint8),
        ("dir", ctypes.c_int32* 3)
    ]

class SDL_HapticConstant(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint32),
        ("delay", ctypes.c_uint16),
        ("button", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("level", ctypes.c_int16),
        ("attack_length", ctypes.c_uint16),
        ("attack_level", ctypes.c_uint16),
        ("fade_length", ctypes.c_uint16),
        ("fade_level", ctypes.c_uint16)
    ]

class SDL_HapticPeriodic(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint32),
        ("delay", ctypes.c_uint16),
        ("button", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("period", ctypes.c_uint16),
        ("magnitude", ctypes.c_int16),
        ("offset", ctypes.c_int16),
        ("phase", ctypes.c_uint16),
        ("attack_length", ctypes.c_uint16),
        ("attack_level", ctypes.c_uint16),
        ("fade_length", ctypes.c_uint16),
        ("fade_level", ctypes.c_uint16)
    ]

class SDL_HapticCondition(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint32),
        ("delay", ctypes.c_uint16),
        ("button", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("right_sat", ctypes.c_uint16* 3),
        ("left_sat", ctypes.c_uint16* 3),
        ("right_coeff", ctypes.c_int16* 3),
        ("left_coeff", ctypes.c_int16* 3),
        ("deadband", ctypes.c_uint16* 3),
        ("center", ctypes.c_int16* 3)
    ]

class SDL_HapticRamp(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint32),
        ("delay", ctypes.c_uint16),
        ("button", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("start", ctypes.c_int16),
        ("end", ctypes.c_int16),
        ("attack_length", ctypes.c_uint16),
        ("attack_level", ctypes.c_uint16),
        ("fade_length", ctypes.c_uint16),
        ("fade_level", ctypes.c_uint16)
    ]

class SDL_HapticLeftRight(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("large_magnitude", ctypes.c_uint16),
        ("small_magnitude", ctypes.c_uint16)
    ]

class SDL_HapticCustom(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("direction", SDL_HapticDirection),
        ("length", ctypes.c_uint32),
        ("delay", ctypes.c_uint16),
        ("button", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("channels", ctypes.c_uint8),
        ("period", ctypes.c_uint16),
        ("samples", ctypes.c_uint16),
        ("data", SDL_POINTER[ctypes.c_uint16]),
        ("attack_length", ctypes.c_uint16),
        ("attack_level", ctypes.c_uint16),
        ("fade_length", ctypes.c_uint16),
        ("fade_level", ctypes.c_uint16)
    ]

class SDL_HapticEffect(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_uint16),
        ("constant", SDL_HapticConstant),
        ("periodic", SDL_HapticPeriodic),
        ("condition", SDL_HapticCondition),
        ("ramp", SDL_HapticRamp),
        ("leftright", SDL_HapticLeftRight),
        ("custom", SDL_HapticCustom)
    ]

SDL_HapticID: typing.TypeAlias = SDL_TYPE["SDL_HapticID", ctypes.c_uint32]

SDL_GetHaptics: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHaptics", SDL_POINTER[SDL_HapticID], [SDL_POINTER[ctypes.c_int]]]
SDL_GetHapticNameForID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticNameForID", ctypes.c_char_p, [SDL_HapticID]]
SDL_OpenHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_OpenHaptic", SDL_POINTER[SDL_Haptic], [SDL_HapticID]]
SDL_GetHapticFromID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticFromID", SDL_POINTER[SDL_Haptic], [SDL_HapticID]]
SDL_GetHapticID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticID", SDL_HapticID, [SDL_POINTER[SDL_Haptic]]]
SDL_GetHapticName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticName", ctypes.c_char_p, [SDL_POINTER[SDL_Haptic]]]
SDL_IsMouseHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_IsMouseHaptic", ctypes.c_bool, []]
SDL_OpenHapticFromMouse: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_OpenHapticFromMouse", SDL_POINTER[SDL_Haptic], []]
SDL_IsJoystickHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_IsJoystickHaptic", ctypes.c_bool, [SDL_POINTER[SDL_Joystick]]]
SDL_OpenHapticFromJoystick: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_OpenHapticFromJoystick", SDL_POINTER[SDL_Haptic], [SDL_POINTER[SDL_Joystick]]]
SDL_CloseHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CloseHaptic", None, [SDL_POINTER[SDL_Haptic]]]
SDL_GetMaxHapticEffects: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetMaxHapticEffects", ctypes.c_int, [SDL_POINTER[SDL_Haptic]]]
SDL_GetMaxHapticEffectsPlaying: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetMaxHapticEffectsPlaying", ctypes.c_int, [SDL_POINTER[SDL_Haptic]]]
SDL_GetHapticFeatures: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticFeatures", ctypes.c_uint32, [SDL_POINTER[SDL_Haptic]]]
SDL_GetNumHapticAxes: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetNumHapticAxes", ctypes.c_int, [SDL_POINTER[SDL_Haptic]]]
SDL_HapticEffectSupported: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_HapticEffectSupported", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], SDL_POINTER[SDL_HapticEffect]]]
SDL_CreateHapticEffect: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CreateHapticEffect", ctypes.c_int, [SDL_POINTER[SDL_Haptic], SDL_POINTER[SDL_HapticEffect]]]
SDL_UpdateHapticEffect: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UpdateHapticEffect", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int, SDL_POINTER[SDL_HapticEffect]]]
SDL_RunHapticEffect: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_RunHapticEffect", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int, ctypes.c_uint32]]
SDL_StopHapticEffect: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StopHapticEffect", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int]]
SDL_DestroyHapticEffect: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DestroyHapticEffect", None, [SDL_POINTER[SDL_Haptic], ctypes.c_int]]
SDL_GetHapticEffectStatus: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHapticEffectStatus", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int]]
SDL_SetHapticGain: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetHapticGain", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int]]
SDL_SetHapticAutocenter: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetHapticAutocenter", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_int]]
SDL_PauseHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_PauseHaptic", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]
SDL_ResumeHaptic: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ResumeHaptic", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]
SDL_StopHapticEffects: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StopHapticEffects", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]
SDL_HapticRumbleSupported: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_HapticRumbleSupported", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]
SDL_InitHapticRumble: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_InitHapticRumble", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]
SDL_PlayHapticRumble: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_PlayHapticRumble", ctypes.c_bool, [SDL_POINTER[SDL_Haptic], ctypes.c_float, ctypes.c_uint32]]
SDL_StopHapticRumble: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_StopHapticRumble", ctypes.c_bool, [SDL_POINTER[SDL_Haptic]]]