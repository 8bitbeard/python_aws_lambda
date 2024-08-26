from typing import Optional

from pydantic import BaseModel

from src.infra.adapters.inbound.dtos.error_dto import ErrorDTO
from src.infra.adapters.outbound.dtos.sts_adapter_response_dto import STSAdapterResponseDTO


class NotificationAdapterResponseDTO(BaseModel):
    status_code: int
    error: Optional[ErrorDTO] = None
    publish: Optional[STSAdapterResponseDTO] = None