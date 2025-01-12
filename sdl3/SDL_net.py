from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_GET_BINARY, SDL_NET_BINARY, SDL_BINARY

from .SDL_version import SDL_VERSIONNUM

SDL_SET_CURRENT_BINARY(SDL_NET_BINARY)

SDL_NET_MAJOR_VERSION = 3
SDL_NET_MINOR_VERSION = 0
SDL_NET_MICRO_VERSION = 0

SDL_NET_VERSION = \
    SDL_VERSIONNUM(SDL_NET_MAJOR_VERSION, SDL_NET_MINOR_VERSION, SDL_NET_MICRO_VERSION)

SDL_NET_VERSION_ATLEAST = lambda x, y, z: \
    (SDL_NET_MAJOR_VERSION >= x) and \
    (SDL_NET_MAJOR_VERSION > x or SDL_NET_MINOR_VERSION >= y) and \
    (SDL_NET_MAJOR_VERSION > x or SDL_NET_MINOR_VERSION > y or SDL_NET_MICRO_VERSION >= z)

SDL_FUNC("SDLNet_Version", ctypes.c_int)
SDL_FUNC("SDLNet_Init", ctypes.c_bool)
SDL_FUNC("SDLNet_Quit", None)

class SDLNet_Address(ctypes.c_void_p):
    ...

SDL_FUNC("SDLNet_ResolveHostname", ctypes.POINTER(SDLNet_Address), ctypes.c_char_p)
SDL_FUNC("SDLNet_WaitUntilResolved", ctypes.c_int, ctypes.POINTER(SDLNet_Address), ctypes.c_int32)
SDL_FUNC("SDLNet_GetAddressStatus", ctypes.c_int, ctypes.POINTER(SDLNet_Address))
SDL_FUNC("SDLNet_GetAddressString", ctypes.c_char_p, ctypes.POINTER(SDLNet_Address))
SDL_FUNC("SDLNet_RefAddress", ctypes.POINTER(SDLNet_Address), ctypes.POINTER(SDLNet_Address))
SDL_FUNC("SDLNet_UnrefAddress", None, ctypes.POINTER(SDLNet_Address))
SDL_FUNC("SDLNet_SimulateAddressResolutionLoss", None, ctypes.c_int)
SDL_FUNC("SDLNet_CompareAddresses", ctypes.c_int, ctypes.POINTER(SDLNet_Address), ctypes.POINTER(SDLNet_Address))
SDL_FUNC("SDLNet_GetLocalAddresses", ctypes.POINTER(ctypes.POINTER(SDLNet_Address)), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDLNet_FreeLocalAddresses", None, ctypes.POINTER(ctypes.POINTER(SDLNet_Address)))

class SDLNet_StreamSocket(ctypes.c_void_p):
    ...

SDL_FUNC("SDLNet_CreateClient", ctypes.POINTER(SDLNet_StreamSocket), ctypes.POINTER(SDLNet_Address), ctypes.c_uint16)
SDL_FUNC("SDLNet_WaitUntilConnected", ctypes.c_int, ctypes.POINTER(SDLNet_StreamSocket), ctypes.c_int32)

class SDLNet_Server(ctypes.c_void_p):
    ...

SDL_FUNC("SDLNet_CreateServer", ctypes.POINTER(SDLNet_Server), ctypes.POINTER(SDLNet_Address), ctypes.c_uint16)
SDL_FUNC("SDLNet_AcceptClient", ctypes.c_bool, ctypes.POINTER(SDLNet_Server), ctypes.POINTER(ctypes.POINTER(SDLNet_StreamSocket)))
SDL_FUNC("SDLNet_DestroyServer", None, ctypes.POINTER(SDLNet_Server))
SDL_FUNC("SDLNet_GetStreamSocketAddress", ctypes.POINTER(SDLNet_Address), ctypes.POINTER(SDLNet_StreamSocket))
SDL_FUNC("SDLNet_GetConnectionStatus", ctypes.c_int, ctypes.POINTER(SDLNet_StreamSocket))
SDL_FUNC("SDLNet_WriteToStreamSocket", ctypes.c_bool, ctypes.POINTER(SDLNet_StreamSocket), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDLNet_GetStreamSocketPendingWrites", ctypes.c_int, ctypes.POINTER(SDLNet_StreamSocket))
SDL_FUNC("SDLNet_WaitUntilStreamSocketDrained", ctypes.c_int, ctypes.POINTER(SDLNet_StreamSocket), ctypes.c_int32)
SDL_FUNC("SDLNet_ReadFromStreamSocket", ctypes.c_int, ctypes.POINTER(SDLNet_StreamSocket), ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDLNet_SimulateStreamPacketLoss", None, ctypes.POINTER(SDLNet_StreamSocket), ctypes.c_int)
SDL_FUNC("SDLNet_DestroyStreamSocket", None, ctypes.POINTER(SDLNet_StreamSocket))

class SDLNet_DatagramSocket(ctypes.c_void_p):
    ...

class SDLNet_Datagram(ctypes.Structure):
    _fields_ = [
        ("addr", ctypes.POINTER(SDLNet_Address)),
        ("port", ctypes.c_uint16),
        ("buf", ctypes.POINTER(ctypes.c_uint8)),
        ("buflen", ctypes.c_int)
    ]

SDL_FUNC("SDLNet_CreateDatagramSocket", ctypes.POINTER(SDLNet_DatagramSocket), ctypes.POINTER(SDLNet_Address), ctypes.c_uint16)
SDL_FUNC("SDLNet_SendDatagram", ctypes.c_bool, ctypes.POINTER(SDLNet_DatagramSocket), ctypes.POINTER(SDLNet_Address), ctypes.c_uint16, ctypes.c_void_p, ctypes.c_int)
SDL_FUNC("SDLNet_ReceiveDatagram", ctypes.c_bool, ctypes.POINTER(SDLNet_DatagramSocket), ctypes.POINTER(ctypes.POINTER(SDLNet_Datagram)))
SDL_FUNC("SDLNet_DestroyDatagram", None, ctypes.POINTER(SDLNet_Datagram))
SDL_FUNC("SDLNet_SimulateDatagramPacketLoss", None, ctypes.POINTER(SDLNet_DatagramSocket), ctypes.c_int)
SDL_FUNC("SDLNet_DestroyDatagramSocket", None, ctypes.POINTER(SDLNet_DatagramSocket))
SDL_FUNC("SDLNet_WaitUntilInputAvailable", ctypes.c_int, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_int32)