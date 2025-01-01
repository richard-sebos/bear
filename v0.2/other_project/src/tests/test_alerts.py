import unittest
from unittest.mock import patch
from task import Task
from alert_manager import AlertManager

class TestAlertManager(unittest.TestCase):
    """
    Unit tests for the AlertManager class.
    """

    def setUp(self):
        """
        Set up a fresh instance of AlertManager for each test.
        """
        self.alert_manager = AlertManager()
        self.task = Task(task_id="123", description="Backup database")

    @patch('builtins.print')
    def test_send_alert(self, mock_print):
        """
        Test that send_alert logs and prints the alert message correctly.
        """
        reason = "Task failed due to timeout."
        self.alert_manager.send_alert(self.task, reason)

        expected_message = f"Alert for Task 123: {reason}"
        mock_print.assert_any_call(expected_message)
        mock_print.assert_any_call(f"LOG: {expected_message}")

    @patch('builtins.print')
    def test_monitor_task_triggers_alert(self, mock_print):
        """
        Test that monitor_task triggers an alert when conditions are met.
        """
        self.task.description = "This task may cause an error."
        self.alert_manager.monitor_task(self.task)

        expected_alert = "Alert for Task 123: Task description indicates a potential error."
        mock_print.assert_any_call(expected_alert)
        mock_print.assert_any_call(f"LOG: {expected_alert}")

    @patch('builtins.print')
    def test_monitor_task_no_alert(self, mock_print):
        """
        Test that monitor_task does not trigger an alert when conditions are not met.
        """
        self.task.description = "Normal task description."
        self.alert_manager.monitor_task(self.task)

        mock_print.assert_called_with(f"Monitoring task 123 for issues...")
        self.assertEqual(mock_print.call_count, 1)  # Only monitoring message printed

if __name__ == "__main__":
    unittest.main()
