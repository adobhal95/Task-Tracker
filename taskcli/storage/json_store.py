import os
import json
import logging
from pathlib import Path

FILENAME = Path("tasks.json")


def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        try:
            tasks: list[dict] = json.load(f)
            return tasks
        except json.JSONDecodeError:
            logging.error("Failed to decode JSON from file. Returning empty task list.")
            return []


def save_tasks(tasks: list[dict], print_format: str = "delete") -> None:
    """Save tasks to a JSON file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        if print_format in [
            "delete",
            "update",
            "mark-todo",
            "mark-done",
            "mark-in-progress",
        ]:
            print("tasks.json file updated.")
        else:
            print(f"Successfully saved {len(tasks)} tasks to {FILENAME}")
    except TypeError as e:
        logging.error(f"Serialization error: {e}")
        raise ValueError(f"Invalid task data format: {e}") from e
    except OSError as e:
        logging.error(f"File operation failed: {e}")
        raise IOError(f"Could not write to {FILENAME}: {e}") from e
