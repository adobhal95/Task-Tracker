from taskcli.storage.json_store import load_tasks, save_tasks
from datetime import datetime
from argparse import _SubParsersAction
import logging


def mark_task_todo(args):
    try:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return False
        task_id = args.id
        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "todo":
                    print(f"Task with ID {task_id} is already marked as todo.")
                    return
                task["status"] = "todo"
                # update the task file
                save_tasks(tasks)
                print(
                    f"""
                    Task_ID:{task_id}.
                    Task marked as todo successfully."""
                )
                return
        print(f"Task with ID {task_id} not found.")
    except (FileExistsError, FileNotFoundError) as e:
        logging.error("File error ", e)
        print("Error accessing task data.")
        return False


def configure_mark_task_todo(subparsers: _SubParsersAction):
    """
    Configure the add subparser for adding a new task.
    """
    mark = subparsers.add_parser("mark-todo", help="update status of task to todo")
    mark.add_argument("id", type=int, help="ID of task to update")
    mark.set_defaults(func=mark_task_todo)
