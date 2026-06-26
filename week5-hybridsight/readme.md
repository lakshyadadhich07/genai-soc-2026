# Week 5 – HybridSight (RAG + Vision Foundations)

## Overview

Week 5 focused on building the core retrieval and vision pipeline for HybridSight.

This week introduced Retrieval-Augmented Generation (RAG), vector databases, embeddings, and image understanding. The objective was to move from a normal chatbot to an AI system capable of retrieving knowledge before generating responses.

---

## Features Implemented

### 1. Vision Module

* Connected image understanding using Groq Vision model
* Generated natural language descriptions from uploaded images
* Tested image reasoning and screenshot understanding

### 2. Document Ingestion Pipeline

* Loaded documents from local files
* Split documents into chunks using Recursive Character Text Splitting
* Prepared data for embedding generation

### 3. Embeddings + Vector Database

* Generated embeddings using:

  * `all-MiniLM-L6-v2`
* Stored vectors using:

  * Chroma Vector Database

### 4. Retrieval-Augmented Generation (RAG)

* Retrieved relevant chunks before answering
* Injected retrieved context into prompts
* Reduced hallucinations using grounded prompting

### 5. Context Optimization

* Reformatted retrieved chunks into structured facts
* Improved synthesis quality of generated responses

---

## Project Flow

User Question
↓
Retriever
↓
Vector Database
↓
Relevant Context
↓
Prompt Injection
↓
LLM
↓
Final Answer

---

## Example

### Input

What is Python?

### Retrieved Context

Fact 1: Python is a programming language
Fact 2: Python supports web development
Fact 3: Python supports AI

### Output

Python is a programming language that supports web development and AI.

---

## Technologies Used

* Python
* LangChain
* LangGraph
* Groq API
* ChromaDB
* HuggingFace Embeddings
* Recursive Character Text Splitter

---

## Learning Outcomes

* Understood how embeddings work
* Built a complete RAG pipeline
* Learned vector similarity search
* Reduced hallucinations using retrieval
* Connected retrieval with generation

---

## Status

Week 5 Progress: ✅ Completed (RAG Foundation)

Next Goal:
Build the complete HybridSight Agent by combining:

* RAG
* Memory
* Vision
* Multi-tool reasoning
