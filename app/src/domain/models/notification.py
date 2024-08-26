from dataclasses import dataclass

from src.domain.models.base_domain_model import BaseDomainModel
from src.domain.models.source_type import SourceType


@dataclass
class DueDate(BaseDomainModel):
    due_date: str

    def to_dict(self) -> dict:
        return {
            "due_date": self.due_date
        }


@dataclass
class NotificationData(BaseDomainModel):
    old_value: DueDate
    new_value: DueDate
    source: SourceType

    def to_dict(self) -> dict:
        return {
            "old_value": self.old_value.to_dict(),
            "new_value": self.new_value.to_dict(),
            "source": self.source.value
        }


@dataclass
class Notification(BaseDomainModel):
    data: NotificationData
    source: str = "fake_source_notification"
    event_type: str = "fake_event_type_notification"

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "event_type": self.event_type,
            "data": self.data.to_dict()
        }
