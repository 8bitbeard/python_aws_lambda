from app.src.domain.ports.outbound.notification_system_port import NotificationSystemPort
from src.domain.exceptions.publish_notification_failed_exception import PublishNotificationFailedException
from src.domain.models.notification import Notification
from src.infra.adapters.outbound.dtos.sts_adapter_response_dto import STSAdapterResponseDTO
from src.infra.utils.custom_logger import CustomLogger


class SNSAdapter(NotificationSystemPort):

    def __init__(self, logger: CustomLogger):
        self.__logger = logger

    def publish(self, notification: Notification) -> STSAdapterResponseDTO:
        print(notification.to_dict())

        if notification.data.new_value == "01/01/01":
            self.__logger.add_event("SNSAdapter", "Success case SNSAdapter")
            return STSAdapterResponseDTO(
                success=True,
                message_id="123456",
                sequence_id=None
            )

        self.__logger.add_event("SNSAdapter", "Failure case SNSAdapter")
        raise PublishNotificationFailedException("Failed to publish notification")
