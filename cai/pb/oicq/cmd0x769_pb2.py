# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/oicq/cmd0x769.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cai/pb/oicq/cmd0x769.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63\x61i/pb/oicq/cmd0x769.proto\"6\n\x03\x43PU\x12\r\n\x05model\x18\x01 \x01(\t\x12\r\n\x05\x63ores\x18\x02 \x01(\r\x12\x11\n\tfrequency\x18\x03 \x01(\r\";\n\x06\x43\x61mera\x12\x0f\n\x07primary\x18\x01 \x01(\x04\x12\x11\n\tsecondary\x18\x02 \x01(\x04\x12\r\n\x05\x66lash\x18\x03 \x01(\x08\"t\n\x06\x43onfig\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x14\n\x0c\x63ontent_list\x18\x03 \x03(\t\x12\x11\n\tdebug_msg\x18\x04 \x01(\t\x12\"\n\x10msg_content_list\x18\x05 \x03(\x0b\x32\x08.Content\"*\n\tConfigSeq\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\r\"=\n\x07\x43ontent\x12\x0f\n\x07task_id\x18\x01 \x01(\r\x12\x10\n\x08\x63ompress\x18\x02 \x01(\r\x12\x0f\n\x07\x63ontent\x18\n \x01(\x0c\"\xb4\x01\n\nDeviceInfo\x12\r\n\x05\x62rand\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0f\n\x02os\x18\x03 \x01(\x0b\x32\x03.OS\x12\x11\n\x03\x63pu\x18\x04 \x01(\x0b\x32\x04.CPU\x12\x17\n\x06memory\x18\x05 \x01(\x0b\x32\x07.Memory\x12\x19\n\x07storage\x18\x06 \x01(\x0b\x32\x08.Storage\x12\x17\n\x06screen\x18\x07 \x01(\x0b\x32\x07.Screen\x12\x17\n\x06\x63\x61mera\x18\x08 \x01(\x0b\x32\x07.Camera\"(\n\x06Memory\x12\r\n\x05total\x18\x01 \x01(\x04\x12\x0f\n\x07process\x18\x02 \x01(\x04\"M\n\x02OS\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sdk\x18\x03 \x01(\t\x12\x0e\n\x06kernel\x18\x04 \x01(\t\x12\x0b\n\x03rom\x18\x05 \x01(\t\">\n\x17QueryUinPackageUsageReq\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x15\n\ruin_file_size\x18\x02 \x01(\x04\"\x9c\x01\n\x17QueryUinPackageUsageRsp\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x14\n\x0cleft_uin_num\x18\x02 \x01(\x04\x12\x13\n\x0bmax_uin_num\x18\x03 \x01(\x04\x12\x12\n\nproportion\x18\x04 \x01(\r\x12\x32\n\x15uin_package_used_list\x18\n \x03(\x0b\x32\x13.UinPackageUsedInfo\"\xd0\x01\n\x07ReqBody\x12\x1f\n\x0b\x63onfig_list\x18\x01 \x03(\x0b\x32\n.ConfigSeq\x12 \n\x0b\x64\x65vice_info\x18\x02 \x01(\x0b\x32\x0b.DeviceInfo\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x10\n\x08province\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x15\n\rreq_debug_msg\x18\x06 \x01(\x05\x12=\n\x1bquery_uin_package_usage_req\x18\x65 \x01(\x0b\x32\x18.QueryUinPackageUsageReq\"v\n\x07RspBody\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x1c\n\x0b\x63onfig_list\x18\x02 \x03(\x0b\x32\x07.Config\x12=\n\x1bquery_uin_package_usage_rsp\x18\x65 \x01(\x0b\x32\x18.QueryUinPackageUsageRsp\"X\n\x06Screen\x12\r\n\x05model\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x0b\n\x03\x64pi\x18\x04 \x01(\r\x12\x13\n\x0bmulti_touch\x18\x05 \x01(\x08\",\n\x07Storage\x12\x0f\n\x07\x62uiltin\x18\x01 \x01(\x04\x12\x10\n\x08\x65xternal\x18\x02 \x01(\x04\"S\n\x12UinPackageUsedInfo\x12\x0f\n\x07rule_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07uin_num\x18\x04 \x01(\x04'
)




_CPU = _descriptor.Descriptor(
  name='CPU',
  full_name='CPU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='CPU.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cores', full_name='CPU.cores', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='CPU.frequency', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=84,
)


