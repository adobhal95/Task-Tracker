from taskcli.storage.json_store import load_tasks
from datetime import datetime
from argparse import _SubParsersAction
import logging


def list_tasks(args):
    try:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return False
        if args.status == "todo":
            formatted_print_tasks(filter_task(tasks, "todo"))
        elif args.status == "done":
            formatted_print_tasks(filter_task(tasks, "done"))
        elif args.status == "in-progress":
            formatted_print_tasks(filter_task(tasks, "in-progress"))
        elif args.status is None:
            formatted_print_tasks(tasks)
            return
    except (FileExistsError, FileNotFoundError) as e:
        logging.error("File error ", e)
        print("No tasks found.")


def filter_task(tasks: list[dict], current_status):
    task_list = []
    for task in tasks:
        if task["status"] == current_status:
            task_list.append(task)
    return task_list


def formatted_print_tasks(tasks: list[dict]):
    print(
        f"\n{'ID':<5}{'Status':<12}{'Description':<40}{'Created At':<30}{'Updated At'}"
    )
    print("-" * 115)
    for task in sorted(tasks, key=lambda x: x["id"]):
        print(
            f"{task['id']:<5}{task['status']:<12}{task['description']:<40}{task['createdAt']:<30}{task['updatedAt']}"
        )


def configure_list_subparser(subparsers: _SubParsersAction):
    """
    Configure the add subparser for adding a new task.
    """
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "status",
        nargs="?",
        help="Filter by status (options)",
        type=str,
        choices=["todo", "done", "in-progress"],
    )
    list_parser.set_defaults(func=list_tasks)
