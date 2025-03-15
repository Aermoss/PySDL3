from .__init__ import ctypes, typing, abc, SDL_POINTER, \
    SDL_FUNC, SDL_TYPE, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Sensor(ctypes.c_void_p):
    ...

SDL_SensorID: typing.TypeAlias = SDL_TYPE["SDL_SensorID", ctypes.c_uint32]

SDL_STANDARD_GRAVITY = 9.80665

SDL_SensorType: typing.TypeAlias = SDL_TYPE["SDL_SensorType", ctypes.c_int]

SDL_SENSOR_INVALID = -1
SDL_SENSOR_UNKNOWN = 0
SDL_SENSOR_ACCEL = 1
SDL_SENSOR_GYRO = 2
SDL_SENSOR_ACCEL_L = 3
SDL_SENSOR_GYRO_L = 4
SDL_SENSOR_ACCEL_R = 5
SDL_SENSOR_GYRO_R = 6

SDL_GetSensors: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensors", SDL_POINTER[SDL_SensorID], [SDL_POINTER[ctypes.c_int]]]
SDL_GetSensorNameForID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorNameForID", ctypes.c_char_p, [SDL_SensorID]]
SDL_GetSensorTypeForID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorTypeForID", SDL_SensorType, [SDL_SensorID]]
SDL_GetSensorNonPortableTypeForID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorNonPortableTypeForID", ctypes.c_int, [SDL_SensorID]]
SDL_OpenSensor: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_OpenSensor", SDL_POINTER[SDL_Sensor], [SDL_SensorID]]
SDL_GetSensorFromID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorFromID", SDL_POINTER[SDL_Sensor], [SDL_SensorID]]
SDL_GetSensorProperties: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorProperties", SDL_PropertiesID, [SDL_POINTER[SDL_Sensor]]]
SDL_GetSensorName: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorName", ctypes.c_char_p, [SDL_POINTER[SDL_Sensor]]]
SDL_GetSensorType: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorType", SDL_SensorType, [SDL_POINTER[SDL_Sensor]]]
SDL_GetSensorNonPortableType: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorNonPortableType", ctypes.c_int, [SDL_POINTER[SDL_Sensor]]]
SDL_GetSensorID: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorID", SDL_SensorID, [SDL_POINTER[SDL_Sensor]]]
SDL_GetSensorData: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_GetSensorData", ctypes.c_bool, [SDL_POINTER[SDL_Sensor], SDL_POINTER[ctypes.c_float], ctypes.c_int]]
SDL_CloseSensor: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_CloseSensor", None, [SDL_POINTER[SDL_Sensor]]]
SDL_UpdateSensors: abc.Callable[..., typing.Any] = SDL_FUNC["SDL_UpdateSensors", None, []]