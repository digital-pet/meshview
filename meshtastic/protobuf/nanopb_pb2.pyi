from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DS_1: DescriptorSize
DS_2: DescriptorSize
DS_4: DescriptorSize
DS_8: DescriptorSize
DS_AUTO: DescriptorSize
FT_CALLBACK: FieldType
FT_DEFAULT: FieldType
FT_IGNORE: FieldType
FT_INLINE: FieldType
FT_POINTER: FieldType
FT_STATIC: FieldType
IS_16: IntSize
IS_32: IntSize
IS_64: IntSize
IS_8: IntSize
IS_DEFAULT: IntSize
M_FLATTEN: TypenameMangling
M_NONE: TypenameMangling
M_PACKAGE_INITIALS: TypenameMangling
M_STRIP_PACKAGE: TypenameMangling
NANOPB_ENUMOPT_FIELD_NUMBER: _ClassVar[int]
NANOPB_FIELD_NUMBER: _ClassVar[int]
NANOPB_FILEOPT_FIELD_NUMBER: _ClassVar[int]
NANOPB_MSGOPT_FIELD_NUMBER: _ClassVar[int]
nanopb: _descriptor.FieldDescriptor
nanopb_enumopt: _descriptor.FieldDescriptor
nanopb_fileopt: _descriptor.FieldDescriptor
nanopb_msgopt: _descriptor.FieldDescriptor

class NanoPBOptions(_message.Message):
    __slots__ = ["anonymous_oneof", "callback_datatype", "callback_function", "default_has", "descriptorsize", "enum_to_string", "exclude", "fallback_type", "fixed_count", "fixed_length", "include", "int_size", "long_names", "mangle_names", "max_count", "max_length", "max_size", "msgid", "no_unions", "package", "packed_enum", "packed_struct", "proto3", "proto3_singular_msgs", "skip_message", "sort_by_tag", "submsg_callback", "type", "type_override"]
    ANONYMOUS_ONEOF_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DATATYPE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_HAS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTORSIZE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIXED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIXED_LENGTH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    INT_SIZE_FIELD_NUMBER: _ClassVar[int]
    LONG_NAMES_FIELD_NUMBER: _ClassVar[int]
    MANGLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    NO_UNIONS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PACKED_ENUM_FIELD_NUMBER: _ClassVar[int]
    PACKED_STRUCT_FIELD_NUMBER: _ClassVar[int]
    PROTO3_FIELD_NUMBER: _ClassVar[int]
    PROTO3_SINGULAR_MSGS_FIELD_NUMBER: _ClassVar[int]
    SKIP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_TAG_FIELD_NUMBER: _ClassVar[int]
    SUBMSG_CALLBACK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    anonymous_oneof: bool
    callback_datatype: str
    callback_function: str
    default_has: bool
    descriptorsize: DescriptorSize
    enum_to_string: bool
    exclude: _containers.RepeatedScalarFieldContainer[str]
    fallback_type: FieldType
    fixed_count: bool
    fixed_length: bool
    include: _containers.RepeatedScalarFieldContainer[str]
    int_size: IntSize
    long_names: bool
    mangle_names: TypenameMangling
    max_count: int
    max_length: int
    max_size: int
    msgid: int
    no_unions: bool
    package: str
    packed_enum: bool
    packed_struct: bool
    proto3: bool
    proto3_singular_msgs: bool
    skip_message: bool
    sort_by_tag: bool
    submsg_callback: bool
    type: FieldType
    type_override: _descriptor_pb2.FieldDescriptorProto.Type
    def __init__(self, max_size: _Optional[int] = ..., max_length: _Optional[int] = ..., max_count: _Optional[int] = ..., int_size: _Optional[_Union[IntSize, str]] = ..., type: _Optional[_Union[FieldType, str]] = ..., long_names: bool = ..., packed_struct: bool = ..., packed_enum: bool = ..., skip_message: bool = ..., no_unions: bool = ..., msgid: _Optional[int] = ..., anonymous_oneof: bool = ..., proto3: bool = ..., proto3_singular_msgs: bool = ..., enum_to_string: bool = ..., fixed_length: bool = ..., fixed_count: bool = ..., submsg_callback: bool = ..., mangle_names: _Optional[_Union[TypenameMangling, str]] = ..., callback_datatype: _Optional[str] = ..., callback_function: _Optional[str] = ..., descriptorsize: _Optional[_Union[DescriptorSize, str]] = ..., default_has: bool = ..., include: _Optional[_Iterable[str]] = ..., exclude: _Optional[_Iterable[str]] = ..., package: _Optional[str] = ..., type_override: _Optional[_Union[_descriptor_pb2.FieldDescriptorProto.Type, str]] = ..., sort_by_tag: bool = ..., fallback_type: _Optional[_Union[FieldType, str]] = ...) -> None: ...

class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IntSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TypenameMangling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DescriptorSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
