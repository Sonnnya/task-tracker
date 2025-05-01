from aiohttp import ClientSession

class HTTPClient():
    def __init__(self, base_url: str):
        self._session = ClientSession(base_url=base_url)

class HuggingFaceClient(HTTPClient):
    def __init__(self, base_url: str, api_key: str) -> None:
        self._session = ClientSession(headers={
            "Authorization": f"Bearer {self._api_key}",
        })
        self.api_key = api_key
    
    async def get_completion(self, user_message: str) -> str:
        query = {"inputs": user_message}
        async with self._session.post('/v1/completion', json=query) as resp:
            result = await resp.json()
            return result