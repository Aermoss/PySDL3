from .__init__ import ctypes, typing, abc, \
    SDL_FUNC_TYPE, SDL_ENUM, SDL_FUNC, SDL_TYPE, SDL_BINARY

SDL_HINT_ALLOW_ALT_TAB_WHILE_GRABBED: bytes = "SDL_ALLOW_ALT_TAB_WHILE_GRABBED".encode()
SDL_HINT_ANDROID_ALLOW_RECREATE_ACTIVITY: bytes = "SDL_ANDROID_ALLOW_RECREATE_ACTIVITY".encode()
SDL_HINT_ANDROID_BLOCK_ON_PAUSE: bytes = "SDL_ANDROID_BLOCK_ON_PAUSE".encode()
SDL_HINT_ANDROID_LOW_LATENCY_AUDIO: bytes = "SDL_ANDROID_LOW_LATENCY_AUDIO".encode()
SDL_HINT_ANDROID_TRAP_BACK_BUTTON: bytes = "SDL_ANDROID_TRAP_BACK_BUTTON".encode()
SDL_HINT_APP_ID: bytes = "SDL_APP_ID".encode()
SDL_HINT_APP_NAME: bytes = "SDL_APP_NAME".encode()
SDL_HINT_APPLE_TV_CONTROLLER_UI_EVENTS: bytes = "SDL_APPLE_TV_CONTROLLER_UI_EVENTS".encode()
SDL_HINT_APPLE_TV_REMOTE_ALLOW_ROTATION: bytes = "SDL_APPLE_TV_REMOTE_ALLOW_ROTATION".encode()
SDL_HINT_AUDIO_ALSA_DEFAULT_DEVICE: bytes = "SDL_AUDIO_ALSA_DEFAULT_DEVICE".encode()
SDL_HINT_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE: bytes = "SDL_AUDIO_ALSA_DEFAULT_PLAYBACK_DEVICE".encode()
SDL_HINT_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE: bytes = "SDL_AUDIO_ALSA_DEFAULT_RECORDING_DEVICE".encode()
SDL_HINT_AUDIO_CATEGORY: bytes = "SDL_AUDIO_CATEGORY".encode()
SDL_HINT_AUDIO_CHANNELS: bytes = "SDL_AUDIO_CHANNELS".encode()
SDL_HINT_AUDIO_DEVICE_APP_ICON_NAME: bytes = "SDL_AUDIO_DEVICE_APP_ICON_NAME".encode()
SDL_HINT_AUDIO_DEVICE_SAMPLE_FRAMES: bytes = "SDL_AUDIO_DEVICE_SAMPLE_FRAMES".encode()
SDL_HINT_AUDIO_DEVICE_STREAM_NAME: bytes = "SDL_AUDIO_DEVICE_STREAM_NAME".encode()
SDL_HINT_AUDIO_DEVICE_STREAM_ROLE: bytes = "SDL_AUDIO_DEVICE_STREAM_ROLE".encode()
SDL_HINT_AUDIO_DISK_INPUT_FILE: bytes = "SDL_AUDIO_DISK_INPUT_FILE".encode()
SDL_HINT_AUDIO_DISK_OUTPUT_FILE: bytes = "SDL_AUDIO_DISK_OUTPUT_FILE".encode()
SDL_HINT_AUDIO_DISK_TIMESCALE: bytes = "SDL_AUDIO_DISK_TIMESCALE".encode()
SDL_HINT_AUDIO_DRIVER: bytes = "SDL_AUDIO_DRIVER".encode()
SDL_HINT_AUDIO_DUMMY_TIMESCALE: bytes = "SDL_AUDIO_DUMMY_TIMESCALE".encode()
SDL_HINT_AUDIO_FORMAT: bytes = "SDL_AUDIO_FORMAT".encode()
SDL_HINT_AUDIO_FREQUENCY: bytes = "SDL_AUDIO_FREQUENCY".encode()
SDL_HINT_AUDIO_INCLUDE_MONITORS: bytes = "SDL_AUDIO_INCLUDE_MONITORS".encode()
SDL_HINT_AUTO_UPDATE_JOYSTICKS: bytes = "SDL_AUTO_UPDATE_JOYSTICKS".encode()
SDL_HINT_AUTO_UPDATE_SENSORS: bytes = "SDL_AUTO_UPDATE_SENSORS".encode()
SDL_HINT_BMP_SAVE_LEGACY_FORMAT: bytes = "SDL_BMP_SAVE_LEGACY_FORMAT".encode()
SDL_HINT_CAMERA_DRIVER: bytes = "SDL_CAMERA_DRIVER".encode()
SDL_HINT_CPU_FEATURE_MASK: bytes = "SDL_CPU_FEATURE_MASK".encode()
SDL_HINT_JOYSTICK_DIRECTINPUT: bytes = "SDL_JOYSTICK_DIRECTINPUT".encode()
SDL_HINT_FILE_DIALOG_DRIVER: bytes = "SDL_FILE_DIALOG_DRIVER".encode()
SDL_HINT_DISPLAY_USABLE_BOUNDS: bytes = "SDL_DISPLAY_USABLE_BOUNDS".encode()
SDL_HINT_EMSCRIPTEN_ASYNCIFY: bytes = "SDL_EMSCRIPTEN_ASYNCIFY".encode()
SDL_HINT_EMSCRIPTEN_CANVAS_SELECTOR: bytes = "SDL_EMSCRIPTEN_CANVAS_SELECTOR".encode()
SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT: bytes = "SDL_EMSCRIPTEN_KEYBOARD_ELEMENT".encode()
SDL_HINT_ENABLE_SCREEN_KEYBOARD: bytes = "SDL_ENABLE_SCREEN_KEYBOARD".encode()
SDL_HINT_EVDEV_DEVICES: bytes = "SDL_EVDEV_DEVICES".encode()
SDL_HINT_EVENT_LOGGING: bytes = "SDL_EVENT_LOGGING".encode()
SDL_HINT_FORCE_RAISEWINDOW: bytes = "SDL_FORCE_RAISEWINDOW".encode()
SDL_HINT_FRAMEBUFFER_ACCELERATION: bytes = "SDL_FRAMEBUFFER_ACCELERATION".encode()
SDL_HINT_GAMECONTROLLERCONFIG: bytes = "SDL_GAMECONTROLLERCONFIG".encode()
SDL_HINT_GAMECONTROLLERCONFIG_FILE: bytes = "SDL_GAMECONTROLLERCONFIG_FILE".encode()
SDL_HINT_GAMECONTROLLERTYPE: bytes = "SDL_GAMECONTROLLERTYPE".encode()
SDL_HINT_GAMECONTROLLER_IGNORE_DEVICES: bytes = "SDL_GAMECONTROLLER_IGNORE_DEVICES".encode()
SDL_HINT_GAMECONTROLLER_IGNORE_DEVICES_EXCEPT: bytes = "SDL_GAMECONTROLLER_IGNORE_DEVICES_EXCEPT".encode()
SDL_HINT_GAMECONTROLLER_SENSOR_FUSION: bytes = "SDL_GAMECONTROLLER_SENSOR_FUSION".encode()
SDL_HINT_GDK_TEXTINPUT_DEFAULT_TEXT: bytes = "SDL_GDK_TEXTINPUT_DEFAULT_TEXT".encode()
SDL_HINT_GDK_TEXTINPUT_DESCRIPTION: bytes = "SDL_GDK_TEXTINPUT_DESCRIPTION".encode()
SDL_HINT_GDK_TEXTINPUT_MAX_LENGTH: bytes = "SDL_GDK_TEXTINPUT_MAX_LENGTH".encode()
SDL_HINT_GDK_TEXTINPUT_SCOPE: bytes = "SDL_GDK_TEXTINPUT_SCOPE".encode()
SDL_HINT_GDK_TEXTINPUT_TITLE: bytes = "SDL_GDK_TEXTINPUT_TITLE".encode()
SDL_HINT_HIDAPI_LIBUSB: bytes = "SDL_HIDAPI_LIBUSB".encode()
SDL_HINT_HIDAPI_LIBUSB_WHITELIST: bytes = "SDL_HIDAPI_LIBUSB_WHITELIST".encode()
SDL_HINT_HIDAPI_UDEV: bytes = "SDL_HIDAPI_UDEV".encode()
SDL_HINT_GPU_DRIVER: bytes = "SDL_GPU_DRIVER".encode()
SDL_HINT_HIDAPI_ENUMERATE_ONLY_CONTROLLERS: bytes = "SDL_HIDAPI_ENUMERATE_ONLY_CONTROLLERS".encode()
SDL_HINT_HIDAPI_IGNORE_DEVICES: bytes = "SDL_HIDAPI_IGNORE_DEVICES".encode()
SDL_HINT_IME_IMPLEMENTED_UI: bytes = "SDL_IME_IMPLEMENTED_UI".encode()
SDL_HINT_IOS_HIDE_HOME_INDICATOR: bytes = "SDL_IOS_HIDE_HOME_INDICATOR".encode()
SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS: bytes = "SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS".encode()
SDL_HINT_JOYSTICK_ARCADESTICK_DEVICES: bytes = "SDL_JOYSTICK_ARCADESTICK_DEVICES".encode()
SDL_HINT_JOYSTICK_ARCADESTICK_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_ARCADESTICK_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_BLACKLIST_DEVICES: bytes = "SDL_JOYSTICK_BLACKLIST_DEVICES".encode()
SDL_HINT_JOYSTICK_BLACKLIST_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_BLACKLIST_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_DEVICE: bytes = "SDL_JOYSTICK_DEVICE".encode()
SDL_HINT_JOYSTICK_ENHANCED_REPORTS: bytes = "SDL_JOYSTICK_ENHANCED_REPORTS".encode()
SDL_HINT_JOYSTICK_FLIGHTSTICK_DEVICES: bytes = "SDL_JOYSTICK_FLIGHTSTICK_DEVICES".encode()
SDL_HINT_JOYSTICK_FLIGHTSTICK_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_FLIGHTSTICK_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_GAMEINPUT: bytes = "SDL_JOYSTICK_GAMEINPUT".encode()
SDL_HINT_JOYSTICK_GAMECUBE_DEVICES: bytes = "SDL_JOYSTICK_GAMECUBE_DEVICES".encode()
SDL_HINT_JOYSTICK_GAMECUBE_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_GAMECUBE_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_HIDAPI: bytes = "SDL_JOYSTICK_HIDAPI".encode()
SDL_HINT_JOYSTICK_HIDAPI_COMBINE_JOY_CONS: bytes = "SDL_JOYSTICK_HIDAPI_COMBINE_JOY_CONS".encode()
SDL_HINT_JOYSTICK_HIDAPI_GAMECUBE: bytes = "SDL_JOYSTICK_HIDAPI_GAMECUBE".encode()
SDL_HINT_JOYSTICK_HIDAPI_GAMECUBE_RUMBLE_BRAKE: bytes = "SDL_JOYSTICK_HIDAPI_GAMECUBE_RUMBLE_BRAKE".encode()
SDL_HINT_JOYSTICK_HIDAPI_JOY_CONS: bytes = "SDL_JOYSTICK_HIDAPI_JOY_CONS".encode()
SDL_HINT_JOYSTICK_HIDAPI_JOYCON_HOME_LED: bytes = "SDL_JOYSTICK_HIDAPI_JOYCON_HOME_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_LUNA: bytes = "SDL_JOYSTICK_HIDAPI_LUNA".encode()
SDL_HINT_JOYSTICK_HIDAPI_NINTENDO_CLASSIC: bytes = "SDL_JOYSTICK_HIDAPI_NINTENDO_CLASSIC".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS3: bytes = "SDL_JOYSTICK_HIDAPI_PS3".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS3_SIXAXIS_DRIVER: bytes = "SDL_JOYSTICK_HIDAPI_PS3_SIXAXIS_DRIVER".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS4: bytes = "SDL_JOYSTICK_HIDAPI_PS4".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS4_REPORT_INTERVAL: bytes = "SDL_JOYSTICK_HIDAPI_PS4_REPORT_INTERVAL".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS5: bytes = "SDL_JOYSTICK_HIDAPI_PS5".encode()
SDL_HINT_JOYSTICK_HIDAPI_PS5_PLAYER_LED: bytes = "SDL_JOYSTICK_HIDAPI_PS5_PLAYER_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_SHIELD: bytes = "SDL_JOYSTICK_HIDAPI_SHIELD".encode()
SDL_HINT_JOYSTICK_HIDAPI_STADIA: bytes = "SDL_JOYSTICK_HIDAPI_STADIA".encode()
SDL_HINT_JOYSTICK_HIDAPI_STEAM: bytes = "SDL_JOYSTICK_HIDAPI_STEAM".encode()
SDL_HINT_JOYSTICK_HIDAPI_STEAM_HOME_LED: bytes = "SDL_JOYSTICK_HIDAPI_STEAM_HOME_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_STEAMDECK: bytes = "SDL_JOYSTICK_HIDAPI_STEAMDECK".encode()
SDL_HINT_JOYSTICK_HIDAPI_STEAM_HORI: bytes = "SDL_JOYSTICK_HIDAPI_STEAM_HORI".encode()
SDL_HINT_JOYSTICK_HIDAPI_SWITCH: bytes = "SDL_JOYSTICK_HIDAPI_SWITCH".encode()
SDL_HINT_JOYSTICK_HIDAPI_SWITCH_HOME_LED: bytes = "SDL_JOYSTICK_HIDAPI_SWITCH_HOME_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_SWITCH_PLAYER_LED: bytes = "SDL_JOYSTICK_HIDAPI_SWITCH_PLAYER_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_VERTICAL_JOY_CONS: bytes = "SDL_JOYSTICK_HIDAPI_VERTICAL_JOY_CONS".encode()
SDL_HINT_JOYSTICK_HIDAPI_WII: bytes = "SDL_JOYSTICK_HIDAPI_WII".encode()
SDL_HINT_JOYSTICK_HIDAPI_WII_PLAYER_LED: bytes = "SDL_JOYSTICK_HIDAPI_WII_PLAYER_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX: bytes = "SDL_JOYSTICK_HIDAPI_XBOX".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX_360: bytes = "SDL_JOYSTICK_HIDAPI_XBOX_360".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_PLAYER_LED: bytes = "SDL_JOYSTICK_HIDAPI_XBOX_360_PLAYER_LED".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_WIRELESS: bytes = "SDL_JOYSTICK_HIDAPI_XBOX_360_WIRELESS".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX_ONE: bytes = "SDL_JOYSTICK_HIDAPI_XBOX_ONE".encode()
SDL_HINT_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED: bytes = "SDL_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED".encode()
SDL_HINT_JOYSTICK_IOKIT: bytes = "SDL_JOYSTICK_IOKIT".encode()
SDL_HINT_JOYSTICK_LINUX_CLASSIC: bytes = "SDL_JOYSTICK_LINUX_CLASSIC".encode()
SDL_HINT_JOYSTICK_LINUX_DEADZONES: bytes = "SDL_JOYSTICK_LINUX_DEADZONES".encode()
SDL_HINT_JOYSTICK_LINUX_DIGITAL_HATS: bytes = "SDL_JOYSTICK_LINUX_DIGITAL_HATS".encode()
SDL_HINT_JOYSTICK_LINUX_HAT_DEADZONES: bytes = "SDL_JOYSTICK_LINUX_HAT_DEADZONES".encode()
SDL_HINT_JOYSTICK_MFI: bytes = "SDL_JOYSTICK_MFI".encode()
SDL_HINT_JOYSTICK_RAWINPUT: bytes = "SDL_JOYSTICK_RAWINPUT".encode()
SDL_HINT_JOYSTICK_RAWINPUT_CORRELATE_XINPUT: bytes = "SDL_JOYSTICK_RAWINPUT_CORRELATE_XINPUT".encode()
SDL_HINT_JOYSTICK_ROG_CHAKRAM: bytes = "SDL_JOYSTICK_ROG_CHAKRAM".encode()
SDL_HINT_JOYSTICK_THREAD: bytes = "SDL_JOYSTICK_THREAD".encode()
SDL_HINT_JOYSTICK_THROTTLE_DEVICES: bytes = "SDL_JOYSTICK_THROTTLE_DEVICES".encode()
SDL_HINT_JOYSTICK_THROTTLE_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_THROTTLE_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_WGI: bytes = "SDL_JOYSTICK_WGI".encode()
SDL_HINT_JOYSTICK_WHEEL_DEVICES: bytes = "SDL_JOYSTICK_WHEEL_DEVICES".encode()
SDL_HINT_JOYSTICK_WHEEL_DEVICES_EXCLUDED: bytes = "SDL_JOYSTICK_WHEEL_DEVICES_EXCLUDED".encode()
SDL_HINT_JOYSTICK_ZERO_CENTERED_DEVICES: bytes = "SDL_JOYSTICK_ZERO_CENTERED_DEVICES".encode()
SDL_HINT_JOYSTICK_HAPTIC_AXES: bytes = "SDL_JOYSTICK_HAPTIC_AXES".encode()
SDL_HINT_KEYCODE_OPTIONS: bytes = "SDL_KEYCODE_OPTIONS".encode()
SDL_HINT_KMSDRM_DEVICE_INDEX: bytes = "SDL_KMSDRM_DEVICE_INDEX".encode()
SDL_HINT_KMSDRM_REQUIRE_DRM_MASTER: bytes = "SDL_KMSDRM_REQUIRE_DRM_MASTER".encode()
SDL_HINT_LOGGING: bytes = "SDL_LOGGING".encode()
SDL_HINT_MAC_BACKGROUND_APP: bytes = "SDL_MAC_BACKGROUND_APP".encode()
SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK: bytes = "SDL_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK".encode()
SDL_HINT_MAC_OPENGL_ASYNC_DISPATCH: bytes = "SDL_MAC_OPENGL_ASYNC_DISPATCH".encode()
SDL_HINT_MAC_OPTION_AS_ALT: bytes = "SDL_MAC_OPTION_AS_ALT".encode()
SDL_HINT_MAC_SCROLL_MOMENTUM: bytes = "SDL_MAC_SCROLL_MOMENTUM".encode()
SDL_HINT_MAIN_CALLBACK_RATE: bytes = "SDL_MAIN_CALLBACK_RATE".encode()
SDL_HINT_MOUSE_AUTO_CAPTURE: bytes = "SDL_MOUSE_AUTO_CAPTURE".encode()
SDL_HINT_MOUSE_DOUBLE_CLICK_RADIUS: bytes = "SDL_MOUSE_DOUBLE_CLICK_RADIUS".encode()
SDL_HINT_MOUSE_DOUBLE_CLICK_TIME: bytes = "SDL_MOUSE_DOUBLE_CLICK_TIME".encode()
SDL_HINT_MOUSE_DEFAULT_SYSTEM_CURSOR: bytes = "SDL_MOUSE_DEFAULT_SYSTEM_CURSOR".encode()
SDL_HINT_MOUSE_EMULATE_WARP_WITH_RELATIVE: bytes = "SDL_MOUSE_EMULATE_WARP_WITH_RELATIVE".encode()
SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH: bytes = "SDL_MOUSE_FOCUS_CLICKTHROUGH".encode()
SDL_HINT_MOUSE_NORMAL_SPEED_SCALE: bytes = "SDL_MOUSE_NORMAL_SPEED_SCALE".encode()
SDL_HINT_MOUSE_RELATIVE_MODE_CENTER: bytes = "SDL_MOUSE_RELATIVE_MODE_CENTER".encode()
SDL_HINT_MOUSE_RELATIVE_SPEED_SCALE: bytes = "SDL_MOUSE_RELATIVE_SPEED_SCALE".encode()
SDL_HINT_MOUSE_RELATIVE_SYSTEM_SCALE: bytes = "SDL_MOUSE_RELATIVE_SYSTEM_SCALE".encode()
SDL_HINT_MOUSE_RELATIVE_WARP_MOTION: bytes = "SDL_MOUSE_RELATIVE_WARP_MOTION".encode()
SDL_HINT_MOUSE_RELATIVE_CURSOR_VISIBLE: bytes = "SDL_MOUSE_RELATIVE_CURSOR_VISIBLE".encode()
SDL_HINT_MOUSE_TOUCH_EVENTS: bytes = "SDL_MOUSE_TOUCH_EVENTS".encode()
SDL_HINT_MUTE_CONSOLE_KEYBOARD: bytes = "SDL_MUTE_CONSOLE_KEYBOARD".encode()
SDL_HINT_NO_SIGNAL_HANDLERS: bytes = "SDL_NO_SIGNAL_HANDLERS".encode()
SDL_HINT_OPENGL_LIBRARY: bytes = "SDL_OPENGL_LIBRARY".encode()
SDL_HINT_EGL_LIBRARY: bytes = "SDL_OPENGL_LIBRARY".encode()
SDL_HINT_OPENGL_ES_DRIVER: bytes = "SDL_OPENGL_ES_DRIVER".encode()
SDL_HINT_OPENVR_LIBRARY: bytes = "SDL_OPENVR_LIBRARY".encode()
SDL_HINT_ORIENTATIONS: bytes = "SDL_ORIENTATIONS".encode()
SDL_HINT_PEN_DELAY_MOUSE_BUTTON: bytes = "SDL_PEN_DELAY_MOUSE_BUTTON".encode()
SDL_HINT_PEN_NOT_MOUSE: bytes = "SDL_PEN_NOT_MOUSE".encode()
SDL_HINT_POLL_SENTINEL: bytes = "SDL_POLL_SENTINEL".encode()
SDL_HINT_PREFERRED_LOCALES: bytes = "SDL_PREFERRED_LOCALES".encode()
SDL_HINT_QUIT_ON_LAST_WINDOW_CLOSE: bytes = "SDL_QUIT_ON_LAST_WINDOW_CLOSE".encode()
SDL_HINT_RENDER_DIRECT3D_THREADSAFE: bytes = "SDL_RENDER_DIRECT3D_THREADSAFE".encode()
SDL_HINT_RENDER_DIRECT3D11_DEBUG: bytes = "SDL_RENDER_DIRECT3D11_DEBUG".encode()
SDL_HINT_RENDER_VULKAN_DEBUG: bytes = "SDL_RENDER_VULKAN_DEBUG".encode()
SDL_HINT_RENDER_GPU_DEBUG: bytes = "SDL_RENDER_GPU_DEBUG".encode()
SDL_HINT_RENDER_GPU_LOW_POWER: bytes = "SDL_RENDER_GPU_LOW_POWER".encode()
SDL_HINT_RENDER_DRIVER: bytes = "SDL_RENDER_DRIVER".encode()
SDL_HINT_RENDER_LINE_METHOD: bytes = "SDL_RENDER_LINE_METHOD".encode()
SDL_HINT_RENDER_METAL_PREFER_LOW_POWER_DEVICE: bytes = "SDL_RENDER_METAL_PREFER_LOW_POWER_DEVICE".encode()
SDL_HINT_RENDER_VSYNC: bytes = "SDL_RENDER_VSYNC".encode()
SDL_HINT_RETURN_KEY_HIDES_IME: bytes = "SDL_RETURN_KEY_HIDES_IME".encode()
SDL_HINT_ROG_GAMEPAD_MICE: bytes = "SDL_ROG_GAMEPAD_MICE".encode()
SDL_HINT_ROG_GAMEPAD_MICE_EXCLUDED: bytes = "SDL_ROG_GAMEPAD_MICE_EXCLUDED".encode()
SDL_HINT_RPI_VIDEO_LAYER: bytes = "SDL_RPI_VIDEO_LAYER".encode()
SDL_HINT_SCREENSAVER_INHIBIT_ACTIVITY_NAME: bytes = "SDL_SCREENSAVER_INHIBIT_ACTIVITY_NAME".encode()
SDL_HINT_SHUTDOWN_DBUS_ON_QUIT: bytes = "SDL_SHUTDOWN_DBUS_ON_QUIT".encode()
SDL_HINT_STORAGE_TITLE_DRIVER: bytes = "SDL_STORAGE_TITLE_DRIVER".encode()
SDL_HINT_STORAGE_USER_DRIVER: bytes = "SDL_STORAGE_USER_DRIVER".encode()
SDL_HINT_THREAD_FORCE_REALTIME_TIME_CRITICAL: bytes = "SDL_THREAD_FORCE_REALTIME_TIME_CRITICAL".encode()
SDL_HINT_THREAD_PRIORITY_POLICY: bytes = "SDL_THREAD_PRIORITY_POLICY".encode()
SDL_HINT_TIMER_RESOLUTION: bytes = "SDL_TIMER_RESOLUTION".encode()
SDL_HINT_TOUCH_MOUSE_EVENTS: bytes = "SDL_TOUCH_MOUSE_EVENTS".encode()
SDL_HINT_TRACKPAD_IS_TOUCH_ONLY: bytes = "SDL_TRACKPAD_IS_TOUCH_ONLY".encode()
SDL_HINT_TV_REMOTE_AS_JOYSTICK: bytes = "SDL_TV_REMOTE_AS_JOYSTICK".encode()
SDL_HINT_VIDEO_ALLOW_SCREENSAVER: bytes = "SDL_VIDEO_ALLOW_SCREENSAVER".encode()
SDL_HINT_VIDEO_DISPLAY_PRIORITY: bytes = "SDL_VIDEO_DISPLAY_PRIORITY".encode()
SDL_HINT_VIDEO_DOUBLE_BUFFER: bytes = "SDL_VIDEO_DOUBLE_BUFFER".encode()
SDL_HINT_VIDEO_DRIVER: bytes = "SDL_VIDEO_DRIVER".encode()
SDL_HINT_VIDEO_DUMMY_SAVE_FRAMES: bytes = "SDL_VIDEO_DUMMY_SAVE_FRAMES".encode()
SDL_HINT_VIDEO_EGL_ALLOW_GETDISPLAY_FALLBACK: bytes = "SDL_VIDEO_EGL_ALLOW_GETDISPLAY_FALLBACK".encode()
SDL_HINT_VIDEO_FORCE_EGL: bytes = "SDL_VIDEO_FORCE_EGL".encode()
SDL_HINT_VIDEO_MAC_FULLSCREEN_SPACES: bytes = "SDL_VIDEO_MAC_FULLSCREEN_SPACES".encode()
SDL_HINT_VIDEO_MAC_FULLSCREEN_MENU_VISIBILITY: bytes = "SDL_VIDEO_MAC_FULLSCREEN_MENU_VISIBILITY".encode()
SDL_HINT_VIDEO_MINIMIZE_ON_FOCUS_LOSS: bytes = "SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS".encode()
SDL_HINT_VIDEO_OFFSCREEN_SAVE_FRAMES: bytes = "SDL_VIDEO_OFFSCREEN_SAVE_FRAMES".encode()
SDL_HINT_VIDEO_SYNC_WINDOW_OPERATIONS: bytes = "SDL_VIDEO_SYNC_WINDOW_OPERATIONS".encode()
SDL_HINT_VIDEO_WAYLAND_ALLOW_LIBDECOR: bytes = "SDL_VIDEO_WAYLAND_ALLOW_LIBDECOR".encode()
SDL_HINT_VIDEO_WAYLAND_MODE_EMULATION: bytes = "SDL_VIDEO_WAYLAND_MODE_EMULATION".encode()
SDL_HINT_VIDEO_WAYLAND_MODE_SCALING: bytes = "SDL_VIDEO_WAYLAND_MODE_SCALING".encode()
SDL_HINT_VIDEO_WAYLAND_PREFER_LIBDECOR: bytes = "SDL_VIDEO_WAYLAND_PREFER_LIBDECOR".encode()
SDL_HINT_VIDEO_WAYLAND_SCALE_TO_DISPLAY: bytes = "SDL_VIDEO_WAYLAND_SCALE_TO_DISPLAY".encode()
SDL_HINT_VIDEO_WIN_D3DCOMPILER: bytes = "SDL_VIDEO_WIN_D3DCOMPILER".encode()
SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR: bytes = "SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR".encode()
SDL_HINT_VIDEO_X11_NET_WM_PING: bytes = "SDL_VIDEO_X11_NET_WM_PING".encode()
SDL_HINT_VIDEO_X11_NODIRECTCOLOR: bytes = "SDL_VIDEO_X11_NODIRECTCOLOR".encode()
SDL_HINT_VIDEO_X11_SCALING_FACTOR: bytes = "SDL_VIDEO_X11_SCALING_FACTOR".encode()
SDL_HINT_VIDEO_X11_VISUALID: bytes = "SDL_VIDEO_X11_VISUALID".encode()
SDL_HINT_VIDEO_X11_WINDOW_VISUALID: bytes = "SDL_VIDEO_X11_WINDOW_VISUALID".encode()
SDL_HINT_VIDEO_X11_XRANDR: bytes = "SDL_VIDEO_X11_XRANDR".encode()
SDL_HINT_VITA_ENABLE_BACK_TOUCH: bytes = "SDL_VITA_ENABLE_BACK_TOUCH".encode()
SDL_HINT_VITA_ENABLE_FRONT_TOUCH: bytes = "SDL_VITA_ENABLE_FRONT_TOUCH".encode()
SDL_HINT_VITA_MODULE_PATH: bytes = "SDL_VITA_MODULE_PATH".encode()
SDL_HINT_VITA_PVR_INIT: bytes = "SDL_VITA_PVR_INIT".encode()
SDL_HINT_VITA_RESOLUTION: bytes = "SDL_VITA_RESOLUTION".encode()
SDL_HINT_VITA_PVR_OPENGL: bytes = "SDL_VITA_PVR_OPENGL".encode()
SDL_HINT_VITA_TOUCH_MOUSE_DEVICE: bytes = "SDL_VITA_TOUCH_MOUSE_DEVICE".encode()
SDL_HINT_VULKAN_DISPLAY: bytes = "SDL_VULKAN_DISPLAY".encode()
SDL_HINT_VULKAN_LIBRARY: bytes = "SDL_VULKAN_LIBRARY".encode()
SDL_HINT_WAVE_FACT_CHUNK: bytes = "SDL_WAVE_FACT_CHUNK".encode()
SDL_HINT_WAVE_CHUNK_LIMIT: bytes = "SDL_WAVE_CHUNK_LIMIT".encode()
SDL_HINT_WAVE_RIFF_CHUNK_SIZE: bytes = "SDL_WAVE_RIFF_CHUNK_SIZE".encode()
SDL_HINT_WAVE_TRUNCATION: bytes = "SDL_WAVE_TRUNCATION".encode()
SDL_HINT_WINDOW_ACTIVATE_WHEN_RAISED: bytes = "SDL_WINDOW_ACTIVATE_WHEN_RAISED".encode()
SDL_HINT_WINDOW_ACTIVATE_WHEN_SHOWN: bytes = "SDL_WINDOW_ACTIVATE_WHEN_SHOWN".encode()
SDL_HINT_WINDOW_ALLOW_TOPMOST: bytes = "SDL_WINDOW_ALLOW_TOPMOST".encode()
SDL_HINT_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN: bytes = "SDL_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN".encode()
SDL_HINT_WINDOWS_CLOSE_ON_ALT_F4: bytes = "SDL_WINDOWS_CLOSE_ON_ALT_F4".encode()
SDL_HINT_WINDOWS_ENABLE_MENU_MNEMONICS: bytes = "SDL_WINDOWS_ENABLE_MENU_MNEMONICS".encode()
SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP: bytes = "SDL_WINDOWS_ENABLE_MESSAGELOOP".encode()
SDL_HINT_WINDOWS_GAMEINPUT: bytes = "SDL_WINDOWS_GAMEINPUT".encode()
SDL_HINT_WINDOWS_RAW_KEYBOARD: bytes = "SDL_WINDOWS_RAW_KEYBOARD".encode()
SDL_HINT_WINDOWS_FORCE_SEMAPHORE_KERNEL: bytes = "SDL_WINDOWS_FORCE_SEMAPHORE_KERNEL".encode()
SDL_HINT_WINDOWS_INTRESOURCE_ICON: bytes = "SDL_WINDOWS_INTRESOURCE_ICON".encode()
SDL_HINT_WINDOWS_INTRESOURCE_ICON_SMALL: bytes = "SDL_WINDOWS_INTRESOURCE_ICON_SMALL".encode()
SDL_HINT_WINDOWS_USE_D3D9EX: bytes = "SDL_WINDOWS_USE_D3D9EX".encode()
SDL_HINT_WINDOWS_ERASE_BACKGROUND_MODE: bytes = "SDL_WINDOWS_ERASE_BACKGROUND_MODE".encode()
SDL_HINT_X11_FORCE_OVERRIDE_REDIRECT: bytes = "SDL_X11_FORCE_OVERRIDE_REDIRECT".encode()
SDL_HINT_X11_WINDOW_TYPE: bytes = "SDL_X11_WINDOW_TYPE".encode()
SDL_HINT_X11_XCB_LIBRARY: bytes = "SDL_X11_XCB_LIBRARY".encode()
SDL_HINT_XINPUT_ENABLED: bytes = "SDL_XINPUT_ENABLED".encode()
SDL_HINT_ASSERT: bytes = "SDL_ASSERT".encode()
SDL_HINT_PEN_MOUSE_EVENTS: bytes = "SDL_PEN_MOUSE_EVENTS".encode()
SDL_HINT_PEN_TOUCH_EVENTS: bytes = "SDL_PEN_TOUCH_EVENTS".encode()

