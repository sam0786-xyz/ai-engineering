# Day 4 21st May 2026 - Async APIs

import asyncio
import httpx
import time

# async def make_toast():
#     print ("Starting Toast")
#     await asyncio.sleep(2)
#     print("Toast is done")

# async def fry_eggs():
#     print("Starting eggs")
#     await asyncio.sleep(3)
#     print("Eggs are done")

# async def main():
#     await asyncio.gather(make_toast(), fry_eggs())

# asyncio.run(main())

async def fetch_status(url):
    # httpx.AsyncClient() opens a network connection
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"{url} returned status: {response.status_code}")

async def main():
    start = time.time()
    await asyncio.gather(
        fetch_status("https://google.com"),
        fetch_status("https://github.com"),
        fetch_status("https://sam18.xyz")
    )
    end = time.time()
    print(f"Total time: {end-start}")

asyncio.run(main())