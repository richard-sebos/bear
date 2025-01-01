from report import Report, MarkdownReport
from task import Task

class ReportGenerator:
    """
    Generates reports for executed tasks.
    """

    def generate_report(self, task: Task) -> Report:
        """
        Generates a report for the specified task.

        Args:
            task (Task): The task for which the report is generated.

        Returns:
            Report: A report object containing the task's details.
        """
        print(f"Generating report for task {task.id}")
        content = f"Task ID: {task.id}\nDescription: {task.description}\nStatus: Completed"
        return MarkdownReport(content=content)

    def __repr__(self) -> str:
        """
        Provides a string representation of the ReportGenerator.

        Returns:
            str: A string describing the ReportGenerator.
        """
        return "ReportGenerator()"
