import ctypes, colorsys, time, sdl3, OpenGL.GL as gl

from imgui_bundle.python_backends.sdl3_backend import imgui, SDL3Renderer

@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS):
        print(f"Failed to initialize library: {sdl3.SDL_GetError().decode()}.")
        return -1
    
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MINOR_VERSION, 6)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_PROFILE_MASK, sdl3.SDL_GL_CONTEXT_PROFILE_COMPATIBILITY)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_FLAGS, sdl3.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)

    if not (window := sdl3.SDL_CreateWindow("Aermoss".encode(), 1600, 900, sdl3.SDL_WINDOW_OPENGL | sdl3.SDL_WINDOW_RESIZABLE)):
        print(f"Failed to create window: {sdl3.SDL_GetError().decode()}.")
        return -1

    context = sdl3.SDL_GL_CreateContext(window)
    sdl3.SDL_GL_MakeCurrent(window, context)

    if not context:
        print(f"Failed to create context: {sdl3.SDL_GetError().decode()}.", flush = True)
        return -1

    imgui.create_context()
    imgui.get_io().set_ini_filename("")

    renderer = SDL3Renderer(window)
    running, hue, lastTime = True, 0.0, time.time()
    event = sdl3.SDL_Event()

    while running:
        renderer.process_inputs()

        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            renderer.process_event(event)

            match event.type:
                case sdl3.SDL_EVENT_QUIT:
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    if event.key.key in [sdl3.SDLK_ESCAPE]:
                        running = False

        lastTime, deltaTime = \
            time.time(), time.time() - lastTime

        hue = (hue + 0.5 * deltaTime) % 360.0
        gl.glClearColor(*colorsys.hsv_to_rgb(hue, 1.0, 0.1), 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.new_frame()
        imgui.show_demo_window()
        imgui.end_frame()

        imgui.render()
        renderer.render(imgui.get_draw_data())
        sdl3.SDL_GL_SwapWindow(window)

    renderer.shutdown()
    imgui.destroy_context()

    sdl3.SDL_GL_MakeCurrent(window, None)
    sdl3.SDL_GL_DestroyContext(context)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0