from pydantic import ValidationError

from src.infra.adapters.inbound.dtos.error_dto import ErrorDTO
from src.infra.adapters.inbound.dtos.notification_adapter_response_dto import NotificationAdapterResponseDTO
from src.infra.utils.custom_logger import CustomLogger



class ExceptionHandler:

    def __init__(self, function, logger: CustomLogger):
        self.function = function
        self.__logger = logger

    def __call__(self, *args, **kwargs):
        try:
            self.function(*args, **kwargs)
        except ValidationError as ex:
            self.__logger.add_event("exception_handler", "validation error")
            return NotificationAdapterResponseDTO(
                status_code=400,
                error=ErrorDTO(
                    code="FAIL",
                    message=ex
                )
            ).model_dump()
        except Exception:
            self.__logger.add_event("exception_handler", "broad exception")
            return NotificationAdapterResponseDTO(
                status_code=500,
                error=ErrorDTO(
                    code="FAIL",
                    message="Internal Server Error"
                )
            ).model_dump()
