from .__init__ import sdl3, ctypes, TEST_RegisterFunction

@TEST_RegisterFunction(["Darwin", "Windows"])
def TEST_SDL_GetPreferredLocales() -> None:
    assert sdl3.SDL_Init(0), sdl3.SDL_GetError().decode()
    count = ctypes.pointer(ctypes.c_int(0))
    locales = sdl3.SDL_GetPreferredLocales(count)
    assert locales, sdl3.SDL_GetError().decode()
    assert count.contents.value != 0, "Failed to get preferred locales."
    sdl3.SDL_Quit()