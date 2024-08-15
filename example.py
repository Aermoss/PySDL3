import sdl3, ctypes, os, \
    sys, colorsys, time

def main(argv):
    print(f"loaded {len(sdl3.functions)} functions.")
    result = sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_TIMER)

    if result:
        print(f"failed to initialize library: {sdl3.SDL_GetError().decode().lower()}.")
        return 1
    
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1200, 600, sdl3.SDL_WINDOW_RESIZABLE)

    drivers = [sdl3.SDL_GetRenderDriver(i).decode() for i in range(sdl3.SDL_GetNumRenderDrivers())]
    print(f"available render drivers: {", ".join(drivers)}")

    renderer = sdl3.SDL_CreateRenderer(window, ("vulkan" if "vulkan" in drivers else "software").encode())

    if not renderer:
        print(f"failed to create renderer: {sdl3.SDL_GetError().decode().lower()}.")
        return 1
    
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

        last, delta = \
            time.time(), time.time() - last

        hue += 0.5 * delta

        sdl3.SDL_SetRenderDrawColorFloat(renderer, *colorsys.hsv_to_rgb(hue, 1.0, 1.0), 255.0)
        sdl3.SDL_RenderClear(renderer)
        sdl3.SDL_RenderPresent(renderer)

    sdl3.SDL_DestroyRenderer(renderer)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0

if __name__ == "__main__":
    os._exit(main(sys.argv))