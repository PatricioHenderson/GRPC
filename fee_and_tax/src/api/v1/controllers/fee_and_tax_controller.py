from kernel.config import log
from typing import Tuple, Union
from marshmallow import ValidationError
from fairplay.templates.service_grpc import ServiceGrpcAbstract

class NameClassController(ServiceGrpcAbstract):

    @classmethod
    def _validate_input_data(cls, input_data: Union[object, dict]) -> Tuple[bool, dict]:
        pass

    @classmethod
    def _generate_data_response(cls, input_data_validated: dict) -> Tuple[bool, Union[object, dict] ]:
        pass
    