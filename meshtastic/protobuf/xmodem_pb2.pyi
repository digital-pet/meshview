from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class XModem(_message.Message):
    __slots__ = ["buffer", "control", "crc16", "seq"]
    class Control(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACK: XModem.Control
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    CAN: XModem.Control
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CRC16_FIELD_NUMBER: _ClassVar[int]
    CTRLZ: XModem.Control
    EOT: XModem.Control
    NAK: XModem.Control
    NUL: XModem.Control
    SEQ_FIELD_NUMBER: _ClassVar[int]
    SOH: XModem.Control
    STX: XModem.Control
    buffer: bytes
    control: XModem.Control
    crc16: int
    seq: int
    def __init__(self, control: _Optional[_Union[XModem.Control, str]] = ..., seq: _Optional[int] = ..., crc16: _Optional[int] = ..., buffer: _Optional[bytes] = ...) -> None: ...
