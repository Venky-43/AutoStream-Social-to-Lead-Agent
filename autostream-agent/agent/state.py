from typing import TypedDict, Optional

class AgentState(TypedDict):
    history: list
    intent: Optional[str]
    lead_mode: bool
    completed: bool
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]


