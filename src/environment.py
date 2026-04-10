import re
from typing import Dict, Any, List, Optional
from src.models import Observation, Action, StepResult

class CodeDebugEnvironment:
    def __init__(self):
        self.task_id = None
        self.buggy_code = None
        self.test_cases = None
        self.current_code = None
        self.step_count = 0
        self.max_steps = 5
        self.submitted = False
        self.score = 0.0

    def reset(self, task_id: str) -> Observation:
        self.task_id = task_id
        self.step_count = 0
        self.submitted = False
        # Load task from tasks module
        if task_id == "easy":
            from src.tasks.easy import buggy_code, test_cases
        elif task_id == "medium":
            from src.tasks.medium import buggy_code, test_cases
        else:
            from src.tasks.hard import buggy_code, test_cases
        self.buggy_code = buggy_code
        self.test_cases = test_cases
        self.current_code = buggy_code
        return self._get_observation()

    def step(self, action: Action) -> StepResult:
        self.step_count += 1
        reward = 0.0
        done = False
        info = {}

        if action.action_type == "submit_code":
            self.current_code = action.parameters.get("code", self.buggy_code)
            self.submitted = True
            # Grade the submitted code
            from src.graders import grade_code
            self.score = grade_code(self.current_code, self.test_cases)
            reward = self.score
            done = True
            info = {"score": self.score}
        else:
            # Invalid action
            reward = -0.1
            done = self.step_count >= self.max_steps

        return StepResult(
            observation=self._get_observation(),
            reward=reward,
            done=done,
            info=info
        )

    def _get_observation(self) -> Observation:
        return Observation(
            task_id=self.task_id,
            current_state={
                "buggy_code": self.buggy_code,
                "current_code": self.current_code,
                "submitted": self.submitted
            },
            available_actions=["submit_code"],
            context=f"Fix the bug in the code. Expected to pass test cases: {self.test_cases}",
            step_count=self.step_count,
            max_steps=self.max_steps
        )

# Alias for existing code (if any other file expects MyEnvironment)
MyEnvironment = CodeDebugEnvironment