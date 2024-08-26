from src.domain.models.source_type import SourceType


def convert_app_id(app_id: str) -> SourceType:
    app_id_to_source_map = {
        "7a9a1203-5f52-4cc1-90cf-981ed6fbb301": SourceType.SOURCE_A
    }

    return app_id_to_source_map.get(app_id, SourceType.UNKNOWN)