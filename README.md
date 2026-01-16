# BHARAT AI
# MULTI-AGENT LLM SYSTEM FOR RESUME ANALYSIS AND CAREER ASSISTANCE

---

## OVERVIEW
Bharat AI is an **LLM-driven multi-agent system** designed to assist users with **resume analysis, resume comparison, interview preparation, and ATS-style evaluation**.  
The system is built using **LangChain for agent orchestration**, a **FastAPI REST backend**, and a **React frontend**.

The project focuses on **LLM-based reasoning, system design, and end-to-end AI application architecture**, rather than model training.

---

## KEY FEATURES
- Resume Question Answering using contextual LLM reasoning  
- Resume Comparison for a given role  
- Interviewer-style Question Generation  
- ATS-style Resume Scoring and Feedback  
- General Conversational Chat using LLMs  
- Role Extraction from Unstructured Job Descriptions  

---

## SYSTEM ARCHITECTURE

### LLM-DRIVEN MULTI-AGENT WORKFLOW
The application follows a **multi-agent architecture**, where each agent is responsible for a specific task:

- Resume QA Agent – answers questions using resume context  
- Resume Comparison Agent – compares two resumes against role requirements  
- ATS Scoring Agent – evaluates resumes using structured prompt workflows  
- Interviewer Agent – generates role-specific interview questions  
- General Chat Agent – handles open-ended user queries  

Agents are orchestrated using **LangChain prompt chains**, enabling **structured, modular, and deterministic workflows**.

---

## NLP AND LLM USAGE
The system applies **Natural Language Processing (NLP)** through **Large Language Models (LLMs)** for:

- Understanding unstructured resume text  
- Skill and role extraction from job descriptions  
- Semantic reasoning over resume content  
- Natural language question answering and generation  

No classical NLP models are trained; the project relies on **LLM-based NLP reasoning**.

---

## RETRIEVAL AND CONTEXT HANDLING (RAG-STYLE)
- Resume content is parsed and injected into prompts  
- A **RAG-style retrieval workflow** is implemented to validate context grounding  
- **Simulated text embeddings** are used to demonstrate retrieval logic and system flow  

This design prioritizes **architecture clarity and reasoning flow** over vector database optimization.

---

## TECH STACK

### BACKEND
- Python  
- FastAPI (REST APIs)  
- LangChain (LLM orchestration)  

### FRONTEND
- React  
- Resume upload and chat-based user interface  

### TOOLS
- Git  
- VS Code  

---

## APPLICATION FLOW
1. User uploads resume(s)  
2. User selects analysis type (QA, comparison, ATS scoring, interview preparation)  
3. Request is routed to the relevant LLM agent  
4. Agent processes input using structured prompt workflows  
5. LLM generates a context-aware response  
6. Response is returned to the frontend  

---

## DESIGN CHOICES AND LIMITATIONS
- The system focuses on **LLM orchestration and reasoning pipelines** rather than training or fine-tuning models, in order to emphasize 
  application-level AI system design      
- Resume context is injected directly into prompts, and a **RAG-style workflow with simulated embeddings** is used to demonstrate retrieval and 
  grounding logic  
- LLM interactions are subject to **API rate limits and usage constraints**, which influenced prompt execution strategies and request batching  
- The application uses **session-based processing** without persistent storage to keep the architecture lightweight and modular  
- The project is designed as a **functional prototype**, prioritizing clarity, modularity, and learning value over production-scale deployment  

---

## FUTURE IMPROVEMENTS
- Integration with a **production-grade vector database (Chroma)** for efficient semantic retrieval  
- Implementation of **persistent conversation memory** to enable multi-session context retention  
- Enhancement of **ATS scoring** using a hybrid **keyword-matching and LLM-based evaluation** approach  
- Addition of **user authentication and session-based history tracking**  
- Development of **structured resume parsing pipelines** for consistent and schema-driven data extraction  
- Improved **storage and system scalability** to support larger resume datasets and concurrent users  


---

## AUTHOR
Kartikey Ahuja  
B.Tech, NIT Patna  
AI / ML Aspirant  

---

## PROJECT HIGHLIGHTS
- LLM-driven multi-agent architecture  
- LangChain-based orchestration  
- FastAPI and React full-stack integration  
- Emphasis on real-world AI application design  

