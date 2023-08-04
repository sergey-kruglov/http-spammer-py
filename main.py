import asyncio
from aiohttp import ClientSession

URL = 'https://sergey-kruglov.com'
METHOD = 'GET'
REQUESTS_COUNT = 50
HEADERS = {}
BODY = {}

success_count = 0


async def main():
    """Entry point"""
    async with ClientSession() as session:
        tasks = []
        for number in range(1, REQUESTS_COUNT + 1):
            tasks.append(make_request(session, number))
        await asyncio.gather(*tasks)
        print(f"{success_count}/{REQUESTS_COUNT}")


async def make_request(session: ClientSession, index: int):
    """Make async request"""
    async with session.request(method=METHOD, url=URL, headers=HEADERS, json=BODY) as resp:
        print(index, resp.status)
    global success_count
    success_count += 1


asyncio.run(main())
