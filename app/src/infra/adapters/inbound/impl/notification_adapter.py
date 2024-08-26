from pydantic import ValidationError

from src.domain.exceptions.publish_notification_failed_exception import PublishNotificationFailedException
from src.domain.exceptions.unknown_source_type_exception import UnknownSourceTypeException
from src.domain.ports.inbound.notification_port import NotificationPort
from src.domain.services.send_notification_service import SendNotificationService
from src.infra.adapters.inbound.dtos.error_dto import ErrorDTO
from src.infra.adapters.inbound.dtos.input_event_dto import InputEventDTO
from src.infra.adapters.inbound.dtos.notification_adapter_response_dto import NotificationAdapterResponseDTO
from src.infra.mappers.dto_to_dto import input_event_dto_to_kafka_topic_schema_dto
from src.infra.mappers.dto_to_model import kafka_topic_schema_dto_to_notification
from src.infra.utils.custom_logger import CustomLogger


class NotificationAdapter(NotificationPort):

    def __init__(self, logger: CustomLogger, send_notification_service: SendNotificationService):
        self.__logger = logger
        self.__send_notification_service = send_notification_service

    def send(self, event: dict) -> NotificationAdapterResponseDTO:
        try:
            self.__logger.add_event("NotificationAdapter", "Chamando service")

            input_event_dto = InputEventDTO.model_validate(event)
            kafka_topic_schema_dto = input_event_dto_to_kafka_topic_schema_dto(input_event_dto)
            notification = kafka_topic_schema_dto_to_notification(kafka_topic_schema_dto)

            response = self.__send_notification_service.send(notification)

            return NotificationAdapterResponseDTO(
                status_code=200,
                error=None,
                publish=response
            )
        except ValidationError as ex:
            self.__logger.add_event("NotificationAdapter", f"Capturou exception ValidationError: {ex}")
            return NotificationAdapterResponseDTO(
                status_code=400,
                error=ErrorDTO(
                    code="400",
                    message="teste"
                )
            )
        except UnknownSourceTypeException as ex:
            self.__logger.add_event("NotificationAdapter", f"Capturou exception UnknownSourceTypeException: {ex}")
            return NotificationAdapterResponseDTO(
                status_code=500,
                error=ErrorDTO(
                    code="500",
                    message=ex.message
                )
            )
        except PublishNotificationFailedException as ex:
            self.__logger.add_event("NotificationAdapter", f"Capturou exception PublishNotificationFailedException: {ex}")
            return NotificationAdapterResponseDTO(
                status_code=500,
                error=ErrorDTO(
                    code="500",
                    message=ex.message
                )
            )
        finally:
            self.__logger.dumps()
