from langgraph.graph import StateGraph

def agent_router():
    graph = StateGraph(dict)

    graph.add_node("base_agent",lambda state:state)
    graph.entry_point("base_agent")
    graph.set_finish_point("base_agent")

    return graph.compile()