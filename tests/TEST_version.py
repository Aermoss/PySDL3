from .__init__ import sdl3, TEST_RegisterFunction

@TEST_RegisterFunction(["Darwin", "Windows", "Linux"])
def TEST_SDL_GetVersion() -> None:
    assert (_ := sdl3.SDL_GetVersion()), "Failed to get version."
    assert (major := sdl3.SDL_VERSIONNUM_MAJOR(_)) == sdl3.SDL_MAJOR_VERSION, f"Major version mismatch: {major}."
    assert (minor := sdl3.SDL_VERSIONNUM_MINOR(_)) == sdl3.SDL_MINOR_VERSION, f"Minor version mismatch: {minor}."
    assert (micro := sdl3.SDL_VERSIONNUM_MICRO(_)) == sdl3.SDL_MICRO_VERSION, f"Micro version mismatch: {micro}."
    assert sdl3.SDL_VERSION_ATLEAST(sdl3.SDL_MAJOR_VERSION, sdl3.SDL_MINOR_VERSION, sdl3.SDL_MICRO_VERSION), "Version is not at least the current version."
    assert _ == sdl3.SDL_VERSION, f"Version mismatch: {_}."

@TEST_RegisterFunction(["Darwin", "Windows", "Linux"])
def TEST_SDL_GetRevision() -> None:
    assert (_ := sdl3.SDL_GetRevision()), "Failed to get revision."
    assert _.decode(), "Revision is empty."