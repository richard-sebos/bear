import socket
from actions.base import Action

class ListAction(Action):
    def __init__(self, active_ips=None):
        """
        Initialize the ListAction with a reference to active IPs.
        """
        self.active_ips = active_ips or []

    def command(self):
        """Return the command to trigger this action in the menu."""
        return "list"

    def description(self):
        """Provide a description for the action."""
        return "Display the list of active IP addresses with host names."

    def include_in_menu(self):
        """Include this action in the interactive menu."""
        return True

    def execute(self, args=None, id_mapping=None):
        """
        Display the list of active IP addresses with host names.
        """
        if not self.active_ips:
            print("No active IPs found.")
            return

        print("\nActive IP Addresses and Host Names:")
        for idx, ip in enumerate(self.active_ips, start=1):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown Host"
            print(f"{idx}. {ip} - {hostname}")

    def set_active_ips(self, active_ips):
        """
        Update the list of active IPs.
        """
        self.active_ips = active_ips
