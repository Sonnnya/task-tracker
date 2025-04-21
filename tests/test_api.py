
import pytest
from httpx import AsyncClient, ASGITransport
from schemas import STaskId
from main import app


@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        response = await ac.get('/users/')
        print(response)
        assert response.status_code == 200
        data = response.json()
        assert data == []


@pytest.mark.asyncio
async def test_post_tasks():
    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        response = await ac.post(
            '/task/',
            json={
                'name': 'to have fun',
                'description': ':)'
            }
        )
        print(response.json())
        assert response.status_code == 200
        data = response.json()
        assert STaskId.model_validate(data)
