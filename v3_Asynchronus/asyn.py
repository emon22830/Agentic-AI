import asyncio
import time



async def fetch_weather():
    print("Fetching weather data")
    await asyncio.sleep(4) #simulate a network delay
    print("weather data fetched")

async def fetch_news():
    print("Fetching news data...")
    await asyncio.sleep(2)
    print("News data fetched")



async def main():
    start_time = time.time()

    await asyncio.gather(fetch_weather(), fetch_news())


    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")




asyncio.run(main())