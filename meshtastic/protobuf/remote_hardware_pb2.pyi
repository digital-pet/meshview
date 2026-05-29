from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HardwareMessage(_message.Message):
    __slots__ = ["gpio_mask", "gpio_value", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    GPIOS_CHANGED: HardwareMessage.Type
    GPIO_MASK_FIELD_NUMBER: _ClassVar[int]
    GPIO_VALUE_FIELD_NUMBER: _ClassVar[int]
    READ_GPIOS: HardwareMessage.Type
    READ_GPIOS_REPLY: HardwareMessage.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNSET: HardwareMessage.Type
    WATCH_GPIOS: HardwareMessage.Type
    WRITE_GPIOS: HardwareMessage.Type
    gpio_mask: int
    gpio_value: int
    type: HardwareMessage.Type
    def __init__(self, type: _Optional[_Union[HardwareMessage.Type, str]] = ..., gpio_mask: _Optional[int] = ..., gpio_value: _Optional[int] = ...) -> None: ...
