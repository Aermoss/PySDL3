from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_endian import SDL_BYTEORDER, SDL_LIL_ENDIAN
from .SDL_properties import SDL_PropertiesID
from .SDL_iostream import SDL_IOStream

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_AUDIO_MASK_BITSIZE = 0xFF
SDL_AUDIO_MASK_FLOAT = 1 << 8
SDL_AUDIO_MASK_BIG_ENDIAN = 1 << 12
SDL_AUDIO_MASK_SIGNED = 1 << 15

SDL_DEFINE_AUDIO_FORMAT = lambda signed, bigendian, _float, size: \
    (signed << 15) | (bigendian << 12) | (_float << 8) | (size & SDL_AUDIO_MASK_BITSIZE)

SDL_AudioFormat = ctypes.c_int

SDL_AUDIO_UNKNOWN = 0x0000
SDL_AUDIO_U8 = 0x0008
SDL_AUDIO_S8 = 0x8008
SDL_AUDIO_S16LE = 0x8010
SDL_AUDIO_S16BE = 0x9010
SDL_AUDIO_S32LE = 0x8020
SDL_AUDIO_S32BE = 0x9020
SDL_AUDIO_F32LE = 0x8120
SDL_AUDIO_F32BE = 0x9120

if SDL_BYTEORDER == SDL_LIL_ENDIAN:
    SDL_AUDIO_S16 = SDL_AUDIO_S16LE
    SDL_AUDIO_S32 = SDL_AUDIO_S32LE
    SDL_AUDIO_F32 = SDL_AUDIO_F32LE

else:
    SDL_AUDIO_S16 = SDL_AUDIO_S16BE
    SDL_AUDIO_S32 = SDL_AUDIO_S32BE
    SDL_AUDIO_F32 = SDL_AUDIO_F32BE

SDL_AUDIO_BITSIZE = lambda x: x & SDL_AUDIO_MASK_BITSIZE
SDL_AUDIO_BYTESIZE = lambda x: SDL_AUDIO_BITSIZE(x) / 8

SDL_AUDIO_ISFLOAT = lambda x: x & SDL_AUDIO_MASK_FLOAT
SDL_AUDIO_ISBIGENDIAN = lambda x: x & SDL_AUDIO_MASK_BIG_ENDIAN
SDL_AUDIO_ISLITTLEENDIAN = lambda x: not SDL_AUDIO_ISBIGENDIAN(x)
SDL_AUDIO_ISSIGNED = lambda x: x & SDL_AUDIO_MASK_SIGNED
SDL_AUDIO_ISINT = lambda x: not SDL_AUDIO_ISFLOAT(x)
SDL_AUDIO_ISUNSIGNED = lambda x: not SDL_AUDIO_ISSIGNED(x)

SDL_AudioDeviceID = ctypes.c_uint32

SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK = 0xFFFFFFFF
SDL_AUDIO_DEVICE_DEFAULT_RECORDING = 0xFFFFFFFE

class SDL_AudioSpec(ctypes.Structure):
    _fields_ = [
        ("format", SDL_AudioFormat),
        ("channels", ctypes.c_int),
        ("freq", ctypes.c_int)
    ]

SDL_AUDIO_FRAMESIZE = lambda x: SDL_AUDIO_BYTESIZE(x.format) * x.channels

class SDL_AudioStream(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_GetNumAudioDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetAudioDriver", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_GetCurrentAudioDriver", ctypes.c_char_p)

SDL_FUNC("SDL_GetAudioPlaybackDevices", ctypes.POINTER(SDL_AudioDeviceID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetAudioRecordingDevices", ctypes.POINTER(SDL_AudioDeviceID), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_GetAudioDeviceName", ctypes.c_char_p, SDL_AudioDeviceID)
SDL_FUNC("SDL_GetAudioDeviceFormat", ctypes.c_bool, SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetAudioDeviceChannelMap", ctypes.POINTER(ctypes.c_int), SDL_AudioDeviceID, ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_OpenAudioDevice", SDL_AudioDeviceID, SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioSpec))
SDL_FUNC("SDL_IsAudioDevicePhysical", ctypes.c_bool, SDL_AudioDeviceID)
SDL_FUNC("SDL_IsAudioDevicePlayback", ctypes.c_bool, SDL_AudioDeviceID)
SDL_FUNC("SDL_PauseAudioDevice", ctypes.c_bool, SDL_AudioDeviceID)
SDL_FUNC("SDL_ResumeAudioDevice", ctypes.c_bool, SDL_AudioDeviceID)
SDL_FUNC("SDL_AudioDevicePaused", ctypes.c_bool, SDL_AudioDeviceID)
SDL_FUNC("SDL_GetAudioDeviceGain", ctypes.c_float, SDL_AudioDeviceID)
SDL_FUNC("SDL_SetAudioDeviceGain", ctypes.c_bool, SDL_AudioDeviceID, ctypes.c_float)
SDL_FUNC("SDL_CloseAudioDevice", None, SDL_AudioDeviceID)

