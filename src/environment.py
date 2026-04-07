class MyEnvironment:
    def __init__(self):
        self.state = None
        self.step_count = 0
        self.max_steps = 20
        self.task = None
    
    def reset(self, task_id: str = "easy") -> Observation:
        """Initialize environment for a specific task."""
        self.task = self._load_task(task_id)
        self.state = self.task.initial_state()
        self.step_count = 0
        return self._get_observation()
    
    def step(self, action: Action) -> StepResult:
        """Execute action and return results."""
        self.step_count += 1
        
        # Apply action to state
        self.state = self._apply_action(action)
        
        # Calculate reward with partial progress
        reward = self._calculate_reward()
        
        # Check termination
        done = self._is_done()
        
        return StepResult(
            observation=self._get_observation(),
            reward=reward,
            done=done,
            info={"step": self.step_count}
        )
    
    def state(self) -> Dict[str, Any]:
        """Return current environment state."""
        return {
            "task_id": self.task.id,
            "step_count": self.step_count,
            "internal_state": self.state
        }
