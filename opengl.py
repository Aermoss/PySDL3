import ctypes, colorsys, time, sdl3, OpenGL.GL as gl

if USE_IMGUI_BUNDLE := True:
    from imgui_bundle.python_backends.opengl_backend import imgui, ProgrammablePipelineRenderer
    # from imgui_bundle.python_backends.sdl3_backend import imgui, SDL3Renderer

else:
    from imgui.integrations.opengl import imgui, ProgrammablePipelineRenderer

class SDL3Renderer(ProgrammablePipelineRenderer):
    """Basic SDL3 integration implementation."""
    MOUSE_WHEEL_OFFSET_SCALE: float = 0.5

    @staticmethod
    def setCustomStyle() -> None:
        style = imgui.get_style()

        for key, value in {
            imgui.Col_.text.value if USE_IMGUI_BUNDLE else imgui.COLOR_TEXT: (1.00, 1.00, 1.00, 1.00),
            imgui.Col_.text_disabled.value if USE_IMGUI_BUNDLE else imgui.COLOR_TEXT_DISABLED: (0.50, 0.50, 0.50, 1.00),
            imgui.Col_.window_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_WINDOW_BACKGROUND: (0.00, 0.00, 0.00, 0.39),
            imgui.Col_.child_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_CHILD_BACKGROUND: (0.00, 0.00, 0.00, 0.00),
            imgui.Col_.popup_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_POPUP_BACKGROUND: (0.00, 0.00, 0.00, 0.63),
            imgui.Col_.border.value if USE_IMGUI_BUNDLE else imgui.COLOR_BORDER: (1.00, 1.00, 1.00, 0.31),
            imgui.Col_.border_shadow.value if USE_IMGUI_BUNDLE else imgui.COLOR_BORDER_SHADOW: (0.00, 0.00, 0.00, 0.00),
            imgui.Col_.frame_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_FRAME_BACKGROUND: (0.00, 0.00, 0.00, 0.63),
            imgui.Col_.frame_bg_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_FRAME_BACKGROUND_HOVERED: (0.23, 0.23, 0.23, 0.63),
            imgui.Col_.frame_bg_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_FRAME_BACKGROUND_ACTIVE: (0.19, 0.19, 0.19, 0.39),
            imgui.Col_.title_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_TITLE_BACKGROUND: (0.00, 0.00, 0.00, 0.63),
            imgui.Col_.title_bg_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_TITLE_BACKGROUND_ACTIVE: (0.00, 0.00, 0.00, 1.00),
            imgui.Col_.title_bg_collapsed.value if USE_IMGUI_BUNDLE else imgui.COLOR_TITLE_BACKGROUND_COLLAPSED: (0.00, 0.00, 0.00, 0.35),
            imgui.Col_.menu_bar_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_MENUBAR_BACKGROUND: (0.00, 0.00, 0.00, 0.78),
            imgui.Col_.scrollbar_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_SCROLLBAR_BACKGROUND: (0.05, 0.05, 0.05, 0.54),
            imgui.Col_.scrollbar_grab.value if USE_IMGUI_BUNDLE else imgui.COLOR_SCROLLBAR_GRAB: (0.34, 0.34, 0.34, 0.63),
            imgui.Col_.scrollbar_grab_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_SCROLLBAR_GRAB_HOVERED: (0.50, 0.50, 0.50, 0.63),
            imgui.Col_.scrollbar_grab_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_SCROLLBAR_GRAB_ACTIVE: (0.38, 0.38, 0.38, 0.63),
            imgui.Col_.check_mark.value if USE_IMGUI_BUNDLE else imgui.COLOR_CHECK_MARK: (0.22, 0.55, 0.74, 1.00),
            imgui.Col_.slider_grab.value if USE_IMGUI_BUNDLE else imgui.COLOR_SLIDER_GRAB: (0.34, 0.34, 0.34, 0.54),
            imgui.Col_.slider_grab_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_SLIDER_GRAB_ACTIVE: (0.56, 0.56, 0.56, 0.54),
            imgui.Col_.button.value if USE_IMGUI_BUNDLE else imgui.COLOR_BUTTON: (0.00, 0.00, 0.00, 0.63),
            imgui.Col_.button_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_BUTTON_HOVERED: (0.20, 0.22, 0.23, 0.63),
            imgui.Col_.button_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_BUTTON_ACTIVE: (0.19, 0.19, 0.19, 0.39),
            imgui.Col_.header.value if USE_IMGUI_BUNDLE else imgui.COLOR_HEADER: (0.20, 0.20, 0.20, 0.78),
            imgui.Col_.header_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_HEADER_HOVERED: (0.29, 0.29, 0.29, 0.78),
            imgui.Col_.header_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_HEADER_ACTIVE: (0.19, 0.19, 0.19, 0.15),
            imgui.Col_.separator.value if USE_IMGUI_BUNDLE else imgui.COLOR_SEPARATOR: (0.28, 0.28, 0.28, 0.29),
            imgui.Col_.separator_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_SEPARATOR_HOVERED: (0.44, 0.44, 0.44, 0.29),
            imgui.Col_.separator_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_SEPARATOR_ACTIVE: (0.40, 0.44, 0.47, 1.00),
            imgui.Col_.resize_grip.value if USE_IMGUI_BUNDLE else imgui.COLOR_RESIZE_GRIP: (0.28, 0.28, 0.28, 0.29),
            imgui.Col_.resize_grip_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_RESIZE_GRIP_HOVERED: (0.44, 0.44, 0.44, 0.29),
            imgui.Col_.resize_grip_active.value if USE_IMGUI_BUNDLE else imgui.COLOR_RESIZE_GRIP_ACTIVE: (0.40, 0.44, 0.47, 1.00),
            imgui.Col_.tab.value if USE_IMGUI_BUNDLE else imgui.COLOR_TAB: (0.00, 0.00, 0.00, 0.52),
            imgui.Col_.tab_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_TAB_HOVERED: (0.20, 0.20, 0.20, 0.36),
            imgui.Col_.tab_selected.value if USE_IMGUI_BUNDLE else imgui.COLOR_TAB_ACTIVE: (0.14, 0.14, 0.14, 1.00),
            imgui.Col_.tab_dimmed.value if USE_IMGUI_BUNDLE else imgui.COLOR_TAB_UNFOCUSED: (0.00, 0.00, 0.00, 0.52),
            imgui.Col_.tab_dimmed_selected.value if USE_IMGUI_BUNDLE else imgui.COLOR_TAB_UNFOCUSED_ACTIVE: (0.14, 0.14, 0.14, 1.00),
            imgui.Col_.plot_lines.value if USE_IMGUI_BUNDLE else imgui.COLOR_PLOT_LINES: (1.00, 0.00, 0.00, 1.00),
            imgui.Col_.plot_lines_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_PLOT_LINES_HOVERED: (1.00, 0.00, 0.00, 1.00),
            imgui.Col_.plot_histogram.value if USE_IMGUI_BUNDLE else imgui.COLOR_PLOT_HISTOGRAM: (1.00, 0.00, 0.00, 1.00),
            imgui.Col_.plot_histogram_hovered.value if USE_IMGUI_BUNDLE else imgui.COLOR_PLOT_HISTOGRAM_HOVERED: (1.00, 0.00, 0.00, 1.00),
            imgui.Col_.table_header_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_TABLE_HEADER_BACKGROUND: (0.00, 0.00, 0.00, 0.52),
            imgui.Col_.table_border_strong.value if USE_IMGUI_BUNDLE else imgui.COLOR_TABLE_BORDER_STRONG: (0.00, 0.00, 0.00, 0.52),
            imgui.Col_.table_border_light.value if USE_IMGUI_BUNDLE else imgui.COLOR_TABLE_BORDER_LIGHT: (0.28, 0.28, 0.28, 0.29),
            imgui.Col_.table_row_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_TABLE_ROW_BACKGROUND: (0.00, 0.00, 0.00, 0.00),
            imgui.Col_.table_row_bg_alt.value if USE_IMGUI_BUNDLE else imgui.COLOR_TABLE_ROW_BACKGROUND_ALT: (1.00, 1.00, 1.00, 0.06),
            imgui.Col_.text_selected_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_TEXT_SELECTED_BACKGROUND: (0.26, 0.59, 0.98, 0.35),
            imgui.Col_.drag_drop_target.value if USE_IMGUI_BUNDLE else imgui.COLOR_DRAG_DROP_TARGET: (1.00, 1.00, 0.00, 0.90),
            imgui.Col_.nav_windowing_highlight.value if USE_IMGUI_BUNDLE else imgui.COLOR_NAV_WINDOWING_HIGHLIGHT: (1.00, 1.00, 1.00, 0.70),
            imgui.Col_.nav_windowing_dim_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_NAV_WINDOWING_DIM_BACKGROUND: (0.80, 0.80, 0.80, 0.20),
            imgui.Col_.modal_window_dim_bg.value if USE_IMGUI_BUNDLE else imgui.COLOR_MODAL_WINDOW_DIM_BACKGROUND: (0.20, 0.20, 0.20, 0.35)
        }.items():
            if USE_IMGUI_BUNDLE: style.set_color_(key, value)
            else: style.colors[key] = value

        style.window_padding, style.frame_padding, style.cell_padding = (6.0, 6.0), (5.0, 2.0), (6.0, 6.0)
        style.item_spacing, style.item_inner_spacing, style.touch_extra_padding = (6.0, 6.0), (6.0, 6.0), (0.0, 0.0)
        style.window_title_align, style.indent_spacing, style.scrollbar_size = (0.5, 0.5), 25.0, 10.0
        style.grab_min_size, style.window_border_size, style.child_border_size = 10.0, 1.0, 1.0
        style.popup_border_size, style.frame_border_size, style.tab_border_size = 1.0, 1.0, 1.0
        style.window_rounding, style.child_rounding, style.frame_rounding = 5.0, 4.0, 2.0
        style.popup_rounding, style.scrollbar_rounding, style.grab_rounding = 4.0, 9.0, 2.0
        style.log_slider_deadzone, style.tab_rounding = 4.0, 4.0

    def __init__(self, window: sdl3.LP_SDL_Window) -> None:
        super(SDL3Renderer, self).__init__()

        self.window = window
        self.lastTime = sdl3.SDL_GetTicks() / 1000.0
        sdl3.SDL_StartTextInput(window)

        if not USE_IMGUI_BUNDLE:
            imgui.get_io().get_clipboard_text_fn = lambda: sdl3.SDL_GetClipboardText().decode()
            imgui.get_io().set_clipboard_text_fn = lambda text: sdl3.SDL_SetClipboardText(text.encode())

            for key, value in {
                imgui.KEY_TAB: sdl3.SDL_SCANCODE_TAB, imgui.KEY_LEFT_ARROW: sdl3.SDL_SCANCODE_LEFT,
                imgui.KEY_RIGHT_ARROW: sdl3.SDL_SCANCODE_RIGHT, imgui.KEY_UP_ARROW: sdl3.SDL_SCANCODE_UP,
                imgui.KEY_DOWN_ARROW: sdl3.SDL_SCANCODE_DOWN, imgui.KEY_PAGE_UP: sdl3.SDL_SCANCODE_PAGEUP,
                imgui.KEY_PAGE_DOWN: sdl3.SDL_SCANCODE_PAGEDOWN, imgui.KEY_HOME: sdl3.SDL_SCANCODE_HOME,
                imgui.KEY_END: sdl3.SDL_SCANCODE_END, imgui.KEY_INSERT: sdl3.SDL_SCANCODE_INSERT,
                imgui.KEY_DELETE: sdl3.SDL_SCANCODE_DELETE, imgui.KEY_BACKSPACE: sdl3.SDL_SCANCODE_BACKSPACE,
                imgui.KEY_SPACE: sdl3.SDL_SCANCODE_SPACE, imgui.KEY_ENTER: sdl3.SDL_SCANCODE_RETURN,
                imgui.KEY_ESCAPE: sdl3.SDL_SCANCODE_ESCAPE, imgui.KEY_PAD_ENTER: sdl3.SDL_SCANCODE_KP_ENTER,
                imgui.KEY_A: sdl3.SDL_SCANCODE_A, imgui.KEY_C: sdl3.SDL_SCANCODE_C, imgui.KEY_V: sdl3.SDL_SCANCODE_V,
                imgui.KEY_X: sdl3.SDL_SCANCODE_X, imgui.KEY_Y: sdl3.SDL_SCANCODE_Y, imgui.KEY_Z: sdl3.SDL_SCANCODE_Z
            }.items(): self.io.key_map[key] = value

        else:
            imgui.get_platform_io().platform_get_clipboard_text_fn = lambda _: sdl3.SDL_GetClipboardText().decode()
            imgui.get_platform_io().platform_set_clipboard_text_fn = lambda _, text: sdl3.SDL_SetClipboardText(text.encode())

            self.key_map = {
                sdl3.SDL_SCANCODE_TAB: imgui.Key.tab, sdl3.SDL_SCANCODE_LEFT: imgui.Key.left_arrow,
                sdl3.SDL_SCANCODE_RIGHT: imgui.Key.right_arrow, sdl3.SDL_SCANCODE_UP: imgui.Key.up_arrow,
                sdl3.SDL_SCANCODE_DOWN: imgui.Key.down_arrow, sdl3.SDL_SCANCODE_PAGEUP: imgui.Key.page_up,
                sdl3.SDL_SCANCODE_PAGEDOWN: imgui.Key.page_down, sdl3.SDL_SCANCODE_HOME: imgui.Key.home,
                sdl3.SDL_SCANCODE_END: imgui.Key.end, sdl3.SDL_SCANCODE_INSERT: imgui.Key.insert,
                sdl3.SDL_SCANCODE_DELETE: imgui.Key.delete, sdl3.SDL_SCANCODE_BACKSPACE: imgui.Key.backspace,
                sdl3.SDL_SCANCODE_SPACE: imgui.Key.space, sdl3.SDL_SCANCODE_RETURN: imgui.Key.enter,
                sdl3.SDL_SCANCODE_ESCAPE: imgui.Key.escape, sdl3.SDL_SCANCODE_KP_ENTER: imgui.Key.keypad_enter,
                sdl3.SDL_SCANCODE_A: imgui.Key.a, sdl3.SDL_SCANCODE_C: imgui.Key.c, sdl3.SDL_SCANCODE_V: imgui.Key.v,
                sdl3.SDL_SCANCODE_X: imgui.Key.x, sdl3.SDL_SCANCODE_Y: imgui.Key.y, sdl3.SDL_SCANCODE_Z: imgui.Key.z,
                sdl3.SDL_SCANCODE_LCTRL: imgui.Key.mod_ctrl, sdl3.SDL_SCANCODE_RCTRL: imgui.Key.mod_ctrl,
                sdl3.SDL_SCANCODE_LSHIFT: imgui.Key.mod_shift, sdl3.SDL_SCANCODE_RSHIFT: imgui.Key.mod_shift,
                sdl3.SDL_SCANCODE_LALT: imgui.Key.mod_alt, sdl3.SDL_SCANCODE_RALT: imgui.Key.mod_alt,
                sdl3.SDL_SCANCODE_LGUI: imgui.Key.mod_super, sdl3.SDL_SCANCODE_RGUI: imgui.Key.mod_super
            }

    def processEvent(self, event: sdl3.SDL_Event) -> bool:
        if event.type in [sdl3.SDL_EVENT_MOUSE_WHEEL]:
            if not USE_IMGUI_BUNDLE: self.io.mouse_wheel = event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE
            else: self.io.add_mouse_wheel_event(event.wheel.x * self.MOUSE_WHEEL_OFFSET_SCALE, event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE)

        elif event.type in [sdl3.SDL_EVENT_MOUSE_BUTTON_UP, sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN]:
            buttons = [sdl3.SDL_BUTTON_LEFT, sdl3.SDL_BUTTON_RIGHT, sdl3.SDL_BUTTON_MIDDLE]

            if (button := event.button.button) in buttons:
                if not USE_IMGUI_BUNDLE: self.io.mouse_down[buttons.index(event.button.button)] = event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN
                else: self.io.add_mouse_button_event(buttons.index(button), event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN)

        elif event.type in [sdl3.SDL_EVENT_MOUSE_MOTION]:
            self.io.mouse_pos = (event.motion.x, event.motion.y) \
                if sdl3.SDL_GetWindowFlags(self.window) & sdl3.SDL_WINDOW_MOUSE_FOCUS else (-1, -1)

        elif event.type in [sdl3.SDL_EVENT_KEY_UP, sdl3.SDL_EVENT_KEY_DOWN]:
            if not USE_IMGUI_BUNDLE:
                if event.key.scancode < sdl3.SDL_SCANCODE_COUNT:
                    self.io.keys_down[event.key.scancode] = event.type == sdl3.SDL_EVENT_KEY_DOWN

                if state := sdl3.SDL_GetModState():
                    self.io.key_shift = (state & sdl3.SDL_KMOD_SHIFT) != 0
                    self.io.key_ctrl = (state & sdl3.SDL_KMOD_CTRL) != 0
                    self.io.key_alt = (state & sdl3.SDL_KMOD_ALT) != 0
                    self.io.key_super = (state & sdl3.SDL_KMOD_GUI) != 0

            else:
                if (scancode := event.key.scancode) in self.key_map:
                    self.io.add_key_event(self.key_map[scancode], event.type == sdl3.SDL_EVENT_KEY_DOWN)

        elif event.type in [sdl3.SDL_EVENT_TEXT_INPUT]:
            for char in event.text.text.decode("utf-8"):
                self.io.add_input_character(ord(char))

        else:
            return False
        
        return True

    def processInputs(self) -> None:
        width, height = ctypes.c_int(0), ctypes.c_int(0)
        sdl3.SDL_GetWindowSize(self.window, ctypes.byref(width), ctypes.byref(height))
        self.io.display_size, self.io.mouse_wheel = (width.value, height.value), 0
        if USE_IMGUI_BUNDLE: self.io.display_framebuffer_scale = (1, 1)
        else: self.io.display_fb_scale = (1, 1)
        
        currentTime = sdl3.SDL_GetTicks() / 1000.0; deltaTime = currentTime - self.lastTime
        self.io.delta_time = 1.0 / 10000.0 if deltaTime <= 0.0 else deltaTime
        self.lastTime = currentTime

