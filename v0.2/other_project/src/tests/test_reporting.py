import unittest
from report import MarkdownReport
from report_generator import ReportGenerator
from task import Task

class TestMarkdownReport(unittest.TestCase):
    """
    Unit tests for the MarkdownReport class.
    """

    def test_markdown_report_format(self):
        """
        Test that the Markdown report is formatted correctly.
        """
        content = "This is a test report."
        report = MarkdownReport(content)
        expected_output = "# Report\n\nThis is a test report."
        self.assertEqual(report.format(), expected_output)

class TestReportGenerator(unittest.TestCase):
    """
    Unit tests for the ReportGenerator class.
    """

    def test_generate_report(self):
        """
        Test that the ReportGenerator generates a report correctly.
        """
        task = Task(task_id="123", description="Backup database")
        generator = ReportGenerator()
        report = generator.generate_report(task)

        self.assertIsInstance(report, MarkdownReport)
        expected_content = "Task ID: 123\nDescription: Backup database\nStatus: Completed"
        self.assertEqual(report.content, expected_content)

if __name__ == "__main__":
    unittest.main()
