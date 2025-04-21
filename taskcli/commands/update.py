from taskcli.storage.json_store import load_tasks, save_tasks
from datetime import datetime
from argparse import _SubParsersAction
import logging


def update_task(args):
    try:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return False
        task_id = args.id
        desc = args.description
        if desc.strip() == "":
            raise ValueError("Description cannot be empty.")
        for task in tasks:
            if task["id"] == task_id:
                task["id"] = task_id
                task["description"] = desc
                # update the task file
                save_tasks(tasks)
                print(f"Task with ID {task_id} updated successfully.")
                return task
        print(f"Task with ID {task_id} not found.")
    except (FileExistsError, FileNotFoundError) as e:
        logging.error("File error ", e)
        print("Error accessing task data.")
        return False


def configure_update_subparser(subparsers: _SubParsersAction):
    """
    Configure the add subparser for adding a new task.
    """
    update_parser = subparsers.add_parser("update", help="update a task by id")
    update_parser.add_argument("id", type=int, help="ID of task to update")
    update_parser.add_argument(
        "description", type=str, help="description of task to be updated with"
    )
    update_parser.set_defaults(func=update_task)
