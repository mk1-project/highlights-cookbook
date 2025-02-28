# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Retrieval is crucial for tasks such as document search and question answering. 

However, traditional retrieval methods, like vector search, often struggle with accuracy when dealing with complex, real-world texts. This significantly limits their effectiveness, especially within typical Retrieval-Augmented Generation (RAG) workflows that leverage long-context generation (see [here](https://www.databricks.com/blog/long-context-rag-performance-llms)).

To overcome these limitations, we've developed a **specialized LLM[^1] optimized explicitly for retrieval tasks**. Our model serves as a seamless, drop-in replacement for the retrieval component in any AI workflow, offering significant advantages:

- **Masive context window** supporting up to 2M tokens.
- **Flexible chunking** Handles chunks as small as single sentences or as large as thousands of tokens—unfeasible with traditional vector search methods.
- **Fast response time** processing 32K tokens in fractions of a second.
- **Accurate retrieval** achieving near perfect recall on [needle-in-a-haystack tests](examples/niah_test.ipynb) and multi-hop tasks.

Think of Highlights as an "automatic highlighter" powered by a custom LLM, efficiently pinpointing crucial text segments from your source material. Our model can be used independently as a pure retrieval solution, or integrated with other LLMs for advanced generative and agent-based workflows.

## Key Use Cases:

- 🚀 **Improve RAG:** Query massive documents (up to 2M tokens) using Highlights and feed results into an LLM for generation. See our [single doc RAG](examples/pdf_chunking_and_generation.ipynb) and [multi doc RAG](examples/pdf_chunking_and_generation.ipynb) examples.

- 🎯 **Reduce hallucinations:** Ground LLM responses with explicit citations.

- 💰 **Reduce prompt size:** Distill lengthy prompts and minimize token costs with minimal impact.

- 🧠 **Flexible memory:** Provide agents access to queryable memory modules for complex workflows.

## Quickstart

To get started with MK1 Highlights, you'll need:
- An API key (sign up [here](https://mk1.ai/products/highlights))

## Examples

Explore our collection of examples to see Highlights in action:
1. [Basic Usage](examples/api_basics.ipynb)
2. [Single Doc Search](examples/pdf_chunking_and_generation.ipynb)
3. [Multiple Doc Search](examples/multi_doc_search.ipynb)
3. [NIAH Tester](examples/niah_test.ipynb)

## Documentation

For detailed documentation, visit our [docs](https://docs.mk1.ai/highlights/highlights_api.html).

[^1]: Our custom LLM is modified from a Llama model.
