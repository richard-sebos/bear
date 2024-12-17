import subprocess
import os
from datetime import datetime
from actions.base import Action

class SshAuditAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the SshAuditAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "ssh-audit"

    def description(self):
        """Provide a description for the action."""
        return "Run SSH-Audit to assess the security of SSH configurations."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute the SSH audit using the ssh-audit tool.
        Args:
            args (list): List of target IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for SSH audit.")
            return

        target_id = args[0] if args else None
        if target_id and target_id.isdigit() and int(target_id) in id_mapping:
            target_ip = id_mapping[int(target_id)]
            print(f"Running SSH audit on IP: {target_ip}")
            try:
                output_file = self.run_ssh_audit(target_ip)
                print(f"SSH audit completed for {target_ip}.")
                print(f"Results saved to: {output_file}")
            except Exception as e:
                print(f"Error performing SSH audit on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target ID.")

    def run_ssh_audit(self, target_ip):
        """
        Run the ssh-audit tool against the target IP.
        Args:
            target_ip (str): Target IP address.
        Returns:
            str: Path to the results file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(self.notes_dir, f"{target_ip}_ssh_audit_{timestamp}.md")

        try:
            print("Starting SSH audit...")
            result = subprocess.run(
                ["ssh-audit", target_ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode == 0:
                self.log_results(output_file, result.stdout)
            else:
                print(f"Error during SSH audit: {result.stderr}")
                self.log_results(output_file, result.stderr)

        except Exception as e:
            print(f"Error executing SSH audit: {e}")
        
        return output_file

    def log_results(self, output_file, results):
        """
        Log the SSH audit results to a file.
        Args:
            output_file (str): Path to the results file.
            results (str): SSH audit output.
        """
        with open(output_file, "w") as file:
            file.write(f"# SSH Audit Results\n")
            file.write(f"**Audit Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"Results logged to: {output_file}")
