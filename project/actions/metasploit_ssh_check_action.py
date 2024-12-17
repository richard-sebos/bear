import subprocess
import os
from datetime import datetime
from actions.base import Action

class MetasploitSshCheckAction(Action):
    def __init__(self, notes_dir="notes"):
        """
        Initialize the MetasploitSshCheckAction class.
        """
        self.notes_dir = notes_dir
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "ssh-metasploit"

    def description(self):
        """Provide a description for the action."""
        return "Run Metasploit auxiliary SSH version and login checks."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Execute the Metasploit SSH checks.
        Args:
            args (list): List of IP addresses or ID numbers.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        if not args or not id_mapping:
            print("No targets provided for Metasploit SSH check.")
            return

        target_id = args[0] if args else None
        if target_id and target_id.isdigit() and int(target_id) in id_mapping:
            target_ip = id_mapping[int(target_id)]
            print(f"Running Metasploit SSH check on IP: {target_ip}")
            
            try:
                script_file = self.create_msf_script(target_ip)
                self.run_metasploit(script_file, target_ip)
            except Exception as e:
                print(f"Error performing Metasploit SSH check on {target_ip}: {e}")
        else:
            print("Invalid target selection. Provide a valid target ID.")

    def create_msf_script(self, target_ip):
        """
        Create a Metasploit script for SSH checks.
        Args:
            target_ip (str): Target IP address.
        Returns:
            str: Path to the Metasploit script file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        script_file = os.path.join(self.notes_dir, f"metasploit_ssh_check_{target_ip}_{timestamp}.rc")

        script_content = f"""
use auxiliary/scanner/ssh/ssh_version
set RHOSTS {target_ip}
run

use auxiliary/scanner/ssh/ssh_login
set RHOSTS {target_ip}
set USER_FILE /usr/share/wordlists/metasploit/common_users.txt
set PASS_FILE /usr/share/wordlists/rockyou.txt
set THREADS 5
run
        """
        with open(script_file, "w") as file:
            file.write(script_content)

        print(f"Metasploit script created: {script_file}")
        return script_file

    def run_metasploit(self, script_file, target_ip):
        """
        Run the Metasploit script and save results.
        Args:
            script_file (str): Path to the Metasploit script file.
            target_ip (str): Target IP address.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(self.notes_dir, f"{target_ip}_metasploit_results_{timestamp}.md")

        try:
            print(f"Starting Metasploit SSH check for {target_ip}...")
            result = subprocess.run(
                ["msfconsole", "-r", script_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Metasploit SSH check completed for {target_ip}.")
                self.log_results(output_file, result.stdout)
            else:
                print(f"Error running Metasploit: {result.stderr}")
        except Exception as e:
            print(f"Error executing Metasploit for {target_ip}: {e}")

    def log_results(self, output_file, results):
        """
        Log the Metasploit results to a file.
        Args:
            output_file (str): Path to the results file.
            results (str): Metasploit output.
        """
        with open(output_file, "w") as file:
            file.write(f"# Metasploit SSH Check Results\n")
            file.write(f"**Scan Date:** {datetime.now().isoformat()}\n\n")
            file.write("## Results\n")
            file.write(results)

        print(f"Results saved to: {output_file}")
