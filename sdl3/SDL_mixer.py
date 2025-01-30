from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_MIXER_BINARY

from .SDL_iostream import SDL_IOStream
from .SDL_audio import SDL_AudioDeviceID, SDL_AudioSpec, SDL_AudioFormat, SDL_AUDIO_S16
from .SDL_version import SDL_VERSIONNUM

SDL_SET_CURRENT_BINARY(SDL_MIXER_BINARY)

SDL_MIXER_MAJOR_VERSION = 3
SDL_MIXER_MINOR_VERSION = 0
SDL_MIXER_MICRO_VERSION = 0

SDL_MIXER_VERSION = \
    SDL_VERSIONNUM(SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_MICRO_VERSION)

SDL_MIXER_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_MIXER_MAJOR_VERSION >= x) and \
    (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION >= y) and \
    (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION > y or SDL_MIXER_MICRO_VERSION >= z)

SDL_FUNC("Mix_Version", ctypes.c_int)

MIX_InitFlags = ctypes.c_uint32

MIX_INIT_FLAC = 0x00000001
MIX_INIT_MOD = 0x00000002
MIX_INIT_MP3 = 0x00000008
MIX_INIT_OGG = 0x00000010
MIX_INIT_MID = 0x00000020
MIX_INIT_OPUS = 0x00000040
MIX_INIT_WAVPACK = 0x00000080

SDL_FUNC("Mix_Init", MIX_InitFlags, MIX_InitFlags)
SDL_FUNC("Mix_Quit", None)

MIX_CHANNELS = 8

MIX_DEFAULT_FREQUENCY = 44100
MIX_DEFAULT_FORMAT = SDL_AUDIO_S16
MIX_DEFAULT_CHANNELS = 2
MIX_MAX_VOLUME = 128 

class Mix_Chunk(ctypes.Structure):
    _fields_ = [
        ("allocated", ctypes.c_int),
        ("abuf", ctypes.POINTER(ctypes.c_uint8)),
        ("alen", ctypes.c_uint32),
        ("volume", ctypes.c_uint8)
    ]

Mix_Fading = ctypes.c_int

MIX_NO_FADING = 0
MIX_FADING_OUT = 1
MIX_FADING_IN = 2

Mix_MusicType = ctypes.c_int

MUS_NONE = 0
MUS_WAV = 1
MUS_MOD = 2
MUS_MID = 3
MUS_OGG = 4
MUS_MP3 = 5
MUS_MP3_MAD_UNUSED = 6
MUS_FLAC = 7
MUS_MODPLUG_UNUSED = 8
MUS_OPUS = 9
MUS_WAVPACK = 10
MUS_GME = 11

class Mix_Music(ctypes.c_void_p):
    ...

