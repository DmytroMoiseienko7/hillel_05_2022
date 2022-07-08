import asyncio


async def get_primes_amount(num: int) -> int:
    result = 0
    for i in range(1, num + 1):
        await asyncio.sleep(0.00000000000001)
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        if not counter > 2:
            result += 1
    return print(result)


def main():

    numbers = [40_000, 350, 70_000, 2_000]

    tasks = [get_primes_amount(num_from_list) for num_from_list in numbers]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*tasks))
    event_loop.close()


if __name__ == "__main__":
    main()
