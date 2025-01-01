import unittest
from task import Task

class TestTask(unittest.TestCase):
    """
    Unit tests for the Task class.
    """

    def test_task_initialization(self):
        """
        Test that a Task is correctly initialized.
        """
        task = Task(task_id="123", description="Backup database")
        self.assertEqual(task.id, "123")
        self.assertEqual(task.description, "Backup database")

    def test_task_schedule(self):
        """
        Test the scheduling method of the Task class.
        """
        task = Task(task_id="123", description="Backup database")
        # Capture printed output
        with self.assertLogs() as log:
            task.schedule()
        self.assertIn("Task 123 has been scheduled.", log.output[0])

    def test_task_repr(self):
        """
        Test the string representation of the Task class.
        """
        task = Task(task_id="123", description="Backup database")
        expected_repr = "Task(id=123, description=Backup database)"
        self.assertEqual(repr(task), expected_repr)

if __name__ == "__main__":
    unittest.main()