SDL_FUNC("Mix_OpenAudio", ctypes.c_bool, SDL_AudioDeviceID, ctypes.POINTER(SDL_AudioSpec))
SDL_FUNC("Mix_PauseAudio", None, ctypes.c_int)
SDL_FUNC("Mix_QuerySpec", ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(SDL_AudioFormat), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("Mix_AllocateChannels", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_LoadWAV_IO", ctypes.POINTER(Mix_Chunk), ctypes.POINTER(SDL_IOStream), ctypes.c_bool)
SDL_FUNC("Mix_LoadWAV", ctypes.POINTER(Mix_Chunk), ctypes.c_char_p)
SDL_FUNC("Mix_LoadMUS", ctypes.POINTER(Mix_Music), ctypes.c_char_p)
SDL_FUNC("Mix_LoadMUS_IO", ctypes.POINTER(Mix_Music), ctypes.POINTER(SDL_IOStream), ctypes.c_bool)
SDL_FUNC("Mix_LoadMUSType_IO", ctypes.POINTER(Mix_Music), ctypes.POINTER(SDL_IOStream), Mix_MusicType, ctypes.c_bool)
SDL_FUNC("Mix_QuickLoad_WAV", ctypes.POINTER(Mix_Chunk), ctypes.POINTER(ctypes.c_uint8))
SDL_FUNC("Mix_QuickLoad_RAW", ctypes.POINTER(Mix_Chunk), ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32)
SDL_FUNC("Mix_FreeChunk", None, ctypes.POINTER(Mix_Chunk))
SDL_FUNC("Mix_FreeMusic", None, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetNumChunkDecoders", ctypes.c_int)
SDL_FUNC("Mix_GetChunkDecoder", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("Mix_HasChunkDecoder", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("Mix_GetNumMusicDecoders", ctypes.c_int)
SDL_FUNC("Mix_GetMusicDecoder", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("Mix_HasMusicDecoder", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("Mix_GetMusicType", Mix_MusicType, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicTitle", ctypes.c_char_p, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicTitleTag", ctypes.c_char_p, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicArtistTag", ctypes.c_char_p, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicAlbumTag", ctypes.c_char_p, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicCopyrightTag", ctypes.c_char_p, ctypes.POINTER(Mix_Music))

Mix_MixCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int)

SDL_FUNC("Mix_SetPostMix", None, Mix_MixCallback, ctypes.c_void_p)
SDL_FUNC("Mix_HookMusic", None, Mix_MixCallback, ctypes.c_void_p)

Mix_MusicFinishedCallback = ctypes.CFUNCTYPE(None)

SDL_FUNC("Mix_HookMusicFinished", None, Mix_MusicFinishedCallback)
SDL_FUNC("Mix_GetMusicHookData", ctypes.c_void_p)

Mix_ChannelFinishedCallback = ctypes.CFUNCTYPE(None, ctypes.c_int)

SDL_FUNC("Mix_ChannelFinished", None, Mix_ChannelFinishedCallback)

MIX_CHANNEL_POST = -2

Mix_EffectFunc_t = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
Mix_EffectDone_t = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p)

SDL_FUNC("Mix_RegisterEffect", ctypes.c_bool, ctypes.c_int, Mix_EffectFunc_t, Mix_EffectDone_t, ctypes.c_void_p)
SDL_FUNC("Mix_UnregisterEffect", ctypes.c_bool, ctypes.c_int, Mix_EffectFunc_t)
SDL_FUNC("Mix_UnregisterAllEffects", ctypes.c_bool, ctypes.c_int)

MIX_EFFECTSMAXSPEED = "MIX_EFFECTSMAXSPEED".encode()

SDL_FUNC("Mix_SetPanning", ctypes.c_bool, ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8)
SDL_FUNC("Mix_SetPosition", ctypes.c_bool, ctypes.c_int, ctypes.c_int16, ctypes.c_uint8)
SDL_FUNC("Mix_SetDistance", ctypes.c_bool, ctypes.c_int, ctypes.c_uint8)
SDL_FUNC("Mix_SetReverseStereo", ctypes.c_bool, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_ReserveChannels", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupChannel", ctypes.c_bool, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupChannels", ctypes.c_bool, ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupAvailable", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupCount", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupOldest", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GroupNewer", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_PlayChannel", ctypes.c_int, ctypes.c_int, ctypes.POINTER(Mix_Chunk), ctypes.c_int)
SDL_FUNC("Mix_PlayChannelTimed", ctypes.c_int, ctypes.c_int, ctypes.POINTER(Mix_Chunk), ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_PlayMusic", ctypes.c_bool, ctypes.POINTER(Mix_Music), ctypes.c_int)    
SDL_FUNC("Mix_FadeInMusic", ctypes.c_bool, ctypes.POINTER(Mix_Music), ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_FadeInMusicPos", ctypes.c_bool, ctypes.POINTER(Mix_Music), ctypes.c_int, ctypes.c_int, ctypes.c_double)
SDL_FUNC("Mix_FadeInChannel", ctypes.c_int, ctypes.c_int, ctypes.POINTER(Mix_Chunk), ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_FadeInChannelTimed", ctypes.c_int, ctypes.c_int, ctypes.POINTER(Mix_Chunk), ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_Volume", ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_VolumeChunk", ctypes.c_int, ctypes.POINTER(Mix_Chunk), ctypes.c_int)
SDL_FUNC("Mix_VolumeMusic", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_GetMusicVolume", ctypes.c_int, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_MasterVolume", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_HaltChannel", None, ctypes.c_int)
SDL_FUNC("Mix_HaltGroup", None, ctypes.c_int)
SDL_FUNC("Mix_HaltMusic", None)
SDL_FUNC("Mix_ExpireChannel", ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_FadeOutChannel", ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_FadeOutGroup", ctypes.c_int, ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_FadeOutMusic", ctypes.c_bool, ctypes.c_int)
SDL_FUNC("Mix_FadingMusic", Mix_Fading)
SDL_FUNC("Mix_FadingChannel", Mix_Fading, ctypes.c_int)
SDL_FUNC("Mix_Pause", None, ctypes.c_int)
SDL_FUNC("Mix_PauseGroup", None, ctypes.c_int)
SDL_FUNC("Mix_Resume", None, ctypes.c_int)
SDL_FUNC("Mix_ResumeGroup", None, ctypes.c_int)
SDL_FUNC("Mix_Paused", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_PauseMusic", None)
SDL_FUNC("Mix_ResumeMusic", None)
SDL_FUNC("Mix_RewindMusic", None)
SDL_FUNC("Mix_PausedMusic", ctypes.c_bool)
SDL_FUNC("Mix_ModMusicJumpToOrder", ctypes.c_bool, ctypes.c_int)
SDL_FUNC("Mix_StartTrack", ctypes.c_bool, ctypes.POINTER(Mix_Music), ctypes.c_int)
SDL_FUNC("Mix_GetNumTracks", ctypes.c_int, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_SetMusicPosition", ctypes.c_bool, ctypes.c_double)
SDL_FUNC("Mix_GetMusicPosition", ctypes.c_double, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_MusicDuration", ctypes.c_double, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicLoopStartTime", ctypes.c_double, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicLoopEndTime", ctypes.c_double, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_GetMusicLoopLengthTime", ctypes.c_double, ctypes.POINTER(Mix_Music))
SDL_FUNC("Mix_Playing", ctypes.c_int, ctypes.c_int)
SDL_FUNC("Mix_PlayingMusic", ctypes.c_bool)
SDL_FUNC("Mix_SetSoundFonts", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("Mix_GetSoundFonts", ctypes.c_char_p)

Mix_EachSoundFontCallback = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_char_p, ctypes.c_void_p)

SDL_FUNC("Mix_EachSoundFont", ctypes.c_bool, Mix_EachSoundFontCallback, ctypes.c_void_p)
SDL_FUNC("Mix_SetTimidityCfg", ctypes.c_bool, ctypes.c_char_p)
SDL_FUNC("Mix_GetTimidityCfg", ctypes.c_char_p)
SDL_FUNC("Mix_GetChunk", ctypes.POINTER(Mix_Chunk), ctypes.c_int)
SDL_FUNC("Mix_CloseAudio", None)