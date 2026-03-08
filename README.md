# 🚀 RAG-Ready Extractor

**The missing ingestion layer for modern RAG systems.**

Turn messy webpages and PDFs into **clean, structured knowledge for AI pipelines** in one API call.

![API](https://img.shields.io/badge/API-RapidAPI-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![Infra](https://img.shields.io/badge/infra-AWS%20Lambda-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

# ⚡ TL;DR

RAG-Ready Extractor is a **high-performance ingestion API** that converts raw web pages and PDFs into **RAG-optimized structured data**.

**Input**

• URL
• PDF

**Output**

• semantic chunks
• importance scoring
• structured tables
• token usage metadata

**Designed for**

• Pinecone
• Weaviate
• Qdrant
• LangChain
• LlamaIndex

---

# 🚨 The Problem

Most RAG systems index **raw HTML or PDF text**.

This introduces a large amount of **noise** into the knowledge base:

• navigation menus
• cookie banners
• footers
• related links
• ads

In many real pipelines **30-40% of indexed tokens are useless**.

This causes:

**Hallucinations**
The model confuses navigation elements with actual knowledge.

**High Costs**
You pay for tokens that add zero value.

**Slow Performance**
Larger contexts increase latency.

---

# 💸 Cost Savings Example

Based on benchmarks using large technical documents (e.g., the BloombergGPT research paper):

| Metric             | Standard Pipeline | RAG-Ready Pipeline                |
| ------------------ | ----------------- | --------------------------------- |
| Input Tokens       | 100k              | ~65k                              |
| Noise Removed      | 0%                | ~35%                              |
| Retrieval Quality  | Variable          | Improved via importance filtering |
| Estimated LLM Cost | 100%              | 30-70% reduction                  |

Filtering noise before embedding **dramatically reduces token usage**.

---

# 🛠 Practical Integration (Pinecone Example)

Extract clean content and index **only meaningful chunks**.

```python
import requests
from pinecone import Pinecone

# 1. Extract structured content
data = requests.post(
    "API_URL",
    json={"url": "https://example.com/blog"}
).json()

# 2. Connect to vector database
pc = Pinecone(api_key="YOUR_KEY")
index = pc.Index("rag-knowledge")

# 3. Index only high-importance chunks
for chunk in data["content"]["chunks"]:
    if chunk["importance_score"] > 6.5:

        index.upsert(vectors=[{
            "id": str(hash(chunk["text"])),
            "values": embed(chunk["text"]),
            "metadata": {
                "section": chunk["heading_context"]
            }
        }])
```

The API returns content that is **ready to be embedded and indexed**.

---

# 🧱 Supported Inputs

The API currently supports:

**Web Pages**

• blogs
• documentation sites
• landing pages

**PDF Documents**

• research papers (ArXiv)
• technical manuals
• financial filings

**Structured Data**

HTML tables are automatically converted into **clean JSON objects**.

---

# 📦 API Response

Example response structure:

```json
{
  "metadata": {
    "title": "BloombergGPT...",
    "word_count": 27938
  },
  "content": {
    "chunks": [
      {
        "text": "The use of NLP in finance...",
        "importance_score": 7.06,
        "heading_context": "Introduction"
      }
    ],
    "tables": [
      {
        "table_type": "pricing",
        "headers": ["Feature", "Basic", "Pro"],
        "rows": []
      }
    ]
  },
  "usage": {
    "latency_ms": 6900,
    "token_count": 57212
  }
}
```

---

# ⚡ Benchmarks

Example benchmark using the **BloombergGPT research paper**.

| Metric             | Result      |
| ------------------ | ----------- |
| Tokens processed   | 57,212      |
| Word count         | 27,938      |
| Processing latency | 6.9 seconds |
| Extracted chunks   | 3,481       |

Large documents can be processed in **a few seconds while preserving semantic structure**.

---

# 🏗 Architecture

```
Client
   ↓
RapidAPI Gateway
   ↓
Extraction Engine
   ↓
Structure Analyzer
   ↓
Importance Scoring
   ↓
Structured JSON Output
```

The API is designed as a **pre-vectorization ingestion layer** for AI pipelines.

---

# 🎯 Ideal Use Cases

RAG-Ready Extractor is designed for:

• RAG pipelines
• AI documentation chatbots
• research assistants
• knowledge base ingestion
• web → vector database pipelines

---

# 🚀 Get Started

Access the API through RapidAPI.

**Step 1 — Get your API key**

👉 RapidAPI:
https://rapidapi.com/cdd-it-cdd-lab-it/api/rag-ready-markdown-pdf-extractor

## 2. Send Request

Use your preferred HTTP client.

Example using Python:

```python
import requests

response = requests.post(
    API_URL,
    json={"url": "https://example.com"}
)
print(response.json())
```

**Step 3 — Extract structured knowledge**

Send a URL or PDF and receive **clean data ready for vector databases**.

---

# ❤️ Built for AI Developers

Created by **Carlos Manuel Díaz**.

Helping developers build **cleaner and more efficient RAG pipelines**.
