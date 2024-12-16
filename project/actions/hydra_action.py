from actions.base import Action
import subprocess
import os
from datetime import datetime

class HydraAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the HydraAction class with a directory for storing notes.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "hydra"

    def description(self):
        """Provide a description for the action."""
        return "Run Hydra brute force attack on a specified target."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Perform a Hydra brute force scan on the specified target.
        Args:
            args (list): List of target IDs or IPs.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for Hydra scanning.")
            return

        target_idx = int(args[0]) - 1 if args and args[0].isdigit() else None
        if target_idx is not None and 0 <= target_idx < len(id_mapping):
            target_ip = id_mapping[target_idx + 1]
            print(f"Starting Hydra scan on IP: {target_ip}")

            try:
                result = subprocess.run(
                    ["hydra", "-l", "admin", "-P", "passwords.txt", f"ssh://{target_ip}"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0:
                    print(f"Hydra scan completed for {target_ip}.")
                    self.log_scan_results(target_ip, result.stdout)
                else:
                    print(f"Error during Hydra scan for {target_ip}:{result.stderr}")
            except Exception as e:
                print(f"Error executing HydraAction on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target index.")

    def log_scan_results(self, target, results):
        """
        Log the Hydra scan results to the notes directory.
        Args:
            target (str): The target IP address or hostname.
            results (str): The scan results.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(self.notes_dir, f"{target}_hydra_{timestamp}.md")

        with open(notes_file, "w") as file:
            file.write(f"# Hydra Scan Results for {target}\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"Hydra scan results logged in {notes_file}.")