SDL_FUNC("SDL_BindAudioStreams", ctypes.c_bool, SDL_AudioDeviceID, ctypes.POINTER(ctypes.POINTER(SDL_AudioStream)), ctypes.c_int)
SDL_FUNC("SDL_BindAudioStream", ctypes.c_bool, SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_UnbindAudioStreams", None, ctypes.POINTER(ctypes.POINTER(SDL_AudioStream)), ctypes.c_int)
SDL_FUNC("SDL_UnbindAudioStream", None, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_GetAudioStreamDevice", SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_CreateAudioStream", ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(SDL_AudioSpec))
SDL_FUNC("SDL_GetAudioStreamProperties", SDL_PropertiesID, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_GetAudioStreamFormat", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(SDL_AudioSpec))
SDL_FUNC("SDL_SetAudioStreamFormat", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(SDL_AudioSpec))
SDL_FUNC("SDL_GetAudioStreamFrequencyRatio", ctypes.c_float, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_SetAudioStreamFrequencyRatio", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.c_float)
SDL_FUNC("SDL_GetAudioStreamGain", ctypes.c_float, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_SetAudioStreamGain", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.c_float)
SDL_FUNC("SDL_GetAudioStreamInputChannelMap", ctypes.POINTER(ctypes.c_int), ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetAudioStreamOutputChannelMap", ctypes.POINTER(ctypes.c_int), ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_SetAudioStreamInputChannelMap", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(ctypes.c_int), ctypes.c_int)
SDL_FUNC("SDL_SetAudioStreamOutputChannelMap", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.POINTER(ctypes.c_int), ctypes.c_int)
SDL_FUNC("SDL_PutAudioStreamData", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_GetAudioStreamData", ctypes.c_int, ctypes.POINTER(SDL_AudioStream), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDL_GetAudioStreamAvailable", ctypes.c_int, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_GetAudioStreamQueued", ctypes.c_int, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_FlushAudioStream", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_ClearAudioStream", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_PauseAudioStreamDevice", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_ResumeAudioStreamDevice", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_AudioStreamDevicePaused", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_LockAudioStream", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_UnlockAudioStream", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream))

SDL_AudioStreamCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(SDL_AudioStream), ctypes.c_int, ctypes.c_int)

SDL_FUNC("SDL_SetAudioStreamGetCallback", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), SDL_AudioStreamCallback, ctypes.c_void_p)
SDL_FUNC("SDL_SetAudioStreamPutCallback", ctypes.c_bool, ctypes.POINTER(SDL_AudioStream), SDL_AudioStreamCallback, ctypes.c_void_p)
SDL_FUNC("SDL_DestroyAudioStream", None, ctypes.POINTER(SDL_AudioStream))
SDL_FUNC("SDL_OpenAudioDeviceStream", ctypes.POINTER(SDL_AudioStream), SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioSpec), SDL_AudioStreamCallback, ctypes.c_void_p)

SDL_AudioPostmixCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.c_float), ctypes.c_int)

SDL_FUNC("SDL_SetAudioPostmixCallback", ctypes.c_bool, SDL_AudioDeviceID, SDL_AudioPostmixCallback, ctypes.c_void_p)

SDL_FUNC("SDL_LoadWAV_IO", ctypes.c_bool, ctypes.POINTER(SDL_IOStream), ctypes.c_bool, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_LoadWAV", ctypes.c_bool, ctypes.c_char_p, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)), ctypes.POINTER(ctypes.c_uint32))
SDL_FUNC("SDL_MixAudio", ctypes.c_bool, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), SDL_AudioFormat, ctypes.c_uint32, ctypes.c_float)
SDL_FUNC("SDL_ConvertAudioSamples", ctypes.c_bool, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.c_uint8), ctypes.c_int, ctypes.POINTER(SDL_AudioSpec), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetAudioFormatName", ctypes.c_char_p, SDL_AudioFormat)
SDL_FUNC("SDL_GetSilenceValueForFormat", ctypes.c_int, SDL_AudioFormat)