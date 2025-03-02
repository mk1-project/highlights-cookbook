# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Effective retrieval is essential for accurate Q&A and document search. However, traditional retrieval methods often struggle with accuracy, especially when handling large, real-world documents.

To overcome these limitations, we've developed **Highlights**, a specialized LLM[^1] optimized explicitly for retrieval tasks. We like to think of it as an "automatic highlighter", efficiently pinpointing key text segments using the power of an LLM.

<img width="864" alt="highlights-2" src="https://github.com/user-attachments/assets/40825619-dd89-4be8-978c-7d49bf8bc270" />

## Key features:

- **Massive context window**: Efficiently queries documents up to 2M tokens.
- **Flexible chunking**: Handles text segments ranging from single sentences to thousands of tokens, scoring each segment _in context_—unlike traditional vector search approaches. 
- **Rapid retrieval**: Processes up to 32K tokens in fractions of a second, significantly faster and more cost-effective than conventional long-context LLM approaches.

Highlights can function independently as a dedicated retrieval module or seamlessly integrate with other LLMs for RAG and agent-driven workflows.

## Recommended Usage Patterns

Below are simple examples showing how Highlights can integrate into your existing Q&A workflows. We encourage you to experiment with these examples on your own data.

### Q&A with a Single Large Document

When querying a large document (128K–2M tokens), a promising approach is to simply use a long context LLM. However, frontier models often lack sufficient context window sizes, and also struggle with precision (resulting in "needle-in-a-haystack" accuracy issues).

Highlights solves these issues by natively supporting documents with millions of tokens, demonstrating significantly better recall accuracy for Q&A tasks. It also offers optimized performance with reduced costs and improved speeds (up to 16x faster) compared to long context LLMs.

[Try Single-Document Q&A on a Large SEC Filing →](examples/pdf_chunking_and_generation.ipynb)

### Q&A with a Multiple Documents (<2M total tokens)

To support multiple documents, a commmon approach is to concatenate all the documents (with marked boundaries via prompting) and sending to a long context LLM. However this approach suffers the same drawbacks as previously described, and quickly becomes infeasible as many frontier models have context windows less than 200K tokens.

Highlights again is an attractive option. In particular, Highlights natively supports multiple documents by including document metadata to each returned text chunk. Furthermore, the ability to support 2M total tokens allows Q&A to extend well beyond the limitations of many frontier models.

[Try Multi-Document Q&A →](examples/multi_doc_search.ipynb)

### Q&A using RAG (>2M total tokens)

Q&A that extends beyond 2M tokens typically requires a sophisticated RAG system that includes vector search, re-ranking, and complex prompting techniques. 

With Highlights, the RAG system becomes significantly simpler: All we need is a lightweight prefiltering stage whose only task is to reduce the documents to manageable size (128K to 2M tokens). Then, these results can plug directly into the same pipeline as above.

## Prerequisites

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
