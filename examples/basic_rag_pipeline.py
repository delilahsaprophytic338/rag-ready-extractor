import requests

# =============================
# Configuration
# =============================

API_URL = "https://rapidapi.com/cdd-it-cdd-lab-it/api/rag-ready-markdown-pdf-extractor/"

HEADERS = {
    "X-RapidAPI-Key": "API_KEY",
    "Content-Type": "application/json"
}

# =============================
# Target Document
# =============================

payload = {
    "url": "https://arxiv.org/pdf/2303.17564.pdf",
    "chunk_size": 1000
}

print("🚀 Starting intelligent extraction...")

# =============================
# API Request
# =============================

response = requests.post(API_URL, json=payload, headers=HEADERS)

if response.status_code != 200:
    print("❌ API request failed")
    exit()

data = response.json()

# =============================
# Semantic Filtering (Core Value)
# =============================

if data and data.get("success"):

    chunks = data["content"]["chunks"]

    # Index only high-quality semantic content
    clean_chunks = [
        c for c in chunks
        if c["importance_score"] > 6.5
    ]

    print(f"✅ Processing latency: {data['usage']['latency_ms']} ms")
    print(f"📊 Total tokens: {data['usage']['token_count']}")
    print(f"✂ Original chunks: {len(chunks)}")
    print(f"🔥 High-quality chunks: {len(clean_chunks)}")

    # Estimated token savings
    savings = 100 - (len(clean_chunks) / len(chunks) * 100)

    print(f"💰 Estimated token savings: {savings:.2f}%")
