from meshtastic.protobuf import channel_pb2 as _channel_pb2
from meshtastic.protobuf import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelSet(_message.Message):
    __slots__ = ["lora_config", "settings"]
    LORA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    lora_config: _config_pb2.Config.LoRaConfig
    settings: _containers.RepeatedCompositeFieldContainer[_channel_pb2.ChannelSettings]
    def __init__(self, settings: _Optional[_Iterable[_Union[_channel_pb2.ChannelSettings, _Mapping]]] = ..., lora_config: _Optional[_Union[_config_pb2.Config.LoRaConfig, _Mapping]] = ...) -> None: ...
