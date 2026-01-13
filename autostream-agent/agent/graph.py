from langgraph.graph.state import StateGraph
from langgraph.graph import END

from agent.state import AgentState
from agent.intents import detect_intent
from agent.rag import KnowledgeBase
from agent.tools import mock_lead_capture

kb = KnowledgeBase()

def chat_node(state: AgentState):
    user_input = state["history"][-1]

    # ✅ If already in lead mode, do not re-detect intent
    if state.get("lead_mode"):
        return state

    intent = detect_intent(user_input)
    state["intent"] = intent

    if intent == "greeting":
        reply = "Hello! How can I help you with AutoStream today?"

    elif intent == "pricing":
        reply = kb.get_pricing_info()

    elif intent == "high_intent":
        reply = "Great! I’ll just need a few details to get you started."
        state["lead_mode"] = True   # 🔥 ENTER LEAD MODE

    else:
        reply = "Could you please clarify what you're looking for?"

    state["history"].append(reply)
    return state


def lead_node(state: AgentState):
    if not state.get("name"):
        state["history"].append("May I know your name?")
        return state

    if not state.get("email"):
        state["history"].append("Please share your email address.")
        return state

    if not state.get("platform"):
        state["history"].append("Which platform do you create content on?")
        return state

    # Final step
    mock_lead_capture(state["name"], state["email"], state["platform"])
    state["history"].append(
        f"Thanks {state['name']}! Your free trial for AutoStream is being set up 🚀"
    )

    # mark lead flow complete
    state["lead_mode"] = False
    state["completed"] = True

    return state   # ✅ ALWAYS RETURN DICT



def router(state: AgentState):
    if state.get("lead_mode"):
        return "lead"
    return END


graph = StateGraph(AgentState)

graph.add_node("chat", chat_node)
graph.add_node("lead", lead_node)

graph.set_entry_point("chat")

graph.add_conditional_edges(
    "chat",
    router,
    {
        "lead": "lead",
        END: END
    }
)

graph.add_edge("lead", END)

app = graph.compile()

