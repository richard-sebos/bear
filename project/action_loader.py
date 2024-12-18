import importlib
import os
import inspect
from actions.base import Action

def load_actions(actions_dir="actions"):
    """
    Dynamically load action classes from Python files in the specified directory.
    
    Args:
        actions_dir (str): The directory containing the action modules.

    Returns:
        list: A list of action class instances.
    """
    actions = []
    for filename in os.listdir(actions_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f"{actions_dir}.{module_name}")
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Action) and obj is not Action:
                        actions.append(obj())
            except Exception as e:
                print(f"Error loading module {module_name}: {e}")
    return actions
