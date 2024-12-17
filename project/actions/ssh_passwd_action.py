import subprocess
import os
from datetime import datetime
from actions.base import Action

class SshPasswdAction(Action):
    def __init__(self, notes_dir="notes", data_dir="data"):
        """
        Initialize the SshPasswdAction class.
        """
        self.notes_dir = notes_dir
        self.data_dir = data_dir
        self.password_file = os.path.join(self.data_dir, "passwords.txt")
        self.user_file = os.path.join(self.data_dir, "users.txt")

        # Ensure required directories exist
        for directory in [self.notes_dir, self.data_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "ssh-passwd"

    def description(self):
        """Provide a description for the action."""
        return "Use Hydra to perform SSH password cracking using user and password files."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute SSH password cracking using Hydra.
        Args:
            args (list): List of IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for SSH password cracking.")
            return

        target_id = args[0] if args else None
        if target_id and target_id.isdigit() and int(target_id) in id_mapping:
            target_ip = id_mapping[int(target_id)]
            print(f"Running Hydra SSH password cracking on IP: {target_ip}")

            if not os.path.isfile(self.password_file) or not os.path.isfile(self.user_file):
                print("Error: Missing user or password file in 'data' directory.")
                return

            try:
                output_file = self.run_hydra(target_ip)
                print(f"Hydra SSH password cracking completed for {target_ip}.")
                print(f"Results saved to: {output_file}")
            except Exception as e:
                print(f"Error running Hydra SSH password cracking on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target ID.")

    def run_hydra(self, target_ip):
        """
        Run Hydra to perform SSH password cracking.
        Args:
            target_ip (str): Target IP address.
        Returns:
            str: Path to the results file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(self.notes_dir, f"{target_ip}_hydra_ssh_{timestamp}.md")

        try:
            print("Starting Hydra SSH password cracking...")
            result = subprocess.run(
                [
                    "hydra",
                    "-L", self.user_file,
                    "-P", self.password_file,
                    target_ip, "ssh"
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode == 0:
                self.log_results(output_file, result.stdout)
            else:
                print(f"Error during Hydra execution: {result.stderr}")
                self.log_results(output_file, result.stderr)

        except Exception as e:
            print(f"Error executing Hydra: {e}")
        
        return output_file

    def log_results(self, output_file, results):
        """
        Log the Hydra results to a file.
        Args:
            output_file (str): Path to the results file.
            results (str): Hydra output.
        """
        with open(output_file, "w") as file:
            file.write(f"# Hydra SSH Password Cracking Results\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"Results logged to: {output_file}")
