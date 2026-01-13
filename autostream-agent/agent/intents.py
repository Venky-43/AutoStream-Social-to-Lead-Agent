def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    high_intent_keywords = [
        "i want to try",
        "i want to buy",
        "sign up",
        "get started",
        "subscribe",
        "start using",
        "try the pro",
        "buy the pro"
    ]

    pricing_keywords = [
        "price",
        "pricing",
        "cost",
        "plans",
        "plan details"
    ]

    greetings = ["hi", "hello", "hey"]

    # ✅ HIGH INTENT FIRST (IMPORTANT)
    if any(phrase in text for phrase in high_intent_keywords):
        return "high_intent"

    if any(word in text for word in pricing_keywords):
        return "pricing"

    if any(word in text for word in greetings):
        return "greeting"

    return "unknown"

