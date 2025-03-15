from .__init__ import ctypes, typing, abc, SDL_POINTER, SDL_FUNC_TYPE, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_MIXER_BINARY, SDL_ENUM

from .SDL_iostream import SDL_IOStream
from .SDL_audio import SDL_AudioDeviceID, SDL_AudioSpec, SDL_AudioFormat, SDL_AUDIO_S16
from .SDL_version import SDL_VERSIONNUM

SDL_SET_CURRENT_BINARY(SDL_MIXER_BINARY)

SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_MICRO_VERSION = 3, 0, 0

SDL_MIXER_VERSION = \
    SDL_VERSIONNUM(SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_MICRO_VERSION)

SDL_MIXER_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_MIXER_MAJOR_VERSION >= x) and \
    (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION >= y) and \
    (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION > y or SDL_MIXER_MICRO_VERSION >= z)

Mix_Version: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Version", ctypes.c_int, []]

MIX_InitFlags: typing.TypeAlias = SDL_TYPE["MIX_InitFlags", ctypes.c_uint32]

MIX_INIT_FLAC = 0x00000001
MIX_INIT_MOD = 0x00000002
MIX_INIT_MP3 = 0x00000008
MIX_INIT_OGG = 0x00000010
MIX_INIT_MID = 0x00000020
MIX_INIT_OPUS = 0x00000040
MIX_INIT_WAVPACK = 0x00000080

Mix_Init: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Init", MIX_InitFlags, [MIX_InitFlags]]
Mix_Quit: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Quit", None, []]

MIX_CHANNELS = 8

MIX_DEFAULT_FREQUENCY = 44100
MIX_DEFAULT_FORMAT = SDL_AUDIO_S16
MIX_DEFAULT_CHANNELS = 2
MIX_MAX_VOLUME = 128

class Mix_Chunk(ctypes.Structure):
    _fields_ = [
        ("allocated", ctypes.c_int),
        ("abuf", SDL_POINTER[ctypes.c_uint8]),
        ("alen", ctypes.c_uint32),
        ("volume", ctypes.c_uint8)
    ]

Mix_Fading: typing.TypeAlias = SDL_TYPE["Mix_Fading", SDL_ENUM]

MIX_NO_FADING, MIX_FADING_OUT, MIX_FADING_IN = range(3)

Mix_MusicType: typing.TypeAlias = SDL_TYPE["Mix_MusicType", SDL_ENUM]

MUS_NONE, MUS_WAV, MUS_MOD, MUS_MID, MUS_OGG, MUS_MP3, MUS_MP3_MAD_UNUSED, \
    MUS_FLAC, MUS_MODPLUG_UNUSED, MUS_OPUS, MUS_WAVPACK, MUS_GME = range(12)

class Mix_Music(ctypes.c_void_p):
    ...

Mix_OpenAudio: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_OpenAudio", ctypes.c_bool, [SDL_AudioDeviceID, SDL_POINTER[SDL_AudioSpec]]]
Mix_PauseAudio: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PauseAudio", None, [ctypes.c_int]]
Mix_QuerySpec: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_QuerySpec", ctypes.c_bool, [SDL_POINTER[ctypes.c_int], SDL_POINTER[SDL_AudioFormat], SDL_POINTER[ctypes.c_int]]]
Mix_AllocateChannels: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_AllocateChannels", ctypes.c_int, [ctypes.c_int]]
Mix_LoadWAV_IO: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_LoadWAV_IO", SDL_POINTER[Mix_Chunk], [SDL_POINTER[SDL_IOStream], ctypes.c_bool]]
Mix_LoadWAV: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_LoadWAV", SDL_POINTER[Mix_Chunk], [ctypes.c_char_p]]
Mix_LoadMUS: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_LoadMUS", SDL_POINTER[Mix_Music], [ctypes.c_char_p]]
Mix_LoadMUS_IO: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_LoadMUS_IO", SDL_POINTER[Mix_Music], [SDL_POINTER[SDL_IOStream], ctypes.c_bool]]
Mix_LoadMUSType_IO: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_LoadMUSType_IO", SDL_POINTER[Mix_Music], [SDL_POINTER[SDL_IOStream], Mix_MusicType, ctypes.c_bool]]
Mix_QuickLoad_WAV: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_QuickLoad_WAV", SDL_POINTER[Mix_Chunk], [SDL_POINTER[ctypes.c_uint8]]]
Mix_QuickLoad_RAW: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_QuickLoad_RAW", SDL_POINTER[Mix_Chunk], [SDL_POINTER[ctypes.c_uint8], ctypes.c_uint32]]
Mix_FreeChunk: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FreeChunk", None, [SDL_POINTER[Mix_Chunk]]]
Mix_FreeMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FreeMusic", None, [SDL_POINTER[Mix_Music]]]
Mix_GetNumChunkDecoders: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetNumChunkDecoders", ctypes.c_int, []]
Mix_GetChunkDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetChunkDecoder", ctypes.c_char_p, [ctypes.c_int]]
Mix_HasChunkDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HasChunkDecoder", ctypes.c_bool, [ctypes.c_char_p]]
Mix_GetNumMusicDecoders: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetNumMusicDecoders", ctypes.c_int, []]
Mix_GetMusicDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicDecoder", ctypes.c_char_p, [ctypes.c_int]]
Mix_HasMusicDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HasMusicDecoder", ctypes.c_bool, [ctypes.c_char_p]]
Mix_GetMusicType: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicType", Mix_MusicType, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicTitle: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicTitle", ctypes.c_char_p, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicTitleTag: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicTitleTag", ctypes.c_char_p, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicArtistTag: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicArtistTag", ctypes.c_char_p, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicAlbumTag: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicAlbumTag", ctypes.c_char_p, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicCopyrightTag: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicCopyrightTag", ctypes.c_char_p, [SDL_POINTER[Mix_Music]]]

