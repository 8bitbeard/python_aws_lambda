from dataclasses import dataclass
from typing import List, Dict

from pydantic import BaseModel

@dataclass
class InputPayloadDTO(BaseModel):
    topic: str
    partition: int
    offset: int
    key: str
    value: str
    headers: List[Dict[str, str]]
    timestamp: int


@dataclass
class InputEventDTO(BaseModel):
    payload: InputPayloadDTO
