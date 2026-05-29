from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACK: MessageType
AHT20_HUMIDITY: MessageType
AHT20_TEMP: MessageType
BEEP_OFF: MessageType
BEEP_ON: MessageType
COLLECT_INTERVAL: MessageType
DESCRIPTOR: _descriptor.FileDescriptor
POWER_ON: MessageType
SCD41_CO2: MessageType
SCD41_HUMIDITY: MessageType
SCD41_TEMP: MessageType
SHUTDOWN: MessageType
TVOC_INDEX: MessageType

class InterdeviceMessage(_message.Message):
    __slots__ = ["nmea", "sensor"]
    NMEA_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    nmea: str
    sensor: SensorData
    def __init__(self, nmea: _Optional[str] = ..., sensor: _Optional[_Union[SensorData, _Mapping]] = ...) -> None: ...

class SensorData(_message.Message):
    __slots__ = ["float_value", "type", "uint32_value"]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    float_value: float
    type: MessageType
    uint32_value: int
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ..., float_value: _Optional[float] = ..., uint32_value: _Optional[int] = ...) -> None: ...

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
