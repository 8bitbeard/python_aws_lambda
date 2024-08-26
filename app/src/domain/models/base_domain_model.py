from abc import abstractmethod, ABC
from typing import Any


class BaseDomainModel:

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError("Method not implemented")