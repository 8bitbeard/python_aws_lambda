from pydantic import BaseModel


class KafkaTopicSchemaDTO(BaseModel):
    nome_canal_requisicao: str
    data_vencimento_anterior: str
    data_vencimento_atual: str
    data_troca_vencimento: str
