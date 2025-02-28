# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Retrieval is crucial for tasks like document search and Q&A. However, for nuanced or complex text found in real-world scenarios, traditional retrieval methods based on vector search often struggle with accuracy.

To address these limitations, we've developed a **specialized LLM[^1] optimized specifically for retrieval**. Think of it as an "automatic highlighter" that uses the power of an LLM to pinpoint key text segments from the source material. Key benefits of Highlights includes:

- **Masive context window** supporting up to 2M tokens
- **Fast response time** processing 32K tokens in fractions of a second 
- **Accurate retrieval** achieving near perfect recall on [needle-in-a-haystack tests](examples/niah_test.ipynb) and multi-hop tasks.
 
Our model can be used in isolation as a pure retrieval tool, or coupled with other LLMs for generation or complex agent workflows.

### Example Use Cases:

- 🚀 **Improve RAG:** Query massive documents (up to 2M tokens) using Highlights and feed results into an LLM for generation. See our [single doc RAG](examples/pdf_chunking_and_generation.ipynb) and [multi doc RAG](examples/pdf_chunking_and_generation.ipynb) examples.

- 🎯 **Reduce hallucinations:** Ground LLM responses with explicit citations.

- 💰 **Reduce prompt size:** Distill lengthy prompts and minimize token costs with minimal impact.

- 🧠 **Flexible memory:** Provide agents access to queryable memory modules for complex workflows.

## Prerequisites

To get started with MK1 Highlights, you'll need:
- An API key (sign up [here](https://mk1.ai/products/highlights))

## Examples

Explore our collection of examples to see Highlights in action:
1. [Basic Usage](examples/api_basics.ipynb)
2. [PDF Chunking and Generation](examples/pdf_chunking_and_generation.ipynb)
3. [NIAH Tester](examples/niah_test.ipynb)

## Documentation

For detailed documentation, visit our [Documentation Portal](link-to-docs).

- [Getting Started Guide](link)
- [API Reference](link)
- [Best Practices](link)
- [Examples](link)

[^1]: Our custom LLM is modified from a Llama model.
