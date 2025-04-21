import os
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from tqdm import tqdm

class Researcher:
    """
    Single responsibility: fetch & scrape web sources for a query
    TODO: NER insted of query w el search 3ltol
    """

    def __init__(self, max_sources: int):
        self.max_sources = max_sources

    def fetch(self, query: str) -> List[Dict]:
        hits = list(DDGS().text(query, max_results=self.max_sources * 2))
        sources = []
        for hit in tqdm(hits, desc="Scraping", unit="page"):
            try:
                html = requests.get(
                    hit["href"], timeout=10,
                    headers={"User-Agent": "Mozilla/5.0"}
                ).text
                soup = BeautifulSoup(html, "html.parser")
                text = " ".join(p.get_text(" ", strip=True)
                                for p in soup.find_all("p"))
            except Exception:
                text = ""
            snippet = (text or hit.get("body", ""))[:200]
            sources.append({
                "url": hit["href"],
                "snippet": snippet,
                "text": text or snippet
            })
            if len(sources) >= self.max_sources:
                break
        print(f"[research] fetched {len(sources)} sources for '{query}'")
        return sources
