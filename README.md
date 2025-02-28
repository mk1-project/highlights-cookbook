# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Retrieval is crucial for tasks like Retrieval-Augmented Generation (RAG), document search, Q&A, and citation identification. However traditional methods like embedding-based semantic search struggle with retrieval accuracy, especially for nuanced or complex text.

To address these limitations, we've developed a **specialized LLM optimized specifically for retrieval**. We think of it as an "automatic highlighter," pinpointing key text segments directly within documents using the power of an LLM. It supports context windows **up to 2M tokens**, processes 32K tokens in fractions of a second, and achieves significantly higher accuracy compared to traditional retrieval methods.

Our Highlights API provides direct access to the model, which can be used:

- In isolation as a pure retrieval tool (e.g., to identify references in large documents).

- Coupled with another LLM for generation tasks, such as in RAG workflows.

- As a memory subsystem in complex agent workflows.

### Example Use Cases:

- 🚀 **Improve RAG:** Query massive documents (up to 2M tokens) using Highlights and feed results into an LLM for generation.

- 🎯 **Reduce hallucinations:** Ground LLM responses with explicit citations.

- 💰 **Reduce prompt size:** Distill lengthy prompts and minimize token costs with minimal impact.

- 🧠 **Flexible memory:** Provide agents access to queryable memory modules for complex workflows.

## Prerequisites

To get started with MK1 Highlights, you'll need:
- An API key (sign up [here](https://mk1.ai/products/highlights))

## Examples

Explore our collection of examples to see MK1 Highlights in action:
1. [Basic Usage](examples/api_basics.ipynb)
2. [PDF Chunking and Generation](examples/pdf_chunking_and_generation.ipynb)
3. [NIAH Tester](examples/niah_test.ipynb)

## Documentation

For detailed documentation, visit our [Documentation Portal](link-to-docs).

- [Getting Started Guide](link)
- [API Reference](link)
- [Best Practices](link)
- [Examples](link)
