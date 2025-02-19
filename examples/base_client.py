from typing import List, Optional
import requests

class HighlightsClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8022"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def search_text_chunks(
        self,
        query: str,
        text_chunks: List[str],
        top_n: Optional[int] = 3
    ) -> dict:
        """
        Search through text chunks to find relevant passages.

        Args:
            query: The search query
            text_chunks: List of text passages to search through
            top_n: Number of top results to return

        Returns:
            Dictionary containing search results and metadata
        """
        endpoint = f"{self.base_url}/moonshine/search/text_chunks"

        payload = {
            "query": query,
            "text_chunks": text_chunks,
            "top_n": top_n
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()