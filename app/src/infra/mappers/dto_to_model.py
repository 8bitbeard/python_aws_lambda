from src.domain.models.notification import Notification, NotificationData, DueDate
from src.infra.adapters.inbound.dtos.kafka_topic_schema_dto import KafkaTopicSchemaDTO
from src.infra.utils.convert_app_id import convert_app_id


def kafka_topic_schema_dto_to_notification(kafka_topic_schema_dto: KafkaTopicSchemaDTO) -> Notification:
    (_, extracted_requester, extracted_app_id) = kafka_topic_schema_dto.nome_canal_requisicao.split("|")

    return Notification(
        data=NotificationData(
            old_value=DueDate(kafka_topic_schema_dto.data_vencimento_anterior),
            new_value=DueDate(kafka_topic_schema_dto.data_vencimento_atual),
            source=convert_app_id(extracted_app_id),
        )
    )
