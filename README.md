# Task-Tracker

A simple command-line tool to manage your tasks — add, update, delete, and track progress — stored in a local JSON file.

---
## Features
It's a CLI based simple task tracker which lets users to:
- ✅ Add tasks
- ✏️ Update task descriptions
- ❌ Delete tasks
- 🔄 Mark tasks as `in-progress` or `done`
- 📋 List tasks (all / by status)

All tasks are stored in *tasks.json* file:
```json
// tasks.json file structure
{
  "tasks": [
    {
      "id": 1,
      "description": "Buy groceries",
      "status": "todo",
      "createdAt": "2023-05-20T10:00:00",
      "updatedAt": "2023-05-20T10:00:00"
    }
  ],
```

Each task contains:
- id: Unique integer
- description: Task detail
- status: todo, in-progress, done
- createdAt, updatedAt: ISO timestamp strings

---
## Project Structure
```bash
task_tracker/
├── taskcli/                      # Python package directory
│   ├── __init__.py
│   ├── __main__.py               # CLI entry point
│   ├── commands/                 # Command-specific logic
│   │   ├── __init__.py
│   │   ├── add.py
│   │   ├── update.py
│   │   ├── delete.py
│   │   ├── mark.py
│   │   ├── list.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── json_store.py         # Handles reading/writing tasks to a JSON file             
├── pyproject.toml                # To make it installable via pip
├── README.md
    # Test cases for the application
```

## Requirements
1. Python 3.8+

## Installation
To install and run the Task-Tracker, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/adobhal95/Task-Tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Task-Tracker
    ```
3. Install:
    ```bash
    pip install -e .
    ```
4. Once installed, run:
    ```bash
    task_cli --help
    ```
5. [Optional]
  After step 2
    run the code as module
    ```
    python -m taskcli  [command] [options]
    ```
    - example:

      python -m taskcli list

      python -m taskcli add "Buy Books"
6. Run Tests
    ```bash
    python -m tests
    ```

## Usage
Run the application using the following command:
### Add a task
```
task-cli add "Buy groceries"
```

### Update a task
```
task-cli update 1 "Buy groceries and cook dinner"
```

### Delete a task
```
task-cli delete 1
```

### Mark as in progress / done
```
task-cli mark-in-progress 2
task-cli mark-done 2
```

### List all tasks
```
task-cli list
```

### List tasks by status
```
task-cli list done
task-cli list todo
task-cli list in-progress
```

