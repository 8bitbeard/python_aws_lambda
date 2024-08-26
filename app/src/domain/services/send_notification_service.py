from src.domain.exceptions.unknown_source_type_exception import UnknownSourceTypeException
from src.domain.models.notification import Notification
from src.domain.models.source_type import SourceType
from src.domain.ports.outbound.notification_system_port import NotificationSystemPort


class SendNotificationService:

    def __init__(self, notification_system_adapter: NotificationSystemPort):
        self.__notification_system_adapter = notification_system_adapter

    def send(self, notification: Notification):
        if notification.data.source is SourceType.UNKNOWN:
            raise UnknownSourceTypeException("Notification with unknown source type detected")
        return self.__notification_system_adapter.publish(notification)
