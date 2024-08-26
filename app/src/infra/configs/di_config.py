# from dependency_injector import containers, providers
#
# from src.domain.services.send_notification_service import SendNotificationService
# from src.infra.adapters.inbound.impl.notification_adapter import NotificationAdapter
# from src.infra.adapters.outbound.impl.sns_adapter import SNSAdapter
# from src.infra.utils.custom_logger import CustomLogger
#
#
# class Container(containers.DeclarativeContainer):
#
#     config = providers.Configuration()
#
#     custom_logger = providers.Singleton(
#         CustomLogger
#     )
#
#     notification_system_adapter = providers.Factory(
#         SNSAdapter,
#         logger=custom_logger
#     )
#
#     send_notification_service = providers.Factory(
#         SendNotificationService,
#         notification_system_adapter=notification_system_adapter
#     )
#
#     notification_adapter = providers.Factory(
#         NotificationAdapter,
#         logger=custom_logger,
#         send_notification_service=send_notification_service
#     )
