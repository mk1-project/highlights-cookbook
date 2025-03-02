# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Retrieval is central to Q&A and document search. However, traditional retrieval methods are often limited and struggle with accuracy—especially when handling large, real-world documents.

To overcome these limitations, we've developed **Highlights**, a specialized LLM[^1] optimized explicitly for retrieval tasks. We like to think of it as an "automatic highlighter", efficiently pinpointing key text segments using the power of an LLM.

<img width="864" alt="highlights-2" src="https://github.com/user-attachments/assets/40825619-dd89-4be8-978c-7d49bf8bc270" />

Key features of Highights:

- **Massive context window**: Efficiently queries documents up to 2M tokens.
- **Flexible chunking**: Handles text segments ranging from single sentences to thousands of tokens, scoring each segment _in context_—unlike traditional vector search approaches. 
- **Rapid retrieval**: Processes 32K tokens in fractions of a second, significantly faster than using a long context LLM.

Highlights can be used independently as a pure retrieval module, or integrated with other LLMs for advanced generative and agent-based workflows. 

## Recommended Usage Patterns

We have prepared simple examples to show how Highlights can be seamlessly integrated into Q&A workflows. We invite you to try these on your own data and compare against your internal workflows.

### Q&A with a Single Large Document

Consider querying a large document with somewhere between 128K to 2M tokens. A common method is to simply load the document into the context of an LLM. However this method has a number of drawbacks:

- Many frontier models have a limited context window that can not fit the entire document.
- Long context frontier models suffer from blindspots, e.g. Needle In A Haystack issues that can lead to inaccuracies.
- The cost of using long context LLMs can be high, where you have to pay for input tokens for each query.

Highlights solves these issues:
- 🚀 Highlights natively supports millions of tokens.
- 🎯 Our internal tests show Highlights has more accurate recall for Q&A.
- 💰 With our custom optimized model, Highlights is both faster and less expensive than using long context (up to 16x).

Try out single-doc Q&A using Highlight on a large SEC filing using Highlights here.

### Q&A with a Multiple Documents (<2M total tokens)

To support multiple documents, a commmon approach is to simply concatenate all the documents (with marked boundaries) and sending to a long context LLM. However this approach suffers the same drawbacks as previously described, and quickly becomes infeasible as many frontier models have context windows less than 200K tokens.

Highlights again is an attractive option. In particular, we can easily support multiple documents by including document metadata to each returned text chunk. Furthermore, the ability to support 2M total tokens allows Q&A to extend well beyond the limitations of many frontier models.

Try out multi-doc Q&A here.

### Integration to RAG-like workflows

Q&A that extends beyond 2M tokens often requires more sophisticated RAG systems that includes vector search, re-ranking, complex prompting techniques. In these cases, long context LLMs hold promise but also pose challenges (see [Databricks analysis](https://www.databricks.com/blog/long-context-rag-performance-llms)).

Highlights offers a simpler approach. We can use a lightweight RAG system to reduce documents to a size compatible with Highlights (128K to 2M tokens), and then use the methods above for the final retrieval and generation step. 

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
