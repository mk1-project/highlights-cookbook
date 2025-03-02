# Highlights API: Enhanced Retrieval Powered by our Custom LLM

Effective retrieval is essential for accurate search and Q&A. However, traditional retrieval methods often struggle with accuracy, especially when handling large documents and the complexity of real-world data.

To overcome these limitations, we've developed **Highlights**, a specialized LLM[^1] optimized explicitly for retrieval tasks. We like to think of it as an "automatic highlighter", efficiently pinpointing key text segments using the power of an LLM.

<img width="864" alt="highlights-2" src="https://github.com/user-attachments/assets/40825619-dd89-4be8-978c-7d49bf8bc270" />

## Key features:

- **Massive context window**: Efficiently queries documents up to 2M tokens.
- **Flexible chunking**: Handles text segments ranging from single sentences to thousands of tokens, scoring each segment _in context_—unlike traditional vector search approaches. 
- **Rapid retrieval**: Processes up to 32K tokens in fractions of a second, significantly faster and more cost-effective than conventional long-context LLM approaches.

Highlights can function independently as a dedicated retrieval module or seamlessly integrate with other LLMs for RAG and agent-driven workflows.

## Recommended Usage Patterns

Below are simple examples showing how Highlights can integrate into your existing workflows. We encourage you to experiment with these examples on your own data.

### Single Large Document Search

When querying a large document, a promising approach is to simply use a long context LLM. However, popular frontier models may not fit the entire document in its context window, and also struggle with precision issues (e.g. they fail needle-in-a-haystack tests).

We can solve this by first sending the large document to Highlights, which nativelty supports millions of tokens. Highlights then extracts the relevant sections and the results can be sent directly to another LLM for generation. The entire process improves on speed (>10x) and cost compared to sending the entire document to a frontier LLM. 

[Try Single-Document Search on a Large Document (Border Act) →](examples/single_doc_search.ipynb)

### Multiple Document Search (<2M total tokens)

When querying across multiple documents, a commmon approach is to concatenate all the documents, mark document boundaries via prompting, and send the prompt and query to a long context LLM. However this approach suffers the same drawbacks as previously described, and quickly becomes infeasible with the 200K token limit of popular frontier models.

Highlights again is an attractive option. Our Highlights API supports multiple documents by including document metadata to each returned text chunk. Furthermore, with its ability to support 2M total tokens, Q&A can extend well beyond the limitations of most frontier models.

[Try Multi-Document Search →](examples/multi_doc_search.ipynb)

### Search using RAG (>2M total tokens)

Search that extends beyond 2M tokens typically requires a sophisticated RAG system that includes vector search, re-ranking, and complex prompting techniques.

With Highlights, the RAG system can be significantly simplified: All we need is a lightweight pre-filtering stage whose only task is to reduce the documents to manageable size (128K to 2M tokens). Then, these results can plug directly into the same pipeline as described above.

## QuickStart

To get started with MK1 Highlights, you'll need an API key (sign up [here](https://mk1.ai/products/highlights)).

Then you can simply post to the Highlights API:

```
curl -X POST "https://api.highlights.mk1.ai/distributor/search" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR-API-KEY" \
  -d '{
    "query": "What is machine learning?",
    "chunk_txts": [
      "Machine learning models can process vast amounts of data quickly.",
      "Natural language processing helps computers understand human language.",
      "Deep learning is a subset of machine learning based on neural networks.",
      "Data science combines statistics, programming, and domain expertise."
    ],
    "top_n": 2,
    "true_order": true
  }'
```

For detailed documentation, visit our [docs](https://docs.mk1.ai/highlights/highlights_api.html).

## Examples

Explore our collection of examples to see Highlights in action:
1. [Basic Usage](examples/api_basics.ipynb)
2. [Single Doc Search](examples/single_doc_search.ipynb)
3. [Multiple Doc Search](examples/multi_doc_search.ipynb)
3. [NIAH Tester](examples/niah_test.ipynb)

[^1]: Our custom LLM is modified from a Llama model.
