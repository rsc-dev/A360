# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sportprofile_mclaren_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sportprofile_mclaren_settings.proto',
  package='data',
  serialized_pb=_b('\n#sportprofile_mclaren_settings.proto\x12\x04\x64\x61ta\"3\n\x1dPbMcLarenSportProfileSettings\x12\x12\n\nauto_start\x18\x04 \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBMCLARENSPORTPROFILESETTINGS = _descriptor.Descriptor(
  name='PbMcLarenSportProfileSettings',
  full_name='data.PbMcLarenSportProfileSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auto_start', full_name='data.PbMcLarenSportProfileSettings.auto_start', index=0,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=45,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['PbMcLarenSportProfileSettings'] = _PBMCLARENSPORTPROFILESETTINGS

PbMcLarenSportProfileSettings = _reflection.GeneratedProtocolMessageType('PbMcLarenSportProfileSettings', (_message.Message,), dict(
  DESCRIPTOR = _PBMCLARENSPORTPROFILESETTINGS,
  __module__ = 'sportprofile_mclaren_settings_pb2'
  # @@protoc_insertion_point(class_scope:data.PbMcLarenSportProfileSettings)
  ))
_sym_db.RegisterMessage(PbMcLarenSportProfileSettings)


# @@protoc_insertion_point(module_scope)