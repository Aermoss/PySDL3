from .__init__ import ctypes, SDL_FUNC

from .SDL_properties import SDL_PropertiesID
from .SDL_surface import SDL_Surface
from .SDL_pixels import SDL_PixelFormat
from .SDL_rect import SDL_Point, SDL_Rect

SDL_DisplayID = ctypes.c_uint32
SDL_WindowID = ctypes.c_uint32

SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER = "SDL.video.wayland.wl_display"

SDL_SystemTheme = ctypes.c_int

SDL_SYSTEM_THEME_UNKNOWN = 0
SDL_SYSTEM_THEME_LIGHT = 1
SDL_SYSTEM_THEME_DARK = 2

class SDL_DisplayModeData(ctypes.Structure):
    ...

class SDL_DisplayMode(ctypes.Structure):
    _fields_ = [
        ("displayID", SDL_DisplayID),
        ("format", SDL_PixelFormat),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pixel_density", ctypes.c_float),
        ("refresh_rate", ctypes.c_float),
        ("refresh_rate_numerator", ctypes.c_int),
        ("refresh_rate_denominator", ctypes.c_int),
        ("internal", ctypes.POINTER(SDL_DisplayModeData))
    ]

SDL_DisplayOrientation = ctypes.c_int

SDL_ORIENTATION_UNKNOWN = 0
SDL_ORIENTATION_LANDSCAPE = 1
SDL_ORIENTATION_LANDSCAPE_FLIPPED = 2
SDL_ORIENTATION_PORTRAIT = 3
SDL_ORIENTATION_PORTRAIT_FLIPPED = 4

class SDL_Window(ctypes.Structure):
    ...

SDL_WindowFlags = ctypes.c_uint64

SDL_WINDOW_FULLSCREEN = 0x0000000000000001
SDL_WINDOW_OPENGL = 0x0000000000000002
SDL_WINDOW_OCCLUDED = 0x0000000000000004
SDL_WINDOW_HIDDEN = 0x0000000000000008
SDL_WINDOW_BORDERLESS = 0x0000000000000010
SDL_WINDOW_RESIZABLE = 0x0000000000000020
SDL_WINDOW_MINIMIZED = 0x0000000000000040
SDL_WINDOW_MAXIMIZED = 0x0000000000000080
SDL_WINDOW_MOUSE_GRABBED = 0x0000000000000100
SDL_WINDOW_INPUT_FOCUS = 0x0000000000000200
SDL_WINDOW_MOUSE_FOCUS = 0x0000000000000400
SDL_WINDOW_EXTERNAL = 0x0000000000000800
SDL_WINDOW_MODAL = 0x0000000000001000
SDL_WINDOW_HIGH_PIXEL_DENSITY = 0x0000000000002000
SDL_WINDOW_MOUSE_CAPTURE = 0x0000000000004000
SDL_WINDOW_MOUSE_RELATIVE_MODE = 0x0000000000008000
SDL_WINDOW_ALWAYS_ON_TOP = 0x0000000000010000
SDL_WINDOW_UTILITY = 0x0000000000020000
SDL_WINDOW_TOOLTIP = 0x0000000000040000
SDL_WINDOW_POPUP_MENU = 0x0000000000080000
SDL_WINDOW_KEYBOARD_GRABBED = 0x0000000000100000
SDL_WINDOW_VULKAN = 0x0000000010000000
SDL_WINDOW_METAL = 0x0000000020000000
SDL_WINDOW_TRANSPARENT = 0x0000000040000000
SDL_WINDOW_NOT_FOCUSABLE = 0x0000000080000000

SDL_WINDOWPOS_UNDEFINED_MASK = 0x1FFF0000
SDL_WINDOWPOS_UNDEFINED_DISPLAY = lambda x: SDL_WINDOWPOS_UNDEFINED_MASK | x
SDL_WINDOWPOS_UNDEFINED = SDL_WINDOWPOS_UNDEFINED_DISPLAY(0)
SDL_WINDOWPOS_ISUNDEFINED = lambda x: (x & 0xFFFF0000) == SDL_WINDOWPOS_UNDEFINED_MASK

