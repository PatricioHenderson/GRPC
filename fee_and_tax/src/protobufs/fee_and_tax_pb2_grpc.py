# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fee_and_tax_pb2 as fee__and__tax__pb2


class FeeAndTaxServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalculateFeeAndTax = channel.unary_unary(
                '/FeeAndTaxService/CalculateFeeAndTax',
                request_serializer=fee__and__tax__pb2.FeeAndTaxRequest.SerializeToString,
                response_deserializer=fee__and__tax__pb2.FeeAndTaxResponse.FromString,
                )
        self.CalculateTax = channel.unary_unary(
                '/FeeAndTaxService/CalculateTax',
                request_serializer=fee__and__tax__pb2.TaxRequest.SerializeToString,
                response_deserializer=fee__and__tax__pb2.TaxResponse.FromString,
                )
        self.CalculateFee = channel.unary_unary(
                '/FeeAndTaxService/CalculateFee',
                request_serializer=fee__and__tax__pb2.FeeRequest.SerializeToString,
                response_deserializer=fee__and__tax__pb2.FeeResponse.FromString,
                )


class FeeAndTaxServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CalculateFeeAndTax(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalculateTax(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalculateFee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeeAndTaxServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CalculateFeeAndTax': grpc.unary_unary_rpc_method_handler(
                    servicer.CalculateFeeAndTax,
                    request_deserializer=fee__and__tax__pb2.FeeAndTaxRequest.FromString,
                    response_serializer=fee__and__tax__pb2.FeeAndTaxResponse.SerializeToString,
            ),
            'CalculateTax': grpc.unary_unary_rpc_method_handler(
                    servicer.CalculateTax,
                    request_deserializer=fee__and__tax__pb2.TaxRequest.FromString,
                    response_serializer=fee__and__tax__pb2.TaxResponse.SerializeToString,
            ),
            'CalculateFee': grpc.unary_unary_rpc_method_handler(
                    servicer.CalculateFee,
                    request_deserializer=fee__and__tax__pb2.FeeRequest.FromString,
                    response_serializer=fee__and__tax__pb2.FeeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FeeAndTaxService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FeeAndTaxService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CalculateFeeAndTax(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FeeAndTaxService/CalculateFeeAndTax',
            fee__and__tax__pb2.FeeAndTaxRequest.SerializeToString,
            fee__and__tax__pb2.FeeAndTaxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CalculateTax(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FeeAndTaxService/CalculateTax',
            fee__and__tax__pb2.TaxRequest.SerializeToString,
            fee__and__tax__pb2.TaxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CalculateFee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FeeAndTaxService/CalculateFee',
            fee__and__tax__pb2.FeeRequest.SerializeToString,
            fee__and__tax__pb2.FeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
