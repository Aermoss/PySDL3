import ctypes, typing, collections.abc as abc

from . import  SDL_POINTER, SDL_FUNC, \
    SDL_FUNC_TYPE, SDL_MIXER_BINARY
from .SDL_iostream import SDL_IOStream
from .SDL_audio import SDL_AudioDeviceID, \
    SDL_AudioSpec, SDL_AudioStream
from .SDL_properties import SDL_PropertiesID
from .SDL_version import SDL_VERSIONNUM

class MIX_Mixer(ctypes.c_void_p):
    ...

class MIX_Audio(ctypes.c_void_p):
    ...

class MIX_Track(ctypes.c_void_p):
    ...

class MIX_Group(ctypes.c_void_p):
    ...

SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_MICRO_VERSION = 3, 1, 0
SDL_MIXER_VERSION: int = SDL_VERSIONNUM(SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_MICRO_VERSION)

SDL_MIXER_VERSION_ATLEAST: abc.Callable[[int, int, int], bool] = lambda x, y, z: \
    (SDL_MIXER_MAJOR_VERSION >= x) and (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION >= y) and \
        (SDL_MIXER_MAJOR_VERSION > x or SDL_MIXER_MINOR_VERSION > y or SDL_MIXER_MICRO_VERSION >= z)

MIX_Version: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_Version", ctypes.c_int, [], SDL_MIXER_BINARY]
MIX_Init: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_Init", ctypes.c_bool, [], SDL_MIXER_BINARY]
MIX_Quit: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_Quit", None, [], SDL_MIXER_BINARY]

MIX_GetNumAudioDecoders: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetNumAudioDecoders", ctypes.c_int, [], SDL_MIXER_BINARY]
MIX_GetAudioDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioDecoder", ctypes.c_char_p, [ctypes.c_int], SDL_MIXER_BINARY]
MIX_CreateMixerDevice: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateMixerDevice", SDL_POINTER[MIX_Mixer], [SDL_AudioDeviceID, SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_CreateMixer: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateMixer", SDL_POINTER[MIX_Mixer], [SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_DestroyMixer: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DestroyMixer", None, [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_GetMixerProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetMixerProperties", SDL_PropertiesID, [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]

MIX_PROP_MIXER_DEVICE_NUMBER: bytes = "SDL_mixer.mixer.device".encode()

MIX_GetMixerFormat: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetMixerFormat", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_LoadAudio_IO: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadAudio_IO", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], SDL_POINTER[SDL_IOStream], ctypes.c_bool, ctypes.c_bool], SDL_MIXER_BINARY]
MIX_LoadAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadAudio", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], ctypes.c_char_p, ctypes.c_bool], SDL_MIXER_BINARY]
MIX_LoadAudioWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadAudioWithProperties", SDL_POINTER[MIX_Audio], [SDL_PropertiesID], SDL_MIXER_BINARY]

MIX_PROP_AUDIO_LOAD_IOSTREAM_POINTER: bytes = "SDL_mixer.audio.load.iostream".encode()
MIX_PROP_AUDIO_LOAD_CLOSEIO_BOOLEAN: bytes = "SDL_mixer.audio.load.closeio".encode()
MIX_PROP_AUDIO_LOAD_PREDECODE_BOOLEAN: bytes = "SDL_mixer.audio.load.predecode".encode()
MIX_PROP_AUDIO_LOAD_PREFERRED_MIXER_POINTER: bytes = "SDL_mixer.audio.load.preferred_mixer".encode()
MIX_PROP_AUDIO_LOAD_SKIP_METADATA_TAGS_BOOLEAN: bytes = "SDL_mixer.audio.load.skip_metadata_tags".encode()
MIX_PROP_AUDIO_DECODER_STRING: bytes = "SDL_mixer.audio.decoder".encode()

MIX_LoadRawAudio_IO: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadRawAudio_IO", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], SDL_POINTER[SDL_IOStream], SDL_POINTER[SDL_AudioSpec], ctypes.c_bool], SDL_MIXER_BINARY]
MIX_LoadRawAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadRawAudio", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], ctypes.c_void_p, ctypes.c_size_t, SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_LoadRawAudioNoCopy: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_LoadRawAudioNoCopy", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], ctypes.c_void_p, ctypes.c_size_t, SDL_POINTER[SDL_AudioSpec], ctypes.c_bool], SDL_MIXER_BINARY]
MIX_CreateSineWaveAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateSineWaveAudio", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Mixer], ctypes.c_int, ctypes.c_float], SDL_MIXER_BINARY]
MIX_GetAudioProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioProperties", SDL_PropertiesID, [SDL_POINTER[MIX_Audio]], SDL_MIXER_BINARY]

