# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metisfl/proto/learner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metisfl.proto import model_pb2 as metisfl_dot_proto_dot_model__pb2
from metisfl.proto import service_common_pb2 as metisfl_dot_proto_dot_service__common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metisfl/proto/learner.proto',
  package='metisfl',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bmetisfl/proto/learner.proto\x12\x07metisfl\x1a\x19metisfl/proto/model.proto\x1a\"metisfl/proto/service_common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe6\x01\n\x04Task\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nlearner_id\x18\x02 \x01(\tR\tlearnerId\x12\x33\n\x07sent_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x06sentAt\x12;\n\x0breceived_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nreceivedAt\x12=\n\x0c\x63ompleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63ompletedAt\"\x85\x01\n\x0cTrainRequest\x12!\n\x04task\x18\x01 \x01(\x0b\x32\r.metisfl.TaskR\x04task\x12$\n\x05model\x18\x02 \x01(\x0b\x32\x0e.metisfl.ModelR\x05model\x12,\n\x06params\x18\x03 \x01(\x0b\x32\x14.metisfl.TrainParamsR\x06params\"\x8a\x01\n\x0bTrainParams\x12\x1d\n\nbatch_size\x18\x02 \x01(\rR\tbatchSize\x12\x16\n\x06\x65pochs\x18\x03 \x01(\rR\x06\x65pochs\x12*\n\x11num_local_updates\x18\x04 \x01(\rR\x0fnumLocalUpdates\x12\x18\n\x07metrics\x18\x05 \x03(\tR\x07metrics\"\x8d\x01\n\x0f\x45valuateRequest\x12!\n\x04task\x18\x01 \x01(\x0b\x32\r.metisfl.TaskR\x04task\x12$\n\x05model\x18\x02 \x01(\x0b\x32\x0e.metisfl.ModelR\x05model\x12\x31\n\x06params\x18\x03 \x01(\x0b\x32\x19.metisfl.EvaluationParamsR\x06params\"K\n\x10\x45valuationParams\x12\x1d\n\nbatch_size\x18\x01 \x01(\rR\tbatchSize\x12\x18\n\x07metrics\x18\x02 \x03(\tR\x07metrics\"k\n\x10\x45valuateResponse\x12!\n\x04task\x18\x01 \x01(\x0b\x32\r.metisfl.TaskR\x04task\x12\x34\n\x07results\x18\x02 \x01(\x0b\x32\x1a.metisfl.EvaluationResultsR\x07results\"\x92\x01\n\x11\x45valuationResults\x12\x41\n\x07metrics\x18\x01 \x03(\x0b\x32\'.metisfl.EvaluationResults.MetricsEntryR\x07metrics\x1a:\n\x0cMetricsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x02\x38\x01\x32\xc3\x02\n\x0eLearnerService\x12\x31\n\x0fGetHealthStatus\x12\x0e.metisfl.Empty\x1a\x0c.metisfl.Ack\"\x00\x12,\n\x08GetModel\x12\x0e.metisfl.Empty\x1a\x0e.metisfl.Model\"\x00\x12\x31\n\x0fSetInitialModel\x12\x0e.metisfl.Model\x1a\x0c.metisfl.Ack\"\x00\x12.\n\x05Train\x12\x15.metisfl.TrainRequest\x1a\x0c.metisfl.Ack\"\x00\x12\x41\n\x08\x45valuate\x12\x18.metisfl.EvaluateRequest\x1a\x19.metisfl.EvaluateResponse\"\x00\x12*\n\x08ShutDown\x12\x0e.metisfl.Empty\x1a\x0c.metisfl.Ack\"\x00\x62\x06proto3'
  ,
  dependencies=[metisfl_dot_proto_dot_model__pb2.DESCRIPTOR,metisfl_dot_proto_dot_service__common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='metisfl.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metisfl.Task.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='learner_id', full_name='metisfl.Task.learner_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='learnerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_at', full_name='metisfl.Task.sent_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sentAt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received_at', full_name='metisfl.Task.received_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='receivedAt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed_at', full_name='metisfl.Task.completed_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='completedAt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=367,
)


_TRAINREQUEST = _descriptor.Descriptor(
  name='TrainRequest',
  full_name='metisfl.TrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='metisfl.TrainRequest.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='task', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='metisfl.TrainRequest.model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='model', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='metisfl.TrainRequest.params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=370,
  serialized_end=503,
)


_TRAINPARAMS = _descriptor.Descriptor(
  name='TrainParams',
  full_name='metisfl.TrainParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='metisfl.TrainParams.batch_size', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='batchSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='metisfl.TrainParams.epochs', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='epochs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_local_updates', full_name='metisfl.TrainParams.num_local_updates', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='numLocalUpdates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='metisfl.TrainParams.metrics', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=644,
)


_EVALUATEREQUEST = _descriptor.Descriptor(
  name='EvaluateRequest',
  full_name='metisfl.EvaluateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='metisfl.EvaluateRequest.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='task', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='metisfl.EvaluateRequest.model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='model', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='metisfl.EvaluateRequest.params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=788,
)


_EVALUATIONPARAMS = _descriptor.Descriptor(
  name='EvaluationParams',
  full_name='metisfl.EvaluationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='metisfl.EvaluationParams.batch_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='batchSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='metisfl.EvaluationParams.metrics', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=790,
  serialized_end=865,
)


_EVALUATERESPONSE = _descriptor.Descriptor(
  name='EvaluateResponse',
  full_name='metisfl.EvaluateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='metisfl.EvaluateResponse.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='task', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='metisfl.EvaluateResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=974,
)


