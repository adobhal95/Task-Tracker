# Task-Tracker
Task tracker is a project used to track and manage your tasks.
It's a CLI based simple task tracker which lets users to:
  1.  Add, Update, and Delete tasks
  2.  Mark a task as in progress or done
  3.  List all tasks
  4.  List all tasks that are done
  5.  List all tasks that are not done
  6.  List all tasks that are in progress

All tasks are stored in *tasks.json* file.
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

## Project Structure
```bash
task-tracker-cli/
│
├── tasks.json          # JSON file storing all tasks (created automatically)
├── task_cli.py         # Main application file (Python example)
│
├── README.md           # Project documentation and usage instructions
└── tests/              # Optional test directory
    └── test_cli.py     # Test cases for the application
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
3. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate #Linux/Mac
   .venv\Scripts\activate #Windows
   pip install -r requirements.txt
   ```

## Usage
Run the application using the following command:
```bash
python main.py
```
Follow the on-screen instructions to manage your tasks.

