import unittest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace


class TestUpdateCommand(unittest.TestCase):
    def setUp(self):
        """Common test setup"""
        self.test_time = "2023-10-01T12:00:00"
        self.mock_now = MagicMock()
        self.mock_now.isoformat.return_value = self.test_time

    def create_mock_datetime(self):
        """Helper to mock datetime consistently"""
        return patch(
            "taskcli.commands.update.datetime", **{"now.return_value": self.mock_now}
        )

    @patch("taskcli.commands.update.save_tasks")
    @patch("taskcli.commands.update.load_tasks")
    def test_update_task(self, mock_load, mock_save):
        """Test task update with existing task"""
        # Setup
        mock_load.return_value = [
            {
                "id": 1,
                "description": "First task",
                "status": "todo",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            }
        ]
        args = SimpleNamespace(id=1, description="Updated task")

        # Execute
        with self.create_mock_datetime():
            from taskcli.commands.update import update_task

            result = update_task(args)

        # Verify
        expected_task = {
            "id": 1,
            "description": "Updated task",
            "status": "todo",
            "createdAt": self.test_time,
            "updatedAt": self.test_time,
        }

        self.assertEqual(result, expected_task)
        mock_save.assert_called_once_with([expected_task])
        mock_load.assert_called_once()

    @patch("taskcli.commands.update.save_tasks")
    @patch("taskcli.commands.update.load_tasks")
    def test_update_task_not_found(self, mock_load, mock_save):
        """Test task update with non-existing task"""
        # Setup
        mock_load.return_value = [
            {
                "id": 1,
                "description": "First task",
                "status": "todo",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            }
        ]
        args = SimpleNamespace(id=2, description="Updated task", status="done")

        # Execute
        with self.create_mock_datetime():
            from taskcli.commands.update import update_task

            result = update_task(args)

        # Verify
        self.assertIsNone(result)
        mock_save.assert_not_called()
        mock_load.assert_called_once()

    @patch("taskcli.commands.update.save_tasks")
    @patch("taskcli.commands.update.load_tasks")
    def test_empty_description(self, mock_load, mock_save):
        """Test validation of empty description"""
        from taskcli.commands.update import update_task

        args = SimpleNamespace(id=1, description="", status="done")

        with self.assertRaises(ValueError):
            update_task(args)
