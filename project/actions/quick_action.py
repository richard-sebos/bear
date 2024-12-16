# App: Bear
# Company: Sebos Technology
# Date: 
# Description: QuickAction class for performing quick scans in the Bear application.

from actions.base import Action
import subprocess
class QuickAction(Action):
    def command(self):
        return "quick"

    def description(self):
        return "Quickly validates the status of the target IP."

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "quick"
    
    def include_in_menu(self):
        return True  # Exclude from the menu

    def execute(self, args, id_mapping):
        """
        Perform a quick validation of a target IP.
        """
        target_idx = int(args[0]) - 1 if args else None
        if target_idx is not None and 0 <= target_idx < len(id_mapping):
            target_ip = id_mapping[target_idx + 1]
            try:
                result = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    print(f"{target_ip} is UP.")
                else:
                    print(f"{target_ip} is DOWN.")
            except Exception as e:
                print(f"Error executing QuickAction on {target_ip}: {e}")
            print(f"Quickly validating IP: {target_ip}")
        else:
            print("Invalid target selection. Provide a valid target index.")
