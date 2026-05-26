from langgraph.graph import END, START, StateGraph

from nodes import planner_node, research_node, retriever_node
from state import ResearchState


def build_graph():
    builder = StateGraph(ResearchState)

    builder.add_node("planner", planner_node)
    builder.add_node("retriever", retriever_node)
    builder.add_node("researcher", research_node)

    builder.add_edge(START, "planner")
    builder.add_edge("planner", "retriever")
    builder.add_edge("retriever", "researcher")
    builder.add_edge("researcher", END)

    return builder.compile()
