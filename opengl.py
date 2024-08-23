import ctypes, sys, os, imgui, \
    colorsys, time, sdl3, OpenGL.GL as gl

from imgui.integrations.opengl import ProgrammablePipelineRenderer

class SDL3Renderer(ProgrammablePipelineRenderer):
    """Basic SDL3 integration implementation."""
    MOUSE_WHEEL_OFFSET_SCALE = 0.5

    def __init__(self, window: sdl3.LP_SDL_Window) -> None:
        super(SDL3Renderer, self).__init__()
        self.window = window

        self.lastTime = sdl3.SDL_GetTicks() / 1000.0
        self.mousePressed = [False, False, False]
        self.mouseWheel = 0.0

        width, height = ctypes.c_int(0), ctypes.c_int(0)
        sdl3.SDL_GetWindowSize(self.window, ctypes.byref(width), ctypes.byref(height))

        self.io.display_size = width.value, height.value
        self.io.get_clipboard_text_fn = lambda: sdl3.SDL_GetClipboardText()
        self.io.set_clipboard_text_fn = lambda text: sdl3.SDL_SetClipboardText(text.encode())

        self.io.key_map[imgui.KEY_TAB] = sdl3.SDL_SCANCODE_TAB
        self.io.key_map[imgui.KEY_LEFT_ARROW] = sdl3.SDL_SCANCODE_LEFT
        self.io.key_map[imgui.KEY_RIGHT_ARROW] = sdl3.SDL_SCANCODE_RIGHT
        self.io.key_map[imgui.KEY_UP_ARROW] = sdl3.SDL_SCANCODE_UP
        self.io.key_map[imgui.KEY_DOWN_ARROW] = sdl3.SDL_SCANCODE_DOWN
        self.io.key_map[imgui.KEY_PAGE_UP] = sdl3.SDL_SCANCODE_PAGEUP
        self.io.key_map[imgui.KEY_PAGE_DOWN] = sdl3.SDL_SCANCODE_PAGEDOWN
        self.io.key_map[imgui.KEY_HOME] = sdl3.SDL_SCANCODE_HOME
        self.io.key_map[imgui.KEY_END] = sdl3.SDL_SCANCODE_END
        self.io.key_map[imgui.KEY_INSERT] = sdl3.SDL_SCANCODE_INSERT
        self.io.key_map[imgui.KEY_DELETE] = sdl3.SDL_SCANCODE_DELETE
        self.io.key_map[imgui.KEY_BACKSPACE] = sdl3.SDL_SCANCODE_BACKSPACE
        self.io.key_map[imgui.KEY_SPACE] = sdl3.SDL_SCANCODE_SPACE
        self.io.key_map[imgui.KEY_ENTER] = sdl3.SDL_SCANCODE_RETURN
        self.io.key_map[imgui.KEY_ESCAPE] = sdl3.SDL_SCANCODE_ESCAPE
        self.io.key_map[imgui.KEY_PAD_ENTER] = sdl3.SDL_SCANCODE_KP_ENTER
        self.io.key_map[imgui.KEY_A] = sdl3.SDL_SCANCODE_A
        self.io.key_map[imgui.KEY_C] = sdl3.SDL_SCANCODE_C
        self.io.key_map[imgui.KEY_V] = sdl3.SDL_SCANCODE_V
        self.io.key_map[imgui.KEY_X] = sdl3.SDL_SCANCODE_X
        self.io.key_map[imgui.KEY_Y] = sdl3.SDL_SCANCODE_Y
        self.io.key_map[imgui.KEY_Z] = sdl3.SDL_SCANCODE_Z

    def processEvent(self, event: sdl3.SDL_Event) -> None:
        if event.type == sdl3.SDL_EVENT_MOUSE_WHEEL:
            self.mouseWheel = event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE

        if event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN:
            if event.button.button == sdl3.SDL_BUTTON_LEFT:
                self.mousePressed[0] = True

            if event.button.button == sdl3.SDL_BUTTON_RIGHT:
                self.mousePressed[1] = True

            if event.button.button == sdl3.SDL_BUTTON_MIDDLE:
                self.mousePressed[2] = True

        if event.type == sdl3.SDL_EVENT_KEY_UP or event.type == sdl3.SDL_EVENT_KEY_DOWN:
            if event.key.scancode < sdl3.SDL_NUM_SCANCODES:
                self.io.keys_down[event.key.scancode] = event.type == sdl3.SDL_EVENT_KEY_DOWN

            self.io.key_shift = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_SHIFT) != 0
            self.io.key_ctrl = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_CTRL) != 0
            self.io.key_alt = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_ALT) != 0
            self.io.key_super = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_GUI) != 0

        if event.type == sdl3.SDL_EVENT_TEXT_INPUT:
            for char in event.text.text.decode("utf-8"):
                self.io.add_input_character(ord(char))

    def processInputs(self) -> None:
        width, height = ctypes.c_int(0), ctypes.c_int(0)
        sdl3.SDL_GetWindowSize(self.window, ctypes.byref(width), ctypes.byref(height))
        self.io.display_size, self.io.display_fb_scale = (width.value, height.value), (1, 1)
        
        currentTime = sdl3.SDL_GetTicks() / 1000.0
        self.io.delta_time = currentTime - self.lastTime
        self.lastTime = currentTime

        x, y = ctypes.c_float(0.0), ctypes.c_float(0.0)
        mouseMask = sdl3.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        x, y = int(x.value), int(y.value)

        self.io.mouse_pos = (x, y) if sdl3.SDL_GetWindowFlags(self.window) & sdl3.SDL_WINDOW_MOUSE_FOCUS else (-1, -1)
        self.io.mouse_down[0] = self.mousePressed[0] or (mouseMask & sdl3.SDL_BUTTON(sdl3.SDL_BUTTON_LEFT)) != 0
        self.io.mouse_down[1] = self.mousePressed[1] or (mouseMask & sdl3.SDL_BUTTON(sdl3.SDL_BUTTON_RIGHT)) != 0
        self.io.mouse_down[2] = self.mousePressed[2] or (mouseMask & sdl3.SDL_BUTTON(sdl3.SDL_BUTTON_MIDDLE)) != 0
        self.io.mouse_wheel, self.mouseWheel = self.mouseWheel, 0
        self.mousePressed = [False, False, False]

