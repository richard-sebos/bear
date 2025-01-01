from src.tasks.task import Task
from src.alerts.logger import Logger

class AlertManager:
    """
    Manages alerts based on task execution and system events.
    
    Attributes:
        logger (Logger): Logger instance for logging alerts.
    """

    def __init__(self):
        """
        Initializes the AlertManager with a Logger instance.
        """
        self.logger = Logger()

    def send_alert(self, task: Task, reason: str) -> None:
        """
        Sends an alert related to a specific task.

        Args:
            task (Task): The task associated with the alert.
            reason (str): The reason for the alert.
        """
        alert_message = f"Alert for Task {task.id}: {reason}"
        print(alert_message)
        self.logger.log(alert_message)

    def monitor_task(self, task: Task) -> None:
        """
        Monitors a task for potential issues and triggers alerts as needed.

        Args:
            task (Task): The task to monitor.
        """
        # Example logic for monitoring
        print(f"Monitoring task {task.id} for issues...")
        # Placeholder for real monitoring and alerting conditions
        if "error" in task.description.lower():
            self.send_alert(task, "Task description indicates a potential error.")

    def __repr__(self) -> str:
        """
        Provides a string representation of the AlertManager.

        Returns:
            str: A string describing the AlertManager.
        """
        return "AlertManager()"
