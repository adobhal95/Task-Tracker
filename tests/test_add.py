import unittest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace


class TestAddCommand(unittest.TestCase):
    def setUp(self):
        """Common test setup"""
        self.test_time = "2023-10-01T12:00:00"
        self.mock_now = MagicMock()
        self.mock_now.isoformat.return_value = self.test_time

    def create_mock_datetime(self):
        """Helper to mock datetime consistently"""
        return patch(
            "taskcli.commands.add.datetime", **{"now.return_value": self.mock_now}
        )

    @patch("taskcli.commands.add.save_tasks")
    @patch("taskcli.commands.add.load_tasks")
    @patch("taskcli.commands.add.Path")
    def test_create_task(self, mock_path, mock_load, mock_save):
        """Test task creation with empty task list"""
        # Setup
        mock_load.return_value = []
        args = SimpleNamespace(description="Test task")

        # Execute
        with self.create_mock_datetime():
            from taskcli.commands.add import create_task

            result = create_task(args)

        # Verify
        expected_task = {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "createdAt": self.test_time,
            "updatedAt": self.test_time,
        }

        self.assertEqual(result, expected_task)
        mock_save.assert_called_once_with([expected_task])
        mock_load.assert_called_once()

    @patch("taskcli.commands.add.save_tasks")
    @patch("taskcli.commands.add.load_tasks")
    @patch("taskcli.commands.add.Path")
    def test_id_increment_property(self, mock_path, mock_load, mock_save):
        """Test ID increments properly with existing tasks"""
        # Setup
        mock_load.return_value = [{"id": 1, "description": "First task"}]
        args = SimpleNamespace(description="Second task")

        # Execute
        with self.create_mock_datetime():
            from taskcli.commands.add import create_task

            result = create_task(args)

        # Verify
        self.assertEqual(result["id"], 2)
        self.assertEqual(result["description"], "Second task")
        mock_load.assert_called_once()
        mock_save.assert_called_once()

    def test_empty_description(self):
        """Test validation of empty description"""
        from taskcli.commands.add import create_task

        with self.assertRaises(ValueError):
            create_task(SimpleNamespace(description=""))
