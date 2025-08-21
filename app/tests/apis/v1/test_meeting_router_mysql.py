import httpx
from starlette.status import HTTP_200_OK
from tortoise.contrib.test import TestCase

from app import app


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_router(self) -> None:
        # When
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.post(url="/v1/mysql/meetings")

        # Then
        assert response.status_code == HTTP_200_OK
