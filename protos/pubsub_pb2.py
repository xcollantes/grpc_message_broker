# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/pubsub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protos/pubsub.proto\x12\x10\x65vergreen.pubsub\x1a\x1fgoogle/protobuf/timestamp.proto\"0\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"=\n\x0fPublishResponse\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\"!\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\"l\n\x07Message\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05topic\x18\x04 \x01(\t2\xb1\x01\n\rPubsubService\x12P\n\x07Publish\x12 .evergreen.pubsub.PublishRequest\x1a!.evergreen.pubsub.PublishResponse\"\x00\x12N\n\tSubscribe\x12\".evergreen.pubsub.SubscribeRequest\x1a\x19.evergreen.pubsub.Message\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.pubsub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PUBLISHREQUEST']._serialized_start=74
  _globals['_PUBLISHREQUEST']._serialized_end=122
  _globals['_PUBLISHRESPONSE']._serialized_start=124
  _globals['_PUBLISHRESPONSE']._serialized_end=185
  _globals['_SUBSCRIBEREQUEST']._serialized_start=187
  _globals['_SUBSCRIBEREQUEST']._serialized_end=220
  _globals['_MESSAGE']._serialized_start=222
  _globals['_MESSAGE']._serialized_end=330
  _globals['_PUBSUBSERVICE']._serialized_start=333
  _globals['_PUBSUBSERVICE']._serialized_end=510
# @@protoc_insertion_point(module_scope)
