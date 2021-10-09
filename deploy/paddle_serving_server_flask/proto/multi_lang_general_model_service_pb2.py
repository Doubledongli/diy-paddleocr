# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multi_lang_general_model_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='multi_lang_general_model_service.proto',
  package='baidu.paddle_serving.multi_lang',
  syntax='proto2',
  serialized_options=b'\n\026io.paddle.serving.grpcB\014ServingProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&multi_lang_general_model_service.proto\x12\x1f\x62\x61idu.paddle_serving.multi_lang\"\x7f\n\x06Tensor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x10\n\x08int_data\x18\x02 \x03(\x05\x12\x12\n\nint64_data\x18\x03 \x03(\x03\x12\x12\n\nfloat_data\x18\x04 \x03(\x02\x12\x11\n\telem_type\x18\x05 \x01(\x05\x12\r\n\x05shape\x18\x06 \x03(\x05\x12\x0b\n\x03lod\x18\x07 \x03(\x05\"I\n\x08\x46\x65\x65\x64Inst\x12=\n\x0ctensor_array\x18\x01 \x03(\x0b\x32\'.baidu.paddle_serving.multi_lang.Tensor\"J\n\tFetchInst\x12=\n\x0ctensor_array\x18\x01 \x03(\x0b\x32\'.baidu.paddle_serving.multi_lang.Tensor\"\xaa\x01\n\x10InferenceRequest\x12\x38\n\x05insts\x18\x01 \x03(\x0b\x32).baidu.paddle_serving.multi_lang.FeedInst\x12\x16\n\x0e\x66\x65\x65\x64_var_names\x18\x02 \x03(\t\x12\x17\n\x0f\x66\x65tch_var_names\x18\x03 \x03(\t\x12\x18\n\tis_python\x18\x04 \x02(\x08:\x05\x66\x61lse\x12\x11\n\x06log_id\x18\x05 \x02(\x04:\x01\x30\"q\n\x11InferenceResponse\x12=\n\x07outputs\x18\x01 \x03(\x0b\x32,.baidu.paddle_serving.multi_lang.ModelOutput\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x10\n\x08\x65rr_code\x18\x03 \x02(\x05\"]\n\x0bModelOutput\x12\x39\n\x05insts\x18\x01 \x03(\x0b\x32*.baidu.paddle_serving.multi_lang.FetchInst\x12\x13\n\x0b\x65ngine_name\x18\x02 \x01(\t\"\'\n\x11SetTimeoutRequest\x12\x12\n\ntimeout_ms\x18\x01 \x02(\x05\"\"\n\x0eSimpleResponse\x12\x10\n\x08\x65rr_code\x18\x01 \x02(\x05\"\x18\n\x16GetClientConfigRequest\"4\n\x17GetClientConfigResponse\x12\x19\n\x11\x63lient_config_str\x18\x01 \x02(\t2\x92\x03\n\x1cMultiLangGeneralModelService\x12t\n\tInference\x12\x31.baidu.paddle_serving.multi_lang.InferenceRequest\x1a\x32.baidu.paddle_serving.multi_lang.InferenceResponse\"\x00\x12s\n\nSetTimeout\x12\x32.baidu.paddle_serving.multi_lang.SetTimeoutRequest\x1a/.baidu.paddle_serving.multi_lang.SimpleResponse\"\x00\x12\x86\x01\n\x0fGetClientConfig\x12\x37.baidu.paddle_serving.multi_lang.GetClientConfigRequest\x1a\x38.baidu.paddle_serving.multi_lang.GetClientConfigResponse\"\x00\x42(\n\x16io.paddle.serving.grpcB\x0cServingProtoP\x01'
)




_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='baidu.paddle_serving.multi_lang.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='baidu.paddle_serving.multi_lang.Tensor.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_data', full_name='baidu.paddle_serving.multi_lang.Tensor.int_data', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_data', full_name='baidu.paddle_serving.multi_lang.Tensor.int64_data', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='baidu.paddle_serving.multi_lang.Tensor.float_data', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elem_type', full_name='baidu.paddle_serving.multi_lang.Tensor.elem_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='baidu.paddle_serving.multi_lang.Tensor.shape', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lod', full_name='baidu.paddle_serving.multi_lang.Tensor.lod', index=6,
      number=7, type=5, cpp_type=1, label=3,
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
  serialized_start=75,
  serialized_end=202,
)