Mix_MixCallback: typing.TypeAlias = SDL_FUNC_TYPE["Mix_MixCallback", None, [ctypes.c_void_p, SDL_POINTER[ctypes.c_uint8], ctypes.c_int]]

Mix_SetPostMix: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetPostMix", None, [Mix_MixCallback, ctypes.c_void_p]]
Mix_HookMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HookMusic", None, [Mix_MixCallback, ctypes.c_void_p]]

Mix_MusicFinishedCallback: typing.TypeAlias = SDL_FUNC_TYPE["Mix_MusicFinishedCallback", None, []]

Mix_HookMusicFinished: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HookMusicFinished", None, [Mix_MusicFinishedCallback]]
Mix_GetMusicHookData: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicHookData", ctypes.c_void_p, []]

Mix_ChannelFinishedCallback: typing.TypeAlias = SDL_FUNC_TYPE["Mix_ChannelFinishedCallback", None, [ctypes.c_int]]

Mix_ChannelFinished: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ChannelFinished", None, [Mix_ChannelFinishedCallback]]

MIX_CHANNEL_POST = -2

Mix_EffectFunc_t: typing.TypeAlias = SDL_FUNC_TYPE["Mix_EffectFunc_t", None, [ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]]
Mix_EffectDone_t: typing.TypeAlias = SDL_FUNC_TYPE["Mix_EffectDone_t", None, [ctypes.c_int, ctypes.c_void_p]]

Mix_RegisterEffect: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_RegisterEffect", ctypes.c_bool, [ctypes.c_int, Mix_EffectFunc_t, Mix_EffectDone_t, ctypes.c_void_p]]
Mix_UnregisterEffect: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_UnregisterEffect", ctypes.c_bool, [ctypes.c_int, Mix_EffectFunc_t]]
Mix_UnregisterAllEffects: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_UnregisterAllEffects", ctypes.c_bool, [ctypes.c_int]]

MIX_EFFECTSMAXSPEED = "MIX_EFFECTSMAXSPEED".encode()

