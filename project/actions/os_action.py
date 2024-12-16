import subprocess
import os
from actions.base import Action
from datetime import datetime

class OsAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the OsAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "os"

    def description(self):
        """Provide a description for the action."""
        return "Detect the operating system of a target IP."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute the OS detection action.
        Args:
            args (list): List of IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for OS detection.")
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
                print(f"Starting OS detection on {target}...")
                result = subprocess.run(
                    ["nmap", "-O", target],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                if result.returncode == 0:
                    print(f"OS detection completed for {target}.")
                    self.log_os_details(target, result.stdout)
                else:
                    print(f"Error detecting OS for {target}: {result.stderr}")

            except Exception as e:
                print(f"Error performing OS detection on {target}: {e}")

    def log_os_details(self, target, os_details):
        """
        Log the OS details to the notes directory.
        Args:
            target (str): The target IP address or hostname.
            os_details (str): The OS detection results.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(self.notes_dir, f"{target}_os_{timestamp}.md")

        with open(notes_file, "w") as file:
            file.write(f"# OS Detection Results for {target}\n")
            file.write(f"**Detection Date:** {datetime.now().isoformat()}\n\n")
            file.write("## OS Details\n")
            file.write(os_details)

        print(f"OS details logged in {notes_file}.")
