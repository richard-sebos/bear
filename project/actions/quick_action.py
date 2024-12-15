# App: Bear
# Company: Sebos Technology
# Date: 
# Description: QuickAction class for performing quick scans in the Bear application.

from actions.base import Action
import subprocess

class QuickAction(Action):
    """Perform quick scans (e.g., ping)."""
    def execute(self, target):
        """Execute a quick scan on the target."""
        try:
            result = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                self.log(f"{target} is UP.")
            else:
                self.log(f"{target} is DOWN.")
        except Exception as e:
            self.log(f"Error executing QuickAction on {target}: {e}")

