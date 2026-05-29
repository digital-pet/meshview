from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SerialHalCommand(_message.Message):
    __slots__ = ["data", "mode", "pin", "transaction_id", "type", "value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ATTACH_INTERRUPT: SerialHalCommand.Type
    DATA_FIELD_NUMBER: _ClassVar[int]
    DETACH_INTERRUPT: SerialHalCommand.Type
    DIGITAL_READ: SerialHalCommand.Type
    DIGITAL_WRITE: SerialHalCommand.Type
    MODE_FIELD_NUMBER: _ClassVar[int]
    NOOP: SerialHalCommand.Type
    PIN_FIELD_NUMBER: _ClassVar[int]
    PIN_MODE: SerialHalCommand.Type
    SPI_TRANSFER: SerialHalCommand.Type
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNSET: SerialHalCommand.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mode: int
    pin: int
    transaction_id: int
    type: SerialHalCommand.Type
    value: int
    def __init__(self, transaction_id: _Optional[int] = ..., type: _Optional[_Union[SerialHalCommand.Type, str]] = ..., pin: _Optional[int] = ..., value: _Optional[int] = ..., mode: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class SerialHalResponse(_message.Message):
    __slots__ = ["data", "error", "result", "transaction_id", "value"]
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BAD_REQUEST: SerialHalResponse.Result
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR: SerialHalResponse.Result
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OK: SerialHalResponse.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    UNSUPPORTED: SerialHalResponse.Result
    VALUE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    error: str
    result: SerialHalResponse.Result
    transaction_id: int
    value: int
    def __init__(self, transaction_id: _Optional[int] = ..., result: _Optional[_Union[SerialHalResponse.Result, str]] = ..., value: _Optional[int] = ..., data: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...