_EVALUATIONRESULTS_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='metisfl.EvaluationResults.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='metisfl.EvaluationResults.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='metisfl.EvaluationResults.MetricsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1065,
  serialized_end=1123,
)

_EVALUATIONRESULTS = _descriptor.Descriptor(
  name='EvaluationResults',
  full_name='metisfl.EvaluationResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='metisfl.EvaluationResults.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVALUATIONRESULTS_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=977,
  serialized_end=1123,
)

_TASK.fields_by_name['sent_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name['received_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name['completed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRAINREQUEST.fields_by_name['task'].message_type = _TASK
_TRAINREQUEST.fields_by_name['model'].message_type = metisfl_dot_proto_dot_model__pb2._MODEL
_TRAINREQUEST.fields_by_name['params'].message_type = _TRAINPARAMS
_EVALUATEREQUEST.fields_by_name['task'].message_type = _TASK
_EVALUATEREQUEST.fields_by_name['model'].message_type = metisfl_dot_proto_dot_model__pb2._MODEL
_EVALUATEREQUEST.fields_by_name['params'].message_type = _EVALUATIONPARAMS
_EVALUATERESPONSE.fields_by_name['task'].message_type = _TASK
_EVALUATERESPONSE.fields_by_name['results'].message_type = _EVALUATIONRESULTS
_EVALUATIONRESULTS_METRICSENTRY.containing_type = _EVALUATIONRESULTS
_EVALUATIONRESULTS.fields_by_name['metrics'].message_type = _EVALUATIONRESULTS_METRICSENTRY
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TrainRequest'] = _TRAINREQUEST
DESCRIPTOR.message_types_by_name['TrainParams'] = _TRAINPARAMS
DESCRIPTOR.message_types_by_name['EvaluateRequest'] = _EVALUATEREQUEST
DESCRIPTOR.message_types_by_name['EvaluationParams'] = _EVALUATIONPARAMS
DESCRIPTOR.message_types_by_name['EvaluateResponse'] = _EVALUATERESPONSE
DESCRIPTOR.message_types_by_name['EvaluationResults'] = _EVALUATIONRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.Task)
  })
_sym_db.RegisterMessage(Task)

TrainRequest = _reflection.GeneratedProtocolMessageType('TrainRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAINREQUEST,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.TrainRequest)
  })
_sym_db.RegisterMessage(TrainRequest)

TrainParams = _reflection.GeneratedProtocolMessageType('TrainParams', (_message.Message,), {
  'DESCRIPTOR' : _TRAINPARAMS,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.TrainParams)
  })
_sym_db.RegisterMessage(TrainParams)

EvaluateRequest = _reflection.GeneratedProtocolMessageType('EvaluateRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEREQUEST,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluateRequest)
  })
_sym_db.RegisterMessage(EvaluateRequest)

EvaluationParams = _reflection.GeneratedProtocolMessageType('EvaluationParams', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONPARAMS,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluationParams)
  })
_sym_db.RegisterMessage(EvaluationParams)

EvaluateResponse = _reflection.GeneratedProtocolMessageType('EvaluateResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATERESPONSE,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluateResponse)
  })
_sym_db.RegisterMessage(EvaluateResponse)

EvaluationResults = _reflection.GeneratedProtocolMessageType('EvaluationResults', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVALUATIONRESULTS_METRICSENTRY,
    '__module__' : 'metisfl.proto.learner_pb2'
    # @@protoc_insertion_point(class_scope:metisfl.EvaluationResults.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _EVALUATIONRESULTS,
  '__module__' : 'metisfl.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:metisfl.EvaluationResults)
  })
_sym_db.RegisterMessage(EvaluationResults)
_sym_db.RegisterMessage(EvaluationResults.MetricsEntry)


_EVALUATIONRESULTS_METRICSENTRY._options = None

_LEARNERSERVICE = _descriptor.ServiceDescriptor(
  name='LearnerService',
  full_name='metisfl.LearnerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1126,
  serialized_end=1449,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHealthStatus',
    full_name='metisfl.LearnerService.GetHealthStatus',
    index=0,
    containing_service=None,
    input_type=metisfl_dot_proto_dot_service__common__pb2._EMPTY,
    output_type=metisfl_dot_proto_dot_service__common__pb2._ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetModel',
    full_name='metisfl.LearnerService.GetModel',
    index=1,
    containing_service=None,
    input_type=metisfl_dot_proto_dot_service__common__pb2._EMPTY,
    output_type=metisfl_dot_proto_dot_model__pb2._MODEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetInitialModel',
    full_name='metisfl.LearnerService.SetInitialModel',
    index=2,
    containing_service=None,
    input_type=metisfl_dot_proto_dot_model__pb2._MODEL,
    output_type=metisfl_dot_proto_dot_service__common__pb2._ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Train',
    full_name='metisfl.LearnerService.Train',
    index=3,
    containing_service=None,
    input_type=_TRAINREQUEST,
    output_type=metisfl_dot_proto_dot_service__common__pb2._ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Evaluate',
    full_name='metisfl.LearnerService.Evaluate',
    index=4,
    containing_service=None,
    input_type=_EVALUATEREQUEST,
    output_type=_EVALUATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ShutDown',
    full_name='metisfl.LearnerService.ShutDown',
    index=5,
    containing_service=None,
    input_type=metisfl_dot_proto_dot_service__common__pb2._EMPTY,
    output_type=metisfl_dot_proto_dot_service__common__pb2._ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEARNERSERVICE)

DESCRIPTOR.services_by_name['LearnerService'] = _LEARNERSERVICE

# @@protoc_insertion_point(module_scope)
