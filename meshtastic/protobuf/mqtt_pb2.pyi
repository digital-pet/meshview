from meshtastic.protobuf import config_pb2 as _config_pb2
from meshtastic.protobuf import mesh_pb2 as _mesh_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapReport(_message.Message):
    __slots__ = ["altitude", "firmware_version", "has_default_channel", "has_opted_report_location", "hw_model", "latitude_i", "long_name", "longitude_i", "modem_preset", "num_online_local_nodes", "position_precision", "region", "role", "short_name"]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HAS_DEFAULT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    HAS_OPTED_REPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    HW_MODEL_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_I_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_I_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEM_PRESET_FIELD_NUMBER: _ClassVar[int]
    NUM_ONLINE_LOCAL_NODES_FIELD_NUMBER: _ClassVar[int]
    POSITION_PRECISION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    altitude: int
    firmware_version: str
    has_default_channel: bool
    has_opted_report_location: bool
    hw_model: _mesh_pb2.HardwareModel
    latitude_i: int
    long_name: str
    longitude_i: int
    modem_preset: _config_pb2.Config.LoRaConfig.ModemPreset
    num_online_local_nodes: int
    position_precision: int
    region: _config_pb2.Config.LoRaConfig.RegionCode
    role: _config_pb2.Config.DeviceConfig.Role
    short_name: str
    def __init__(self, long_name: _Optional[str] = ..., short_name: _Optional[str] = ..., role: _Optional[_Union[_config_pb2.Config.DeviceConfig.Role, str]] = ..., hw_model: _Optional[_Union[_mesh_pb2.HardwareModel, str]] = ..., firmware_version: _Optional[str] = ..., region: _Optional[_Union[_config_pb2.Config.LoRaConfig.RegionCode, str]] = ..., modem_preset: _Optional[_Union[_config_pb2.Config.LoRaConfig.ModemPreset, str]] = ..., has_default_channel: bool = ..., latitude_i: _Optional[int] = ..., longitude_i: _Optional[int] = ..., altitude: _Optional[int] = ..., position_precision: _Optional[int] = ..., num_online_local_nodes: _Optional[int] = ..., has_opted_report_location: bool = ...) -> None: ...

class ServiceEnvelope(_message.Message):
    __slots__ = ["channel_id", "gateway_id", "packet"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    gateway_id: str
    packet: _mesh_pb2.MeshPacket
    def __init__(self, packet: _Optional[_Union[_mesh_pb2.MeshPacket, _Mapping]] = ..., channel_id: _Optional[str] = ..., gateway_id: _Optional[str] = ...) -> None: ...
