
from kernel import settings

import grpc
from protobufs.fee_and_tax_pb2_grpc import FeeAndTaxServiceStub
from protobufs.fee_and_tax_pb2 import FeeAndTaxResponse, FeeAndTaxRequest, FeeInput, TaxInput
channel = grpc.insecure_channel("localhost:50051")
client = FeeAndTaxServiceStub(channel)

request = FeeAndTaxRequest(amount=100, fee={"fee": FeeInput(fee_rates={"fee1": 0.1, "fee2": 0.2})}, tax={"tax": TaxInput(tax_rates={"tax1":0.9})}, save=True)
print(f'Fee and tax : {client.CalculateFeeAndTax(request)}')
print(f" Tax: {client.CalculateTax(request)}")
print(f" Fee: {client.CalculateFee(request)}")