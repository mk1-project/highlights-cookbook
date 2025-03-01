# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Retrieval is crucial for tasks such as document search and question answering.

However, traditional retrieval methods often struggle with accuracy, especially when handling large, complex, real-world documents. This significantly limits their effectiveness, especially within typical Retrieval-Augmented Generation (RAG) workflows that try to leverage long-context generation (see [Databricks analysis](https://www.databricks.com/blog/long-context-rag-performance-llms)).

To overcome these limitations, we've developed a **specialized LLM[^1] optimized explicitly for retrieval tasks**. Our model serves as a seamless, drop-in replacement for the retrieval component in any AI workflow, offering significant advantages:

- **Massive context window**: Efficiently queries documents up to 2M tokens.
- **Flexible chunking**: Handles text segments ranging from single sentences to thousands of tokens—something traditional vector search methods cannot.
- **Rapid retrieval**: Processes 32K tokens in fractions of a second, significantly faster and more accurately than conventional methods.

Think of Highlights as an "automatic highlighter" powered by a custom LLM, efficiently pinpointing crucial text segments from your source material. Our model can be used independently as a pure retrieval solution, or integrated with other LLMs for advanced generative and agent-based workflows.

![highlights](https://github.com/user-attachments/assets/0396d958-9fee-449f-aacd-4e7454addb22)

## Recommended Usage Patterns

We invite users to test our workflow (Highlights retrieval + LLM generation) and directly compare it against traditional long-context LLM approaches or their own RAG workflows.

### Documents under 2M tokens

- **Direct Q&A / Document Search**: Highlights retrieves relevant information directly, feeding precise context into an LLM for generation. This yields better accuracy and faster responses than standard long-context LLMs or complex RAG systems.

- **Agent Memory**: Agents can leverage Highlights as dynamic memory, querying contextually relevant information on-demand.

### Documents over 2M tokens

- **RAG-like pre-filtering**: First use a lightweight RAG system to reduce documents to a manageable size (128K to 2M tokens). Highlights then seamlessly takes over the retrieval step, replacing traditional vector search and re-ranking methods, improving both accuracy and efficiency.

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
