from typing import List
from src.tasks.task import Task

class TaskScheduler:
    """
    Schedules and delegates task execution.

    Attributes:
        tasks (List[Task]): A list of scheduled tasks.
    """

    def __init__(self):
        """
        Initializes the TaskScheduler with an empty task list.
        """
        self.tasks: List[Task] = []

    def schedule_task(self, task: Task) -> None:
        """
        Adds a task to the schedule and invokes its scheduling logic.

        Args:
            task (Task): The task to be scheduled.
        """
        print(f"Scheduling task: {task.description}")
        self.tasks.append(task)
        task.schedule()

    def delegate_execution(self, task: Task) -> None:
        """
        Delegates the execution of a task.

        This method can be extended to integrate with execution managers.

        Args:
            task (Task): The task to be executed.
        """
        print(f"Delegating execution of task: {task.description}")
        # Integration with ExecutionManager would occur here.

    def list_scheduled_tasks(self) -> None:
        """
        Prints a list of all scheduled tasks.
        """
        if not self.tasks:
            print("No tasks scheduled.")
        else:
            print("Scheduled Tasks:")
            for task in self.tasks:
                print(f"- {task}")

    def __repr__(self) -> str:
        """
        Provides a string representation of the scheduler.

        Returns:
            str: A string describing the current state of the scheduler.
        """
        return f"TaskScheduler(tasks={len(self.tasks)})"