_CAMERA = _descriptor.Descriptor(
  name='Camera',
  full_name='Camera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary', full_name='Camera.primary', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secondary', full_name='Camera.secondary', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flash', full_name='Camera.flash', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=145,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Config.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='Config.version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_list', full_name='Config.content_list', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_msg', full_name='Config.debug_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_content_list', full_name='Config.msg_content_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=263,
)


_CONFIGSEQ = _descriptor.Descriptor(
  name='ConfigSeq',
  full_name='ConfigSeq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ConfigSeq.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='ConfigSeq.version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=307,
)


_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='Content.task_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compress', full_name='Content.compress', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='Content.content', index=2,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=370,
)


_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='brand', full_name='DeviceInfo.brand', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='DeviceInfo.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os', full_name='DeviceInfo.os', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='DeviceInfo.cpu', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='DeviceInfo.memory', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage', full_name='DeviceInfo.storage', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screen', full_name='DeviceInfo.screen', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='camera', full_name='DeviceInfo.camera', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=553,
)


_MEMORY = _descriptor.Descriptor(
  name='Memory',
  full_name='Memory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='Memory.total', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process', full_name='Memory.process', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=595,
)


_OS = _descriptor.Descriptor(
  name='OS',
  full_name='OS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='OS.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='OS.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdk', full_name='OS.sdk', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kernel', full_name='OS.kernel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rom', full_name='OS.rom', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=674,
)


_QUERYUINPACKAGEUSAGEREQ = _descriptor.Descriptor(
  name='QueryUinPackageUsageReq',
  full_name='QueryUinPackageUsageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='QueryUinPackageUsageReq.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uin_file_size', full_name='QueryUinPackageUsageReq.uin_file_size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=676,
  serialized_end=738,
)


_QUERYUINPACKAGEUSAGERSP = _descriptor.Descriptor(
  name='QueryUinPackageUsageRsp',
  full_name='QueryUinPackageUsageRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='QueryUinPackageUsageRsp.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left_uin_num', full_name='QueryUinPackageUsageRsp.left_uin_num', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_uin_num', full_name='QueryUinPackageUsageRsp.max_uin_num', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proportion', full_name='QueryUinPackageUsageRsp.proportion', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uin_package_used_list', full_name='QueryUinPackageUsageRsp.uin_package_used_list', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=897,
)


_REQBODY = _descriptor.Descriptor(
  name='ReqBody',
  full_name='ReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_list', full_name='ReqBody.config_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='ReqBody.device_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='ReqBody.info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='province', full_name='ReqBody.province', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='ReqBody.city', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='req_debug_msg', full_name='ReqBody.req_debug_msg', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_uin_package_usage_req', full_name='ReqBody.query_uin_package_usage_req', index=6,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=900,
  serialized_end=1108,
)


_RSPBODY = _descriptor.Descriptor(
  name='RspBody',
  full_name='RspBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='RspBody.result', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config_list', full_name='RspBody.config_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_uin_package_usage_rsp', full_name='RspBody.query_uin_package_usage_rsp', index=2,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1228,
)


_SCREEN = _descriptor.Descriptor(
  name='Screen',
  full_name='Screen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='Screen.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Screen.width', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='Screen.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dpi', full_name='Screen.dpi', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi_touch', full_name='Screen.multi_touch', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1230,
  serialized_end=1318,
)


_STORAGE = _descriptor.Descriptor(
  name='Storage',
  full_name='Storage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='builtin', full_name='Storage.builtin', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external', full_name='Storage.external', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1320,
  serialized_end=1364,
)


_UINPACKAGEUSEDINFO = _descriptor.Descriptor(
  name='UinPackageUsedInfo',
  full_name='UinPackageUsedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rule_id', full_name='UinPackageUsedInfo.rule_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='UinPackageUsedInfo.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='UinPackageUsedInfo.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uin_num', full_name='UinPackageUsedInfo.uin_num', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1366,
  serialized_end=1449,
)

