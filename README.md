# Scholarship Finder Agent

## Overview

Scholarship Finder Agent is an agentic AI system that helps students discover suitable scholarships based on their academic background and interests.

The system combines:
- LangGraph
- LangChain
- Retrieval-Augmented Generation (RAG)
- Web Search

to provide intelligent scholarship recommendations.

---

## Features

- Scholarship recommendation system
- RAG-based document retrieval
- Web search integration
- LangGraph branching workflow
- Vector database with ChromaDB
- Scholarship knowledge base with 15 documents

---

## Architecture

```text
User Query
     ↓
LangGraph Decision Node
     ↓
 ┌───────────────┐
 │ RAG Retrieval │
 │ Web Search    │
 └───────────────┘
     ↓
Final Response
```

---

## Technologies Used

- Python
- LangGraph
- LangChain
- ChromaDB
- DuckDuckGo Search
- GitHub Models API

---

## Project Structure

```text
scholarship-finder-agent/
│
├── app.py
├── graph.py
├── rag.py
├── tools.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── .env.example
│
└── docs/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_token_here
```

---

## Run the Project

```bash
python app.py
```

---

## Example Queries

### RAG Example

```text
Find scholarships for international students
```

### Web Search Example

```text
latest scholarships 2026
```

---

## Example Output

```text
Recommended Scholarships:
- Erasmus Scholarship
- Fulbright Scholarship
- DAAD Scholarship
```

---

## AI Usage

See `AI_USAGE.md` for details about AI technologies and AI-assisted development.

---

## Authors

University Project — Agentic AI System