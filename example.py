import os, sdl3, ctypes, colorsys, time

@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:
    print(f"Total lines of code: {sum([len(open(f'sdl3/{i}', 'r').readlines()) for i in os.listdir('sdl3') if i.endswith('.py')])}.")
    print(f"Loaded {sum(len(v) for k, v in sdl3.functions.items())} functions.")

    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_AUDIO):
        print(f"Failed to initialize library: {sdl3.SDL_GetError().decode()}.")
        return -1

    if not (window := sdl3.SDL_CreateWindow("Aermoss".encode(), 1600, 900, sdl3.SDL_WINDOW_RESIZABLE)):
        print(f"Failed to create window: {sdl3.SDL_GetError().decode()}.")
        return -1

    renderDrivers = [sdl3.SDL_GetRenderDriver(i).decode() for i in range(sdl3.SDL_GetNumRenderDrivers())]
    tryGetDriver, tryUseVulkan = lambda order, drivers: next((i for i in order if i in drivers), None), False
    renderDriver = tryGetDriver((["vulkan"] if tryUseVulkan else []) + ["opengl", "software"], renderDrivers)
    print(f"Available render drivers: {', '.join(renderDrivers)} (current: {renderDriver}).")

    if not (renderer := sdl3.SDL_CreateRenderer(window, renderDriver.encode())):
        print(f"Failed to create renderer: {sdl3.SDL_GetError().decode()}.")
        return -1
    
    audioDrivers = [sdl3.SDL_GetAudioDriver(i).decode() for i in range(sdl3.SDL_GetNumAudioDrivers())]
    print(f"Available audio drivers: {', '.join(audioDrivers)} (current: {sdl3.SDL_GetCurrentAudioDriver().decode()}).")

    if not sdl3.MIX_Init():
        print(f"Failed to initialize mixer: {sdl3.SDL_GetError().decode()}.")
        return -1

    if mixer := sdl3.MIX_CreateMixerDevice(audioDevice := sdl3.SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK, None):
        # print(f"Current audio device: {sdl3.SDL_GetAudioDeviceName(audioDevice).decode()}.")
        track, audios, index = sdl3.MIX_CreateTrack(mixer), [], -1

        for file in os.listdir("res/voice"):
            if audio := sdl3.MIX_LoadAudio(mixer, f"res/voice/{file}".encode(), False):
                audios.append(audio)

            else:
                print(f"Failed to load audio: {sdl3.SDL_GetError().decode()}.")
                return -1

    else:
        print(f"Failed to create mixer device: {sdl3.SDL_GetError().decode()}.")
        return -1

    surface = sdl3.IMG_Load("res/example.png".encode())
    texture = sdl3.SDL_CreateTextureFromSurface(renderer, surface)

    rect = sdl3.SDL_Rect()
    sdl3.SDL_GetSurfaceClipRect(surface, ctypes.byref(rect))

    frect = sdl3.SDL_FRect()
    sdl3.SDL_RectToFRect(ctypes.byref(rect), ctypes.byref(frect))
    running, hue, lastTime, scale = True, 0.0, time.time(), 0.75

    sdl3.TTF_Init()
    font = sdl3.TTF_OpenFont("res/example.ttf".encode(), 32.0)

    frames, frameCooldown = 0.0, 1.0
    textTexture, textFRect = None, sdl3.SDL_FRect()
    sinceLastFrame = frameCooldown
    event = sdl3.SDL_Event()

    while running:
        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            match event.type:
                case sdl3.SDL_EVENT_QUIT:
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    if event.key.key in [sdl3.SDLK_ESCAPE]:
                        running = False

        width, height = ctypes.c_int(), ctypes.c_int()
        sdl3.SDL_GetWindowSize(window, width, height)

        frect.w, frect.h = frect.w * width.value / frect.w * scale, frect.h * width.value / frect.w * scale
        frect.x, frect.y = width.value / 2 - frect.w / 2, height.value / 2 - frect.h / 2

        if not sdl3.MIX_TrackPlaying(track):
            index = (index + 1) % len(audios)
            sdl3.MIX_SetTrackAudio(track, audios[index])
            sdl3.MIX_PlayTrack(track, 0)

        lastTime, deltaTime = time.time(), time.time() - lastTime
        hue, frames = (hue + 0.5 * deltaTime) % 1.0, frames + 1.0
        sdl3.SDL_SetRenderDrawColorFloat(renderer, *colorsys.hsv_to_rgb(hue, 1.0, 0.1), 1.0)
        sdl3.SDL_RenderClear(renderer)
        sdl3.SDL_RenderTexture(renderer, texture, None, ctypes.byref(frect))
        sinceLastFrame += deltaTime

        if sinceLastFrame >= frameCooldown:
            framesPerSecond = int(frames / sinceLastFrame)
            sinceLastFrame, frames = 0.0, 0.0

            if textTexture is not None:
                sdl3.SDL_DestroySurface(textSurface)
                sdl3.SDL_DestroyTexture(textTexture)

            textSurface = sdl3.TTF_RenderText_Blended(font, f"FPS: {framesPerSecond}".encode(), 0, sdl3.SDL_Color(255, 255, 255, 255))
            textTexture = sdl3.SDL_CreateTextureFromSurface(renderer, textSurface)

            textRect = sdl3.SDL_Rect()
            sdl3.SDL_GetSurfaceClipRect(textSurface, ctypes.byref(textRect))
            sdl3.SDL_RectToFRect(ctypes.byref(textRect), ctypes.byref(textFRect))

        if error := sdl3.SDL_GetError():
            print(f"Error: {error.decode()}.")
            return -1

        if textTexture is not None:
            sdl3.SDL_RenderTexture(renderer, textTexture, None, ctypes.byref(textFRect))

        sdl3.SDL_RenderPresent(renderer)

    if textTexture is not None:
        sdl3.SDL_DestroySurface(textSurface)
        sdl3.SDL_DestroyTexture(textTexture)

    for audio in audios:
        sdl3.MIX_DestroyAudio(audio)

    sdl3.MIX_DestroyTrack(track)
    sdl3.MIX_DestroyMixer(mixer)
    sdl3.MIX_Quit()

    sdl3.TTF_CloseFont(font)
    sdl3.TTF_Quit()

    sdl3.SDL_DestroySurface(surface)
    sdl3.SDL_DestroyTexture(texture)

    sdl3.SDL_DestroyRenderer(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0