from abc import ABC, abstractmethod

class Report(ABC):
    """
    Abstract base class for reports.

    Attributes:
        content (str): The content of the report.
    """

    def __init__(self, content: str):
        """
        Initializes the report with its content.

        Args:
            content (str): The content of the report.
        """
        self.content = content

    @abstractmethod
    def format(self) -> str:
        """
        Formats the report content into a specific structure.

        Returns:
            str: The formatted report content.
        """
        pass

class MarkdownReport(Report):
    """
    Markdown implementation of a report.
    """

    def format(self) -> str:
        """
        Formats the report content as Markdown.

        Returns:
            str: The formatted Markdown report content.
        """
        return f"# Report\n\n{self.content}"
