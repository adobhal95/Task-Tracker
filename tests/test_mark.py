import unittest
from unittest.mock import patch, MagicMock
from taskcli.storage.json_store import load_tasks, save_tasks


class TestMarkTask(unittest.TestCase):
    def setUp(self):
        """Common test setup"""
        self.test_time = "2023-10-01T12:00:00"
        self.mock_now = MagicMock()
        self.mock_now.isoformat.return_value = self.test_time
        self.task_id = 1
        self.tasks = [
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

    @patch("taskcli.commands.mark_done.load_tasks")
    @patch("taskcli.commands.mark_done.save_tasks")
    def test_mark_task_done(self, mock_save, mock_load):
        """Test marking a task as done"""
        # Setup
        mock_load.return_value = self.tasks
        args = MagicMock()
        args.id = 1

        # Execute
        with patch(
            "taskcli.commands.mark_done.datetime", **{"now.return_value": self.mock_now}
        ):
            from taskcli.commands.mark_done import mark_task_done

            mark_task_done(args)

        # Verify
        updated_tasks = mock_save.call_args[0][0]
        self.assertEqual(len(updated_tasks), 3)
        self.assertEqual(updated_tasks[0]["status"], "done")
        self.assertEqual(updated_tasks[0]["updatedAt"], self.test_time)

    @patch("taskcli.commands.mark_todo.load_tasks")
    @patch("taskcli.commands.mark_todo.save_tasks")
    def test_mark_task_todo(self, mock_save, mock_load):
        """Test marking a task as done"""
        # Setup
        mock_load.return_value = self.tasks
        args = MagicMock()
        args.id = 2

        # Execute
        with patch(
            "taskcli.commands.mark_todo.datetime", **{"now.return_value": self.mock_now}
        ):
            from taskcli.commands.mark_todo import mark_task_todo

            mark_task_todo(args)

        # Verify
        updated_tasks = mock_save.call_args[0][0]
        self.assertEqual(len(updated_tasks), 3)
        self.assertEqual(updated_tasks[0]["status"], "todo")
        self.assertEqual(updated_tasks[0]["updatedAt"], self.test_time)

    @patch("taskcli.commands.mark_in_progress.load_tasks")
    @patch("taskcli.commands.mark_in_progress.save_tasks")
    def test_mark_in_progress(self, mock_save, mock_load):
        """Test marking a task as done"""
        # Setup
        mock_load.return_value = self.tasks
        args = MagicMock()
        args.id = 1

        # Execute
        with patch(
            "taskcli.commands.mark_in_progress.datetime",
            **{"now.return_value": self.mock_now}
        ):
            from taskcli.commands.mark_in_progress import mark_task_in_progress

            mark_task_in_progress(args)

        # Verify
        updated_tasks = mock_save.call_args[0][0]
        self.assertEqual(len(updated_tasks), 3)
        self.assertEqual(updated_tasks[0]["status"], "in-progress")
        self.assertEqual(updated_tasks[0]["updatedAt"], self.test_time)
