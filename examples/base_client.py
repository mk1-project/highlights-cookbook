from typing import List, Optional, Dict, Union
import requests

class HighlightsClient:
    def __init__(self, api_key: str, base_url: str = "https://api.highlights.mk1.ai"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        }

    def search(
        self,
        query: str,
        chunk_txts: List[Union[str, Dict]],
        top_n: Optional[int] = 10,
        true_order: Optional[bool] = True
    ) -> dict:
        """
        Search through text chunks to find relevant passages.

        Args:
            query: The search query
            chunk_txts: List of text passages to search through. Each chunk can be either:
                       - A string containing the text
                       - A dict with required 'text' field and optional 'metadata' and 'original_index' fields
            top_n: Number of top results to return (default: 10)
            true_order: Whether to maintain original chunk order in results (default: True)

        Returns:
            Dictionary containing search results and metadata
        """
        endpoint = f"{self.base_url}/search"

        # Validate and format chunks
        formatted_chunks = []
        for i, chunk in enumerate(chunk_txts):
            if isinstance(chunk, str):
                formatted_chunks.append(chunk)
            elif isinstance(chunk, dict):
                if 'text' not in chunk:
                    raise ValueError(f"Chunk at index {i} is missing required 'text' field")
                formatted_chunks.append(chunk)
            else:
                raise ValueError(f"Invalid chunk type at index {i}. Must be string or dict")

        payload = {
            "query": query,
            "chunk_txts": formatted_chunks,
            "top_n": top_n,
            "true_order": true_order
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    client = HighlightsClient(api_key="YOUR_API_KEY")
    text_chunks = [
        "This is a test chunk",
        {"text": "Another test chunk", "metadata": {"source": "test_source"}, "original_index": 1}
    ]
    results = client.search_text_chunks("test query", text_chunks)
    print(results)