MIX_PROP_METADATA_TITLE_STRING: bytes = "SDL_mixer.metadata.title".encode()
MIX_PROP_METADATA_ARTIST_STRING: bytes = "SDL_mixer.metadata.artist".encode()
MIX_PROP_METADATA_ALBUM_STRING: bytes = "SDL_mixer.metadata.album".encode()
MIX_PROP_METADATA_COPYRIGHT_STRING: bytes = "SDL_mixer.metadata.copyright".encode()
MIX_PROP_METADATA_TRACK_NUMBER: bytes = "SDL_mixer.metadata.track".encode()
MIX_PROP_METADATA_TOTAL_TRACKS_NUMBER: bytes = "SDL_mixer.metadata.total_tracks".encode()
MIX_PROP_METADATA_YEAR_NUMBER: bytes = "SDL_mixer.metadata.year".encode()
MIX_PROP_METADATA_DURATION_FRAMES_NUMBER: bytes = "SDL_mixer.metadata.duration_frames".encode()
MIX_PROP_METADATA_DURATION_INFINITE_BOOLEAN: bytes = "SDL_mixer.metadata.duration_infinite".encode()

MIX_GetAudioDuration: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioDuration", ctypes.c_int64, [SDL_POINTER[MIX_Audio]], SDL_MIXER_BINARY]

MIX_DURATION_UNKNOWN, MIX_DURATION_INFINITE = -1, -2