def main(argv: list[str]) -> int:
    print(f"loaded {sum(len(v) for k, v in sdl3.functions.items())} functions.")

    if sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS | sdl3.SDL_INIT_TIMER):
        print(f"failed to initialize library: {sdl3.SDL_GetError().decode().lower()}.")
        return 1
    
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_DEPTH_SIZE, 24)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_STENCIL_SIZE, 8)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_DOUBLEBUFFER, 1)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_ACCELERATED_VISUAL, 1)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_MULTISAMPLEBUFFERS, 1)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_MULTISAMPLESAMPLES, 8)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MINOR_VERSION, 6)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_PROFILE_MASK, sdl3.SDL_GL_CONTEXT_PROFILE_CORE)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_FLAGS, sdl3.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1200, 600, sdl3.SDL_WINDOW_OPENGL | sdl3.SDL_WINDOW_RESIZABLE)

    if not window:
        print(f"failed to create window: {sdl3.SDL_GetError().decode().lower()}.", flush = True)
        return 1

    context = sdl3.SDL_GL_CreateContext(window)
    sdl3.SDL_GL_MakeCurrent(window, context)
    sdl3.SDL_GL_SetSwapInterval(1)

    if not context:
        print(f"failed to create context: {sdl3.SDL_GetError().decode().lower()}.", flush = True)
        return 1

    imgui.create_context()
    imgui.get_io().ini_file_name = None
    imgui.style_colors_dark()

    renderer = SDL3Renderer(window)
    running, hue, last = True, 0.0, 0.0
    event = sdl3.SDL_Event()

    while running:
        while sdl3.SDL_PollEvent(event):
            renderer.processEvent(event)

            match event.type:
                case sdl3.SDL_EVENT_QUIT:
                    running = False

                case sdl3.SDL_EVENT_KEY_DOWN:
                    if event.key.key == sdl3.SDLK_ESCAPE:
                        running = False

        last, delta = \
            time.time(), time.time() - last

        hue += 0.5 * delta
        renderer.processInputs()

        gl.glClearColor(*colorsys.hsv_to_rgb(hue, 1.0, 0.1), 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.new_frame()

        imgui.begin("Hello, World!")
        imgui.text("This is some useful text.")
        imgui.end()

        imgui.render()
        renderer.render(imgui.get_draw_data())
        sdl3.SDL_GL_SwapWindow(window)

    renderer.shutdown()
    # imgui.destroy_context()

    sdl3.SDL_GL_DestroyContext(context)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0

if __name__ == "__main__":
    try:
        os._exit(main(sys.argv))

    except Exception as e:
        print(f"error: {e}")
        os._exit(1)