# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fee_and_tax.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66\x65\x65_and_tax.proto\"g\n\x08TaxInput\x12*\n\ttax_rates\x18\x01 \x03(\x0b\x32\x17.TaxInput.TaxRatesEntry\x1a/\n\rTaxRatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"g\n\x08\x46\x65\x65Input\x12*\n\tfee_rates\x18\x01 \x03(\x0b\x32\x17.FeeInput.FeeRatesEntry\x1a/\n\rFeeRatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xf0\x01\n\x10\x46\x65\x65\x41ndTaxRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x05\x12\'\n\x03\x66\x65\x65\x18\x02 \x03(\x0b\x32\x1a.FeeAndTaxRequest.FeeEntry\x12\'\n\x03tax\x18\x03 \x03(\x0b\x32\x1a.FeeAndTaxRequest.TaxEntry\x12\x0c\n\x04save\x18\x04 \x01(\x08\x1a\x35\n\x08\x46\x65\x65\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.FeeInput:\x02\x38\x01\x1a\x35\n\x08TaxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.TaxInput:\x02\x38\x01\"\xde\x01\n\nTaxRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x05\x12!\n\x03\x66\x65\x65\x18\x02 \x03(\x0b\x32\x14.TaxRequest.FeeEntry\x12!\n\x03tax\x18\x03 \x03(\x0b\x32\x14.TaxRequest.TaxEntry\x12\x0c\n\x04save\x18\x04 \x01(\x08\x1a\x35\n\x08\x46\x65\x65\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.FeeInput:\x02\x38\x01\x1a\x35\n\x08TaxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.TaxInput:\x02\x38\x01\"\xde\x01\n\nFeeRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x05\x12!\n\x03\x66\x65\x65\x18\x02 \x03(\x0b\x32\x14.FeeRequest.FeeEntry\x12!\n\x03tax\x18\x03 \x03(\x0b\x32\x14.FeeRequest.TaxEntry\x12\x0c\n\x04save\x18\x04 \x01(\x08\x1a\x35\n\x08\x46\x65\x65\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.FeeInput:\x02\x38\x01\x1a\x35\n\x08TaxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.TaxInput:\x02\x38\x01\"\xbf\x01\n\x11\x46\x65\x65\x41ndTaxResponse\x12(\n\x03\x66\x65\x65\x18\x01 \x03(\x0b\x32\x1b.FeeAndTaxResponse.FeeEntry\x12(\n\x03tax\x18\x02 \x03(\x0b\x32\x1b.FeeAndTaxResponse.TaxEntry\x1a*\n\x08\x46\x65\x65\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a*\n\x08TaxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n\x0bTaxResponse\x12\"\n\x03tax\x18\x01 \x03(\x0b\x32\x15.TaxResponse.TaxEntry\x1a*\n\x08TaxEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n\x0b\x46\x65\x65Response\x12\"\n\x03\x66\x65\x65\x18\x01 \x03(\x0b\x32\x15.FeeResponse.FeeEntry\x1a*\n\x08\x46\x65\x65\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xa5\x01\n\x10\x46\x65\x65\x41ndTaxService\x12;\n\x12\x43\x61lculateFeeAndTax\x12\x11.FeeAndTaxRequest\x1a\x12.FeeAndTaxResponse\x12)\n\x0c\x43\x61lculateTax\x12\x0b.TaxRequest\x1a\x0c.TaxResponse\x12)\n\x0c\x43\x61lculateFee\x12\x0b.FeeRequest\x1a\x0c.FeeResponseb\x06proto3')



