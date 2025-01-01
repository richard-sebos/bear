from typing import Any
from task import Task

class ActionExecutor:
    """
    Executes actions on behalf of tasks.
    """

    def execute_action(self, task: Task) -> None:
        """
        Executes an action for the given task.

        Args:
            task (Task): The task to be executed.
        """
        print(f"Executing action for task {task.id}: {task.description}")
        # Simulated action execution logic
        result = self.perform_action(task)
        print(f"Task {task.id} completed with result: {result}")

    def perform_action(self, task: Task) -> Any:
        """
        Performs the actual logic for the action execution.

        Args:
            task (Task): The task being executed.

        Returns:
            Any: The result of the action.
        """
        # Placeholder for action execution logic
        return f"Action for {task.description} executed successfully"

    def __repr__(self) -> str:
        """
        Provides a string representation of the ActionExecutor.

        Returns:
            str: A string describing the ActionExecutor.
        """
        return "ActionExecutor()"
