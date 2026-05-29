from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PowerMon(_message.Message):
    __slots__ = []
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BT_On: PowerMon.State
    CPU_DeepSleep: PowerMon.State
    CPU_LightSleep: PowerMon.State
    GPS_Active: PowerMon.State
    LED_On: PowerMon.State
    Lora_RXActive: PowerMon.State
    Lora_RXOn: PowerMon.State
    Lora_TXOn: PowerMon.State
    None: PowerMon.State
    Screen_Drawing: PowerMon.State
    Screen_On: PowerMon.State
    Vext1_On: PowerMon.State
    Wifi_On: PowerMon.State
    def __init__(self) -> None: ...

class PowerStressMessage(_message.Message):
    __slots__ = ["cmd", "num_seconds"]
    class Opcode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BT_OFF: PowerStressMessage.Opcode
    BT_ON: PowerStressMessage.Opcode
    CMD_FIELD_NUMBER: _ClassVar[int]
    CPU_DEEPSLEEP: PowerStressMessage.Opcode
    CPU_FULLON: PowerStressMessage.Opcode
    CPU_IDLE: PowerStressMessage.Opcode
    END_QUIET: PowerStressMessage.Opcode
    FORCE_QUIET: PowerStressMessage.Opcode
    GPS_OFF: PowerStressMessage.Opcode
    GPS_ON: PowerStressMessage.Opcode
    LED_OFF: PowerStressMessage.Opcode
    LED_ON: PowerStressMessage.Opcode
    LORA_OFF: PowerStressMessage.Opcode
    LORA_RX: PowerStressMessage.Opcode
    LORA_TX: PowerStressMessage.Opcode
    NUM_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PRINT_INFO: PowerStressMessage.Opcode
    SCREEN_OFF: PowerStressMessage.Opcode
    SCREEN_ON: PowerStressMessage.Opcode
    UNSET: PowerStressMessage.Opcode
    WIFI_OFF: PowerStressMessage.Opcode
    WIFI_ON: PowerStressMessage.Opcode
    cmd: PowerStressMessage.Opcode
    num_seconds: float
    def __init__(self, cmd: _Optional[_Union[PowerStressMessage.Opcode, str]] = ..., num_seconds: _Optional[float] = ...) -> None: ...