_TAXINPUT = DESCRIPTOR.message_types_by_name['TaxInput']
_TAXINPUT_TAXRATESENTRY = _TAXINPUT.nested_types_by_name['TaxRatesEntry']
_FEEINPUT = DESCRIPTOR.message_types_by_name['FeeInput']
_FEEINPUT_FEERATESENTRY = _FEEINPUT.nested_types_by_name['FeeRatesEntry']
_FEEANDTAXREQUEST = DESCRIPTOR.message_types_by_name['FeeAndTaxRequest']
_FEEANDTAXREQUEST_FEEENTRY = _FEEANDTAXREQUEST.nested_types_by_name['FeeEntry']
_FEEANDTAXREQUEST_TAXENTRY = _FEEANDTAXREQUEST.nested_types_by_name['TaxEntry']
_TAXREQUEST = DESCRIPTOR.message_types_by_name['TaxRequest']
_TAXREQUEST_FEEENTRY = _TAXREQUEST.nested_types_by_name['FeeEntry']
_TAXREQUEST_TAXENTRY = _TAXREQUEST.nested_types_by_name['TaxEntry']
_FEEREQUEST = DESCRIPTOR.message_types_by_name['FeeRequest']
_FEEREQUEST_FEEENTRY = _FEEREQUEST.nested_types_by_name['FeeEntry']
_FEEREQUEST_TAXENTRY = _FEEREQUEST.nested_types_by_name['TaxEntry']
_FEEANDTAXRESPONSE = DESCRIPTOR.message_types_by_name['FeeAndTaxResponse']
_FEEANDTAXRESPONSE_FEEENTRY = _FEEANDTAXRESPONSE.nested_types_by_name['FeeEntry']
_FEEANDTAXRESPONSE_TAXENTRY = _FEEANDTAXRESPONSE.nested_types_by_name['TaxEntry']
_TAXRESPONSE = DESCRIPTOR.message_types_by_name['TaxResponse']
_TAXRESPONSE_TAXENTRY = _TAXRESPONSE.nested_types_by_name['TaxEntry']
_FEERESPONSE = DESCRIPTOR.message_types_by_name['FeeResponse']
_FEERESPONSE_FEEENTRY = _FEERESPONSE.nested_types_by_name['FeeEntry']
TaxInput = _reflection.GeneratedProtocolMessageType('TaxInput', (_message.Message,), {

  'TaxRatesEntry' : _reflection.GeneratedProtocolMessageType('TaxRatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAXINPUT_TAXRATESENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:TaxInput.TaxRatesEntry)
    })
  ,
  'DESCRIPTOR' : _TAXINPUT,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:TaxInput)
  })
_sym_db.RegisterMessage(TaxInput)
_sym_db.RegisterMessage(TaxInput.TaxRatesEntry)

FeeInput = _reflection.GeneratedProtocolMessageType('FeeInput', (_message.Message,), {

  'FeeRatesEntry' : _reflection.GeneratedProtocolMessageType('FeeRatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEINPUT_FEERATESENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeInput.FeeRatesEntry)
    })
  ,
  'DESCRIPTOR' : _FEEINPUT,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:FeeInput)
  })
_sym_db.RegisterMessage(FeeInput)
_sym_db.RegisterMessage(FeeInput.FeeRatesEntry)

FeeAndTaxRequest = _reflection.GeneratedProtocolMessageType('FeeAndTaxRequest', (_message.Message,), {

  'FeeEntry' : _reflection.GeneratedProtocolMessageType('FeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEANDTAXREQUEST_FEEENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeAndTaxRequest.FeeEntry)
    })
  ,

  'TaxEntry' : _reflection.GeneratedProtocolMessageType('TaxEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEANDTAXREQUEST_TAXENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeAndTaxRequest.TaxEntry)
    })
  ,
  'DESCRIPTOR' : _FEEANDTAXREQUEST,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:FeeAndTaxRequest)
  })
_sym_db.RegisterMessage(FeeAndTaxRequest)
_sym_db.RegisterMessage(FeeAndTaxRequest.FeeEntry)
_sym_db.RegisterMessage(FeeAndTaxRequest.TaxEntry)

TaxRequest = _reflection.GeneratedProtocolMessageType('TaxRequest', (_message.Message,), {

  'FeeEntry' : _reflection.GeneratedProtocolMessageType('FeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAXREQUEST_FEEENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:TaxRequest.FeeEntry)
    })
  ,

  'TaxEntry' : _reflection.GeneratedProtocolMessageType('TaxEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAXREQUEST_TAXENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:TaxRequest.TaxEntry)
    })
  ,
  'DESCRIPTOR' : _TAXREQUEST,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:TaxRequest)
  })
