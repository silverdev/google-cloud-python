# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling_v1beta1/proto/instruction.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.datalabeling_v1beta1.proto import (
    dataset_pb2 as google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datalabeling_v1beta1/proto/instruction.proto",
    package="google.cloud.datalabeling.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling"
    ),
    serialized_pb=_b(
        '\n9google/cloud/datalabeling_v1beta1/proto/instruction.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x35google/cloud/datalabeling_v1beta1/proto/dataset.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x03\n\x0bInstruction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\tdata_type\x18\x06 \x01(\x0e\x32+.google.cloud.datalabeling.v1beta1.DataType\x12J\n\x0f\x63sv_instruction\x18\x07 \x01(\x0b\x32\x31.google.cloud.datalabeling.v1beta1.CsvInstruction\x12J\n\x0fpdf_instruction\x18\t \x01(\x0b\x32\x31.google.cloud.datalabeling.v1beta1.PdfInstruction\x12\x1a\n\x12\x62locking_resources\x18\n \x03(\t"&\n\x0e\x43svInstruction\x12\x14\n\x0cgcs_file_uri\x18\x01 \x01(\t"&\n\x0ePdfInstruction\x12\x14\n\x0cgcs_file_uri\x18\x01 \x01(\tBx\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabelingb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_INSTRUCTION = _descriptor.Descriptor(
    name="Instruction",
    full_name="google.cloud.datalabeling.v1beta1.Instruction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.create_time",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.update_time",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data_type",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.data_type",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="csv_instruction",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.csv_instruction",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pdf_instruction",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.pdf_instruction",
            index=7,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="blocking_resources",
            full_name="google.cloud.datalabeling.v1beta1.Instruction.blocking_resources",
            index=8,
            number=10,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=215,
    serialized_end=627,
)


_CSVINSTRUCTION = _descriptor.Descriptor(
    name="CsvInstruction",
    full_name="google.cloud.datalabeling.v1beta1.CsvInstruction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="gcs_file_uri",
            full_name="google.cloud.datalabeling.v1beta1.CsvInstruction.gcs_file_uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=629,
    serialized_end=667,
)


_PDFINSTRUCTION = _descriptor.Descriptor(
    name="PdfInstruction",
    full_name="google.cloud.datalabeling.v1beta1.PdfInstruction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="gcs_file_uri",
            full_name="google.cloud.datalabeling.v1beta1.PdfInstruction.gcs_file_uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=669,
    serialized_end=707,
)

_INSTRUCTION.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INSTRUCTION.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INSTRUCTION.fields_by_name[
    "data_type"
].enum_type = (
    google_dot_cloud_dot_datalabeling__v1beta1_dot_proto_dot_dataset__pb2._DATATYPE
)
_INSTRUCTION.fields_by_name["csv_instruction"].message_type = _CSVINSTRUCTION
_INSTRUCTION.fields_by_name["pdf_instruction"].message_type = _PDFINSTRUCTION
DESCRIPTOR.message_types_by_name["Instruction"] = _INSTRUCTION
DESCRIPTOR.message_types_by_name["CsvInstruction"] = _CSVINSTRUCTION
DESCRIPTOR.message_types_by_name["PdfInstruction"] = _PDFINSTRUCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Instruction = _reflection.GeneratedProtocolMessageType(
    "Instruction",
    (_message.Message,),
    dict(
        DESCRIPTOR=_INSTRUCTION,
        __module__="google.cloud.datalabeling_v1beta1.proto.instruction_pb2",
        __doc__="""Instruction of how to perform the labeling task for human operators.
  Currently two types of instruction are supported - CSV file and PDF. One
  of the two types instruction must be provided. CSV file is only
  supported for image classification task. Instructions for other task
  should be provided as PDF. For image classification, CSV and PDF can be
  provided at the same time.
  
  
  Attributes:
      name:
          Output only. Instruction resource name, format:
          projects/{project\_id}/instructions/{instruction\_id}
      display_name:
          Required. The display name of the instruction. Maximum of 64
          characters.
      description:
          Optional. User-provided description of the instruction. The
          description can be up to 10000 characters long.
      create_time:
          Output only. Creation time of instruction.
      update_time:
          Output only. Last update time of instruction.
      data_type:
          Required. The data type of this instruction.
      csv_instruction:
          One of CSV or PDF instruction is required. Instruction from a
          CSV file, such as for classification task. The CSV file should
          have exact two columns, in the following format:  -  The first
          column is labeled data, such as an image reference, text. -
          The second column is comma separated labels associated with
          data.
      pdf_instruction:
          One of CSV or PDF instruction is required. Instruction from a
          PDF document. The PDF should be in a Cloud Storage bucket.
      blocking_resources:
          Output only. The names of any related resources that are
          blocking changes to the instruction.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.Instruction)
    ),
)
_sym_db.RegisterMessage(Instruction)

CsvInstruction = _reflection.GeneratedProtocolMessageType(
    "CsvInstruction",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CSVINSTRUCTION,
        __module__="google.cloud.datalabeling_v1beta1.proto.instruction_pb2",
        __doc__="""Instruction from a CSV file.
  
  
  Attributes:
      gcs_file_uri:
          CSV file for the instruction. Only gcs path is allowed.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.CsvInstruction)
    ),
)
_sym_db.RegisterMessage(CsvInstruction)

PdfInstruction = _reflection.GeneratedProtocolMessageType(
    "PdfInstruction",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PDFINSTRUCTION,
        __module__="google.cloud.datalabeling_v1beta1.proto.instruction_pb2",
        __doc__="""Instruction from a PDF file.
  
  
  Attributes:
      gcs_file_uri:
          PDF file for the instruction. Only gcs path is allowed.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.PdfInstruction)
    ),
)
_sym_db.RegisterMessage(PdfInstruction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)