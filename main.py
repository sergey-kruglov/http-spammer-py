import asyncio
import random

URL = 'http://localhost:3008/api'
REQUESTS_COUNT = 100
HEADERS = {}
BODY = {}

request_index = 0
success_count = 0


async def main():
    tasks = []
    for i in range(REQUESTS_COUNT):
        task = asyncio.create_task(make_request(i))
        tasks.append(task)
    await asyncio.gather(*tasks)


async def make_request(i):
    await asyncio.sleep(random.randint(0, 2))
    global success_count, request_index
    request_index += 1
    success_count += 1
    print(success_count, i, URL)


asyncio.run(main())