MIX_GetAudioFormat: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioFormat", ctypes.c_bool, [SDL_POINTER[MIX_Audio], SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_DestroyAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DestroyAudio", None, [SDL_POINTER[MIX_Audio]], SDL_MIXER_BINARY]
MIX_CreateTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateTrack", SDL_POINTER[MIX_Track], [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_DestroyTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DestroyTrack", None, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_GetTrackProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackProperties", SDL_PropertiesID, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_GetTrackMixer: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackMixer", SDL_POINTER[MIX_Mixer], [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_SetTrackAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackAudio", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[MIX_Audio]], SDL_MIXER_BINARY]
MIX_SetTrackAudioStream: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackAudioStream", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[SDL_AudioStream]], SDL_MIXER_BINARY]
MIX_SetTrackIOStream: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackIOStream", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[SDL_IOStream], ctypes.c_bool], SDL_MIXER_BINARY]
MIX_SetTrackRawIOStream: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackRawIOStream", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[SDL_IOStream], SDL_POINTER[SDL_AudioSpec], ctypes.c_bool], SDL_MIXER_BINARY]
MIX_TagTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TagTrack", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_char_p], SDL_MIXER_BINARY]
MIX_UntagTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_UntagTrack", None, [SDL_POINTER[MIX_Track], ctypes.c_char_p], SDL_MIXER_BINARY]
MIX_GetTrackTags: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackTags", SDL_POINTER[ctypes.c_char_p], [SDL_POINTER[MIX_Track], SDL_POINTER[ctypes.c_int]], SDL_MIXER_BINARY]
MIX_GetTaggedTracks: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTaggedTracks", SDL_POINTER[SDL_POINTER[MIX_Track]], [SDL_POINTER[MIX_Mixer], ctypes.c_char_p, SDL_POINTER[ctypes.c_int]], SDL_MIXER_BINARY]
MIX_SetTrackPlaybackPosition: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackPlaybackPosition", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_GetTrackPlaybackPosition: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackPlaybackPosition", ctypes.c_int64, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_GetTrackFadeFrames: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackFadeFrames", ctypes.c_int64, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_TrackLooping: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TrackLooping", ctypes.c_bool, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_SetTrackLoops: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackLoops", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_int], SDL_MIXER_BINARY]
MIX_GetTrackAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackAudio", SDL_POINTER[MIX_Audio], [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_GetTrackAudioStream: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackAudioStream", SDL_POINTER[SDL_AudioStream], [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_GetTrackRemaining: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackRemaining", ctypes.c_int64, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_TrackMSToFrames: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TrackMSToFrames", ctypes.c_int64, [SDL_POINTER[MIX_Track], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_TrackFramesToMS: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TrackFramesToMS", ctypes.c_int64, [SDL_POINTER[MIX_Track], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_AudioMSToFrames: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_AudioMSToFrames", ctypes.c_int64, [SDL_POINTER[MIX_Audio], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_AudioFramesToMS: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_AudioFramesToMS", ctypes.c_int64, [SDL_POINTER[MIX_Audio], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_MSToFrames: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_MSToFrames", ctypes.c_int64, [ctypes.c_int, ctypes.c_int64], SDL_MIXER_BINARY]
MIX_FramesToMS: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_FramesToMS", ctypes.c_int64, [ctypes.c_int, ctypes.c_int64], SDL_MIXER_BINARY]
MIX_PlayTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PlayTrack", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_PropertiesID], SDL_MIXER_BINARY]

MIX_PROP_PLAY_LOOPS_NUMBER: bytes = "SDL_mixer.play.loops".encode()
MIX_PROP_PLAY_MAX_FRAME_NUMBER: bytes = "SDL_mixer.play.max_frame".encode()
MIX_PROP_PLAY_MAX_MILLISECONDS_NUMBER: bytes = "SDL_mixer.play.max_milliseconds".encode()
MIX_PROP_PLAY_START_FRAME_NUMBER: bytes = "SDL_mixer.play.start_frame".encode()
MIX_PROP_PLAY_START_MILLISECOND_NUMBER: bytes = "SDL_mixer.play.start_millisecond".encode()
MIX_PROP_PLAY_LOOP_START_FRAME_NUMBER: bytes = "SDL_mixer.play.loop_start_frame".encode()
MIX_PROP_PLAY_LOOP_START_MILLISECOND_NUMBER: bytes = "SDL_mixer.play.loop_start_millisecond".encode()
MIX_PROP_PLAY_FADE_IN_FRAMES_NUMBER: bytes = "SDL_mixer.play.fade_in_frames".encode()
MIX_PROP_PLAY_FADE_IN_MILLISECONDS_NUMBER: bytes = "SDL_mixer.play.fade_in_milliseconds".encode()
MIX_PROP_PLAY_APPEND_SILENCE_FRAMES_NUMBER: bytes = "SDL_mixer.play.append_silence_frames".encode()
MIX_PROP_PLAY_APPEND_SILENCE_MILLISECONDS_NUMBER: bytes = "SDL_mixer.play.append_silence_milliseconds".encode()

MIX_PlayTag: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PlayTag", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_char_p, SDL_PropertiesID], SDL_MIXER_BINARY]
MIX_PlayAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PlayAudio", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], SDL_POINTER[MIX_Audio]], SDL_MIXER_BINARY]
MIX_StopTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_StopTrack", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_StopAllTracks: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_StopAllTracks", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_int64], SDL_MIXER_BINARY]
MIX_StopTag: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_StopTag", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_char_p, ctypes.c_int64], SDL_MIXER_BINARY]
MIX_PauseTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PauseTrack", ctypes.c_bool, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_PauseAllTracks: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PauseAllTracks", ctypes.c_bool, [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_PauseTag: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_PauseTag", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_char_p], SDL_MIXER_BINARY]
MIX_ResumeTrack: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_ResumeTrack", ctypes.c_bool, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_ResumeAllTracks: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_ResumeAllTracks", ctypes.c_bool, [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_ResumeTag: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_ResumeTag", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_char_p], SDL_MIXER_BINARY]
MIX_TrackPlaying: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TrackPlaying", ctypes.c_bool, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_TrackPaused: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_TrackPaused", ctypes.c_bool, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_SetMasterGain: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetMasterGain", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_float], SDL_MIXER_BINARY]
MIX_GetMasterGain: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetMasterGain", ctypes.c_float, [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_SetTrackGain: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackGain", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_float], SDL_MIXER_BINARY]
MIX_GetTrackGain: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackGain", ctypes.c_float, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_SetTagGain: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTagGain", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_char_p, ctypes.c_float], SDL_MIXER_BINARY]
MIX_SetTrackFrequencyRatio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackFrequencyRatio", ctypes.c_bool, [SDL_POINTER[MIX_Track], ctypes.c_float], SDL_MIXER_BINARY]
MIX_GetTrackFrequencyRatio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrackFrequencyRatio", ctypes.c_float, [SDL_POINTER[MIX_Track]], SDL_MIXER_BINARY]
MIX_SetTrackOutputChannelMap: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackOutputChannelMap", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[ctypes.c_int], ctypes.c_int], SDL_MIXER_BINARY]

class MIX_StereoGains(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_float),
        ("right", ctypes.c_float)
    ]

MIX_SetTrackStereo: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackStereo", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[MIX_StereoGains]], SDL_MIXER_BINARY]

class MIX_Point3D(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float)
    ]

MIX_SetTrack3DPosition: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrack3DPosition", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[MIX_Point3D]], SDL_MIXER_BINARY]
MIX_GetTrack3DPosition: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetTrack3DPosition", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[MIX_Point3D]], SDL_MIXER_BINARY]

