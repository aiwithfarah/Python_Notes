import asyncio

# define a coroutine


async def make_toast():
    print("Put bread in")
    await asyncio.sleep(2)  # Non-blocking. I'm waiting go do something else
    print("Toast is done!")


async def make_coffee():
    print("Start Coffee")
    await asyncio.sleep(2)
    print("Coffee is done!")


async def main():
    # schedule both of them to run at the same time
    # gather() runs them concurrently
    await asyncio.gather(make_toast(), make_coffee())

# We need an even loop to run async code
asyncio.run(main())
# Total time: 2 seconds (Concurrent)
