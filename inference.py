import os
import json

# Stubs to avoid NameError when Scaler loads the file
class MyEnvClient:
    def __init__(self, base_url): pass
    def reset(self, task_id): return None
    def step(self, action): return None
    def grade(self, task_id): return 0.0

def format_prompt(obs): return ""
def parse_action(text): return None

# Your original run_inference (kept, but won't run during validation)
# ... (keep your existing run_inference and __main__ block) ...

# The required server entry point
def app():
    from fastapi import FastAPI
    from src.environment import MyEnvironment
    
    api = FastAPI()
    env = MyEnvironment()
    
    @api.post("/reset")
    def reset(task_id: str = "easy"):
        obs = env.reset(task_id)
        return obs.dict()
    
    @api.post("/step")
    def step(action: dict):
        from src.models import Action
        result = env.step(Action(**action))
        return result.dict()
    
    return api