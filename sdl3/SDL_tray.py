from .__init__ import ctypes, typing, SDL_POINTER, SDL_FUNC_TYPE, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_surface import SDL_Surface

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Tray(ctypes.c_void_p):
    ...

class SDL_TrayMenu(ctypes.c_void_p):
    ...

class SDL_TrayEntry(ctypes.c_void_p):
    ...

SDL_TrayEntryFlags: typing.TypeAlias = SDL_TYPE["SDL_TrayEntryFlags", ctypes.c_uint32]

SDL_TRAYENTRY_BUTTON = 0x00000001
SDL_TRAYENTRY_CHECKBOX = 0x00000002
SDL_TRAYENTRY_SUBMENU = 0x00000004
SDL_TRAYENTRY_DISABLED = 0x80000000
SDL_TRAYENTRY_CHECKED = 0x40000000

SDL_TrayCallback: typing.TypeAlias = SDL_FUNC_TYPE["SDL_TrayCallback", None, ctypes.c_void_p, SDL_POINTER[SDL_TrayEntry]]

SDL_FUNC("SDL_CreateTray", SDL_POINTER[SDL_Tray], SDL_POINTER[SDL_Surface], ctypes.c_char_p)
SDL_FUNC("SDL_SetTrayIcon", None, SDL_POINTER[SDL_Tray], SDL_POINTER[SDL_Surface])
SDL_FUNC("SDL_SetTrayTooltip", None, SDL_POINTER[SDL_Tray], ctypes.c_char_p)
SDL_FUNC("SDL_CreateTrayMenu", SDL_POINTER[SDL_TrayMenu], SDL_POINTER[SDL_Tray])
SDL_FUNC("SDL_CreateTraySubmenu", SDL_POINTER[SDL_TrayMenu], SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_GetTrayMenu", SDL_POINTER[SDL_TrayMenu], SDL_POINTER[SDL_Tray])
SDL_FUNC("SDL_GetTraySubmenu", SDL_POINTER[SDL_TrayMenu], SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_GetTrayEntries", SDL_POINTER[SDL_POINTER[SDL_TrayEntry]], SDL_POINTER[SDL_TrayMenu], SDL_POINTER[ctypes.c_int])
SDL_FUNC("SDL_RemoveTrayEntry", None, SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_InsertTrayEntryAt", SDL_POINTER[SDL_TrayEntry], SDL_POINTER[SDL_TrayMenu], ctypes.c_int, ctypes.c_char_p, SDL_TrayEntryFlags)
SDL_FUNC("SDL_SetTrayEntryLabel", None, SDL_POINTER[SDL_TrayEntry], ctypes.c_char_p)
SDL_FUNC("SDL_GetTrayEntryLabel", ctypes.c_char_p, SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_SetTrayEntryChecked", None, SDL_POINTER[SDL_TrayEntry], ctypes.c_bool)
SDL_FUNC("SDL_GetTrayEntryChecked", ctypes.c_bool, SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_SetTrayEntryEnabled", None, SDL_POINTER[SDL_TrayEntry], ctypes.c_bool)
SDL_FUNC("SDL_GetTrayEntryEnabled", ctypes.c_bool, SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_SetTrayEntryCallback", None, SDL_POINTER[SDL_TrayEntry], SDL_TrayCallback, ctypes.c_void_p)
SDL_FUNC("SDL_ClickTrayEntry", None, SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_DestroyTray", None, SDL_POINTER[SDL_Tray])
SDL_FUNC("SDL_GetTrayEntryParent", SDL_POINTER[SDL_TrayMenu], SDL_POINTER[SDL_TrayEntry])
SDL_FUNC("SDL_GetTrayMenuParentEntry", SDL_POINTER[SDL_TrayEntry], SDL_POINTER[SDL_TrayMenu])
SDL_FUNC("SDL_GetTrayMenuParentTray", SDL_POINTER[SDL_Tray], SDL_POINTER[SDL_TrayMenu])
SDL_FUNC("SDL_UpdateTrays", None)