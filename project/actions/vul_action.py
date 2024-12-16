import subprocess
import os
from actions.base import Action
from datetime import datetime

class VulAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the VulAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "vul"

    def description(self):
        """Provide a description for the action."""
        return "Perform vulnerability scans using nmap scripts."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute the vulnerability scan.
        Args:
            args (list): List of IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for vulnerability scanning.")
            return

        # Resolve IDs or IPs from the arguments
        targets = []
        for arg in args:
            if arg.isdigit() and int(arg) in id_mapping:
                targets.append(id_mapping[int(arg)])
            else:
                targets.append(arg)

        for target in targets:
            try:
                print(f"Starting vulnerability scan on {target}...")
                result = subprocess.run(
                    ["nmap", "-sV", "--script=vuln", target],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                if result.returncode == 0:
                    print(f"Scan completed for {target}.")
                    self.log_findings(target, result.stdout)
                else:
                    print(f"Error scanning {target}: {result.stderr}")

            except Exception as e:
                print(f"Error performing scan on {target}: {e}")

    def log_findings(self, target, findings):
        """
        Log the findings to the notes directory.
        Args:
            target (str): The target IP address or hostname.
            findings (str): The scan results.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(self.notes_dir, f"{target}_vuln_{timestamp}.md")

        with open(notes_file, "w") as file:
            file.write(f"# Vulnerability Scan Results for {target}\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Findings\n")
            file.write(findings)

        print(f"Findings logged in {notes_file}.")
