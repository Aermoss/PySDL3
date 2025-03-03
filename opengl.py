import ctypes, colorsys, time, sdl3, OpenGL.GL as gl

if USE_IMGUI_BUNDLE := True:
    from imgui_bundle import imgui
    from imgui_bundle.python_backends.opengl_backend import ProgrammablePipelineRenderer

    class SDL3Renderer(ProgrammablePipelineRenderer):
        """Basic SDL3 integration implementation."""
        MOUSE_WHEEL_OFFSET_SCALE = 0.5

        @staticmethod
        def setCustomStyle() -> None:
            style = imgui.get_style()
            style.set_color_(imgui.Col_.text.value, imgui.ImVec4(1.00, 1.00, 1.00, 1.00))
            style.set_color_(imgui.Col_.text_disabled.value, imgui.ImVec4(0.50, 0.50, 0.50, 1.00))
            style.set_color_(imgui.Col_.window_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.39))
            style.set_color_(imgui.Col_.child_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.00))
            style.set_color_(imgui.Col_.popup_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.63))
            style.set_color_(imgui.Col_.border.value, imgui.ImVec4(1.00, 1.00, 1.00, 0.31))
            style.set_color_(imgui.Col_.border_shadow.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.00))
            style.set_color_(imgui.Col_.frame_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.63))
            style.set_color_(imgui.Col_.frame_bg_hovered.value, imgui.ImVec4(0.23, 0.23, 0.23, 0.63))
            style.set_color_(imgui.Col_.frame_bg_active.value, imgui.ImVec4(0.19, 0.19, 0.19, 0.39))
            style.set_color_(imgui.Col_.title_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.63))
            style.set_color_(imgui.Col_.title_bg_active.value, imgui.ImVec4(0.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.title_bg_collapsed.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.35))
            style.set_color_(imgui.Col_.menu_bar_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.78))
            style.set_color_(imgui.Col_.scrollbar_bg.value, imgui.ImVec4(0.05, 0.05, 0.05, 0.54))
            style.set_color_(imgui.Col_.scrollbar_grab.value, imgui.ImVec4(0.34, 0.34, 0.34, 0.63))
            style.set_color_(imgui.Col_.scrollbar_grab_hovered.value, imgui.ImVec4(0.50, 0.50, 0.50, 0.63))
            style.set_color_(imgui.Col_.scrollbar_grab_active.value, imgui.ImVec4(0.38, 0.38, 0.38, 0.63))
            style.set_color_(imgui.Col_.check_mark.value, imgui.ImVec4(0.22, 0.55, 0.74, 1.00))
            style.set_color_(imgui.Col_.slider_grab.value, imgui.ImVec4(0.34, 0.34, 0.34, 0.54))
            style.set_color_(imgui.Col_.slider_grab_active.value, imgui.ImVec4(0.56, 0.56, 0.56, 0.54))
            style.set_color_(imgui.Col_.button.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.63))
            style.set_color_(imgui.Col_.button_hovered.value, imgui.ImVec4(0.20, 0.22, 0.23, 0.63))
            style.set_color_(imgui.Col_.button_active.value, imgui.ImVec4(0.19, 0.19, 0.19, 0.39))
            style.set_color_(imgui.Col_.header.value, imgui.ImVec4(0.20, 0.20, 0.20, 0.78))
            style.set_color_(imgui.Col_.header_hovered.value, imgui.ImVec4(0.29, 0.29, 0.29, 0.78))
            style.set_color_(imgui.Col_.header_active.value, imgui.ImVec4(0.19, 0.19, 0.19, 0.15))
            style.set_color_(imgui.Col_.separator.value, imgui.ImVec4(0.28, 0.28, 0.28, 0.29))
            style.set_color_(imgui.Col_.separator_hovered.value, imgui.ImVec4(0.44, 0.44, 0.44, 0.29))
            style.set_color_(imgui.Col_.separator_active.value, imgui.ImVec4(0.40, 0.44, 0.47, 1.00))
            style.set_color_(imgui.Col_.resize_grip.value, imgui.ImVec4(0.28, 0.28, 0.28, 0.29))
            style.set_color_(imgui.Col_.resize_grip_hovered.value, imgui.ImVec4(0.44, 0.44, 0.44, 0.29))
            style.set_color_(imgui.Col_.resize_grip_active.value, imgui.ImVec4(0.40, 0.44, 0.47, 1.00))
            style.set_color_(imgui.Col_.tab.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.52))
            style.set_color_(imgui.Col_.tab_hovered.value, imgui.ImVec4(0.20, 0.20, 0.20, 0.36))
            style.set_color_(imgui.Col_.tab_selected.value, imgui.ImVec4(0.14, 0.14, 0.14, 1.00))
            style.set_color_(imgui.Col_.tab_dimmed.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.52))
            style.set_color_(imgui.Col_.tab_dimmed_selected.value, imgui.ImVec4(0.14, 0.14, 0.14, 1.00))
            style.set_color_(imgui.Col_.plot_lines.value, imgui.ImVec4(1.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.plot_lines_hovered.value, imgui.ImVec4(1.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.plot_histogram.value, imgui.ImVec4(1.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.plot_histogram_hovered.value, imgui.ImVec4(1.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.table_header_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.52))
            style.set_color_(imgui.Col_.table_border_strong.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.52))
            style.set_color_(imgui.Col_.table_border_light.value, imgui.ImVec4(0.28, 0.28, 0.28, 0.29))
            style.set_color_(imgui.Col_.table_row_bg.value, imgui.ImVec4(0.00, 0.00, 0.00, 0.00))
            style.set_color_(imgui.Col_.table_row_bg_alt.value, imgui.ImVec4(1.00, 1.00, 1.00, 0.06))
            style.set_color_(imgui.Col_.text_selected_bg.value, imgui.ImVec4(0.20, 0.22, 0.23, 1.00))
            style.set_color_(imgui.Col_.drag_drop_target.value, imgui.ImVec4(0.33, 0.67, 0.86, 1.00))
            style.set_color_(imgui.Col_.nav_windowing_highlight.value, imgui.ImVec4(1.00, 0.00, 0.00, 1.00))
            style.set_color_(imgui.Col_.nav_windowing_dim_bg.value, imgui.ImVec4(1.00, 0.00, 0.00, 0.20))
            style.set_color_(imgui.Col_.modal_window_dim_bg.value, imgui.ImVec4(1.00, 0.00, 0.00, 0.35))

            style.window_padding = imgui.ImVec2(6.0, 6.0)
            style.frame_padding = imgui.ImVec2(5.0, 2.0)
            style.cell_padding = imgui.ImVec2(6.0, 6.0)
            style.item_spacing = imgui.ImVec2(6.0, 6.0)
            style.item_inner_spacing = imgui.ImVec2(6.0, 6.0)
            style.touch_extra_padding = imgui.ImVec2(0.0, 0.0)
            style.window_title_align = imgui.ImVec2(0.5, 0.5)
            style.indent_spacing = 25.0
            style.scrollbar_size = 10.0
            style.grab_min_size = 10.0
            style.window_border_size = 1.0
            style.child_border_size = 1.0
            style.popup_border_size = 1.0
            style.frame_border_size = 1.0
            style.tab_border_size = 1.0
            style.window_rounding = 5.0
            style.child_rounding = 4.0
            style.frame_rounding = 2.0
            style.popup_rounding = 4.0
            style.scrollbar_rounding = 9.0
            style.grab_rounding = 2.0
            style.log_slider_deadzone = 4.0
            style.tab_rounding = 4.0

        def __init__(self, window):
            super(SDL3Renderer, self).__init__()

            self.window = window
            self.lastTime = sdl3.SDL_GetTicks() / 1000.0
            imgui.get_platform_io().platform_get_clipboard_text_fn = lambda: sdl3.SDL_GetClipboardText()
            imgui.get_platform_io().platform_set_clipboard_text_fn = lambda text: sdl3.SDL_SetClipboardText(text.encode())
            sdl3.SDL_StartTextInput(window)

            self.key_map = {
                sdl3.SDL_SCANCODE_TAB: imgui.Key.tab,
                sdl3.SDL_SCANCODE_LEFT: imgui.Key.left_arrow,
                sdl3.SDL_SCANCODE_RIGHT: imgui.Key.right_arrow,
                sdl3.SDL_SCANCODE_UP: imgui.Key.up_arrow,
                sdl3.SDL_SCANCODE_DOWN: imgui.Key.down_arrow,
                sdl3.SDL_SCANCODE_PAGEUP: imgui.Key.page_up,
                sdl3.SDL_SCANCODE_PAGEDOWN: imgui.Key.page_down,
                sdl3.SDL_SCANCODE_HOME: imgui.Key.home,
                sdl3.SDL_SCANCODE_END: imgui.Key.end,
                sdl3.SDL_SCANCODE_INSERT: imgui.Key.insert,
                sdl3.SDL_SCANCODE_DELETE: imgui.Key.delete,
                sdl3.SDL_SCANCODE_BACKSPACE: imgui.Key.backspace,
                sdl3.SDL_SCANCODE_SPACE: imgui.Key.space,
                sdl3.SDL_SCANCODE_RETURN: imgui.Key.enter,
                sdl3.SDL_SCANCODE_ESCAPE: imgui.Key.escape,
                sdl3.SDL_SCANCODE_KP_ENTER: imgui.Key.keypad_enter,
                sdl3.SDL_SCANCODE_A: imgui.Key.a,
                sdl3.SDL_SCANCODE_C: imgui.Key.c,
                sdl3.SDL_SCANCODE_V: imgui.Key.v,
                sdl3.SDL_SCANCODE_X: imgui.Key.x,
                sdl3.SDL_SCANCODE_Y: imgui.Key.y,
                sdl3.SDL_SCANCODE_Z: imgui.Key.z,
                sdl3.SDL_SCANCODE_LCTRL: imgui.Key.mod_ctrl,
                sdl3.SDL_SCANCODE_RCTRL: imgui.Key.mod_ctrl,
                sdl3.SDL_SCANCODE_LSHIFT: imgui.Key.mod_shift,
                sdl3.SDL_SCANCODE_RSHIFT: imgui.Key.mod_shift,
                sdl3.SDL_SCANCODE_LALT: imgui.Key.mod_alt,
                sdl3.SDL_SCANCODE_RALT: imgui.Key.mod_alt,
                sdl3.SDL_SCANCODE_LGUI: imgui.Key.mod_super,
                sdl3.SDL_SCANCODE_RGUI: imgui.Key.mod_super
            }

        def processEvent(self, event):
            if event.type in [sdl3.SDL_EVENT_MOUSE_WHEEL]:
                self.io.add_mouse_wheel_event(event.wheel.x * self.MOUSE_WHEEL_OFFSET_SCALE, event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE)

            if event.type in [sdl3.SDL_EVENT_MOUSE_BUTTON_UP, sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN]:
                buttons = [sdl3.SDL_BUTTON_LEFT, sdl3.SDL_BUTTON_RIGHT, sdl3.SDL_BUTTON_MIDDLE]

                if (button := event.button.button) in buttons:
                    self.io.add_mouse_button_event(buttons.index(button), event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN)

            if event.type in [sdl3.SDL_EVENT_MOUSE_MOTION]:
                self.io.mouse_pos = (event.motion.x, event.motion.y) \
                    if sdl3.SDL_GetWindowFlags(self.window) & sdl3.SDL_WINDOW_MOUSE_FOCUS else (-1, -1)

            if event.type in [sdl3.SDL_EVENT_KEY_UP, sdl3.SDL_EVENT_KEY_DOWN]:
                if (scancode := event.key.scancode) in self.key_map:
                    self.io.add_key_event(self.key_map[scancode], event.type == sdl3.SDL_EVENT_KEY_DOWN)

            if event.type in [sdl3.SDL_EVENT_TEXT_INPUT]:
                for char in event.text.text.decode("utf-8"):
                    self.io.add_input_character(ord(char))

        def processInputs(self):
            width, height = ctypes.c_int(0), ctypes.c_int(0)
            sdl3.SDL_GetWindowSize(self.window, ctypes.byref(width), ctypes.byref(height))
            self.io.display_size, self.io.display_framebuffer_scale = (width.value, height.value), (1, 1)
            self.io.mouse_wheel = 0
            
            currentTime = sdl3.SDL_GetTicks() / 1000.0; deltaTime = currentTime - self.lastTime
            self.io.delta_time = 1.0 / 10000.0 if deltaTime <= 0.0 else deltaTime
            self.lastTime = currentTime

else:
    import imgui

    from imgui.integrations.opengl import ProgrammablePipelineRenderer

    class SDL3Renderer(ProgrammablePipelineRenderer):
        """Basic SDL3 integration implementation."""
        MOUSE_WHEEL_OFFSET_SCALE = 0.5

        @staticmethod
        def setCustomStyle() -> None:
            style = imgui.get_style()
            style.colors[imgui.COLOR_TEXT] = imgui.Vec4(1.00, 1.00, 1.00, 1.00)
            style.colors[imgui.COLOR_TEXT_DISABLED] = imgui.Vec4(0.50, 0.50, 0.50, 1.00)
            style.colors[imgui.COLOR_WINDOW_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.39)
            style.colors[imgui.COLOR_CHILD_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.00)
            style.colors[imgui.COLOR_POPUP_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.63)
            style.colors[imgui.COLOR_BORDER] = imgui.Vec4(1.00, 1.00, 1.00, 0.31)
            style.colors[imgui.COLOR_BORDER_SHADOW] = imgui.Vec4(0.00, 0.00, 0.00, 0.00)
            style.colors[imgui.COLOR_FRAME_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.63)
            style.colors[imgui.COLOR_FRAME_BACKGROUND_HOVERED] = imgui.Vec4(0.23, 0.23, 0.23, 0.63)
            style.colors[imgui.COLOR_FRAME_BACKGROUND_ACTIVE] = imgui.Vec4(0.19, 0.19, 0.19, 0.39)
            style.colors[imgui.COLOR_TITLE_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.63)
            style.colors[imgui.COLOR_TITLE_BACKGROUND_ACTIVE] = imgui.Vec4(0.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_TITLE_BACKGROUND_COLLAPSED] = imgui.Vec4(0.00, 0.00, 0.00, 0.35)
            style.colors[imgui.COLOR_MENUBAR_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.78)
            style.colors[imgui.COLOR_SCROLLBAR_BACKGROUND] = imgui.Vec4(0.05, 0.05, 0.05, 0.54)
            style.colors[imgui.COLOR_SCROLLBAR_GRAB] = imgui.Vec4(0.34, 0.34, 0.34, 0.63)
            style.colors[imgui.COLOR_SCROLLBAR_GRAB_HOVERED] = imgui.Vec4(0.50, 0.50, 0.50, 0.63)
            style.colors[imgui.COLOR_SCROLLBAR_GRAB_ACTIVE] = imgui.Vec4(0.38, 0.38, 0.38, 0.63)
            style.colors[imgui.COLOR_CHECK_MARK] = imgui.Vec4(0.22, 0.55, 0.74, 1.00)
            style.colors[imgui.COLOR_SLIDER_GRAB] = imgui.Vec4(0.34, 0.34, 0.34, 0.54)
            style.colors[imgui.COLOR_SLIDER_GRAB_ACTIVE] = imgui.Vec4(0.56, 0.56, 0.56, 0.54)
            style.colors[imgui.COLOR_BUTTON] = imgui.Vec4(0.00, 0.00, 0.00, 0.63)
            style.colors[imgui.COLOR_BUTTON_HOVERED] = imgui.Vec4(0.20, 0.22, 0.23, 0.63)
            style.colors[imgui.COLOR_BUTTON_ACTIVE] = imgui.Vec4(0.19, 0.19, 0.19, 0.39)
            style.colors[imgui.COLOR_HEADER] = imgui.Vec4(0.20, 0.20, 0.20, 0.78)
            style.colors[imgui.COLOR_HEADER_HOVERED] = imgui.Vec4(0.29, 0.29, 0.29, 0.78)
            style.colors[imgui.COLOR_HEADER_ACTIVE] = imgui.Vec4(0.19, 0.19, 0.19, 0.15)
            style.colors[imgui.COLOR_SEPARATOR] = imgui.Vec4(0.28, 0.28, 0.28, 0.29)
            style.colors[imgui.COLOR_SEPARATOR_HOVERED] = imgui.Vec4(0.44, 0.44, 0.44, 0.29)
            style.colors[imgui.COLOR_SEPARATOR_ACTIVE] = imgui.Vec4(0.40, 0.44, 0.47, 1.00)
            style.colors[imgui.COLOR_RESIZE_GRIP] = imgui.Vec4(0.28, 0.28, 0.28, 0.29)
            style.colors[imgui.COLOR_RESIZE_GRIP_HOVERED] = imgui.Vec4(0.44, 0.44, 0.44, 0.29)
            style.colors[imgui.COLOR_RESIZE_GRIP_ACTIVE] = imgui.Vec4(0.40, 0.44, 0.47, 1.00)
            style.colors[imgui.COLOR_TAB] = imgui.Vec4(0.00, 0.00, 0.00, 0.52)
            style.colors[imgui.COLOR_TAB_HOVERED] = imgui.Vec4(0.20, 0.20, 0.20, 0.36)
            style.colors[imgui.COLOR_TAB_ACTIVE] = imgui.Vec4(0.14, 0.14, 0.14, 1.00)
            style.colors[imgui.COLOR_TAB_UNFOCUSED] = imgui.Vec4(0.00, 0.00, 0.00, 0.52)
            style.colors[imgui.COLOR_TAB_UNFOCUSED_ACTIVE] = imgui.Vec4(0.14, 0.14, 0.14, 1.00)
            style.colors[imgui.COLOR_PLOT_LINES] = imgui.Vec4(1.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_PLOT_LINES_HOVERED] = imgui.Vec4(1.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_PLOT_HISTOGRAM] = imgui.Vec4(1.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_PLOT_HISTOGRAM_HOVERED] = imgui.Vec4(1.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_TABLE_HEADER_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.52)
            style.colors[imgui.COLOR_TABLE_BORDER_STRONG] = imgui.Vec4(0.00, 0.00, 0.00, 0.52)
            style.colors[imgui.COLOR_TABLE_BORDER_LIGHT] = imgui.Vec4(0.28, 0.28, 0.28, 0.29)
            style.colors[imgui.COLOR_TABLE_ROW_BACKGROUND] = imgui.Vec4(0.00, 0.00, 0.00, 0.00)
            style.colors[imgui.COLOR_TABLE_ROW_BACKGROUND_ALT] = imgui.Vec4(1.00, 1.00, 1.00, 0.06)
            style.colors[imgui.COLOR_TEXT_SELECTED_BACKGROUND] = imgui.Vec4(0.20, 0.22, 0.23, 1.00)
            style.colors[imgui.COLOR_DRAG_DROP_TARGET] = imgui.Vec4(0.33, 0.67, 0.86, 1.00)
            style.colors[imgui.COLOR_NAV_HIGHLIGHT] = imgui.Vec4(1.00, 0.00, 0.00, 1.00)
            style.colors[imgui.COLOR_NAV_WINDOWING_HIGHLIGHT] = imgui.Vec4(1.00, 0.00, 0.00, 0.70)
            style.colors[imgui.COLOR_NAV_WINDOWING_DIM_BACKGROUND] = imgui.Vec4(1.00, 0.00, 0.00, 0.20)
            style.colors[imgui.COLOR_MODAL_WINDOW_DIM_BACKGROUND] = imgui.Vec4(1.00, 0.00, 0.00, 0.35)

            style.window_padding = imgui.Vec2(6.0, 6.0)
            style.frame_padding = imgui.Vec2(5.0, 2.0)
            style.cell_padding = imgui.Vec2(6.0, 6.0)
            style.item_spacing = imgui.Vec2(6.0, 6.0)
            style.item_inner_spacing = imgui.Vec2(6.0, 6.0)
            style.touch_extra_padding = imgui.Vec2(0.0, 0.0)
            style.window_title_align = imgui.Vec2(0.5, 0.5)
            style.indent_spacing = 25.0
            style.scrollbar_size = 10.0
            style.grab_min_size = 10.0
            style.window_border_size = 1.0
            style.child_border_size = 1.0
            style.popup_border_size = 1.0
            style.frame_border_size = 1.0
            style.tab_border_size = 1.0
            style.window_rounding = 5.0
            style.child_rounding = 4.0
            style.frame_rounding = 2.0
            style.popup_rounding = 4.0
            style.scrollbar_rounding = 9.0
            style.grab_rounding = 2.0
            style.log_slider_deadzone = 4.0
            style.tab_rounding = 4.0

        def __init__(self, window: sdl3.LP_SDL_Window) -> None:
            super(SDL3Renderer, self).__init__()
            
            self.window = window
            self.lastTime = sdl3.SDL_GetTicks() / 1000.0
            self.io.get_clipboard_text_fn = lambda: sdl3.SDL_GetClipboardText()
            self.io.set_clipboard_text_fn = lambda text: sdl3.SDL_SetClipboardText(text.encode())
            sdl3.SDL_StartTextInput(window)

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
            if event.type in [sdl3.SDL_EVENT_MOUSE_WHEEL]:
                self.io.mouse_wheel = event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE

            if event.type in [sdl3.SDL_EVENT_MOUSE_BUTTON_UP, sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN]:
                buttons = [sdl3.SDL_BUTTON_LEFT, sdl3.SDL_BUTTON_RIGHT, sdl3.SDL_BUTTON_MIDDLE]

                if event.button.button in buttons:
                    self.io.mouse_down[buttons.index(event.button.button)] = event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN

            if event.type in [sdl3.SDL_EVENT_MOUSE_MOTION]:
                self.io.mouse_pos = (event.motion.x, event.motion.y) \
                    if sdl3.SDL_GetWindowFlags(self.window) & sdl3.SDL_WINDOW_MOUSE_FOCUS else (-1, -1)

            if event.type in [sdl3.SDL_EVENT_KEY_UP, sdl3.SDL_EVENT_KEY_DOWN]:
                if event.key.scancode < sdl3.SDL_SCANCODE_COUNT:
                    self.io.keys_down[event.key.scancode] = event.type == sdl3.SDL_EVENT_KEY_DOWN

                self.io.key_shift = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_SHIFT) != 0
                self.io.key_ctrl = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_CTRL) != 0
                self.io.key_alt = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_ALT) != 0
                self.io.key_super = (sdl3.SDL_GetModState() & sdl3.SDL_KMOD_GUI) != 0

            if event.type in [sdl3.SDL_EVENT_TEXT_INPUT]:
                for char in event.text.text.decode("utf-8"):
                    self.io.add_input_character(ord(char))

        def processInputs(self) -> None:
            width, height = ctypes.c_int(0), ctypes.c_int(0)
            sdl3.SDL_GetWindowSize(self.window, ctypes.byref(width), ctypes.byref(height))
            self.io.display_size, self.io.display_fb_scale = (width.value, height.value), (1, 1)
            self.io.mouse_wheel = 0
            
            currentTime = sdl3.SDL_GetTicks() / 1000.0; deltaTime = currentTime - self.lastTime
            self.io.delta_time = 1.0 / 10000.0 if deltaTime <= 0.0 else deltaTime
            self.lastTime = currentTime

@sdl3.SDL_main_func
def main(argc: ctypes.c_int, argv: sdl3.LP_c_char_p) -> ctypes.c_int:
    if not sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_EVENTS):
        print(f"failed to initialize library: {sdl3.SDL_GetError().decode().lower()}.")
        return -1
    
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_MINOR_VERSION, 6)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_PROFILE_MASK, sdl3.SDL_GL_CONTEXT_PROFILE_COMPATIBILITY)
    sdl3.SDL_GL_SetAttribute(sdl3.SDL_GL_CONTEXT_FLAGS, sdl3.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
    window = sdl3.SDL_CreateWindow("Aermoss".encode(), 1600, 900, sdl3.SDL_WINDOW_OPENGL | sdl3.SDL_WINDOW_RESIZABLE)

    if not window:
        print(f"failed to create window: {sdl3.SDL_GetError().decode().lower()}.", flush = True)
        return -1

    context = sdl3.SDL_GL_CreateContext(window)
    sdl3.SDL_GL_MakeCurrent(window, context)

    if not context:
        print(f"failed to create context: {sdl3.SDL_GetError().decode().lower()}.", flush = True)
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