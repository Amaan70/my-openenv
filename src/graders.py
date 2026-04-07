class TaskGrader:
    def grade(self, trajectory: List[StepResult], final_state: Dict) -> float:
        """
        Grade agent performance on a task.
        Returns score between 0.0 and 1.0.
        """
        score = 0.0
        
        # Correctness (0.0–0.6)
        correctness = self._evaluate_correctness(final_state)
        score += correctness * 0.6
        
        # Completeness (0.0–0.25)
        completeness = self._evaluate_completeness(final_state)
        score += completeness * 0.25
        
        # Efficiency (0.0–0.15)
        efficiency = self._evaluate_efficiency(trajectory)
        score += efficiency * 0.15
        
        return score
