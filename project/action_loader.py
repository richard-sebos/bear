import importlib
import os
import inspect
from actions.base import Action

def load_actions(actions_dir="actions"):
    """
    Dynamically load all action classes from the specified directory.

    Args:
        actions_dir (str): Path to the directory containing action files.

    Returns:
        list: A list of instantiated action classes.
    """
    actions = []

    # Ensure the actions directory exists
    if not os.path.isdir(actions_dir):
        print(f"Error: The actions directory '{actions_dir}' does not exist.")
        return actions

    # Iterate over all Python files in the actions directory
    for filename in os.listdir(actions_dir):
        if filename.endswith(".py") and filename != "base.py":
            module_name = f"{actions_dir}.{filename[:-3]}"
            try:
                # Dynamically import the module
                module = importlib.import_module(module_name)

                # Find classes in the module that inherit from Action
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Action) and obj is not Action:
                        actions.append(obj())  # Instantiate the class

            except Exception as e:
                print(f"Error loading action from {filename}: {e}")

    return actions