Mix_SetPanning: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetPanning", ctypes.c_bool, [ctypes.c_int, ctypes.c_uint8, ctypes.c_uint8]]
Mix_SetPosition: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetPosition", ctypes.c_bool, [ctypes.c_int, ctypes.c_int16, ctypes.c_uint8]]
Mix_SetDistance: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetDistance", ctypes.c_bool, [ctypes.c_int, ctypes.c_uint8]]
Mix_SetReverseStereo: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetReverseStereo", ctypes.c_bool, [ctypes.c_int, ctypes.c_int]]
Mix_ReserveChannels: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ReserveChannels", ctypes.c_int, [ctypes.c_int]]
Mix_GroupChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupChannel", ctypes.c_bool, [ctypes.c_int, ctypes.c_int]]
Mix_GroupChannels: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupChannels", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.c_int]]
Mix_GroupAvailable: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupAvailable", ctypes.c_int, [ctypes.c_int]]
Mix_GroupCount: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupCount", ctypes.c_int, [ctypes.c_int]]
Mix_GroupOldest: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupOldest", ctypes.c_int, [ctypes.c_int]]
Mix_GroupNewer: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GroupNewer", ctypes.c_int, [ctypes.c_int]]
Mix_PlayChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PlayChannel", ctypes.c_int, [ctypes.c_int, SDL_POINTER[Mix_Chunk], ctypes.c_int]]
Mix_PlayChannelTimed: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PlayChannelTimed", ctypes.c_int, [ctypes.c_int, SDL_POINTER[Mix_Chunk], ctypes.c_int, ctypes.c_int]]
Mix_PlayMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PlayMusic", ctypes.c_bool, [SDL_POINTER[Mix_Music], ctypes.c_int]]    
Mix_FadeInMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeInMusic", ctypes.c_bool, [SDL_POINTER[Mix_Music], ctypes.c_int, ctypes.c_int]]
Mix_FadeInMusicPos: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeInMusicPos", ctypes.c_bool, [SDL_POINTER[Mix_Music], ctypes.c_int, ctypes.c_int, ctypes.c_double]]
Mix_FadeInChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeInChannel", ctypes.c_int, [ctypes.c_int, SDL_POINTER[Mix_Chunk], ctypes.c_int, ctypes.c_int]]
Mix_FadeInChannelTimed: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeInChannelTimed", ctypes.c_int, [ctypes.c_int, SDL_POINTER[Mix_Chunk], ctypes.c_int, ctypes.c_int, ctypes.c_int]]
Mix_Volume: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Volume", ctypes.c_int, [ctypes.c_int, ctypes.c_int]]
Mix_VolumeChunk: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_VolumeChunk", ctypes.c_int, [SDL_POINTER[Mix_Chunk], ctypes.c_int]]
Mix_VolumeMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_VolumeMusic", ctypes.c_int, [ctypes.c_int]]
Mix_GetMusicVolume: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicVolume", ctypes.c_int, [SDL_POINTER[Mix_Music]]]
Mix_MasterVolume: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_MasterVolume", ctypes.c_int, [ctypes.c_int]]
Mix_HaltChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HaltChannel", None, [ctypes.c_int]]
Mix_HaltGroup: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HaltGroup", None, [ctypes.c_int]]
Mix_HaltMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_HaltMusic", None, []]
Mix_ExpireChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ExpireChannel", ctypes.c_int, [ctypes.c_int, ctypes.c_int]]
Mix_FadeOutChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeOutChannel", ctypes.c_int, [ctypes.c_int, ctypes.c_int]]
Mix_FadeOutGroup: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeOutGroup", ctypes.c_int, [ctypes.c_int, ctypes.c_int]]
Mix_FadeOutMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadeOutMusic", ctypes.c_bool, [ctypes.c_int]]
Mix_FadingMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadingMusic", Mix_Fading, []]
Mix_FadingChannel: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_FadingChannel", Mix_Fading, [ctypes.c_int]]
Mix_Pause: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Pause", None, [ctypes.c_int]]
Mix_PauseGroup: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PauseGroup", None, [ctypes.c_int]]
Mix_Resume: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Resume", None, [ctypes.c_int]]
Mix_ResumeGroup: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ResumeGroup", None, [ctypes.c_int]]
Mix_Paused: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Paused", ctypes.c_int, [ctypes.c_int]]
Mix_PauseMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PauseMusic", None, []]
Mix_ResumeMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ResumeMusic", None, []]
Mix_RewindMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_RewindMusic", None, []]
Mix_PausedMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PausedMusic", ctypes.c_bool, []]
Mix_ModMusicJumpToOrder: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_ModMusicJumpToOrder", ctypes.c_bool, [ctypes.c_int]]
Mix_StartTrack: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_StartTrack", ctypes.c_bool, [SDL_POINTER[Mix_Music], ctypes.c_int]]
Mix_GetNumTracks: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetNumTracks", ctypes.c_int, [SDL_POINTER[Mix_Music]]]
Mix_SetMusicPosition: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetMusicPosition", ctypes.c_bool, [ctypes.c_double]]
Mix_GetMusicPosition: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicPosition", ctypes.c_double, [SDL_POINTER[Mix_Music]]]
Mix_MusicDuration: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_MusicDuration", ctypes.c_double, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicLoopStartTime: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicLoopStartTime", ctypes.c_double, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicLoopEndTime: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicLoopEndTime", ctypes.c_double, [SDL_POINTER[Mix_Music]]]
Mix_GetMusicLoopLengthTime: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetMusicLoopLengthTime", ctypes.c_double, [SDL_POINTER[Mix_Music]]]
Mix_Playing: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_Playing", ctypes.c_int, [ctypes.c_int]]
Mix_PlayingMusic: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_PlayingMusic", ctypes.c_bool, []]
Mix_SetSoundFonts: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetSoundFonts", ctypes.c_bool, [ctypes.c_char_p]]
Mix_GetSoundFonts: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetSoundFonts", ctypes.c_char_p, []]

Mix_EachSoundFontCallback: typing.TypeAlias = SDL_FUNC_TYPE["Mix_EachSoundFontCallback", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_void_p]]

Mix_EachSoundFont: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_EachSoundFont", ctypes.c_bool, [Mix_EachSoundFontCallback, ctypes.c_void_p]]
Mix_SetTimidityCfg: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_SetTimidityCfg", ctypes.c_bool, [ctypes.c_char_p]]
Mix_GetTimidityCfg: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetTimidityCfg", ctypes.c_char_p, []]
Mix_GetChunk: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_GetChunk", SDL_POINTER[Mix_Chunk], [ctypes.c_int]]
Mix_CloseAudio: abc.Callable[..., typing.Any] = SDL_FUNC["Mix_CloseAudio", None, []]