from .__init__ import sdl3, TEST_RegisterFunction

@TEST_RegisterFunction(["Darwin", "Windows"])
def TEST_SDL_CreateWindow() -> None:
    assert sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO), sdl3.SDL_GetError().decode()
    assert (window := sdl3.SDL_CreateWindow("Test".encode(), 1600, 900, sdl3.SDL_WINDOW_RESIZABLE)), sdl3.SDL_GetError().decode()
    assert (error := sdl3.SDL_GetError()) == "".encode(), error.decode()
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()