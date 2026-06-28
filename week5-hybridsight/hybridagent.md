# HybridSight — Hybrid RAG + Web + Vision Agent

HybridSight is a multi-tool AI assistant built during **Week 5 of GenAI SoC 2026**.

It combines:

* 📄 PDF Question Answering (RAG)
* 🌐 Live Web Search
* 🖼 Image Understanding
* 📚 Wikipedia Knowledge Retrieval
* 🧠 Tool Routing
* 🔍 Reasoning Trace

The agent decides which tool to use depending on the query.

---

# Features

## 1. RAG (Retrieval Augmented Generation)

Upload PDFs and ask questions based on document contents.

Example:

* Upload Resume
* Ask:
  `What projects are mentioned?`

---

## 2. Live Web Search

Fetch recent information using DuckDuckGo.

Example:

* `latest AI news`

---

## 3. Vision Tool

Upload images and get descriptions.

Example:

* Upload image
* Ask:
  `what's in this picture?`

---

## 4. Wikipedia Tool

Answer general factual questions.

Example:

* `What is Python?`

---

## 5. Tool Routing

HybridSight automatically routes requests:

| Query Type     | Tool       |
| -------------- | ---------- |
| Uploaded PDFs  | RAG        |
| Current Events | Web Search |
| Images         | Vision     |
| General Facts  | Wikipedia  |

---

# Project Structure

```bash
week5-hybridsight/

app.py
agent.py
ingest.py

tools_rag.py
tools_web.py
tools_wiki.py
tools_vision.py

docs/
chroma_store/

requirements.txt
.env.example
README.md
```

---

# Installation

Clone:

```bash
git clone <repo-link>
cd week5-hybridsight
```

Create environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

---

# Technologies Used

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq API
* Llama Models
* DuckDuckGo Search
* Wikipedia
* Gradio

---

# Test Results

## Test Case 1 — PDF Question Answering

Question:
What projects are mentioned?

Expected Tool:
RAG

Result:
✅ Passed

![alt text](<Screenshot 2026-06-28 145023.png>)

---

## Test Case 2 — Current Event

Question:
latest AI news

Expected Tool:
Web Search

Result:
✅ Passed

![alt text](<Screenshot 2026-06-28 145101.png>)
---

## Test Case 3 — Vision Tool

Question:
what's in this picture?

Expected Tool:
Vision

Result:
✅ Passed

![alt text](<Screenshot 2026-06-28 145201.png>)
![alt text](<Screenshot 2026-06-28 145222.png>)

---

## Test Case 4 — General Knowledge

Question:
What is Python?

Expected Tool:
Wikipedia

Result:
✅ Passed

![alt text](<Screenshot 2026-06-28 145123.png>)

---


# Learnings

This project helped me understand:

* Retrieval Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Multi-tool AI Agents
* Prompt Routing
* Agent Design
* Vision Models
* Building AI Apps with Gradio

---

# Future Improvements

* LangGraph reasoning
* Better tool selection
* Conversation memory
* Streaming responses
* Deployment on Hugging Face Spaces

---

Built during **GenAI SoC 2026 • Week 5 🚀**
