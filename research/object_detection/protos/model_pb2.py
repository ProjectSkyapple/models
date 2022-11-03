# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import center_net_pb2 as center__net__pb2
import faster_rcnn_pb2 as faster__rcnn__pb2
import ssd_pb2 as ssd__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x17object_detection.protos\x1a\x10\x63\x65nter_net.proto\x1a\x11\x66\x61ster_rcnn.proto\x1a\tssd.proto\"\x86\x02\n\x0e\x44\x65tectionModel\x12:\n\x0b\x66\x61ster_rcnn\x18\x01 \x01(\x0b\x32#.object_detection.protos.FasterRcnnH\x00\x12+\n\x03ssd\x18\x02 \x01(\x0b\x32\x1c.object_detection.protos.SsdH\x00\x12H\n\x12\x65xperimental_model\x18\x03 \x01(\x0b\x32*.object_detection.protos.ExperimentalModelH\x00\x12\x38\n\ncenter_net\x18\x04 \x01(\x0b\x32\".object_detection.protos.CenterNetH\x00\x42\x07\n\x05model\"!\n\x11\x45xperimentalModel\x12\x0c\n\x04name\x18\x01 \x01(\t')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DETECTIONMODEL._serialized_start=89
  _DETECTIONMODEL._serialized_end=351
  _EXPERIMENTALMODEL._serialized_start=353
  _EXPERIMENTALMODEL._serialized_end=386
# @@protoc_insertion_point(module_scope)
