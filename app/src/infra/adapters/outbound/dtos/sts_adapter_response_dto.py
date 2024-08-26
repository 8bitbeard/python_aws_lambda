from typing import Optional

from pydantic import BaseModel


class STSAdapterResponseDTO(BaseModel):
    success: bool
    message_id: Optional[str]
    sequence_id: Optional[str]
