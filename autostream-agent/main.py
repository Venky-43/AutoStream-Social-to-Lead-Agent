from agent.graph import app

state = {
    "history": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

print("AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # Capture lead info safely
    if state["intent"] == "high_intent":
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input

    state["history"].append(user_input)
    state = app.invoke(state)

    print("Agent:", state["history"][-1])
