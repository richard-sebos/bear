import subprocess
import os
from datetime import datetime
from actions.base import Action

class SshCheckAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the SshCheckAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "ssh-check"

    def description(self):
        """Provide a description for the action."""
        return "Check SSH host keys, authentication methods, and algorithms using nmap."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute the SSH scan using nmap.
        Args:
            args (list): List of IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for SSH check.")
            return

        # Parse target and optional port
        target_id = args[0] if args else None
        port = args[1] if len(args) > 1 else 22

        if target_id and target_id.isdigit() and int(target_id) in id_mapping:
            target_ip = id_mapping[int(target_id)]
            print(f"Performing SSH check on IP: {target_ip}, Port: {port}")
            try:
                # Execute the nmap command
                result = subprocess.run(
                    ["nmap", f"-p {port}", "--script", "ssh-hostkey,ssh-auth-methods,ssh2-enum-algos", target_ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0:
                    print(f"SSH check completed for {target_ip}.")
                    self.log_results(target_ip, port, result.stdout)
                else:
                    print(f"Error scanning {target_ip}: {result.stderr}")
            except Exception as e:
                print(f"Error performing SSH check on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target ID.")

    def log_results(self, target, port, results):
        """
        Log the SSH check results to the notes directory.
        Args:
            target (str): The target IP address or hostname.
            port (int): The port number used for SSH check.
            results (str): The nmap results.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        notes_file = os.path.join(self.notes_dir, f"{target}_ssh_check_{timestamp}.md")

        with open(notes_file, "w") as file:
            file.write(f"# SSH Check Results for {target} (Port {port})\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"SSH check results logged in {notes_file}.")
