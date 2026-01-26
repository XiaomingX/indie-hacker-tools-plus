高价值：否

标题：
《Together Rerank API：优化搜索与RAG，提升相关性》

### Rerank：提升搜索与RAG系统相关性的利器

#### 开篇：主题与背景
在信息爆炸的时代，提升搜索结果的相关性至关重要。Reranker就是这样一种专门用于优化搜索相关性的工具。它能对已检索的文档重新评估排序，筛选出更相关的信息，在检索增强生成（RAG）流程中起着关键的质量过滤作用，帮助优化语言模型生成的文档选择，提升生成质量并降低成本。

#### 一、Reranker是什么
Reranker是一种模型，它的主要作用是提升搜索相关性。具体来说，它对已检索的文档重新评估并重新排序，根据查询的相关性给每个文档分配分数，从而筛选出最重要的信息。在RAG流程里，它处于初始检索步骤和最终生成步骤之间，就像一个质量把关的角色，优化用于语言模型生成的文档选择，让生成结果更精准，还能减少处理成本。打个比方，它就像是一个精准的分拣员，把最相关的文档挑出来给后续的生成步骤。

#### 二、Together的Rerank API如何工作
1. **基本功能与兼容性**
Together的无服务器Rerank API能轻松把支持的rerank模型集成到企业应用中。它接收查询和一组文档，输出每个文档的相关性评分和排序索引，还支持筛选出前n个最相关的文档。这个API兼容Cohere Rerank，方便用户在现有应用中尝试其Reranker模型。它有几个主要功能：支持Salesforce的旗舰Reranker模型LlamaRank；支持JSON和表格数据；每个文档支持最长8K的上下文；低延迟，适合快速查询；与Cohere Rerank API完全兼容。
2. **文本示例**
    - **请求**：用Python代码示例，首先导入Together模块，创建客户端，指定查询“ What animals can I find near Peru?”以及相关文档，然后调用rerank.create方法，指定模型、查询、文档和要返回的前n个文档数量。例如：
```python
from together import Together

client = Together()

query = "What animals can I find near Peru?"

documents = [
    "The giant panda is endemic to China.",
    "The llama is a domesticated camelid from South America.",
    "The wild Bactrian camel is native to Northwest China and Mongolia.",
    "The guanaco, native to South America, is closely related to the llama.",
]

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=documents,
    top_n=2
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {documents[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```
    - **结果**：这个查询会把文档按与问题的相关性从高到低排序，返回前2个最相关的文档及其评分。
3. **JSON示例**
    - **请求**：同样用Python代码示例，指定查询“Which pricing did we get from Oracle?”，文档以JSON对象格式传入，还指定了用于排序的字段及顺序，调用rerank.create方法。例如：
```python
from together import Together

client = Together()

query = "Which pricing did we get from Oracle?"

documents = [
    {
        "from": "Paul Doe <paul@oracle.com>",
        "date": "2026-03-27",
        "subject": "Follow-up",
        "text": "We are happy to give you the following pricing for your project."
    },
    {
        "from": "John McGill <john@microsoft.com>",
        "date": "2026-03-28",
        "subject": "Missing Information",
        "text": "Here is the pricing you asked for."
    },
    {
        "from": "Generic SaaS Company <marketing@example.com>",
        "date": "2026-01-26",
        "subject": "Generative AI tips",
        "text": "Learn how to build generative AI applications fast!"
    },
]

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=documents,
    rank_fields=["from", "date", "text"],
    return_documents=True
)

print(response)
```
    - **结果**：返回按指定字段排序的文档列表，同时提供每个文档的相关性评分。

#### 总结
通过Together Rerank API，用户能够轻松提升搜索相关性，优化生成结果的质量，进而显著提高用户体验。它在搜索和RAG系统中起到了关键的优化作用，无论是文本还是JSON格式的文档都能很好地处理，为企业应用在信息处理方面提供了强大的支持。