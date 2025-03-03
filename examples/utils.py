from typing import Tuple, List
from base_client import HighlightsClient
from datasets import load_dataset
from langchain_text_splitters import RecursiveCharacterTextSplitter

import random
import openai
import PyPDF2

class NIAHTester:
    def __init__(self, api_key: str):
        self.client = HighlightsClient(api_key=api_key)

    def generate_test_data(
        self,
        needle: str,
        haystack: str,
        needle_position: int = None,
    ) -> Tuple[List[str], int]:
        """
        Generate test data with a needle hidden in a haystack.

        Args:
            needle: The text to find
            num_haystack_items: Number of distractor texts to generate

        Returns:
            Tuple of (list of text chunks, index of needle)
        """
        chunk_size = 1024
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
        haystack_chunks = splitter.split_text(haystack)

        # Insert needle at random position or at specified position
        if needle_position is None:
            # Choose random chunk and position
            chunk_idx = random.randint(0, len(haystack_chunks) - 1)
            chunk_text = haystack_chunks[chunk_idx]
            insert_position = random.randint(0, len(chunk_text) - len(needle))

            # Insert needle and calculate absolute position
            haystack_chunks[chunk_idx] = f"{chunk_text[:insert_position]}{needle}{chunk_text[insert_position:]}"
            needle_position = chunk_idx * chunk_size + insert_position
        else:
            # Calculate chunk and position from absolute position
            chunk_idx = needle_position // chunk_size
            insert_position = needle_position % chunk_size
            chunk_text = haystack_chunks[chunk_idx]

            # Insert needle at specified position
            haystack_chunks[chunk_idx] = f"{chunk_text[:insert_position]}{needle}{chunk_text[insert_position:]}"

        return haystack_chunks

    def run_test(
        self,
        needle: str,
        query: str,
        haystack: str,
        needle_position: int = None,
    ) -> dict:
        """
        Run a needle-in-haystack test.

        Args:
            needle: The text to find
            query: The search query
            num_haystack_items: Number of distractor texts

        Returns:
            Dictionary containing test results
        """
        # Generate test data
        haystack = self.generate_test_data(
            needle=needle,
            haystack=haystack,
            needle_position=needle_position
        )

        # Perform search
        results = self.client.search(
            query=query,
            chunk_txts=haystack,
            top_n=1
        )

        success = False
        matching_chunk = None
        if results["results"]:
            # Check if needle is in first result for success metric
            first_chunk = results["results"][0]['chunk_txt']
            success = needle.strip() in first_chunk.strip()

            # Find which chunk actually contains the needle
            for result in results["results"]:
                chunk_text = result['chunk_txt']
                if needle.strip() in chunk_text.strip():
                    matching_chunk = chunk_text
                    break

        return {
            "success": success,
            "matching_chunk": matching_chunk,
            "total_chunks": len(haystack),
            "metadata": results.get("metadata", {})
        }

class PDFProcessor:
    def __init__(self, highlights_client, temperature: float = 0.7):
        self.highlights_client = highlights_client
        self.temperature = temperature

    def extract_text_from_pdf(self, pdf_path: str) -> List[str]:
        """
        Extract text from PDF, split by pages.

        Args:
            pdf_path: Path to the PDF file

        Returns:
            List of strings, where each string is the text from one page
        """
        text_chunks = []

        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Extract text from each page
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text.strip():  # Only add non-empty pages
                    text_chunks.append(text)

        return text_chunks

    def search_relevant_chunks(self, query: str, text_chunks: List[str], top_n: int = 3) -> List[str]:
        """
        Search for relevant chunks using Highlights API.

        Args:
            query: Search query
            text_chunks: List of text chunks to search through
            top_n: Number of top results to return

        Returns:
            List of most relevant text chunks
        """
        results = self.highlights_client.search(
            query=query,
            chunk_txts=text_chunks,
            top_n=top_n
        )

        return [result['chunk_txt'] for result in results['results']]

    def generate_response(self, query: str, context: List[str]) -> str:
        """
        Generate response using OpenAI API with context.

        Args:
            query: The question to answer
            context: List of relevant text chunks to use as context

        Returns:
            Generated response
        """
        # Combine context and prompt
        combined_prompt = f"""
        Context information is below.
        ----------------
        {' '.join(context)}
        ----------------
        Using the above context, please answer the following question: {query}
        """

        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or another appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
                {"role": "user", "content": combined_prompt}
            ],
            temperature=self.temperature
        )

        return response.choices[0].message.content