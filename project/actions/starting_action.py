
from actions.base import Action
import subprocess
class StartingAction:

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "start"

    def description(self):
        """Provide a description for the action."""
        return "Displays the list of active IP addresses found."

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "restart"
        
    def include_in_menu(self):
        return False  # Exclude from the menu

    def execute(self, target):
        """Execute a quick scan on the target."""
        try:
            result = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return "UP"
            else:
                return "DOWN"
        except Exception as e:
            print(f"Error executing StartingAction on {target}: {e}")
