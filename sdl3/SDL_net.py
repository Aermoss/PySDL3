from .__init__ import ctypes, typing, abc, \
    SDL_POINTER, SDL_FUNC, SDL_NET_BINARY

from .SDL_version import SDL_VERSIONNUM

SDL_NET_MAJOR_VERSION, SDL_NET_MINOR_VERSION, SDL_NET_MICRO_VERSION = 3, 0, 0
SDL_NET_VERSION: int = SDL_VERSIONNUM(SDL_NET_MAJOR_VERSION, SDL_NET_MINOR_VERSION, SDL_NET_MICRO_VERSION)

SDL_NET_VERSION_ATLEAST: abc.Callable[[int, int, int], bool] = lambda x, y, z: \
    (SDL_NET_MAJOR_VERSION >= x) and (SDL_NET_MAJOR_VERSION > x or SDL_NET_MINOR_VERSION >= y) and \
        (SDL_NET_MAJOR_VERSION > x or SDL_NET_MINOR_VERSION > y or SDL_NET_MICRO_VERSION >= z)

SDLNet_Version: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_Version", ctypes.c_int, [], SDL_NET_BINARY]
SDLNet_Init: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_Init", ctypes.c_bool, [], SDL_NET_BINARY]
SDLNet_Quit: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_Quit", None, [], SDL_NET_BINARY]

class SDLNet_Address(ctypes.c_void_p):
    ...

SDLNet_ResolveHostname: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_ResolveHostname", SDL_POINTER[SDLNet_Address], [ctypes.c_char_p], SDL_NET_BINARY]
SDLNet_WaitUntilResolved: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_WaitUntilResolved", ctypes.c_int, [SDL_POINTER[SDLNet_Address], ctypes.c_int32], SDL_NET_BINARY]
SDLNet_GetAddressStatus: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetAddressStatus", ctypes.c_int, [SDL_POINTER[SDLNet_Address]], SDL_NET_BINARY]
SDLNet_GetAddressString: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetAddressString", ctypes.c_char_p, [SDL_POINTER[SDLNet_Address]], SDL_NET_BINARY]
SDLNet_RefAddress: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_RefAddress", SDL_POINTER[SDLNet_Address], [SDL_POINTER[SDLNet_Address]], SDL_NET_BINARY]
SDLNet_UnrefAddress: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_UnrefAddress", None, [SDL_POINTER[SDLNet_Address]], SDL_NET_BINARY]
SDLNet_SimulateAddressResolutionLoss: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_SimulateAddressResolutionLoss", None, [ctypes.c_int], SDL_NET_BINARY]
SDLNet_CompareAddresses: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_CompareAddresses", ctypes.c_int, [SDL_POINTER[SDLNet_Address], SDL_POINTER[SDLNet_Address]], SDL_NET_BINARY]
SDLNet_GetLocalAddresses: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetLocalAddresses", SDL_POINTER[SDL_POINTER[SDLNet_Address]], [SDL_POINTER[ctypes.c_int]], SDL_NET_BINARY]
SDLNet_FreeLocalAddresses: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_FreeLocalAddresses", None, [SDL_POINTER[SDL_POINTER[SDLNet_Address]]], SDL_NET_BINARY]

class SDLNet_StreamSocket(ctypes.c_void_p):
    ...

SDLNet_CreateClient: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_CreateClient", SDL_POINTER[SDLNet_StreamSocket], [SDL_POINTER[SDLNet_Address], ctypes.c_uint16], SDL_NET_BINARY]
SDLNet_WaitUntilConnected: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_WaitUntilConnected", ctypes.c_int, [SDL_POINTER[SDLNet_StreamSocket], ctypes.c_int32], SDL_NET_BINARY]

class SDLNet_Server(ctypes.c_void_p):
    ...

