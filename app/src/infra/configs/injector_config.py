from injector import Module, singleton, Binder, provider

from src.domain.ports.inbound.notification_port import NotificationPort
from src.domain.ports.outbound.notification_system_port import NotificationSystemPort
from src.domain.services.send_notification_service import SendNotificationService
from src.infra.adapters.inbound.handler.exception_handler import ExceptionHandler
from src.infra.adapters.inbound.impl.notification_adapter import NotificationAdapter
from src.infra.adapters.outbound.impl.sns_adapter import SNSAdapter
from src.infra.utils.custom_logger import CustomLogger


class LambdaModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(CustomLogger, to=CustomLogger, scope=singleton)
        # binder.bind(NotificationPort, to=NotificationAdapter)
        # binder.bind(SendNotificationService, to=SendNotificationService)
        # binder.bind(NotificationSystemPort, to=SNSAdapter)

    # @provider
    # @singleton
    # def provide_custom_logger(self) -> CustomLogger:
    #     return CustomLogger()

    @provider
    def provide_exception_handler(
            self,
            logger: CustomLogger
    ) -> ExceptionHandler:
        return

    @provider
    def provide_notification_adapter(
            self,
            logger: CustomLogger,
            send_notification_service: SendNotificationService
    ) -> NotificationAdapter:
        return NotificationAdapter(logger, send_notification_service)

    @provider
    def provide_send_notification_service(
            self,
            notification_system_adapter: SNSAdapter
    ) -> SendNotificationService:
        return SendNotificationService(notification_system_adapter)

    @provider
    def provide_notification_system_adapter(self, logger: CustomLogger) -> SNSAdapter:
        return SNSAdapter(logger)
