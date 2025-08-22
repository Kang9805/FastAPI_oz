from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.service.meeting_service_mysql import service_create_meeting_mysql

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB를 쓰는지 URL을 적을 필요 없습니다!
# 강의에서만 이렇게 합니다!
# 실전에는 db 이름을 url에 넣지 마세요!


@edgedb_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    # 먼저 함수를 await 하여 반환값을 'meeting' 변수에 할당
    meeting = await service_create_meeting_mysql()
    # 그 다음에 'meeting' 객체의 'url_code' 속성에 접근
    return CreateMeetingResponse(url_code=meeting.url_code)


@edgedb_router.get(
    "/{meeting_url_code",
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:
    return GetMeetingResponse(url_code="abc")


@mysql_router.get(
    "/{meeting_url_code",
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    return GetMeetingResponse(url_code="abc")
