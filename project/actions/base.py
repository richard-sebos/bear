# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Base class for all actions in the Bear application.

class Action:
    """Base class for all actions."""
    def execute(self, target):
        """Execute the action on a given target. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

    def log(self, message):
        """Log a message related to the action."""
        print(f"LOG: {message}")

