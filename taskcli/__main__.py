import argparse
from taskcli.commands import add
from taskcli.commands import list
from taskcli.commands import delete
from taskcli.commands import update
from taskcli.commands import mark_done, mark_in_progress, mark_todo


def main():
    parser = argparse.ArgumentParser(
        prog="task-cli", description="A simple Task Tracker CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add.configure_add_subparser(subparsers)
    list.configure_list_subparser(subparsers)
    delete.configure_delete_subparser(subparsers)
    update.configure_update_subparser(subparsers)
    mark_done.configure_mark_task_todo(subparsers)
    mark_todo.configure_mark_task_todo(subparsers)
    mark_in_progress.configure_mark_task_todo(subparsers)

    args = parser.parse_args()

    # Execute the command if function exists
    if hasattr(args, "func"):
        result = args.func(args)
    else:
        print("Error: No command function found")


if __name__ == "__main__":
    main()
