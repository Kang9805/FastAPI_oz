import datetime
import uuid

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class ParticipantDateMysql(BaseModel):
    model_config = FROZEN_CONFIG
    id: int
    date: datetime.date


# ParticipantMysql 클래스는 사용되지 않으므로 삭제하거나 이름을 변경합니다.
# class ParticipantMysql:
#     pass


class CreateParticipantMysqlResponse(BaseModel):
    model_config = FROZEN_CONFIG
    participant_id: int
    # list[ParticipantMysql] -> list[ParticipantDateMysql]
    participant_dates: list[ParticipantDateMysql]


class ParticipantDateEdgedb(BaseModel):
    model_config = FROZEN_CONFIG
    id: uuid.UUID
    date: datetime.date


# ParticipantEdgedb 클래스는 사용되지 않으므로 삭제하거나 이름을 변경합니다.
# class ParticipantEdgedb:
#     pass


class CreateParticipantEdgedbResponse(BaseModel):
    model_config = FROZEN_CONFIG
    participant_id: uuid.UUID
    # list[ParticipantEdgedb] -> list[ParticipantDateEdgedb]
    participant_dates: list[ParticipantDateEdgedb]
