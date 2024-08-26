from dataclasses import dataclass


@dataclass
class ErrorDTO:
    code: str
    message: str