_FEEDINST = _descriptor.Descriptor(
  name='FeedInst',
  full_name='baidu.paddle_serving.multi_lang.FeedInst',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_array', full_name='baidu.paddle_serving.multi_lang.FeedInst.tensor_array', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=204,
  serialized_end=277,
)


_FETCHINST = _descriptor.Descriptor(
  name='FetchInst',
  full_name='baidu.paddle_serving.multi_lang.FetchInst',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_array', full_name='baidu.paddle_serving.multi_lang.FetchInst.tensor_array', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=279,
  serialized_end=353,
)


_INFERENCEREQUEST = _descriptor.Descriptor(
  name='InferenceRequest',
  full_name='baidu.paddle_serving.multi_lang.InferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='insts', full_name='baidu.paddle_serving.multi_lang.InferenceRequest.insts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed_var_names', full_name='baidu.paddle_serving.multi_lang.InferenceRequest.feed_var_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fetch_var_names', full_name='baidu.paddle_serving.multi_lang.InferenceRequest.fetch_var_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_python', full_name='baidu.paddle_serving.multi_lang.InferenceRequest.is_python', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_id', full_name='baidu.paddle_serving.multi_lang.InferenceRequest.log_id', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=True, default_value=0,
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
  serialized_start=356,
  serialized_end=526,
)


_INFERENCERESPONSE = _descriptor.Descriptor(
  name='InferenceResponse',
  full_name='baidu.paddle_serving.multi_lang.InferenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='baidu.paddle_serving.multi_lang.InferenceResponse.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='baidu.paddle_serving.multi_lang.InferenceResponse.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='baidu.paddle_serving.multi_lang.InferenceResponse.err_code', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=528,
  serialized_end=641,
)


_MODELOUTPUT = _descriptor.Descriptor(
  name='ModelOutput',
  full_name='baidu.paddle_serving.multi_lang.ModelOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='insts', full_name='baidu.paddle_serving.multi_lang.ModelOutput.insts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='engine_name', full_name='baidu.paddle_serving.multi_lang.ModelOutput.engine_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=643,
  serialized_end=736,
)


_SETTIMEOUTREQUEST = _descriptor.Descriptor(
  name='SetTimeoutRequest',
  full_name='baidu.paddle_serving.multi_lang.SetTimeoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout_ms', full_name='baidu.paddle_serving.multi_lang.SetTimeoutRequest.timeout_ms', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=738,
  serialized_end=777,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='baidu.paddle_serving.multi_lang.SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='baidu.paddle_serving.multi_lang.SimpleResponse.err_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=779,
  serialized_end=813,
)


_GETCLIENTCONFIGREQUEST = _descriptor.Descriptor(
  name='GetClientConfigRequest',
  full_name='baidu.paddle_serving.multi_lang.GetClientConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=815,
  serialized_end=839,
)


_GETCLIENTCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetClientConfigResponse',
  full_name='baidu.paddle_serving.multi_lang.GetClientConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_config_str', full_name='baidu.paddle_serving.multi_lang.GetClientConfigResponse.client_config_str', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=841,
  serialized_end=893,
)

_FEEDINST.fields_by_name['tensor_array'].message_type = _TENSOR
_FETCHINST.fields_by_name['tensor_array'].message_type = _TENSOR
_INFERENCEREQUEST.fields_by_name['insts'].message_type = _FEEDINST
_INFERENCERESPONSE.fields_by_name['outputs'].message_type = _MODELOUTPUT
_MODELOUTPUT.fields_by_name['insts'].message_type = _FETCHINST
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.message_types_by_name['FeedInst'] = _FEEDINST
DESCRIPTOR.message_types_by_name['FetchInst'] = _FETCHINST
DESCRIPTOR.message_types_by_name['InferenceRequest'] = _INFERENCEREQUEST
DESCRIPTOR.message_types_by_name['InferenceResponse'] = _INFERENCERESPONSE
DESCRIPTOR.message_types_by_name['ModelOutput'] = _MODELOUTPUT
DESCRIPTOR.message_types_by_name['SetTimeoutRequest'] = _SETTIMEOUTREQUEST
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE
DESCRIPTOR.message_types_by_name['GetClientConfigRequest'] = _GETCLIENTCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetClientConfigResponse'] = _GETCLIENTCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.Tensor)
  })
