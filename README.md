# 🧠 AgentFlow API — Multi-Agent Research Platform

A production-oriented multi-agent AI research platform built using FastAPI, LangGraph, RAG, and ChromaDB.

This system performs intelligent research using a structured multi-agent workflow and Retrieval-Augmented Generation (RAG), delivering context-aware and reliable responses through a scalable API-first architecture.

---

# 🚀 Overview

This system uses a multi-agent architecture to process user queries through multiple stages:

1. Planner Agent → Refines user query  
2. Retriever Agent → Fetches relevant context using RAG  
3. Research Agent → Generates structured research notes  
4. Answer Generator → Produces final response with confidence and sources  

The system is designed with:

- scalability
- modularity
- observability
- structured outputs
- production-oriented architecture

---

# 🏗️ Updated Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
LangGraph Workflow
        ↓
Planner Agent
        ↓
Retriever Agent (RAG)
        ↓
Research Agent
        ↓
Answer Generator
        ↓
Structured Response
```

---

# 🏗️ Architecture Diagram

![Architecture](assets/architecture_diagram.png)

---

# 🔄 Workflow

1. User submits research query through Streamlit UI  
2. Frontend sends API request to FastAPI backend  
3. Planner agent refines the query  
4. Retriever fetches relevant context using ChromaDB + embeddings  
5. Research agent generates structured notes  
6. Answer generator produces final response  
7. System returns:
   - refined query
   - retrieved context
   - research notes
   - final answer
   - confidence score
   - sources

---

# 🧠 Production-Oriented Features

## ✅ Multi-Agent Workflow

Built using LangGraph with modular agent orchestration.

---

## ✅ RAG Pipeline

Uses:
- ChromaDB
- OpenAI embeddings
- semantic retrieval

for context-grounded responses.

---

## ✅ FastAPI Backend

Production-style backend architecture using FastAPI:
- REST API endpoints
- frontend/backend separation
- scalable deployment architecture

---

## ✅ Structured Output Validation

Uses:
- Pydantic schemas
- JSON validation
- safe parsing utilities

to ensure reliable outputs.

---

## ✅ Retry Mechanism

Implements:
- retry with stricter prompts
- malformed JSON handling
- fallback responses

for robust AI generation.

---

## ✅ Logging & Observability

Includes:
- workflow logging
- error tracking
- debugging support

through centralized logger utilities.

---

# 🌟 Highlights

- Designed production-oriented multi-agent AI architecture
- Implemented RAG pipeline with persistent ChromaDB
- Built FastAPI backend for scalable API-first deployment
- Developed structured output system with validation and retries
- Added observability through centralized logging
- Created end-to-end AI research platform with Streamlit frontend

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- LangGraph
- LangChain
- ChromaDB
- OpenAI API
- Pydantic

---

# 📂 Final Project Structure

```text
agentflow-api/
│
├── backend/
│   ├── main.py
│   ├── graph.py
│   ├── nodes.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── vector_store.py
│   ├── logger.py
│   ├── utils.py
│   ├── schemas.py
│   ├── state.py
│   ├── llm.py
│   ├── config.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
├── chroma_db/
├── logs/
├── data/
├── assets/
│
├── README.md
└── .gitignore
```

---

# 🧪 Example Queries

- What is RAG and how does it improve LLM performance?
- Explain how multi-agent AI systems work
- What are the risks of AI adoption in enterprises?
- How is generative AI used in customer support?
- Explain differences between vector databases and relational databases

---

# 🧪 Example Output

## Query

What is Retrieval-Augmented Generation?

---

## Answer

Retrieval-Augmented Generation (RAG) improves LLM performance by retrieving relevant external context before generating responses, reducing hallucinations and improving factual grounding.

---

## Confidence

0.92

---

## Sources

- Document 1
- Document 2

---

# 📸 Demo Screenshots

## 🏠 Home Screen

![Home](assets/home_screen.png)

---

## 🔍 Sample Query & Output

![Output](assets/sample_output.png)

---

## 📚 Retrieved Context

![Context](assets/retrieved_context.png)

---

## 📄 JSON Export

![JSON](assets/json_export.png)

---

## 🕘 Run History

![History](assets/run_history.png)

---

# ⚙️ Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/smrutilale21/agentflow-api.git
cd agentflow-api
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🔐 Environment Setup

Create `.env` inside backend folder:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

---

# ▶️ Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```bash
cd frontend

streamlit run app.py
```

---

# 🌐 Deployment Architecture

| Layer | Platform |
|---|---|
| FastAPI Backend | Render |
| Streamlit Frontend | Streamlit Cloud |

---

# 🚀 Render Deployment

## Root Directory

```text
backend
```

---

## Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# 🚀 Streamlit Deployment

Add environment variable:

```text
BACKEND_URL=https://your-render-url.onrender.com/research
```

---

# ⚠️ Notes

- ChromaDB files are excluded from Git
- `.env` is ignored for security
- Logs are stored locally
- Frontend and backend are independently deployable
- Existing production logic remains unchanged

---

# 🔮 Future Improvements

- Hybrid retrieval
- Web search integration
- Conversational memory
- Evaluation metrics
- React frontend migration

---

# 📌 Conclusion

AgentFlow API demonstrates a production-oriented implementation of:

- multi-agent AI systems
- RAG pipelines
- FastAPI backend architecture
- structured outputs
- validation and retries
- scalable AI engineering

This project showcases strong understanding of modern AI system design and production-ready backend architecture.