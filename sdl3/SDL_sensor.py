from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

from .SDL_properties import SDL_PropertiesID

SDL_SET_CURRENT_BINARY(SDL_BINARY)

class SDL_Sensor(ctypes.c_void_p):
    ...

SDL_SensorID = ctypes.c_uint32

SDL_STANDARD_GRAVITY = 9.80665

SDL_SensorType = ctypes.c_int

SDL_SENSOR_INVALID = -1
SDL_SENSOR_UNKNOWN = 0
SDL_SENSOR_ACCEL = 1
SDL_SENSOR_GYRO = 2
SDL_SENSOR_ACCEL_L = 3
SDL_SENSOR_GYRO_L = 4
SDL_SENSOR_ACCEL_R = 5
SDL_SENSOR_GYRO_R = 6

SDL_FUNC("SDL_GetSensors", ctypes.POINTER(SDL_SensorID), ctypes.POINTER(ctypes.c_int))
SDL_FUNC("SDL_GetSensorNameForID", ctypes.c_char_p, SDL_SensorID)
SDL_FUNC("SDL_GetSensorTypeForID", SDL_SensorType, SDL_SensorID)
SDL_FUNC("SDL_GetSensorNonPortableTypeForID", ctypes.c_int, SDL_SensorID)
SDL_FUNC("SDL_OpenSensor", ctypes.POINTER(SDL_Sensor), SDL_SensorID)
SDL_FUNC("SDL_GetSensorFromID", ctypes.POINTER(SDL_Sensor), SDL_SensorID)
SDL_FUNC("SDL_GetSensorProperties", SDL_PropertiesID, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_GetSensorName", ctypes.c_char_p, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_GetSensorType", SDL_SensorType, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_GetSensorNonPortableType", ctypes.c_int, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_GetSensorID", SDL_SensorID, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_GetSensorData", ctypes.c_bool, ctypes.POINTER(SDL_Sensor), ctypes.POINTER(ctypes.c_float), ctypes.c_int)
SDL_FUNC("SDL_CloseSensor", None, ctypes.POINTER(SDL_Sensor))
SDL_FUNC("SDL_UpdateSensors", None)