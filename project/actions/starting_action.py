from actions.base import Action
import subprocess

class StartingAction(Action):
    def __init__(self, active_ips=None):
        """
        Initialize the StartingAction class.
        """
        self.active_ips = active_ips or []

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "start"

    def description(self):
        """Provide a description for the action."""
        return "Start a scan and discover active IP addresses."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Discover active IP addresses.
        Args:
            args (list): List of targets.
            id_mapping (dict): Mapping of ID numbers to IP addresses.
        """
        targets = args or []
        if not targets:
            print("No targets provided.")
            return

        self.active_ips.clear()
        for target in targets:
            try:
                print(f"Pinging {target}...")
                result = subprocess.run(["ping", "-c", "1", target],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    print(f"{target} is UP.")
                    self.active_ips.append(target)
                else:
                    print(f"{target} is DOWN.")
            except Exception as e:
                print(f"Error scanning {target}: {e}")

        print("\nScan complete. Active IPs:")
        for ip in self.active_ips:
            print(ip)

    def get_active_ips(self):
        """
        Return the list of active IPs.
        """
        return self.active_ips
