# App: Bear
# Company: Sebos Technology
# Date: 
# Description: ScanAction class for performing detailed network scans in the Bear application.

from actions.base import Action
import subprocess

class ScanAction(Action):
    """Perform detailed network scans using nmap."""
    def execute(self, target):
        """Execute a detailed scan on the target."""
        try:
            result = subprocess.run(["nmap", "-sT", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                self.log(f"Scan results for {target}:\n{result.stdout.decode()}")
            else:
                self.log(f"Error scanning {target}:\n{result.stderr.decode()}")
        except Exception as e:
            self.log(f"Error executing ScanAction on {target}: {e}")

