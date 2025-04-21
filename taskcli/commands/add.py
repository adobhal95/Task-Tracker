from taskcli.storage.json_store import load_tasks, save_tasks
from datetime import datetime
from argparse import _SubParsersAction
from pathlib import Path


def create_task(args):
    """
    Create a new task with the given name and description.
    """
    TASKS_FILE = Path("tasks.json")
    tasks = load_tasks()
    id = max(task["id"] for task in tasks) + 1 if tasks else 1
    now = datetime.now().isoformat()
    if args.description == "":
        raise ValueError("Task description cannot be empty")
    new_task = {
        "id": id,
        "description": args.description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(
        f"""
    ✅ Task added successfully!
    ID: {id}
    Description: {args.description}
    Status: "todo"
    Created: {now}
    
    View all tasks in: {TASKS_FILE.resolve()}
    """
    )
    return new_task


def configure_add_subparser(subparsers: _SubParsersAction):
    """
    Configure the add subparser for adding a new task.
    """
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task", type=str)
    add_parser.set_defaults(func=create_task)
