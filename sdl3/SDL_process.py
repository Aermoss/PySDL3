from .__init__ import ctypes, typing, abc, SDL_POINTER, SDL_ENUM, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID
from .SDL_iostream import SDL_IOStream

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Process(ctypes.c_void_p):
    ...

SDL_CreateProcess: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CreateProcess", SDL_POINTER[SDL_Process], [SDL_POINTER[ctypes.c_char_p], ctypes.c_bool]]

SDL_ProcessIO: typing.TypeAlias = SDL_TYPE["SDL_ProcessIO", SDL_ENUM]

SDL_PROCESS_STDIO_INHERITED, SDL_PROCESS_STDIO_NULL, \
    SDL_PROCESS_STDIO_APP, SDL_PROCESS_STDIO_REDIRECT = range(4)

SDL_CreateProcessWithProperties: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CreateProcessWithProperties", SDL_POINTER[SDL_Process], [SDL_PropertiesID]]

SDL_PROP_PROCESS_CREATE_ARGS_POINTER = "SDL.process.create.args".encode()
SDL_PROP_PROCESS_CREATE_ENVIRONMENT_POINTER = "SDL.process.create.environment".encode()
SDL_PROP_PROCESS_CREATE_STDIN_NUMBER = "SDL.process.create.stdin_option".encode()
SDL_PROP_PROCESS_CREATE_STDIN_POINTER = "SDL.process.create.stdin_source".encode()
SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER = "SDL.process.create.stdout_option".encode()
SDL_PROP_PROCESS_CREATE_STDOUT_POINTER = "SDL.process.create.stdout_source".encode()
SDL_PROP_PROCESS_CREATE_STDERR_NUMBER = "SDL.process.create.stderr_option".encode()
SDL_PROP_PROCESS_CREATE_STDERR_POINTER = "SDL.process.create.stderr_source".encode()
SDL_PROP_PROCESS_CREATE_STDERR_TO_STDOUT_BOOLEAN = "SDL.process.create.stderr_to_stdout".encode()
SDL_PROP_PROCESS_CREATE_BACKGROUND_BOOLEAN = "SDL.process.create.background".encode()

SDL_GetProcessProperties: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetProcessProperties", SDL_PropertiesID, [SDL_POINTER[SDL_Process]]]

SDL_PROP_PROCESS_PID_NUMBER = "SDL.process.pid".encode()
SDL_PROP_PROCESS_STDIN_POINTER = "SDL.process.stdin".encode()
SDL_PROP_PROCESS_STDOUT_POINTER = "SDL.process.stdout".encode()
SDL_PROP_PROCESS_STDERR_POINTER = "SDL.process.stderr".encode()
SDL_PROP_PROCESS_BACKGROUND_BOOLEAN = "SDL.process.background".encode()

SDL_ReadProcess: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ReadProcess", ctypes.c_void_p, [SDL_POINTER[SDL_Process], SDL_POINTER[ctypes.c_size_t], SDL_POINTER[ctypes.c_int]]]

SDL_GetProcessInput: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetProcessInput", SDL_POINTER[SDL_IOStream], [SDL_POINTER[SDL_Process]]]
SDL_GetProcessOutput: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetProcessOutput", SDL_POINTER[SDL_IOStream], [SDL_POINTER[SDL_Process]]]

SDL_KillProcess: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_KillProcess", ctypes.c_bool, [SDL_POINTER[SDL_Process], ctypes.c_bool]]
SDL_WaitProcess: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_WaitProcess", ctypes.c_bool, [SDL_POINTER[SDL_Process], ctypes.c_bool, SDL_POINTER[ctypes.c_int]]]
SDL_DestroyProcess: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_DestroyProcess", None, [SDL_POINTER[SDL_Process]]]