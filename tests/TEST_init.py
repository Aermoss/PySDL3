from .__init__ import sdl3, ctypes, TEST_RegisterFunction

@TEST_RegisterFunction(["Linux", "Darwin", "Windows"])
def TEST_SDL_Init() -> None:
    assert sdl3.SDL_Init(sdl3.SDL_INIT_EVENTS), sdl3.SDL_GetError().decode()
    assert sdl3.SDL_WasInit(0) & sdl3.SDL_INIT_EVENTS, "Failed to initialize subsystem."
    assert (error := sdl3.SDL_GetError()) == "".encode(), error.decode()
    sdl3.SDL_Quit()

@TEST_RegisterFunction(["Linux", "Darwin", "Windows"])
def TEST_SDL_InitSubSystem() -> None:
    assert sdl3.SDL_Init(0), sdl3.SDL_GetError().decode()
    assert sdl3.SDL_InitSubSystem(sdl3.SDL_INIT_EVENTS), sdl3.SDL_GetError().decode()
    assert (error := sdl3.SDL_GetError()) == "".encode(), error.decode()
    assert sdl3.SDL_WasInit(0) & sdl3.SDL_INIT_EVENTS, "Failed to initialize subsystem."
    sdl3.SDL_QuitSubSystem(sdl3.SDL_INIT_EVENTS)
    sdl3.SDL_Quit()

@TEST_RegisterFunction(["Linux", "Darwin", "Windows"])
def TEST_SDL_IsMainThread() -> None:
    assert sdl3.SDL_IsMainThread(), sdl3.SDL_GetError().decode()

@sdl3.SDL_MainThreadCallback
def callback(data: ctypes.c_void_p) -> None:
    ctypes.cast(data, sdl3.SDL_POINTER[ctypes.c_bool])[0] = True

@TEST_RegisterFunction(["Linux", "Darwin", "Windows"])
def TEST_SDL_RunOnMainThread() -> None:
    data = ctypes.pointer(ctypes.c_bool(False))
    assert sdl3.SDL_RunOnMainThread(callback, ctypes.cast(data, ctypes.c_void_p), True), sdl3.SDL_GetError().decode()
    assert data[0], "Failed to run on main thread."