SDL_WINDOWPOS_CENTERED_MASK = 0x2FFF0000
SDL_WINDOWPOS_CENTERED_DISPLAY = lambda x: SDL_WINDOWPOS_CENTERED_MASK | x
SDL_WINDOWPOS_CENTERED = SDL_WINDOWPOS_CENTERED_DISPLAY(0)
SDL_WINDOWPOS_ISCENTERED = lambda x: (x & 0xFFFF0000) == SDL_WINDOWPOS_CENTERED_MASK

SDL_FlashOperation = ctypes.c_int

SDL_FLASH_CANCEL = 0
SDL_FLASH_BRIEFLY = 1
SDL_FLASH_UNTIL_FOCUSED = 2

SDL_FUNC("SDL_GetNumVideoDrivers", ctypes.c_int)
SDL_FUNC("SDL_GetVideoDriver", ctypes.c_char_p, ctypes.c_int)
SDL_FUNC("SDL_GetCurrentVideoDriver", ctypes.c_char_p)
SDL_FUNC("SDL_GetSystemTheme", SDL_SystemTheme)
SDL_FUNC("SDL_GetDisplays", ctypes.POINTER(SDL_DisplayID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetPrimaryDisplay", SDL_DisplayID)
SDL_FUNC("SDL_GetDisplayProperties", SDL_PropertiesID, SDL_DisplayID)

SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN = "SDL.display.HDR_enabled"
SDL_PROP_DISPLAY_KMSDRM_PANEL_ORIENTATION_NUMBER = "SDL.display.KMSDRM.panel_orientation"

SDL_FUNC("SDL_GetDisplayName", ctypes.c_char_p, SDL_DisplayID)
SDL_FUNC("SDL_GetDisplayBounds", ctypes.c_int, SDL_DisplayID, ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetDisplayUsableBounds", ctypes.c_int, SDL_DisplayID, ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_GetNaturalDisplayOrientation", SDL_DisplayOrientation, SDL_DisplayID)
SDL_FUNC("SDL_GetCurrentDisplayOrientation", SDL_DisplayOrientation, SDL_DisplayID)

SDL_FUNC("SDL_GetDisplayContentScale", ctypes.c_float, SDL_DisplayID)

SDL_FUNC("SDL_GetFullscreenDisplayModes", ctypes.POINTER(ctypes.POINTER(SDL_DisplayMode)), SDL_DisplayID, ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetClosestFullscreenDisplayMode", ctypes.c_int, SDL_DisplayID, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_bool, ctypes.POINTER(SDL_DisplayMode))

SDL_FUNC("SDL_GetDesktopDisplayMode", ctypes.POINTER(SDL_DisplayMode), SDL_DisplayID)
SDL_FUNC("SDL_GetCurrentDisplayMode", ctypes.POINTER(SDL_DisplayMode), SDL_DisplayID)

SDL_FUNC("SDL_GetDisplayForPoint", SDL_DisplayID, ctypes.POINTER(SDL_Point))
SDL_FUNC("SDL_GetDisplayForRect", SDL_DisplayID, ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetDisplayForWindow", SDL_DisplayID, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetWindowPixelDensity", ctypes.c_float, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetWindowDisplayScale", ctypes.c_float, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowFullscreenMode", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_DisplayMode))
SDL_FUNC("SDL_GetWindowFullscreenMode", ctypes.POINTER(SDL_DisplayMode), ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetWindowICCProfile", ctypes.c_void_p, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_size_t))
SDL_FUNC("SDL_GetWindowPixelFormat", SDL_PixelFormat, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetWindows", ctypes.POINTER(ctypes.POINTER(SDL_Window)), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_CreateWindow", ctypes.POINTER(SDL_Window), ctypes.c_char_p, ctypes.c_int, ctypes.c_int, SDL_WindowFlags)
SDL_FUNC("SDL_CreatePopupWindow", ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, SDL_WindowFlags)
SDL_FUNC("SDL_CreateWindowWithProperties", ctypes.POINTER(SDL_Window), SDL_PropertiesID)

SDL_PROP_WINDOW_CREATE_ALWAYS_ON_TOP_BOOLEAN = "always_on_top"
SDL_PROP_WINDOW_CREATE_BORDERLESS_BOOLEAN = "borderless"
SDL_PROP_WINDOW_CREATE_FOCUSABLE_BOOLEAN = "focusable"
SDL_PROP_WINDOW_CREATE_EXTERNAL_GRAPHICS_CONTEXT_BOOLEAN = "external_graphics_context"
SDL_PROP_WINDOW_CREATE_FULLSCREEN_BOOLEAN = "fullscreen"
SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER = "height"
SDL_PROP_WINDOW_CREATE_HIDDEN_BOOLEAN = "hidden"
SDL_PROP_WINDOW_CREATE_HIGH_PIXEL_DENSITY_BOOLEAN = "high_pixel_density"
SDL_PROP_WINDOW_CREATE_MAXIMIZED_BOOLEAN = "maximized"
SDL_PROP_WINDOW_CREATE_MENU_BOOLEAN = "menu"
SDL_PROP_WINDOW_CREATE_METAL_BOOLEAN = "metal"
SDL_PROP_WINDOW_CREATE_MINIMIZED_BOOLEAN = "minimized"
SDL_PROP_WINDOW_CREATE_MODAL_BOOLEAN = "modal"
SDL_PROP_WINDOW_CREATE_MOUSE_GRABBED_BOOLEAN = "mouse_grabbed"
SDL_PROP_WINDOW_CREATE_OPENGL_BOOLEAN = "opengl"
SDL_PROP_WINDOW_CREATE_PARENT_POINTER = "parent"
SDL_PROP_WINDOW_CREATE_RESIZABLE_BOOLEAN = "resizable"
SDL_PROP_WINDOW_CREATE_TITLE_STRING = "title"
SDL_PROP_WINDOW_CREATE_TRANSPARENT_BOOLEAN = "transparent"
SDL_PROP_WINDOW_CREATE_TOOLTIP_BOOLEAN = "tooltip"
SDL_PROP_WINDOW_CREATE_UTILITY_BOOLEAN = "utility"
SDL_PROP_WINDOW_CREATE_VULKAN_BOOLEAN = "vulkan"
SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER = "width"
SDL_PROP_WINDOW_CREATE_X_NUMBER = "x"
SDL_PROP_WINDOW_CREATE_Y_NUMBER = "y"
SDL_PROP_WINDOW_CREATE_COCOA_WINDOW_POINTER = "cocoa.window"
SDL_PROP_WINDOW_CREATE_COCOA_VIEW_POINTER = "cocoa.view"
SDL_PROP_WINDOW_CREATE_WAYLAND_SURFACE_ROLE_CUSTOM_BOOLEAN = "wayland.surface_role_custom"
SDL_PROP_WINDOW_CREATE_WAYLAND_CREATE_EGL_WINDOW_BOOLEAN = "wayland.create_egl_window"
SDL_PROP_WINDOW_CREATE_WAYLAND_WL_SURFACE_POINTER = "wayland.wl_surface"
SDL_PROP_WINDOW_CREATE_WIN32_HWND_POINTER = "win32.hwnd"
SDL_PROP_WINDOW_CREATE_WIN32_PIXEL_FORMAT_HWND_POINTER = "win32.pixel_format_hwnd"
SDL_PROP_WINDOW_CREATE_X11_WINDOW_NUMBER = "x11.window"

SDL_FUNC("SDL_GetWindowID", SDL_WindowID, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetWindowFromID", ctypes.POINTER(SDL_Window), SDL_WindowID)
SDL_FUNC("SDL_GetWindowParent", ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetWindowProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Window))

SDL_PROP_WINDOW_SHAPE_POINTER = "SDL.window.shape"
SDL_PROP_WINDOW_HDR_ENABLED_BOOLEAN = "SDL.window.HDR_enabled"
SDL_PROP_WINDOW_SDR_WHITE_LEVEL_FLOAT = "SDL.window.SDR_white_level"
SDL_PROP_WINDOW_HDR_HEADROOM_FLOAT = "SDL.window.HDR_headroom"
SDL_PROP_WINDOW_ANDROID_WINDOW_POINTER = "SDL.window.android.window"
SDL_PROP_WINDOW_ANDROID_SURFACE_POINTER = "SDL.window.android.surface"
SDL_PROP_WINDOW_UIKIT_WINDOW_POINTER = "SDL.window.uikit.window"
SDL_PROP_WINDOW_UIKIT_METAL_VIEW_TAG_NUMBER = "SDL.window.uikit.metal_view_tag"
SDL_PROP_WINDOW_UIKIT_OPENGL_FRAMEBUFFER_NUMBER = "SDL.window.uikit.opengl.framebuffer"
SDL_PROP_WINDOW_UIKIT_OPENGL_RENDERBUFFER_NUMBER = "SDL.window.uikit.opengl.renderbuffer"
SDL_PROP_WINDOW_UIKIT_OPENGL_RESOLVE_FRAMEBUFFER_NUMBER = "SDL.window.uikit.opengl.resolve_framebuffer"
SDL_PROP_WINDOW_KMSDRM_DEVICE_INDEX_NUMBER = "SDL.window.kmsdrm.dev_index"
SDL_PROP_WINDOW_KMSDRM_DRM_FD_NUMBER = "SDL.window.kmsdrm.drm_fd"
SDL_PROP_WINDOW_KMSDRM_GBM_DEVICE_POINTER = "SDL.window.kmsdrm.gbm_dev"
SDL_PROP_WINDOW_COCOA_WINDOW_POINTER = "SDL.window.cocoa.window"
SDL_PROP_WINDOW_COCOA_METAL_VIEW_TAG_NUMBER = "SDL.window.cocoa.metal_view_tag"
SDL_PROP_WINDOW_VIVANTE_DISPLAY_POINTER = "SDL.window.vivante.display"
SDL_PROP_WINDOW_VIVANTE_WINDOW_POINTER = "SDL.window.vivante.window"
SDL_PROP_WINDOW_VIVANTE_SURFACE_POINTER = "SDL.window.vivante.surface"
SDL_PROP_WINDOW_WINRT_WINDOW_POINTER = "SDL.window.winrt.window"
SDL_PROP_WINDOW_WIN32_HWND_POINTER = "SDL.window.win32.hwnd"
SDL_PROP_WINDOW_WIN32_HDC_POINTER = "SDL.window.win32.hdc"
SDL_PROP_WINDOW_WIN32_INSTANCE_POINTER = "SDL.window.win32.instance"
SDL_PROP_WINDOW_WAYLAND_DISPLAY_POINTER = "SDL.window.wayland.display"
SDL_PROP_WINDOW_WAYLAND_SURFACE_POINTER = "SDL.window.wayland.surface"
SDL_PROP_WINDOW_WAYLAND_EGL_WINDOW_POINTER = "SDL.window.wayland.egl_window"
SDL_PROP_WINDOW_WAYLAND_XDG_SURFACE_POINTER = "SDL.window.wayland.xdg_surface"
SDL_PROP_WINDOW_WAYLAND_XDG_TOPLEVEL_POINTER = "SDL.window.wayland.xdg_toplevel"
SDL_PROP_WINDOW_WAYLAND_XDG_TOPLEVEL_EXPORT_HANDLE_STRING = "SDL.window.wayland.xdg_toplevel_export_handle"
SDL_PROP_WINDOW_WAYLAND_XDG_POPUP_POINTER = "SDL.window.wayland.xdg_popup"
SDL_PROP_WINDOW_WAYLAND_XDG_POSITIONER_POINTER = "SDL.window.wayland.xdg_positioner"
SDL_PROP_WINDOW_X11_DISPLAY_POINTER = "SDL.window.x11.display"
SDL_PROP_WINDOW_X11_SCREEN_NUMBER = "SDL.window.x11.screen"
SDL_PROP_WINDOW_X11_WINDOW_NUMBER = "SDL.window.x11.window"

SDL_FUNC("SDL_GetWindowFlags", SDL_WindowFlags, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowTitle", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_char_p)
SDL_FUNC("SDL_GetWindowTitle", ctypes.c_char_p, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowIcon", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_SetWindowPosition", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetWindowPosition", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_SetWindowSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetWindowSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_GetWindowSafeArea", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Rect))

SDL_FUNC("SDL_SetWindowAspectRatio", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_float, ctypes.c_float)
SDL_FUNC("SDL_GetWindowAspectRatio", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float))

SDL_FUNC("SDL_GetWindowBordersSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetWindowSizeInPixels", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_SetWindowMinimumSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetWindowMinimumSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_SetWindowMaximumSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int)
SDL_FUNC("SDL_GetWindowMaximumSize", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_SetWindowBordered", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)
SDL_FUNC("SDL_SetWindowResizable", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)
SDL_FUNC("SDL_SetWindowAlwaysOnTop", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)

SDL_FUNC("SDL_ShowWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_HideWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_RaiseWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_MaximizeWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_MinimizeWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_RestoreWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowFullscreen", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)
SDL_FUNC("SDL_SyncWindow", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_WindowHasSurface", ctypes.c_bool, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetWindowSurface", ctypes.POINTER(SDL_Surface), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_SetWindowSurfaceVSync", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int)

SDL_WINDOW_SURFACE_VSYNC_DISABLED = 0
SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE = -1

SDL_FUNC("SDL_GetWindowSurfaceVSync", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(ctypes.c_int))

SDL_FUNC("SDL_UpdateWindowSurface", ctypes.c_int, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_UpdateWindowSurfaceRects", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Rect), ctypes.c_int)
SDL_FUNC("SDL_DestroyWindowSurface", ctypes.c_int, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowKeyboardGrab", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)
SDL_FUNC("SDL_SetWindowMouseGrab", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)

SDL_FUNC("SDL_GetWindowKeyboardGrab", ctypes.c_bool, ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_GetWindowMouseGrab", ctypes.c_bool, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_GetGrabbedWindow", ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowMouseRect", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Rect))
SDL_FUNC("SDL_GetWindowMouseRect", ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowOpacity", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_float)
SDL_FUNC("SDL_GetWindowOpacity", ctypes.c_float, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_SetWindowModalFor", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Window))
SDL_FUNC("SDL_SetWindowFocusable", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_bool)

SDL_FUNC("SDL_ShowWindowSystemMenu", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.c_int, ctypes.c_int)

SDL_HitTestResult = ctypes.c_int

SDL_HITTEST_NORMAL = 0
SDL_HITTEST_DRAGGABLE = 1
SDL_HITTEST_RESIZE_TOPLEFT = 2
SDL_HITTEST_RESIZE_TOP = 3
SDL_HITTEST_RESIZE_TOPRIGHT = 4
SDL_HITTEST_RESIZE_RIGHT = 5
SDL_HITTEST_RESIZE_BOTTOMRIGHT = 6
SDL_HITTEST_RESIZE_BOTTOM = 7
SDL_HITTEST_RESIZE_BOTTOMLEFT = 8
SDL_HITTEST_RESIZE_LEFT = 9

SDL_HitTest = ctypes.CFUNCTYPE(SDL_HitTestResult, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Point), ctypes.c_void_p)

SDL_FUNC("SDL_SetWindowHitTest", ctypes.c_int, ctypes.POINTER(SDL_Window), SDL_HitTest, ctypes.c_void_p)
SDL_FUNC("SDL_SetWindowShape", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_Surface))

SDL_FUNC("SDL_FlashWindow", ctypes.c_int, ctypes.POINTER(SDL_Window), ctypes.POINTER(SDL_FlashOperation))
SDL_FUNC("SDL_DestroyWindow", None, ctypes.POINTER(SDL_Window))

SDL_FUNC("SDL_ScreenSaverEnabled", ctypes.c_bool)
SDL_FUNC("SDL_EnableScreenSaver", ctypes.c_int)
SDL_FUNC("SDL_DisableScreenSaver", ctypes.c_int)