from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent.graph import app

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {
    "history": [],
    "intent": None,
    "lead_mode": False,
    "name": None,
    "email": None,
    "platform": None
}

class UserMessage(BaseModel):
    message: str

@api.post("/chat")
def chat(user: UserMessage):
    global state

    user_input = user.message.strip()

    # 🚫 If lead already completed, ignore further inputs
    if (
        state.get("name")
        and state.get("email")
        and state.get("platform")
        and not state.get("lead_mode")
    ):
        return {
            "reply": f"Thanks {state['name']}! Our team will reach out to you shortly 🚀"
        }

    # Capture lead details progressively
    if state["lead_mode"]:
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input

    # Store user message
    state["history"].append(user_input)

    # Invoke LangGraph
    state = app.invoke(state)

    return {"reply": state["history"][-1]}


