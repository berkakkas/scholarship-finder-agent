from langgraph.graph import StateGraph, END
from typing import TypedDict

from rag import search_documents
from tools import web_search    
class AgentState(TypedDict):
    query: str
    context: str
    web_context: str
    answer: str
def decide_tool(state):
    query = state["query"].lower()

    if "latest" in query or "deadline" in query or "2026" in query:
        return "both"

    return "rag"



def rag_node(state):
    context = search_documents(state["query"])

    return {
        "context": context
    }

def web_node(state):
    context = web_search(state["query"])

    return {
        "context": context
    }
def both_node(state):
    rag_context = search_documents(state["query"])
    web_context = web_search(state["query"])

    combined = f"""
RAG RESULTS:
{rag_context}

WEB SEARCH RESULTS:
{web_context}
"""

    return {
        "context": combined
    }

def final_node(state):
    return {
        "answer": f"""
========================================
   SCHOLARSHIP FINDER RESULTS
========================================

Recommended Scholarships:

{state['context']}

----------------------------------------
These scholarships may match the student's profile.
Please verify eligibility and deadlines.
========================================
"""
    }

graph = StateGraph(AgentState)

graph.add_node("rag", rag_node)
graph.add_node("web", web_node)
graph.add_node("both", both_node)
graph.add_node("final", final_node)

graph.set_conditional_entry_point(
    decide_tool,
    {
        "rag": "rag",
        "both": "both"
    }
)

graph.add_edge("rag", "final")
graph.add_edge("web", "final")
graph.add_edge("both", "final")
graph.add_edge("final", END)
app_graph = graph.compile()