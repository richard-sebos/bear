from task import Task
from action_executor import ActionExecutor
from report_generator import ReportGenerator

class ExecutionManager:
    """
    Coordinates task execution and report generation.

    Attributes:
        action_executor (ActionExecutor): Responsible for executing task actions.
        report_generator (ReportGenerator): Responsible for generating reports for tasks.
    """

    def __init__(self):
        """
        Initializes the ExecutionManager with dependencies.
        """
        self.action_executor = ActionExecutor()
        self.report_generator = ReportGenerator()

    def execute(self, task: Task) -> None:
        """
        Executes a task and generates its report.

        Args:
            task (Task): The task to be executed.
        """
        print(f"Executing task: {task.id}")
        self.action_executor.execute_action(task)
        report = self.generate_report(task)
        print(report.format())

    def generate_report(self, task: Task):
        """
        Generates a report for the specified task.

        Args:
            task (Task): The task for which to generate the report.

        Returns:
            Report: A report object containing task results.
        """
        print(f"Generating report for task: {task.id}")
        return self.report_generator.generate_report(task)

    def __repr__(self) -> str:
        """
        Provides a string representation of the execution manager.

        Returns:
            str: A string describing the execution manager.
        """
        return "ExecutionManager()"
