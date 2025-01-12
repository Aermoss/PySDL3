from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_hid_device(ctypes.c_void_p):
    ...

SDL_hid_bus_type = ctypes.c_int

SDL_HID_API_BUS_UNKNOWN = 0x00
SDL_HID_API_BUS_USB = 0x01
SDL_HID_API_BUS_BLUETOOTH = 0x02
SDL_HID_API_BUS_I2C = 0x03
SDL_HID_API_BUS_SPI = 0x04

SDL_hid_device_info = ctypes.c_void_p

class SDL_hid_device_info(ctypes.Structure):
    _fields_ = [
        ("path", ctypes.c_char_p),
        ("vendor_id", ctypes.c_ushort),
        ("product_id", ctypes.c_ushort),
        ("serial_number", ctypes.c_wchar_p),
        ("release_number", ctypes.c_ushort),
        ("manufacturer_string", ctypes.c_wchar_p),
        ("product_string", ctypes.c_wchar_p),
        ("usage_page", ctypes.c_ushort),
        ("usage", ctypes.c_ushort),
        ("interface_number", ctypes.c_int),
        ("interface_class", ctypes.c_int),
        ("interface_subclass", ctypes.c_int),
        ("interface_protocol", ctypes.c_int),
        ("bus_type", SDL_hid_bus_type),
        ("next", ctypes.POINTER(SDL_hid_device_info))
    ]

SDL_FUNC("SDL_hid_init", ctypes.c_int)
SDL_FUNC("SDL_hid_exit", ctypes.c_int)
SDL_FUNC("SDL_hid_device_change_count", ctypes.c_uint32)
SDL_FUNC("SDL_hid_enumerate", ctypes.POINTER(SDL_hid_device_info), ctypes.c_ushort, ctypes.c_ushort)
SDL_FUNC("SDL_hid_free_enumeration", None, ctypes.POINTER(SDL_hid_device_info))
SDL_FUNC("SDL_hid_open", ctypes.POINTER(SDL_hid_device), ctypes.c_ushort, ctypes.c_ushort, ctypes.c_wchar_p)
SDL_FUNC("SDL_hid_open_path", ctypes.POINTER(SDL_hid_device), ctypes.c_char_p)
SDL_FUNC("SDL_hid_write", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_read_timeout", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.c_int)
SDL_FUNC("SDL_hid_read", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_set_nonblocking", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.c_int)
SDL_FUNC("SDL_hid_send_feature_report", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_feature_report", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_input_report", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_close", ctypes.c_int, ctypes.POINTER(SDL_hid_device))
SDL_FUNC("SDL_hid_get_manufacturer_string", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_product_string", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_serial_number_string", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_indexed_string", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.c_int, ctypes.c_wchar_p, ctypes.c_size_t)
SDL_FUNC("SDL_hid_get_device_info", ctypes.POINTER(SDL_hid_device_info), ctypes.POINTER(SDL_hid_device))
SDL_FUNC("SDL_hid_get_report_descriptor", ctypes.c_int, ctypes.POINTER(SDL_hid_device), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)
SDL_FUNC("SDL_hid_ble_scan", None, ctypes.c_bool)