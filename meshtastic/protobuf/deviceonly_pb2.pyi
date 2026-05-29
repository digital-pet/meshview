from meshtastic.protobuf import channel_pb2 as _channel_pb2
from meshtastic.protobuf import config_pb2 as _config_pb2
from meshtastic.protobuf import localonly_pb2 as _localonly_pb2
from meshtastic.protobuf import mesh_pb2 as _mesh_pb2
from meshtastic.protobuf import telemetry_pb2 as _telemetry_pb2
from meshtastic.protobuf import nanopb_pb2 as _nanopb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupPreferences(_message.Message):
    __slots__ = ["channels", "config", "module_config", "owner", "timestamp", "version"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    channels: ChannelFile
    config: _localonly_pb2.LocalConfig
    module_config: _localonly_pb2.LocalModuleConfig
    owner: _mesh_pb2.User
    timestamp: int
    version: int
    def __init__(self, version: _Optional[int] = ..., timestamp: _Optional[int] = ..., config: _Optional[_Union[_localonly_pb2.LocalConfig, _Mapping]] = ..., module_config: _Optional[_Union[_localonly_pb2.LocalModuleConfig, _Mapping]] = ..., channels: _Optional[_Union[ChannelFile, _Mapping]] = ..., owner: _Optional[_Union[_mesh_pb2.User, _Mapping]] = ...) -> None: ...

class ChannelFile(_message.Message):
    __slots__ = ["channels", "version"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    version: int
    def __init__(self, channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class DeviceState(_message.Message):
    __slots__ = ["did_gps_reset", "my_node", "no_save", "node_remote_hardware_pins", "owner", "receive_queue", "rx_text_message", "rx_waypoint", "version"]
    DID_GPS_RESET_FIELD_NUMBER: _ClassVar[int]
    MY_NODE_FIELD_NUMBER: _ClassVar[int]
    NODE_REMOTE_HARDWARE_PINS_FIELD_NUMBER: _ClassVar[int]
    NO_SAVE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    RX_TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RX_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    did_gps_reset: bool
    my_node: _mesh_pb2.MyNodeInfo
    no_save: bool
    node_remote_hardware_pins: _containers.RepeatedCompositeFieldContainer[_mesh_pb2.NodeRemoteHardwarePin]
    owner: _mesh_pb2.User
    receive_queue: _containers.RepeatedCompositeFieldContainer[_mesh_pb2.MeshPacket]
    rx_text_message: _mesh_pb2.MeshPacket
    rx_waypoint: _mesh_pb2.MeshPacket
    version: int
    def __init__(self, my_node: _Optional[_Union[_mesh_pb2.MyNodeInfo, _Mapping]] = ..., owner: _Optional[_Union[_mesh_pb2.User, _Mapping]] = ..., receive_queue: _Optional[_Iterable[_Union[_mesh_pb2.MeshPacket, _Mapping]]] = ..., version: _Optional[int] = ..., rx_text_message: _Optional[_Union[_mesh_pb2.MeshPacket, _Mapping]] = ..., no_save: bool = ..., did_gps_reset: bool = ..., rx_waypoint: _Optional[_Union[_mesh_pb2.MeshPacket, _Mapping]] = ..., node_remote_hardware_pins: _Optional[_Iterable[_Union[_mesh_pb2.NodeRemoteHardwarePin, _Mapping]]] = ...) -> None: ...

class NodeDatabase(_message.Message):
    __slots__ = ["nodes", "version"]
    NODES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[NodeInfoLite]
    version: int
    def __init__(self, version: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[NodeInfoLite, _Mapping]]] = ...) -> None: ...

class NodeInfoLite(_message.Message):
    __slots__ = ["bitfield", "channel", "device_metrics", "hops_away", "is_favorite", "is_ignored", "last_heard", "next_hop", "num", "position", "snr", "user", "via_mqtt"]
    BITFIELD_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_METRICS_FIELD_NUMBER: _ClassVar[int]
    HOPS_AWAY_FIELD_NUMBER: _ClassVar[int]
    IS_FAVORITE_FIELD_NUMBER: _ClassVar[int]
    IS_IGNORED_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARD_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    VIA_MQTT_FIELD_NUMBER: _ClassVar[int]
    bitfield: int
    channel: int
    device_metrics: _telemetry_pb2.DeviceMetrics
    hops_away: int
    is_favorite: bool
    is_ignored: bool
    last_heard: int
    next_hop: int
    num: int
    position: PositionLite
    snr: float
    user: UserLite
    via_mqtt: bool
    def __init__(self, num: _Optional[int] = ..., user: _Optional[_Union[UserLite, _Mapping]] = ..., position: _Optional[_Union[PositionLite, _Mapping]] = ..., snr: _Optional[float] = ..., last_heard: _Optional[int] = ..., device_metrics: _Optional[_Union[_telemetry_pb2.DeviceMetrics, _Mapping]] = ..., channel: _Optional[int] = ..., via_mqtt: bool = ..., hops_away: _Optional[int] = ..., is_favorite: bool = ..., is_ignored: bool = ..., next_hop: _Optional[int] = ..., bitfield: _Optional[int] = ...) -> None: ...

class PositionLite(_message.Message):
    __slots__ = ["altitude", "latitude_i", "location_source", "longitude_i", "time"]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_I_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_I_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    altitude: int
    latitude_i: int
    location_source: _mesh_pb2.Position.LocSource
    longitude_i: int
    time: int
    def __init__(self, latitude_i: _Optional[int] = ..., longitude_i: _Optional[int] = ..., altitude: _Optional[int] = ..., time: _Optional[int] = ..., location_source: _Optional[_Union[_mesh_pb2.Position.LocSource, str]] = ...) -> None: ...

class UserLite(_message.Message):
    __slots__ = ["hw_model", "is_licensed", "is_unmessagable", "long_name", "macaddr", "public_key", "role", "short_name"]
    HW_MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_LICENSED_FIELD_NUMBER: _ClassVar[int]
    IS_UNMESSAGABLE_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    MACADDR_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    hw_model: _mesh_pb2.HardwareModel
    is_licensed: bool
    is_unmessagable: bool
    long_name: str
    macaddr: bytes
    public_key: bytes
    role: _config_pb2.Config.DeviceConfig.Role
    short_name: str
    def __init__(self, macaddr: _Optional[bytes] = ..., long_name: _Optional[str] = ..., short_name: _Optional[str] = ..., hw_model: _Optional[_Union[_mesh_pb2.HardwareModel, str]] = ..., is_licensed: bool = ..., role: _Optional[_Union[_config_pb2.Config.DeviceConfig.Role, str]] = ..., public_key: _Optional[bytes] = ..., is_unmessagable: bool = ...) -> None: ...
