from abc import ABC, abstractmethod

from src.domain.models.notification import Notification


class NotificationSystemPort(ABC):

    @abstractmethod
    def publish(self, notification: Notification):
        raise NotImplementedError("Method not implemented")
