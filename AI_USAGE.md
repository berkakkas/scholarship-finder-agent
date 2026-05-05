# AI_USAGE.md

## Project AI Usage Report

### Project Name
Scholarship Finder Agent

---

## Overview

This project implements an agentic AI system designed to help students discover suitable scholarship opportunities using Retrieval-Augmented Generation (RAG), web search tools, and LangGraph workflows.

The system combines document retrieval and web-based information gathering to generate context-aware scholarship recommendations.

---

## AI Technologies Used

### 1. LangGraph

LangGraph is used to create the agent workflow and branching logic.

The agent decides:
- when to use RAG retrieval
- when to use web search
- how to combine retrieved information

This enables autonomous tool-selection behavior.

---

### 2. Retrieval-Augmented Generation (RAG)

The project uses a RAG pipeline with a scholarship knowledge base consisting of 15 documents stored in the `docs/` folder.

The RAG system:
- retrieves relevant scholarship information
- searches semantically similar documents
- improves response relevance

ChromaDB is used as the vector database.

---

### 3. Web Search Tool

The system includes a DuckDuckGo-based web search tool.

This tool is used for:
- latest scholarship information
- deadlines
- updated online scholarship data

The agent can dynamically decide when to use web search.

---

### 4. LangChain

LangChain is used to:
- connect tools
- manage retrieval logic
- integrate the vector database
- structure the AI workflow

---

## AI-Assisted Development

AI tools such as ChatGPT were used during:
- architecture planning
- debugging
- workflow design
- documentation preparation

All generated code was reviewed, modified, tested, and understood before submission.

---

## Conclusion

The project demonstrates the use of:
- agentic AI workflows
- tool calling
- branching logic
- RAG systems
- vector databases
- web retrieval integration

within a unified scholarship recommendation system.