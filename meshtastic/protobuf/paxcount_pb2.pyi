from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Paxcount(_message.Message):
    __slots__ = ["ble", "uptime", "wifi"]
    BLE_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    ble: int
    uptime: int
    wifi: int
    def __init__(self, wifi: _Optional[int] = ..., ble: _Optional[int] = ..., uptime: _Optional[int] = ...) -> None: ...
