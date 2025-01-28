from .__init__ import sdl3, TEST_RegisterFunction

@TEST_RegisterFunction
def TEST_SDL_Init():
    assert sdl3.SDL_Init(0), "SDL_Init failed."
    assert sdl3.SDL_GetError() == "".encode(), "SDL_GetError failed."
    sdl3.SDL_Quit()

@TEST_RegisterFunction
def TEST_SDL_CreateWindow():
    assert sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO), "SDL_Init failed."
    assert (window := sdl3.SDL_CreateWindow("Test".encode(), 1600, 900, sdl3.SDL_WINDOW_RESIZABLE)), "SDL_CreateWindow failed."
    assert sdl3.SDL_GetError() == "".encode(), "SDL_GetError failed."
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()