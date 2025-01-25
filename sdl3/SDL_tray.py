from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_surface import SDL_Surface

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Tray(ctypes.c_void_p):
    ...

class SDL_TrayMenu(ctypes.c_void_p):
    ...

class SDL_TrayEntry(ctypes.c_void_p):
    ...

SDL_TrayEntryFlags = ctypes.c_uint32

SDL_TRAYENTRY_BUTTON = 0x00000001
SDL_TRAYENTRY_CHECKBOX = 0x00000002
SDL_TRAYENTRY_SUBMENU = 0x00000004
SDL_TRAYENTRY_DISABLED = 0x80000000
SDL_TRAYENTRY_CHECKED = 0x40000000

SDL_TrayCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(SDL_TrayEntry))

SDL_FUNC("SDL_CreateTray", ctypes.POINTER(SDL_Tray), ctypes.POINTER(SDL_Surface), ctypes.c_char_p)
SDL_FUNC("SDL_SetTrayIcon", None, ctypes.POINTER(SDL_Tray), ctypes.POINTER(SDL_Surface))
SDL_FUNC("SDL_SetTrayTooltip", None, ctypes.POINTER(SDL_Tray), ctypes.c_char_p)
SDL_FUNC("SDL_CreateTrayMenu", ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(SDL_Tray))
SDL_FUNC("SDL_CreateTraySubmenu", ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_GetTrayMenu", ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(SDL_Tray))
SDL_FUNC("SDL_GetTraySubmenu", ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_GetTrayEntries", ctypes.POINTER(ctypes.POINTER(SDL_TrayEntry)), ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_RemoveTrayEntry", None, ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_InsertTrayEntryAt", ctypes.POINTER(SDL_TrayEntry), ctypes.POINTER(SDL_TrayMenu), ctypes.c_int, ctypes.c_char_p, SDL_TrayEntryFlags)
SDL_FUNC("SDL_SetTrayEntryLabel", None, ctypes.POINTER(SDL_TrayEntry), ctypes.c_char_p)
SDL_FUNC("SDL_GetTrayEntryLabel", ctypes.c_char_p, ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_SetTrayEntryChecked", None, ctypes.POINTER(SDL_TrayEntry), ctypes.c_bool)
SDL_FUNC("SDL_GetTrayEntryChecked", ctypes.c_bool, ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_SetTrayEntryEnabled", None, ctypes.POINTER(SDL_TrayEntry), ctypes.c_bool)
SDL_FUNC("SDL_GetTrayEntryEnabled", ctypes.c_bool, ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_SetTrayEntryCallback", None, ctypes.POINTER(SDL_TrayEntry), SDL_TrayCallback, ctypes.c_void_p)
SDL_FUNC("SDL_ClickTrayEntry", None, ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_DestroyTray", None, ctypes.POINTER(SDL_Tray))
SDL_FUNC("SDL_GetTrayEntryParent", ctypes.POINTER(SDL_TrayMenu), ctypes.POINTER(SDL_TrayEntry))
SDL_FUNC("SDL_GetTrayMenuParentEntry", ctypes.POINTER(SDL_TrayEntry), ctypes.POINTER(SDL_TrayMenu))
SDL_FUNC("SDL_GetTrayMenuParentTray", ctypes.POINTER(SDL_Tray), ctypes.POINTER(SDL_TrayMenu))
SDL_FUNC("SDL_UpdateTrays", None)