from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID
from .SDL_iostream import SDL_IOStream

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Process(ctypes.c_void_p):
    ...

SDL_FUNC("SDL_CreateProcess", ctypes.POINTER(SDL_Process), ctypes.POINTER(ctypes.c_char_p), ctypes.c_bool)

SDL_ProcessIO = ctypes.c_int

SDL_PROCESS_STDIO_INHERITED = 0
SDL_PROCESS_STDIO_NULL = 1
SDL_PROCESS_STDIO_APP = 2
SDL_PROCESS_STDIO_REDIRECT = 3

SDL_FUNC("SDL_CreateProcessWithProperties", ctypes.POINTER(SDL_Process), SDL_PropertiesID)

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

SDL_FUNC("SDL_GetProcessProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Process))

SDL_PROP_PROCESS_PID_NUMBER = "SDL.process.pid".encode()
SDL_PROP_PROCESS_STDIN_POINTER = "SDL.process.stdin".encode()
SDL_PROP_PROCESS_STDOUT_POINTER = "SDL.process.stdout".encode()
SDL_PROP_PROCESS_STDERR_POINTER = "SDL.process.stderr".encode()
SDL_PROP_PROCESS_BACKGROUND_BOOLEAN = "SDL.process.background".encode()

SDL_FUNC("SDL_ReadProcess", ctypes.c_void_p, ctypes.POINTER(SDL_Process), ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_GetProcessInput", ctypes.POINTER(SDL_IOStream), ctypes.POINTER(SDL_Process))
SDL_FUNC("SDL_GetProcessOutput", ctypes.POINTER(SDL_IOStream), ctypes.POINTER(SDL_Process))

SDL_FUNC("SDL_KillProcess", ctypes.c_bool, ctypes.POINTER(SDL_Process), ctypes.c_bool)
SDL_FUNC("SDL_WaitProcess", ctypes.c_bool, ctypes.POINTER(SDL_Process), ctypes.c_bool, ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_DestroyProcess", None, ctypes.POINTER(SDL_Process))