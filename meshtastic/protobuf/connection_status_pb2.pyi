from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BluetoothConnectionStatus(_message.Message):
    __slots__ = ["is_connected", "pin", "rssi"]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    is_connected: bool
    pin: int
    rssi: int
    def __init__(self, pin: _Optional[int] = ..., rssi: _Optional[int] = ..., is_connected: bool = ...) -> None: ...

class DeviceConnectionStatus(_message.Message):
    __slots__ = ["bluetooth", "ethernet", "serial", "wifi"]
    BLUETOOTH_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    bluetooth: BluetoothConnectionStatus
    ethernet: EthernetConnectionStatus
    serial: SerialConnectionStatus
    wifi: WifiConnectionStatus
    def __init__(self, wifi: _Optional[_Union[WifiConnectionStatus, _Mapping]] = ..., ethernet: _Optional[_Union[EthernetConnectionStatus, _Mapping]] = ..., bluetooth: _Optional[_Union[BluetoothConnectionStatus, _Mapping]] = ..., serial: _Optional[_Union[SerialConnectionStatus, _Mapping]] = ...) -> None: ...

class EthernetConnectionStatus(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: NetworkConnectionStatus
    def __init__(self, status: _Optional[_Union[NetworkConnectionStatus, _Mapping]] = ...) -> None: ...

class NetworkConnectionStatus(_message.Message):
    __slots__ = ["ip_address", "is_connected", "is_mqtt_connected", "is_syslog_connected"]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    IS_MQTT_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    IS_SYSLOG_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ip_address: int
    is_connected: bool
    is_mqtt_connected: bool
    is_syslog_connected: bool
    def __init__(self, ip_address: _Optional[int] = ..., is_connected: bool = ..., is_mqtt_connected: bool = ..., is_syslog_connected: bool = ...) -> None: ...

class SerialConnectionStatus(_message.Message):
    __slots__ = ["baud", "is_connected"]
    BAUD_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    baud: int
    is_connected: bool
    def __init__(self, baud: _Optional[int] = ..., is_connected: bool = ...) -> None: ...

class WifiConnectionStatus(_message.Message):
    __slots__ = ["rssi", "ssid", "status"]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    rssi: int
    ssid: str
    status: NetworkConnectionStatus
    def __init__(self, status: _Optional[_Union[NetworkConnectionStatus, _Mapping]] = ..., ssid: _Optional[str] = ..., rssi: _Optional[int] = ...) -> None: ...
