import asyncio
import random
from time import perf_counter

import aiohttp

# import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_random_id() -> str:
    return str(random.randint(1, 150))


async def get_random_pokemon() -> str:
    url = BASE_URL + get_random_id()

    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            pokemon = await response.json()
            return pokemon["name"]


async def main():

    start_time = perf_counter()
    tasks = [get_random_pokemon() for _ in range(100)]
    result = await asyncio.gather(*tasks)
    print(result)
    end_time = perf_counter()
    print(end_time - start_time)


# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


##############################

# httpx

# def get_random_id() -> str:
#     return str(random.randint(1,150))


# async def get_random_pokemon() -> str:
#     url = BASE_URL + get_random_id()

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response.json()["name"]

# async def main():
#     start_time = perf_counter()
#     tasks = [ get_random_pokemon() for _ in range(10)]
#     results = await asyncio.gather(*tasks)
#     print(results)
#     end_time = perf_counter()
#     print(end_time - start_time)


# asyncio.run(main())

#################################