SDL_HintPriority: typing.TypeAlias = SDL_TYPE["SDL_HintPriority", SDL_ENUM]

SDL_HINT_DEFAULT, SDL_HINT_NORMAL, SDL_HINT_OVERRIDE = range(3)

SDL_SetHintWithPriority: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetHintWithPriority", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_char_p, SDL_HintPriority], SDL_BINARY]
SDL_SetHint: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_SetHint", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_char_p], SDL_BINARY]
SDL_ResetHint: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ResetHint", ctypes.c_bool, [ctypes.c_char_p], SDL_BINARY]
SDL_ResetHints: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_ResetHints", None, [], SDL_BINARY]
SDL_GetHint: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHint", ctypes.c_char_p, [ctypes.c_char_p], SDL_BINARY]
SDL_GetHintBoolean: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetHintBoolean", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_bool], SDL_BINARY]

SDL_HintCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_HintCallback", None, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]]

SDL_AddHintCallback: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_AddHintCallback", ctypes.c_bool, [ctypes.c_char_p, SDL_HintCallback, ctypes.c_void_p], SDL_BINARY]
SDL_RemoveHintCallback: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_RemoveHintCallback", None, [ctypes.c_char_p, SDL_HintCallback, ctypes.c_void_p], SDL_BINARY]