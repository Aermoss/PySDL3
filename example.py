import sdl3, ctypes, os, \
    sys, colorsys, time

def main(argv):
    print(f"loaded {sum(len(v) for k, v in sdl3.functions.items())} functions.")
    result = sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_TIMER | sdl3.SDL_INIT_AUDIO)

    if result:
        print(f"failed to initialize library: {sdl3.SDL_GetError().decode().lower()}.")
        return 1
    
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1200, 600, sdl3.SDL_WINDOW_RESIZABLE)

    renderDrivers = [sdl3.SDL_GetRenderDriver(i).decode() for i in range(sdl3.SDL_GetNumRenderDrivers())]
    print(f"available render drivers: {", ".join(renderDrivers)}")

    renderer = sdl3.SDL_CreateRenderer(window, ("vulkan" if "vulkan" in renderDrivers else "software").encode())

    if not renderer:
        print(f"failed to create renderer: {sdl3.SDL_GetError().decode().lower()}.")
        return 1
    
    audioDrivers = [sdl3.SDL_GetAudioDriver(i).decode() for i in range(sdl3.SDL_GetNumAudioDrivers())]
    print(f"available audio drivers: {", ".join(audioDrivers)}")
    audioDevices = sdl3.SDL_GetAudioPlaybackDevices(None)

    if not audioDevices:
        print(f"failed to get audio devices: {sdl3.SDL_GetError().decode().lower()}.")
        return 1

    currentAudioDevice = sdl3.SDL_OpenAudioDevice(audioDevices[0], None)
    print(f"current audio device: {sdl3.SDL_GetAudioDeviceName(currentAudioDevice).decode().lower()}.")

    audioSpec, audioBuffer, audioSize = sdl3.SDL_AudioSpec(), ctypes.POINTER(ctypes.c_uint8)(), ctypes.c_uint32()
    sdl3.SDL_LoadWAV("example.wav".encode(), ctypes.byref(audioSpec), ctypes.byref(audioBuffer), ctypes.byref(audioSize))
    audioStream = sdl3.SDL_CreateAudioStream(ctypes.byref(audioSpec), ctypes.byref(audioSpec))
    sdl3.SDL_PutAudioStreamData(audioStream, audioBuffer, audioSize.value)
    sdl3.SDL_BindAudioStream(currentAudioDevice, audioStream)
    sdl3.SDL_SetAudioStreamFrequencyRatio(audioStream, 1.0)
    
    running, hue, last = True, 0.0, 0.0

    while running:
        event = sdl3.SDL_Event()

        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            match event.type:
                case sdl3.SDL_EVENT_QUIT:
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    if event.key.key == sdl3.SDLK_ESCAPE:
                        running = False

        if not sdl3.SDL_GetAudioStreamAvailable(audioStream):
            sdl3.SDL_PutAudioStreamData(audioStream, audioBuffer, audioSize.value)

        last, delta = \
            time.time(), time.time() - last

        hue += 0.5 * delta

        sdl3.SDL_SetRenderDrawColorFloat(renderer, *colorsys.hsv_to_rgb(hue, 1.0, 0.1), 255.0)
        sdl3.SDL_RenderClear(renderer)
        sdl3.SDL_RenderPresent(renderer)

    sdl3.SDL_UnbindAudioStream(audioStream)
    sdl3.SDL_DestroyAudioStream(audioStream)
    sdl3.SDL_CloseAudioDevice(currentAudioDevice)

    sdl3.SDL_DestroyRenderer(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0

if __name__ == "__main__":
    os._exit(main(sys.argv))