_CONFIG.fields_by_name['msg_content_list'].message_type = _CONTENT
_DEVICEINFO.fields_by_name['os'].message_type = _OS
_DEVICEINFO.fields_by_name['cpu'].message_type = _CPU
_DEVICEINFO.fields_by_name['memory'].message_type = _MEMORY
_DEVICEINFO.fields_by_name['storage'].message_type = _STORAGE
_DEVICEINFO.fields_by_name['screen'].message_type = _SCREEN
_DEVICEINFO.fields_by_name['camera'].message_type = _CAMERA
_QUERYUINPACKAGEUSAGERSP.fields_by_name['uin_package_used_list'].message_type = _UINPACKAGEUSEDINFO
_REQBODY.fields_by_name['config_list'].message_type = _CONFIGSEQ
_REQBODY.fields_by_name['device_info'].message_type = _DEVICEINFO
_REQBODY.fields_by_name['query_uin_package_usage_req'].message_type = _QUERYUINPACKAGEUSAGEREQ
_RSPBODY.fields_by_name['config_list'].message_type = _CONFIG
_RSPBODY.fields_by_name['query_uin_package_usage_rsp'].message_type = _QUERYUINPACKAGEUSAGERSP
DESCRIPTOR.message_types_by_name['CPU'] = _CPU
DESCRIPTOR.message_types_by_name['Camera'] = _CAMERA
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['ConfigSeq'] = _CONFIGSEQ
DESCRIPTOR.message_types_by_name['Content'] = _CONTENT
DESCRIPTOR.message_types_by_name['DeviceInfo'] = _DEVICEINFO
DESCRIPTOR.message_types_by_name['Memory'] = _MEMORY
DESCRIPTOR.message_types_by_name['OS'] = _OS
DESCRIPTOR.message_types_by_name['QueryUinPackageUsageReq'] = _QUERYUINPACKAGEUSAGEREQ
DESCRIPTOR.message_types_by_name['QueryUinPackageUsageRsp'] = _QUERYUINPACKAGEUSAGERSP
DESCRIPTOR.message_types_by_name['ReqBody'] = _REQBODY
DESCRIPTOR.message_types_by_name['RspBody'] = _RSPBODY
DESCRIPTOR.message_types_by_name['Screen'] = _SCREEN
DESCRIPTOR.message_types_by_name['Storage'] = _STORAGE
DESCRIPTOR.message_types_by_name['UinPackageUsedInfo'] = _UINPACKAGEUSEDINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CPU = _reflection.GeneratedProtocolMessageType('CPU', (_message.Message,), {
  'DESCRIPTOR' : _CPU,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:CPU)
  })
_sym_db.RegisterMessage(CPU)

Camera = _reflection.GeneratedProtocolMessageType('Camera', (_message.Message,), {
  'DESCRIPTOR' : _CAMERA,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Camera)
  })
_sym_db.RegisterMessage(Camera)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)

ConfigSeq = _reflection.GeneratedProtocolMessageType('ConfigSeq', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSEQ,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:ConfigSeq)
  })
_sym_db.RegisterMessage(ConfigSeq)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Content)
  })
_sym_db.RegisterMessage(Content)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFO,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:DeviceInfo)
  })
_sym_db.RegisterMessage(DeviceInfo)

Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), {
  'DESCRIPTOR' : _MEMORY,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Memory)
  })
_sym_db.RegisterMessage(Memory)

OS = _reflection.GeneratedProtocolMessageType('OS', (_message.Message,), {
  'DESCRIPTOR' : _OS,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:OS)
  })
_sym_db.RegisterMessage(OS)

QueryUinPackageUsageReq = _reflection.GeneratedProtocolMessageType('QueryUinPackageUsageReq', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUINPACKAGEUSAGEREQ,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:QueryUinPackageUsageReq)
  })
_sym_db.RegisterMessage(QueryUinPackageUsageReq)

QueryUinPackageUsageRsp = _reflection.GeneratedProtocolMessageType('QueryUinPackageUsageRsp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUINPACKAGEUSAGERSP,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:QueryUinPackageUsageRsp)
  })
_sym_db.RegisterMessage(QueryUinPackageUsageRsp)

ReqBody = _reflection.GeneratedProtocolMessageType('ReqBody', (_message.Message,), {
  'DESCRIPTOR' : _REQBODY,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:ReqBody)
  })
_sym_db.RegisterMessage(ReqBody)

RspBody = _reflection.GeneratedProtocolMessageType('RspBody', (_message.Message,), {
  'DESCRIPTOR' : _RSPBODY,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:RspBody)
  })
_sym_db.RegisterMessage(RspBody)

Screen = _reflection.GeneratedProtocolMessageType('Screen', (_message.Message,), {
  'DESCRIPTOR' : _SCREEN,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Screen)
  })
_sym_db.RegisterMessage(Screen)

Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {
  'DESCRIPTOR' : _STORAGE,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:Storage)
  })
_sym_db.RegisterMessage(Storage)

UinPackageUsedInfo = _reflection.GeneratedProtocolMessageType('UinPackageUsedInfo', (_message.Message,), {
  'DESCRIPTOR' : _UINPACKAGEUSEDINFO,
  '__module__' : 'cai.pb.oicq.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:UinPackageUsedInfo)
  })
_sym_db.RegisterMessage(UinPackageUsedInfo)


# @@protoc_insertion_point(module_scope)