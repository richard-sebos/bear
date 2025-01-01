from src.tasks.task import Task
from src.tasks.scheduler import TaskScheduler
from src.alerts.alert_manager import AlertManager

import json
import importlib

def load_tasks_from_json(file_path):
    """
    Load task definitions from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of task definitions.
    """
    with open(file_path, 'r') as file:
        task_data = json.load(file)
    return task_data

def load_class(class_name):
    """
    Dynamically load a class by name from the `tasks.classes` module.

    Args:
        class_name (str): The name of the class to load.

    Returns:
        type: The loaded class object.
    """
    # Assuming task classes are in the `tasks.classes` module
    module = importlib.import_module('tasks.classes')
    return getattr(module, class_name)

def main():
    """
    Main entry point for the dynamic task system.
    """
    print("Starting the dynamic task system with class-based execution...")

    # Load tasks from JSON
    tasks = load_tasks_from_json("tasks.json")

    for task_data in tasks:
        task_class = load_class(task_data['class_name'])
        task_instance = task_class(task_data['parameters'])
        print(f"Executing task: {task_data['description']}")
        task_instance.execute()

if __name__ == "__main__":
    main()
