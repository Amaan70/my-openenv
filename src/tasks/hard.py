#!/usr/bin/env python3
import os
import sys
import json
from openai import OpenAI

API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
API_KEY = os.environ.get("API_KEY", "dummy")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

def extract_code(response: str) -> str:
    # Try to extract code between ```python ... ``` or just use whole response
    import re
    match = re.search(r"```python\n(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1)
    return response

def run_inference(env, task_id: str):
    print(f"[START] task={task_id}", flush=True)
    obs = env.reset(task_id)
    total_reward = 0.0
    steps = 0
    done = False

    while not done and steps < env.max_steps:
        # Build prompt from observation
        prompt = f"""
You are given a buggy Python code. Fix it so that it passes the test cases.
Buggy code:
```python
{obs.current_state['buggy_code']}