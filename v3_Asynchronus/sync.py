import time

def fetch_weather():
    print("Fetching weather data")
    time.sleep(4) #simulate a network delay
    print("weather data fetched")

def fetch_news():
    print("Fetching news data...")
    time.sleep(2)
    print("News data fetched")



def main():
    start_time = time.time()

    fetch_weather()
    fetch_news()


    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")




main()