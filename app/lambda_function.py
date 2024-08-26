from injector import Injector

from src.infra.adapters.inbound.impl.notification_adapter import NotificationAdapter
from src.infra.configs.injector_config import LambdaModule
from src.infra.utils.custom_logger import CustomLogger

injector = Injector([LambdaModule()])
logger = injector.get(CustomLogger)
adapter = injector.get(NotificationAdapter)


def lambda_handler(event: dict, context):
    return adapter.send(event).model_dump()
