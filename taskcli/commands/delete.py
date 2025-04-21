from taskcli.storage.json_store import load_tasks, save_tasks
from datetime import datetime
from argparse import _SubParsersAction
import logging


def delete_task(args):
    try:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return False
        task_id = args.id
        confirm = input(f"Are you sure you want to delete task {task_id}? [y/N] ")
        if confirm.lower() != "y":
            print("Deletion cancelled")
            return False
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                # update the task file
                save_tasks(tasks)
                print(f"Task with ID {task_id} deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")
    except (FileExistsError, FileNotFoundError) as e:
        logging.error("File error ", e)
        print("Error accessing task data.")
        return False


def configure_delete_subparser(subparsers: _SubParsersAction):
    """
    Configure the add subparser for adding a new task.
    """
    delete_parser = subparsers.add_parser("delete", help="delete a task by id")
    delete_parser.add_argument("id", type=int, help="ID of task to delete")
    delete_parser.set_defaults(func=delete_task)
