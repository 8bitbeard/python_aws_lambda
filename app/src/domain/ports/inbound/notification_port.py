from abc import abstractmethod, ABC
from typing import Any


class NotificationPort(ABC):

    @abstractmethod
    def send(self, event: dict) -> Any:
        raise NotImplementedError("Method not implemented")