MIX_CreateGroup: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateGroup", SDL_POINTER[MIX_Group], [SDL_POINTER[MIX_Mixer]], SDL_MIXER_BINARY]
MIX_DestroyGroup: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DestroyGroup", None, [SDL_POINTER[MIX_Group]], SDL_MIXER_BINARY]
MIX_GetGroupProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetGroupProperties", SDL_PropertiesID, [SDL_POINTER[MIX_Group]], SDL_MIXER_BINARY]
MIX_GetGroupMixer: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetGroupMixer", SDL_POINTER[MIX_Mixer], [SDL_POINTER[MIX_Group]], SDL_MIXER_BINARY]
MIX_SetTrackGroup: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackGroup", ctypes.c_bool, [SDL_POINTER[MIX_Track], SDL_POINTER[MIX_Group]], SDL_MIXER_BINARY]

MIX_TrackStoppedCallback: typing.TypeAlias = SDL_FUNC_TYPE["MIX_TrackStoppedCallback", None, [ctypes.c_void_p, SDL_POINTER[MIX_Track]]]
MIX_SetTrackStoppedCallback: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackStoppedCallback", ctypes.c_bool, [SDL_POINTER[MIX_Track], MIX_TrackStoppedCallback, ctypes.c_void_p], SDL_MIXER_BINARY]

MIX_TrackMixCallback: typing.TypeAlias = SDL_FUNC_TYPE["MIX_TrackMixCallback", None, [ctypes.c_void_p, SDL_POINTER[MIX_Track], SDL_POINTER[SDL_AudioSpec], SDL_POINTER[ctypes.c_float], ctypes.c_int]]
MIX_SetTrackRawCallback: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackRawCallback", ctypes.c_bool, [SDL_POINTER[MIX_Track], MIX_TrackMixCallback, ctypes.c_void_p], SDL_MIXER_BINARY]
MIX_SetTrackCookedCallback: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetTrackCookedCallback", ctypes.c_bool, [SDL_POINTER[MIX_Track], MIX_TrackMixCallback, ctypes.c_void_p], SDL_MIXER_BINARY]

MIX_GroupMixCallback: typing.TypeAlias = SDL_FUNC_TYPE["MIX_GroupMixCallback", None, [ctypes.c_void_p, SDL_POINTER[MIX_Group], SDL_POINTER[SDL_AudioSpec], SDL_POINTER[ctypes.c_float], ctypes.c_int]]
MIX_SetGroupPostMixCallback: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetGroupPostMixCallback", ctypes.c_bool, [SDL_POINTER[MIX_Group], MIX_GroupMixCallback, ctypes.c_void_p], SDL_MIXER_BINARY]

MIX_PostMixCallback: typing.TypeAlias = SDL_FUNC_TYPE["MIX_PostMixCallback", None, [ctypes.c_void_p, SDL_POINTER[MIX_Mixer], SDL_POINTER[SDL_AudioSpec], SDL_POINTER[ctypes.c_float], ctypes.c_int]]
MIX_SetPostMixCallback: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_SetPostMixCallback", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], MIX_PostMixCallback, ctypes.c_void_p], SDL_MIXER_BINARY]

MIX_Generate: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_Generate", ctypes.c_bool, [SDL_POINTER[MIX_Mixer], ctypes.c_void_p, ctypes.c_int], SDL_MIXER_BINARY]

class MIX_AudioDecoder(ctypes.c_void_p):
    ...

MIX_CreateAudioDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateAudioDecoder", SDL_POINTER[MIX_AudioDecoder], [ctypes.c_char_p, SDL_PropertiesID], SDL_MIXER_BINARY]
MIX_CreateAudioDecoder_IO: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_CreateAudioDecoder_IO", SDL_POINTER[MIX_AudioDecoder], [SDL_POINTER[SDL_IOStream], ctypes.c_bool, SDL_PropertiesID], SDL_MIXER_BINARY]
MIX_DestroyAudioDecoder: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DestroyAudioDecoder", None, [SDL_POINTER[MIX_AudioDecoder]], SDL_MIXER_BINARY]
MIX_GetAudioDecoderProperties: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioDecoderProperties", SDL_PropertiesID, [SDL_POINTER[MIX_AudioDecoder]], SDL_MIXER_BINARY]
MIX_GetAudioDecoderFormat: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_GetAudioDecoderFormat", ctypes.c_bool, [SDL_POINTER[MIX_AudioDecoder], SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]
MIX_DecodeAudio: abc.Callable[..., typing.Any] = SDL_FUNC["MIX_DecodeAudio", ctypes.c_int, [SDL_POINTER[MIX_AudioDecoder], ctypes.c_void_p, ctypes.c_int, SDL_POINTER[SDL_AudioSpec]], SDL_MIXER_BINARY]