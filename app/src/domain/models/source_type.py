from enum import Enum


class SourceType(Enum):
    SOURCE_A = "SOURCE_A"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def is_valid(cls, value):
        return value is not cls.UNKNOWN
