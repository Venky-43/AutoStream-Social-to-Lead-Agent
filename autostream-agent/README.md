# AutoStream Social-to-Lead Agent

## How to Run
1. Create a virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

## Architecture Explanation
This project uses LangGraph to manage conversation flow and state. LangGraph
was chosen because it allows explicit control over multi-step agent workflows.
State is preserved across multiple turns using a shared AgentState object.

The RAG system reads from a local JSON knowledge base to ensure factual,
hallucination-free responses. Tool execution is gated strictly after collecting
all lead details.

