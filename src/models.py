from pydantic import BaseModel
from typing import Dict, Any, List

class Observation(BaseModel):
    task_id: str
    current_state: Dict[str, Any]
    available_actions: List[str]
    context: str
    step_count: int
    max_steps: int

class Action(BaseModel):
    action_type: str   # "submit_code"
    parameters: Dict[str, Any]  # {"code": "def solution()..."}

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Dict[str, Any]