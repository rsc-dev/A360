# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gpsalmanacinfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gpsalmanacinfo.proto',
  package='data',
  serialized_pb=_b('\n\x14gpsalmanacinfo.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"7\n\x10PbGPSAlmanacInfo\x12#\n\x08\x65nd_time\x18\x01 \x02(\x0b\x32\x11.PbSystemDateTime')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBGPSALMANACINFO = _descriptor.Descriptor(
  name='PbGPSAlmanacInfo',
  full_name='data.PbGPSAlmanacInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='end_time', full_name='data.PbGPSAlmanacInfo.end_time', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=98,
)

_PBGPSALMANACINFO.fields_by_name['end_time'].message_type = types_pb2._PBSYSTEMDATETIME
DESCRIPTOR.message_types_by_name['PbGPSAlmanacInfo'] = _PBGPSALMANACINFO

PbGPSAlmanacInfo = _reflection.GeneratedProtocolMessageType('PbGPSAlmanacInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBGPSALMANACINFO,
  __module__ = 'gpsalmanacinfo_pb2'
  # @@protoc_insertion_point(class_scope:data.PbGPSAlmanacInfo)
  ))
_sym_db.RegisterMessage(PbGPSAlmanacInfo)


# @@protoc_insertion_point(module_scope)