@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS):
        print(f"Failed to initialize library: {sdl3.SDL_GetError().decode()}.")
        return -1
    
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MINOR_VERSION, 6)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_PROFILE_MASK, sdl3.SDL_GL_CONTEXT_PROFILE_COMPATIBILITY)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_FLAGS, sdl3.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1600, 900, sdl3.SDL_WINDOW_OPENGL | sdl3.SDL_WINDOW_RESIZABLE)

    if not window:
        print(f"Failed to create window: {sdl3.SDL_GetError().decode()}.", flush = True)
        return -1

    context = sdl3.SDL_GL_CreateContext(window)
    sdl3.SDL_GL_MakeCurrent(window, context)

    if not context:
        print(f"Failed to create context: {sdl3.SDL_GetError().decode()}.", flush = True)
        return -1

    imgui.create_context()
    if USE_IMGUI_BUNDLE: imgui.get_io().set_ini_filename("")
    else: imgui.get_io().ini_file_name = None
    SDL3Renderer.setCustomStyle()

    renderer = SDL3Renderer(window)
    running, hue, lastTime = True, 0.0, time.time()
    event = sdl3.SDL_Event()

    while running:
        renderer.processInputs()

        while sdl3.SDL_PollEvent(ctypes.byref(event)):
            renderer.processEvent(event)

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

    if USE_IMGUI_BUNDLE:
        imgui.destroy_context()

    sdl3.SDL_GL_MakeCurrent(window, None)
    sdl3.SDL_GL_DestroyContext(context)
    sdl3.SDL_DestroyWindow(window)
    sdl3.SDL_Quit()
    return 0