_sym_db.RegisterMessage(TaxRequest)
_sym_db.RegisterMessage(TaxRequest.FeeEntry)
_sym_db.RegisterMessage(TaxRequest.TaxEntry)

FeeRequest = _reflection.GeneratedProtocolMessageType('FeeRequest', (_message.Message,), {

  'FeeEntry' : _reflection.GeneratedProtocolMessageType('FeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEREQUEST_FEEENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeRequest.FeeEntry)
    })
  ,

  'TaxEntry' : _reflection.GeneratedProtocolMessageType('TaxEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEREQUEST_TAXENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeRequest.TaxEntry)
    })
  ,
  'DESCRIPTOR' : _FEEREQUEST,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:FeeRequest)
  })
_sym_db.RegisterMessage(FeeRequest)
_sym_db.RegisterMessage(FeeRequest.FeeEntry)
_sym_db.RegisterMessage(FeeRequest.TaxEntry)

FeeAndTaxResponse = _reflection.GeneratedProtocolMessageType('FeeAndTaxResponse', (_message.Message,), {

  'FeeEntry' : _reflection.GeneratedProtocolMessageType('FeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEANDTAXRESPONSE_FEEENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeAndTaxResponse.FeeEntry)
    })
  ,

  'TaxEntry' : _reflection.GeneratedProtocolMessageType('TaxEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEEANDTAXRESPONSE_TAXENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeAndTaxResponse.TaxEntry)
    })
  ,
  'DESCRIPTOR' : _FEEANDTAXRESPONSE,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:FeeAndTaxResponse)
  })
_sym_db.RegisterMessage(FeeAndTaxResponse)
_sym_db.RegisterMessage(FeeAndTaxResponse.FeeEntry)
_sym_db.RegisterMessage(FeeAndTaxResponse.TaxEntry)

TaxResponse = _reflection.GeneratedProtocolMessageType('TaxResponse', (_message.Message,), {

  'TaxEntry' : _reflection.GeneratedProtocolMessageType('TaxEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAXRESPONSE_TAXENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:TaxResponse.TaxEntry)
    })
  ,
  'DESCRIPTOR' : _TAXRESPONSE,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:TaxResponse)
  })
_sym_db.RegisterMessage(TaxResponse)
_sym_db.RegisterMessage(TaxResponse.TaxEntry)

FeeResponse = _reflection.GeneratedProtocolMessageType('FeeResponse', (_message.Message,), {

  'FeeEntry' : _reflection.GeneratedProtocolMessageType('FeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEERESPONSE_FEEENTRY,
    '__module__' : 'fee_and_tax_pb2'
    # @@protoc_insertion_point(class_scope:FeeResponse.FeeEntry)
    })
  ,
  'DESCRIPTOR' : _FEERESPONSE,
  '__module__' : 'fee_and_tax_pb2'
  # @@protoc_insertion_point(class_scope:FeeResponse)
  })
_sym_db.RegisterMessage(FeeResponse)
_sym_db.RegisterMessage(FeeResponse.FeeEntry)

