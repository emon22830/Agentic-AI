from src.tools.tools import web_search,scrape_url

# output = web_search("Lastest neses on AI Reseach")

# print(output)



output = scrape_url.invoke(
    "https://news.mit.edu/topic/artificial-intelligence2"
)

print(output)