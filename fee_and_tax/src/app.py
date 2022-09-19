from kernel import settings
from abc import ABC, abstractmethod
from typing_extensions import Self


from concurrent import futures
import grpc

from protobufs import fee_and_tax_pb2_grpc
from protobufs.fee_and_tax_pb2 import FeeAndTaxResponse, TaxResponse, FeeResponse


class Calculator(ABC):

    def calculate_fee_or_tax(self,input_data:dict):
        amount = self.get_amount(input_data)
        values_to_calculate = self.get_values_to_calculate(input_data)
        response = {}
        for key,value in values_to_calculate.items():
            response[key] = str(value*amount)
        self.save_to_db(input_data)
        return(response)
    

    @abstractmethod
    def get_amount(self, input_data:dict):
        pass
    
    @abstractmethod
    def get_values_to_calculate(self, input_data:dict):
        pass
    
    @abstractmethod
    def save_to_db(self, input_data):
        pass

class FeeCalculator(Calculator):
        
        def get_amount(self, input_data: dict) -> float:
            return input_data.amount
        
        def get_values_to_calculate(self, input_data: dict) -> dict:
            return input_data.fee["fee"].fee_rates
            
        
        def save_to_db(self, input_data: dict):
            if input_data.save:
                print("Saving to DB")
            else:
                print("Not saving to DB")


class TaxCalculator(Calculator):

    def get_amount(self, input_data: dict) -> float:
        return input_data.amount
    
    def get_values_to_calculate(self, input_data: dict) -> list:
        taxes = input_data.tax['tax'].tax_rates
        return taxes
    
    def save_to_db(self, input_data: dict):
            if input_data.save:
                print("Saving to DB")
            else:
                print("Not saving to DB")

class FeeAndTaxCalculatorService(fee_and_tax_pb2_grpc.FeeAndTaxServiceServicer):

    def CalculateTax(self,request,context):
        tax_calculator = TaxCalculator()
        tax_response = tax_calculator.calculate_fee_or_tax(request)
        return TaxResponse(tax=tax_response)

    def CalculateFee(self,request,context):
        fee_calculator = FeeCalculator()
        fee_response = fee_calculator.calculate_fee_or_tax(request)
        return FeeResponse(fee=fee_response)

    def CalculateFeeAndTax(self, request, context):
        tax_calculator = TaxCalculator()
        tax_response = tax_calculator.calculate_fee_or_tax(request)
        fee_calculator = FeeCalculator()
        fee_response = fee_calculator.calculate_fee_or_tax(request)
        return FeeAndTaxResponse(tax=tax_response, fee=fee_response)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fee_and_tax_pb2_grpc.add_FeeAndTaxServiceServicer_to_server(
        FeeAndTaxCalculatorService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