_FEEANDTAXSERVICE = DESCRIPTOR.services_by_name['FeeAndTaxService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TAXINPUT_TAXRATESENTRY._options = None
  _TAXINPUT_TAXRATESENTRY._serialized_options = b'8\001'
  _FEEINPUT_FEERATESENTRY._options = None
  _FEEINPUT_FEERATESENTRY._serialized_options = b'8\001'
  _FEEANDTAXREQUEST_FEEENTRY._options = None
  _FEEANDTAXREQUEST_FEEENTRY._serialized_options = b'8\001'
  _FEEANDTAXREQUEST_TAXENTRY._options = None
  _FEEANDTAXREQUEST_TAXENTRY._serialized_options = b'8\001'
  _TAXREQUEST_FEEENTRY._options = None
  _TAXREQUEST_FEEENTRY._serialized_options = b'8\001'
  _TAXREQUEST_TAXENTRY._options = None
  _TAXREQUEST_TAXENTRY._serialized_options = b'8\001'
  _FEEREQUEST_FEEENTRY._options = None
  _FEEREQUEST_FEEENTRY._serialized_options = b'8\001'
  _FEEREQUEST_TAXENTRY._options = None
  _FEEREQUEST_TAXENTRY._serialized_options = b'8\001'
  _FEEANDTAXRESPONSE_FEEENTRY._options = None
  _FEEANDTAXRESPONSE_FEEENTRY._serialized_options = b'8\001'
  _FEEANDTAXRESPONSE_TAXENTRY._options = None
  _FEEANDTAXRESPONSE_TAXENTRY._serialized_options = b'8\001'
  _TAXRESPONSE_TAXENTRY._options = None
  _TAXRESPONSE_TAXENTRY._serialized_options = b'8\001'
  _FEERESPONSE_FEEENTRY._options = None
  _FEERESPONSE_FEEENTRY._serialized_options = b'8\001'
  _TAXINPUT._serialized_start=21
  _TAXINPUT._serialized_end=124
  _TAXINPUT_TAXRATESENTRY._serialized_start=77
  _TAXINPUT_TAXRATESENTRY._serialized_end=124
  _FEEINPUT._serialized_start=126
  _FEEINPUT._serialized_end=229
  _FEEINPUT_FEERATESENTRY._serialized_start=182
  _FEEINPUT_FEERATESENTRY._serialized_end=229
  _FEEANDTAXREQUEST._serialized_start=232
  _FEEANDTAXREQUEST._serialized_end=472
  _FEEANDTAXREQUEST_FEEENTRY._serialized_start=364
  _FEEANDTAXREQUEST_FEEENTRY._serialized_end=417
  _FEEANDTAXREQUEST_TAXENTRY._serialized_start=419
  _FEEANDTAXREQUEST_TAXENTRY._serialized_end=472
  _TAXREQUEST._serialized_start=475
  _TAXREQUEST._serialized_end=697
  _TAXREQUEST_FEEENTRY._serialized_start=364
  _TAXREQUEST_FEEENTRY._serialized_end=417
  _TAXREQUEST_TAXENTRY._serialized_start=419
  _TAXREQUEST_TAXENTRY._serialized_end=472
  _FEEREQUEST._serialized_start=700
  _FEEREQUEST._serialized_end=922
  _FEEREQUEST_FEEENTRY._serialized_start=364
  _FEEREQUEST_FEEENTRY._serialized_end=417
  _FEEREQUEST_TAXENTRY._serialized_start=419
  _FEEREQUEST_TAXENTRY._serialized_end=472
  _FEEANDTAXRESPONSE._serialized_start=925
  _FEEANDTAXRESPONSE._serialized_end=1116
  _FEEANDTAXRESPONSE_FEEENTRY._serialized_start=1030
  _FEEANDTAXRESPONSE_FEEENTRY._serialized_end=1072
  _FEEANDTAXRESPONSE_TAXENTRY._serialized_start=1074
  _FEEANDTAXRESPONSE_TAXENTRY._serialized_end=1116
  _TAXRESPONSE._serialized_start=1118
  _TAXRESPONSE._serialized_end=1211
  _TAXRESPONSE_TAXENTRY._serialized_start=1074
  _TAXRESPONSE_TAXENTRY._serialized_end=1116
  _FEERESPONSE._serialized_start=1213
  _FEERESPONSE._serialized_end=1306
  _FEERESPONSE_FEEENTRY._serialized_start=1030
  _FEERESPONSE_FEEENTRY._serialized_end=1072
  _FEEANDTAXSERVICE._serialized_start=1309
  _FEEANDTAXSERVICE._serialized_end=1474
# @@protoc_insertion_point(module_scope)
