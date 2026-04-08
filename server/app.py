from fastapi import FastAPI
from src.environment import MyEnvironment
from src.models import Action, Observation, StepResult

app = FastAPI()

@app.post("/reset")
def reset(task_id: str = "easy"):
    env = MyEnvironment()
    obs = env.reset(task_id)
    return obs.dict()

@app.post("/step")
def step(action: dict):
    env = MyEnvironment()
    result = env.step(Action(**action))
    return result.dict()

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()