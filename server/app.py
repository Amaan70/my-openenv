echo from fastapi import FastAPI > server\app.py
echo from src.environment import MyEnvironment >> server\app.py
echo from src.models import Action, Observation, StepResult >> server\app.py
echo. >> server\app.py
echo app = FastAPI() >> server\app.py
echo. >> server\app.py
echo @app.post("/reset") >> server\app.py
echo def reset(task_id: str = "easy"): >> server\app.py
echo     env = MyEnvironment() >> server\app.py
echo     obs = env.reset(task_id) >> server\app.py
echo     return obs.dict() >> server\app.py
echo. >> server\app.py
echo @app.post("/step") >> server\app.py
echo def step(action: dict): >> server\app.py
echo     env = MyEnvironment() >> server\app.py
echo     result = env.step(Action(**action)) >> server\app.py
echo     return result.dict() >> server\app.py
echo. >> server\app.py
echo def main(): >> server\app.py
echo     import uvicorn >> server\app.py
echo     uvicorn.run(app, host="0.0.0.0", port=7860) >> server\app.py