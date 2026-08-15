from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os
from tavily import TavilyClient
from bs4 import BeautifulSoup
from readability import Document
import trafilatura
import re

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic , Returns Titles, URls and important things"""
    results = tavily.search(query=query, max_results=5)

    

    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL:{r['url']}\nSnippet: {r['content'] [:300]}"
        )

    return "\n----\n".join(out)



@tool
def scrape_url(url: str) -> str:
    """
    Scrape and extract clean readable content from a URL.
    Uses multiple extraction strategies for better reliability.
    """

    try:
        # Clean URL if it accidentally contains "URL:"
        url = url.strip()

        if url.startswith("URL:"):
            url = url.replace("URL:", "", 1).strip()

        # Fetch webpage
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"
                )
            },
        )

        response.raise_for_status()

        html = response.text

        # --------------------------------------------------
        # Strategy 1: Trafilatura
        # --------------------------------------------------

        text = trafilatura.extract(
            html,
            include_links=True,
            include_tables=True,
        )

        if text and len(text.strip()) > 200:
            return text.strip()[:15000]

        # --------------------------------------------------
        # Strategy 2: Readability
        # --------------------------------------------------

        doc = Document(html)

        title = doc.title()
        cleaned_html = doc.summary()

        soup = BeautifulSoup(
            cleaned_html,
            "html.parser"
        )

        text = soup.get_text(
            separator="\n",
            strip=True
        )

        if text and len(text.strip()) > 200:
            return f"Title: {title}\n\n{text[:15000]}"

        # --------------------------------------------------
        # Strategy 3: BeautifulSoup
        # --------------------------------------------------

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # Remove unnecessary elements
        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside",
            "form",
            "noscript",
            "iframe",
        ]):
            tag.decompose()

        # Prefer article/main content
        main = (
            soup.find("article")
            or soup.find("main")
            or soup.find("div", class_=re.compile(
                r"(article|content|main|post|entry)",
                re.I
            ))
        )

        if main:
            text = main.get_text(
                separator="\n",
                strip=True
            )
        else:
            text = soup.get_text(
                separator="\n",
                strip=True
            )

        # Clean whitespace
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        text = text.strip()

        if text:
            return text[:15000]

        return "Could not extract readable content from this URL."

    except requests.RequestException as e:
        return f"Failed to fetch URL: {e}"

    except Exception as e:
        return f"Error scraping URL: {e}"