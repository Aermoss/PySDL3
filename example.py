import sdl3, ctypes, os, \
    sys, colorsys, time

def countLines() -> int:
    lines = 0

    for i in os.listdir("sdl3"):
        if i.endswith(".py"):
            with open(f"sdl3/{i}", "r") as file:
                lines += file.read().count("\n") + 1

    return lines

def main(argv: list[str]) -> int:
    print(f"total lines of code: {countLines()}.")
    print(f"loaded {sum(len(v) for k, v in sdl3.functions.items())} functions.")

    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_TIMER | sdl3.SDL_INIT_AUDIO):
        print(f"failed to initialize library: {sdl3.SDL_GetError().decode().lower()}.")
        return -1
    
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1200, 600, sdl3.SDL_WINDOW_RESIZABLE)

    renderDrivers = [sdl3.SDL_GetRenderDriver(i).decode() for i in range(sdl3.SDL_GetNumRenderDrivers())]
    tryGetDriver, tryUseVulkan = lambda order, drivers: next((i for i in order if i in drivers), None), False
    renderDriver = tryGetDriver((["vulkan"] if tryUseVulkan else []) + ["opengl", "software"], renderDrivers)
    print(f"available render drivers: {', '.join(renderDrivers)}. (current: {renderDriver})")
    renderer = sdl3.SDL_CreateRenderer(window, renderDriver.encode())

    if not renderer:
        print(f"failed to create renderer: {sdl3.SDL_GetError().decode().lower()}.")
        return -1
    
    audioDrivers = [sdl3.SDL_GetAudioDriver(i).decode() for i in range(sdl3.SDL_GetNumAudioDrivers())]
    print(f"available audio drivers: {', '.join(audioDrivers)}. (current: {sdl3.SDL_GetCurrentAudioDriver().decode().lower()})")
    audioDevices = sdl3.SDL_GetAudioPlaybackDevices(None)

    if not audioDevices:
        print(f"failed to get audio devices: {sdl3.SDL_GetError().decode().lower()}.")
        return -1

    currentAudioDevice = sdl3.SDL_OpenAudioDevice(audioDevices[0], None)
    
    if currentAudioDevice:
        print(f"current audio device: {sdl3.SDL_GetAudioDeviceName(currentAudioDevice).decode().lower()}.")

    sdl3.IMG_Init(sdl3.IMG_INIT_JPG | sdl3.IMG_INIT_PNG)
    surface = sdl3.IMG_Load("res/example.png".encode())
    texture = sdl3.SDL_CreateTextureFromSurface(renderer, surface)

    rect = sdl3.SDL_Rect()
    sdl3.SDL_GetSurfaceClipRect(surface, ctypes.byref(rect))

    frect = sdl3.SDL_FRect()
    sdl3.SDL_RectToFRect(ctypes.byref(rect), ctypes.byref(frect))
    running, hue, lastTime, scale = True, 0.0, time.time(), 0.75

    sdl3.TTF_Init()
    font = sdl3.TTF_OpenFont("res/example.ttf".encode(), 32)

    if currentAudioDevice:
        sdl3.Mix_Init(sdl3.MIX_INIT_WAVPACK)
        audioSpec = sdl3.SDL_AudioSpec()
        sdl3.Mix_OpenAudio(currentAudioDevice, ctypes.byref(audioSpec))
        chunks = [sdl3.Mix_LoadWAV(f"res/voice/{i}".encode()) for i in os.listdir("res/voice")]
        currentIndex, channel = 0, 0

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
                    if event.key.key == sdl3.SDLK_ESCAPE:
                        running = False

        width, height = ctypes.c_int(), ctypes.c_int()
        sdl3.SDL_GetWindowSize(window, width, height)

        frect.w, frect.h = frect.w * width.value / frect.w * scale, frect.h * width.value / frect.w * scale
        frect.x, frect.y = width.value / 2 - frect.w / 2, height.value / 2 - frect.h / 2

        if currentAudioDevice and not sdl3.Mix_Playing(channel):
            channel = sdl3.Mix_PlayChannel(-1, chunks[currentIndex], 1)
            currentIndex += 1

            if currentIndex >= len(chunks):
                currentIndex = 0

        lastTime, deltaTime = \
            time.time(), time.time() - lastTime

        hue, frames = (hue + 0.5 * deltaTime) % 1.0, frames + 1.0
        sdl3.SDL_SetRenderDrawColorFloat(renderer, *colorsys.hsv_to_rgb(hue, 1.0, 0.1), 255.0)
        sdl3.SDL_RenderClear(renderer)
        sdl3.SDL_RenderTexture(renderer, texture, None, ctypes.byref(frect))
        sinceLastFrame += deltaTime

        if sinceLastFrame >= frameCooldown:
            framesPerSecond = int(frames / sinceLastFrame)
            sinceLastFrame, frames = 0.0, 0.0

            if textTexture:
                sdl3.SDL_DestroySurface(textSurface)
                sdl3.SDL_DestroyTexture(textTexture)

            textSurface = sdl3.TTF_RenderText_Solid(font, f"FPS: {framesPerSecond}".encode(), sdl3.SDL_Color(255, 255, 255, 255))
            textTexture = sdl3.SDL_CreateTextureFromSurface(renderer, textSurface)

            textRect = sdl3.SDL_Rect()
            sdl3.SDL_GetSurfaceClipRect(textSurface, ctypes.byref(textRect))
            sdl3.SDL_RectToFRect(ctypes.byref(textRect), ctypes.byref(textFRect))

        error = sdl3.SDL_GetError()

        if error:
            print(f"error: {error.decode().lower()}.")
            return -1

        if textTexture is not None:
            sdl3.SDL_RenderTexture(renderer, textTexture, None, ctypes.byref(textFRect))

        sdl3.SDL_RenderPresent(renderer)

    if textTexture:
        sdl3.SDL_DestroySurface(textSurface)
        sdl3.SDL_DestroyTexture(textTexture)

    if currentAudioDevice:
        for i in chunks:
            sdl3.Mix_FreeChunk(i)

        sdl3.Mix_CloseAudio()
        sdl3.Mix_Quit()

    sdl3.TTF_CloseFont(font)
    sdl3.TTF_Quit()

    sdl3.SDL_DestroySurface(surface)
    sdl3.SDL_DestroyTexture(texture)
    sdl3.IMG_Quit()

    sdl3.SDL_DestroyRenderer(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0

if __name__ == "__main__":
    os._exit(main(sys.argv))