import asyncio

# define coroutine


async def download_page(url):
    print(f"Downloading {url}")
    await asyncio.sleep(2)
    print(f"Data from {url}")

# define main coroutine


async def main():
    url_list = ["google.com", "yahoo.com", "bing.com"]
    # 1. Create a list of pending tasks (Coroutines)
    # We use a List Comprehension here
    tasks = [download_page(url)for url in url_list]

    # 2. Run them all at once
    # We use the * operator to "unpack" the list into separate arguments
    # It becomes: gather(task1, task2, task3)
    results = await asyncio.gather(*tasks)

    print(results)

asyncio.run(main())
