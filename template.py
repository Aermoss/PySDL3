import os, ctypes, time

os.environ["SDL_MAIN_USE_CALLBACKS"] = "1"

import sdl3

class AppState(ctypes.Structure):
    _fields_ = [
        ("window", sdl3.LP_SDL_Window),
        ("renderer", sdl3.LP_SDL_Renderer)
    ]

def SDL_AppInit(appstate: sdl3.LP_c_void_p, argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> sdl3.SDL_AppResult:
    state = AppState()

    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO):
        sdl3.SDL_Log("Couldn't initialize SDL: %s", sdl3.SDL_GetError())
        return sdl3.SDL_APP_FAILURE

    if not sdl3.SDL_CreateWindowAndRenderer("Hello, World!".encode(), 640, 480, 0, ctypes.byref(state.window), ctypes.byref(state.renderer)):
        sdl3.SDL_Log("Couldn't create window/renderer: %s", sdl3.SDL_GetError())
        return sdl3.SDL_APP_FAILURE

    appstate[0] = ctypes.cast(ctypes.pointer(state), ctypes.c_void_p)
    return sdl3.SDL_APP_CONTINUE

def SDL_AppEvent(appstate: ctypes.c_void_p, event: sdl3.LP_SDL_Event) -> sdl3.SDL_AppResult:
    if sdl3.SDL_DEREFERENCE(event).type == sdl3.SDL_EVENT_QUIT:
        return sdl3.SDL_APP_SUCCESS
    
    return sdl3.SDL_APP_CONTINUE

def SDL_AppIterate(appstate: ctypes.c_void_p) -> sdl3.SDL_AppResult:
    state: AppState = sdl3.SDL_DEREFERENCE(ctypes.cast(appstate, ctypes.POINTER(AppState)))
    sdl3.SDL_SetRenderDrawColor(state.renderer, int(time.time() * 255 / 2) % 256, 0, 0, sdl3.SDL_ALPHA_OPAQUE)
    sdl3.SDL_RenderClear(state.renderer)
    sdl3.SDL_RenderPresent(state.renderer)
    return sdl3.SDL_APP_CONTINUE

def SDL_AppQuit(appstate: ctypes.c_void_p, result: sdl3.SDL_AppResult) -> None:
    ... # SDL will clean up the window/renderer for us.