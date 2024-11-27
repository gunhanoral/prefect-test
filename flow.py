import asyncio

from prefect import flow


@flow
async def subflow_1():
    print("Subflow 1 started!")
    await asyncio.sleep(1)


@flow
async def main_flow():
    await asyncio.gather(*[subflow_1() for _ in range(5)])


def main():
    asyncio.run(main_flow())


if __name__ == "__main__":
    main()
