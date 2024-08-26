import json

from src.infra.adapters.inbound.dtos.input_event_dto import InputEventDTO
from src.infra.adapters.inbound.dtos.kafka_topic_schema_dto import KafkaTopicSchemaDTO


def input_event_dto_to_kafka_topic_schema_dto(input_event_dto: InputEventDTO) -> KafkaTopicSchemaDTO:
    value = json.loads(input_event_dto.payload.value)
    return KafkaTopicSchemaDTO(**value)