_sym_db.RegisterMessage(Tensor)

FeedInst = _reflection.GeneratedProtocolMessageType('FeedInst', (_message.Message,), {
  'DESCRIPTOR' : _FEEDINST,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.FeedInst)
  })
_sym_db.RegisterMessage(FeedInst)

FetchInst = _reflection.GeneratedProtocolMessageType('FetchInst', (_message.Message,), {
  'DESCRIPTOR' : _FETCHINST,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.FetchInst)
  })
_sym_db.RegisterMessage(FetchInst)

InferenceRequest = _reflection.GeneratedProtocolMessageType('InferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREQUEST,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.InferenceRequest)
  })
_sym_db.RegisterMessage(InferenceRequest)

InferenceResponse = _reflection.GeneratedProtocolMessageType('InferenceResponse', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCERESPONSE,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.InferenceResponse)
  })
_sym_db.RegisterMessage(InferenceResponse)

ModelOutput = _reflection.GeneratedProtocolMessageType('ModelOutput', (_message.Message,), {
  'DESCRIPTOR' : _MODELOUTPUT,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.ModelOutput)
  })
_sym_db.RegisterMessage(ModelOutput)

SetTimeoutRequest = _reflection.GeneratedProtocolMessageType('SetTimeoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETTIMEOUTREQUEST,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.SetTimeoutRequest)
  })
_sym_db.RegisterMessage(SetTimeoutRequest)

SimpleResponse = _reflection.GeneratedProtocolMessageType('SimpleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSE,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.SimpleResponse)
  })
_sym_db.RegisterMessage(SimpleResponse)

GetClientConfigRequest = _reflection.GeneratedProtocolMessageType('GetClientConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTCONFIGREQUEST,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.GetClientConfigRequest)
  })
_sym_db.RegisterMessage(GetClientConfigRequest)

GetClientConfigResponse = _reflection.GeneratedProtocolMessageType('GetClientConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTCONFIGRESPONSE,
  '__module__' : 'multi_lang_general_model_service_pb2'
  # @@protoc_insertion_point(class_scope:baidu.paddle_serving.multi_lang.GetClientConfigResponse)
  })
_sym_db.RegisterMessage(GetClientConfigResponse)


DESCRIPTOR._options = None

_MULTILANGGENERALMODELSERVICE = _descriptor.ServiceDescriptor(
  name='MultiLangGeneralModelService',
  full_name='baidu.paddle_serving.multi_lang.MultiLangGeneralModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=896,
  serialized_end=1298,
  methods=[
  _descriptor.MethodDescriptor(
    name='Inference',
    full_name='baidu.paddle_serving.multi_lang.MultiLangGeneralModelService.Inference',
    index=0,
    containing_service=None,
    input_type=_INFERENCEREQUEST,
    output_type=_INFERENCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetTimeout',
    full_name='baidu.paddle_serving.multi_lang.MultiLangGeneralModelService.SetTimeout',
    index=1,
    containing_service=None,
    input_type=_SETTIMEOUTREQUEST,
    output_type=_SIMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetClientConfig',
    full_name='baidu.paddle_serving.multi_lang.MultiLangGeneralModelService.GetClientConfig',
    index=2,
    containing_service=None,
    input_type=_GETCLIENTCONFIGREQUEST,
    output_type=_GETCLIENTCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MULTILANGGENERALMODELSERVICE)

DESCRIPTOR.services_by_name['MultiLangGeneralModelService'] = _MULTILANGGENERALMODELSERVICE

# @@protoc_insertion_point(module_scope)