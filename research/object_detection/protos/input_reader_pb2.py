# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/input_reader.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/input_reader.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n*object_detection/protos/input_reader.proto\x12\x17object_detection.protos\"\xde\x04\n\x0bInputReader\x12\x18\n\x0elabel_map_path\x18\x01 \x01(\t:\x00\x12\x15\n\x07shuffle\x18\x02 \x01(\x08:\x04true\x12!\n\x13shuffle_buffer_size\x18\x0b \x01(\r:\x04\x32\x30\x34\x38\x12*\n\x1d\x66ilenames_shuffle_buffer_size\x18\x0c \x01(\r:\x03\x31\x30\x30\x12\x1c\n\x0equeue_capacity\x18\x03 \x01(\r:\x04\x32\x30\x30\x30\x12\x1f\n\x11min_after_dequeue\x18\x04 \x01(\r:\x04\x31\x30\x30\x30\x12\x15\n\nnum_epochs\x18\x05 \x01(\r:\x01\x30\x12\x17\n\x0bnum_readers\x18\x06 \x01(\r:\x02\x33\x32\x12\x1a\n\rprefetch_size\x18\r \x01(\r:\x03\x35\x31\x32\x12\"\n\x16num_parallel_map_calls\x18\x0e \x01(\r:\x02\x36\x34\x12\"\n\x13load_instance_masks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12M\n\tmask_type\x18\n \x01(\x0e\x32).object_detection.protos.InstanceMaskType:\x0fNUMERICAL_MASKS\x12N\n\x16tf_record_input_reader\x18\x08 \x01(\x0b\x32,.object_detection.protos.TFRecordInputReaderH\x00\x12M\n\x15\x65xternal_input_reader\x18\t \x01(\x0b\x32,.object_detection.protos.ExternalInputReaderH\x00\x42\x0e\n\x0cinput_reader\")\n\x13TFRecordInputReader\x12\x12\n\ninput_path\x18\x01 \x03(\t\"\x1c\n\x13\x45xternalInputReader*\x05\x08\x01\x10\xe8\x07*C\n\x10InstanceMaskType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x13\n\x0fNUMERICAL_MASKS\x10\x01\x12\r\n\tPNG_MASKS\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INSTANCEMASKTYPE = _descriptor.EnumDescriptor(
  name='InstanceMaskType',
  full_name='object_detection.protos.InstanceMaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMERICAL_MASKS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNG_MASKS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=753,
  serialized_end=820,
)
_sym_db.RegisterEnumDescriptor(_INSTANCEMASKTYPE)

InstanceMaskType = enum_type_wrapper.EnumTypeWrapper(_INSTANCEMASKTYPE)
DEFAULT = 0
NUMERICAL_MASKS = 1
PNG_MASKS = 2



_INPUTREADER = _descriptor.Descriptor(
  name='InputReader',
  full_name='object_detection.protos.InputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='object_detection.protos.InputReader.label_map_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shuffle', full_name='object_detection.protos.InputReader.shuffle', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shuffle_buffer_size', full_name='object_detection.protos.InputReader.shuffle_buffer_size', index=2,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2048,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filenames_shuffle_buffer_size', full_name='object_detection.protos.InputReader.filenames_shuffle_buffer_size', index=3,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queue_capacity', full_name='object_detection.protos.InputReader.queue_capacity', index=4,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_after_dequeue', full_name='object_detection.protos.InputReader.min_after_dequeue', index=5,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='object_detection.protos.InputReader.num_epochs', index=6,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_readers', full_name='object_detection.protos.InputReader.num_readers', index=7,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefetch_size', full_name='object_detection.protos.InputReader.prefetch_size', index=8,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_parallel_map_calls', full_name='object_detection.protos.InputReader.num_parallel_map_calls', index=9,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='load_instance_masks', full_name='object_detection.protos.InputReader.load_instance_masks', index=10,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_type', full_name='object_detection.protos.InputReader.mask_type', index=11,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tf_record_input_reader', full_name='object_detection.protos.InputReader.tf_record_input_reader', index=12,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_input_reader', full_name='object_detection.protos.InputReader.external_input_reader', index=13,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='input_reader', full_name='object_detection.protos.InputReader.input_reader',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=678,
)


_TFRECORDINPUTREADER = _descriptor.Descriptor(
  name='TFRecordInputReader',
  full_name='object_detection.protos.TFRecordInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_path', full_name='object_detection.protos.TFRecordInputReader.input_path', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=721,
)


_EXTERNALINPUTREADER = _descriptor.Descriptor(
  name='ExternalInputReader',
  full_name='object_detection.protos.ExternalInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1, 1000), ],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=751,
)

_INPUTREADER.fields_by_name['mask_type'].enum_type = _INSTANCEMASKTYPE
_INPUTREADER.fields_by_name['tf_record_input_reader'].message_type = _TFRECORDINPUTREADER
_INPUTREADER.fields_by_name['external_input_reader'].message_type = _EXTERNALINPUTREADER
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['tf_record_input_reader'])
_INPUTREADER.fields_by_name['tf_record_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['external_input_reader'])
_INPUTREADER.fields_by_name['external_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
DESCRIPTOR.message_types_by_name['InputReader'] = _INPUTREADER
DESCRIPTOR.message_types_by_name['TFRecordInputReader'] = _TFRECORDINPUTREADER
DESCRIPTOR.message_types_by_name['ExternalInputReader'] = _EXTERNALINPUTREADER
DESCRIPTOR.enum_types_by_name['InstanceMaskType'] = _INSTANCEMASKTYPE

InputReader = _reflection.GeneratedProtocolMessageType('InputReader', (_message.Message,), dict(
  DESCRIPTOR = _INPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.InputReader)
  ))
_sym_db.RegisterMessage(InputReader)

TFRecordInputReader = _reflection.GeneratedProtocolMessageType('TFRecordInputReader', (_message.Message,), dict(
  DESCRIPTOR = _TFRECORDINPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TFRecordInputReader)
  ))
_sym_db.RegisterMessage(TFRecordInputReader)

ExternalInputReader = _reflection.GeneratedProtocolMessageType('ExternalInputReader', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALINPUTREADER,
  __module__ = 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExternalInputReader)
  ))
_sym_db.RegisterMessage(ExternalInputReader)


# @@protoc_insertion_point(module_scope)
