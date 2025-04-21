import unittest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from taskcli.commands.list import filter_task
from taskcli.storage.json_store import load_tasks


class TestListCommand(unittest.TestCase):
    def setUp(self):
        """Common test setup"""
        self.test_time = "2023-10-01T12:00:00"
        self.mock_now = MagicMock()
        self.mock_now.isoformat.return_value = self.test_time

    def create_mock_datetime(self):
        """Helper to mock datetime consistently"""
        return patch(
            "taskcli.commands.list.datetime", **{"now.return_value": self.mock_now}
        )

    @patch("taskcli.commands.list.load_tasks")
    def test_list_tasks(self, mock_load):
        """Test listing tasks with different statuses"""
        # Setup
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Task 1",
                "status": "todo",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            },
            {
                "id": 2,
                "description": "Task 2",
                "status": "done",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            },
            {
                "id": 3,
                "description": "Task 3",
                "status": "in-progress",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            },
        ]
        args1 = SimpleNamespace(status="todo")
        args2 = SimpleNamespace(status="in-progress")
        args3 = SimpleNamespace(status="done")

        # Execute
        with self.create_mock_datetime():
            result_todo = filter_task(mock_load.return_value, args1.status)
            result_done = filter_task(mock_load.return_value, args3.status)
            result_in_progress = filter_task(mock_load.return_value, args2.status)

        # Verify
        expected_result_todo = [
            {
                "id": 1,
                "description": "Task 1",
                "status": "todo",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            }
        ]
        expected_result_in_progress = [
            {
                "id": 3,
                "description": "Task 3",
                "status": "in-progress",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            }
        ]
        expected_result_done = [
            {
                "id": 2,
                "description": "Task 2",
                "status": "done",
                "createdAt": self.test_time,
                "updatedAt": self.test_time,
            }
        ]
        self.assertEqual(result_todo, expected_result_todo)
        self.assertEqual(result_done, expected_result_done)
        self.assertEqual(result_in_progress, expected_result_in_progress)
