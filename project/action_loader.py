# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Module for dynamically loading action classes from the actions directory.

import os
import importlib

def load_actions():
    """Dynamically load action classes from the actions/ directory."""
    actions = []
    action_dir = os.path.join(os.path.dirname(__file__), 'actions')

    for file in os.listdir(action_dir):
        if file=='list_action.py':
            continue
        if file.endswith('.py') and file != '__init__.py':
            module_name = f'actions.{file[:-3]}'
            module = importlib.import_module(module_name)
            for attr in dir(module):
                cls = getattr(module, attr)
                if isinstance(cls, type) and hasattr(cls, 'execute'):
                    actions.append(cls())
    return actions