SDLNet_CreateServer: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_CreateServer", SDL_POINTER[SDLNet_Server], [SDL_POINTER[SDLNet_Address], ctypes.c_uint16], SDL_NET_BINARY]
SDLNet_AcceptClient: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_AcceptClient", ctypes.c_bool, [SDL_POINTER[SDLNet_Server], SDL_POINTER[SDL_POINTER[SDLNet_StreamSocket]]], SDL_NET_BINARY]
SDLNet_DestroyServer: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_DestroyServer", None, [SDL_POINTER[SDLNet_Server]], SDL_NET_BINARY]
SDLNet_GetStreamSocketAddress: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetStreamSocketAddress", SDL_POINTER[SDLNet_Address], [SDL_POINTER[SDLNet_StreamSocket]], SDL_NET_BINARY]
SDLNet_GetConnectionStatus: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetConnectionStatus", ctypes.c_int, [SDL_POINTER[SDLNet_StreamSocket]], SDL_NET_BINARY]
SDLNet_WriteToStreamSocket: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_WriteToStreamSocket", ctypes.c_bool, [SDL_POINTER[SDLNet_StreamSocket], ctypes.c_void_p, ctypes.c_int], SDL_NET_BINARY]
SDLNet_GetStreamSocketPendingWrites: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_GetStreamSocketPendingWrites", ctypes.c_int, [SDL_POINTER[SDLNet_StreamSocket]], SDL_NET_BINARY]
SDLNet_WaitUntilStreamSocketDrained: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_WaitUntilStreamSocketDrained", ctypes.c_int, [SDL_POINTER[SDLNet_StreamSocket], ctypes.c_int32], SDL_NET_BINARY]
SDLNet_ReadFromStreamSocket: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_ReadFromStreamSocket", ctypes.c_int, [SDL_POINTER[SDLNet_StreamSocket], ctypes.c_void_p, ctypes.c_int], SDL_NET_BINARY]
SDLNet_SimulateStreamPacketLoss: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_SimulateStreamPacketLoss", None, [SDL_POINTER[SDLNet_StreamSocket], ctypes.c_int], SDL_NET_BINARY]
SDLNet_DestroyStreamSocket: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_DestroyStreamSocket", None, [SDL_POINTER[SDLNet_StreamSocket]], SDL_NET_BINARY]

class SDLNet_DatagramSocket(ctypes.c_void_p):
    ...

class SDLNet_Datagram(ctypes.Structure):
    _fields_ = [
        ("addr", SDL_POINTER[SDLNet_Address]),
        ("port", ctypes.c_uint16),
        ("buf", SDL_POINTER[ctypes.c_uint8]),
        ("buflen", ctypes.c_int)
    ]

SDLNet_CreateDatagramSocket: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_CreateDatagramSocket", SDL_POINTER[SDLNet_DatagramSocket], [SDL_POINTER[SDLNet_Address], ctypes.c_uint16], SDL_NET_BINARY]
SDLNet_SendDatagram: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_SendDatagram", ctypes.c_bool, [SDL_POINTER[SDLNet_DatagramSocket], SDL_POINTER[SDLNet_Address], ctypes.c_uint16, ctypes.c_void_p, ctypes.c_int], SDL_NET_BINARY]
SDLNet_ReceiveDatagram: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_ReceiveDatagram", ctypes.c_bool, [SDL_POINTER[SDLNet_DatagramSocket], SDL_POINTER[SDL_POINTER[SDLNet_Datagram]]], SDL_NET_BINARY]
SDLNet_DestroyDatagram: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_DestroyDatagram", None, [SDL_POINTER[SDLNet_Datagram]], SDL_NET_BINARY]
SDLNet_SimulateDatagramPacketLoss: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_SimulateDatagramPacketLoss", None, [SDL_POINTER[SDLNet_DatagramSocket], ctypes.c_int], SDL_NET_BINARY]
SDLNet_DestroyDatagramSocket: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_DestroyDatagramSocket", None, [SDL_POINTER[SDLNet_DatagramSocket]], SDL_NET_BINARY]
SDLNet_WaitUntilInputAvailable: abc.Callable[..., typing.Any] = SDL_FUNC["SDLNet_WaitUntilInputAvailable", ctypes.c_int, [SDL_POINTER[ctypes.c_void_p], ctypes.c_int, ctypes.c_int32], SDL_NET_BINARY]