# App: Bear
# Company: Sebos Technology
# Date: 
# Description: ScanAction class for performing detailed network scans in the Bear application.
import subprocess
import os
from actions.base import Action
from datetime import datetime

class ScanAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the ScanAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "scan"

    def description(self):
        """Provide a description for the action."""
        return "Performs a detailed scan on the target IP and saves the results."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args, id_mapping):
        """
        Perform a detailed scan of a target IP.
        Args:
            args (list): List of target IDs or IPs.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for scanning.")
            return

        target_idx = int(args[0]) - 1 if args and args[0].isdigit() else None
        if target_idx is not None and 0 <= target_idx < len(id_mapping):
            target_ip = id_mapping[target_idx + 1]
            print(f"Performing a detailed scan on IP: {target_ip}")
            try:
                result = subprocess.run(
                    ["nmap", "-sT", target_ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0:
                    print(f"Scan completed for {target_ip}.")
                    self.log_scan_results(target_ip, result.stdout)
                else:
                    print(f"Error scanning {target_ip}:\n{result.stderr}")
            except Exception as e:
                print(f"Error executing ScanAction on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target index.")

    def log_scan_results(self, target, results):
        """
        Log the scan results to the notes directory.
        Args:
            target (str): The target IP address or hostname.
            results (str): The scan results.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(self.notes_dir, f"{target}_scan_{timestamp}.md")

        with open(notes_file, "w") as file:
            file.write(f"# Scan Results for {target}\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"Scan results logged in {notes_file}.")


