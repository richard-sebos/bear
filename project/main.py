import argparse
import importlib
import os
from ipaddress import ip_network, ip_address
import socket

# Directory containing actions
actions_dir = "actions"

class Main:
    def __init__(self):
        self.active_ips = []
        self.actions = []
        self.id_mapping = {}

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Main application module.")
        parser.add_argument("--ip", type=str, help="Single IP address to scan.")
        parser.add_argument("--cidr", type=str, help="CIDR range of IPs to scan.")
        parser.add_argument("--list", type=str, help="File containing a list of IPs to scan.")
        return parser.parse_args()

    def load_actions(self):
        print("Loading actions dynamically...")
        for file in os.listdir(actions_dir):
            if file.endswith(".py") and file != "base.py":
                module_name = f"actions.{file[:-3]}"
                try:
                    module = importlib.import_module(module_name)
                    for attr in dir(module):
                        cls = getattr(module, attr)
                        if isinstance(cls, type) and cls.__name__.endswith("Action"):
                            instance = cls()
                            if instance.include_in_menu():
                                self.actions.append(instance)
                except Exception as e:
                    print(f"Failed to load action {module_name}: {e}")

    def resolve_ips(self, args):
        if args.ip:
            self.active_ips = [args.ip] if self.is_active_ip(args.ip) else []
        elif args.cidr:
            self.active_ips = [str(ip) for ip in ip_network(args.cidr, strict=False) if self.is_active_ip(str(ip))]
        elif args.list:
            with open(args.list, "r") as file:
                self.active_ips = [line.strip() for line in file if self.is_active_ip(line.strip())]
        self.id_mapping = {i + 1: ip for i, ip in enumerate(self.active_ips)}

    def is_active_ip(self, ip):
        try:
            socket.setdefaulttimeout(1)
            socket.gethostbyaddr(ip)
            return True
        except (socket.herror, socket.timeout):
            return False

    def display_active_ips(self):
        if not self.active_ips:
            print("No active IPs found.")
            return

        print("Active IP Addresses:")
        for idx, ip in self.id_mapping.items():
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"
            print(f"{idx}. {ip} ({hostname})")

    def interactive_menu(self):
        print("\nInteractive Menu")
        while True:
            print("\nAvailable Actions:")
            for idx, action in enumerate(self.actions, start=1):
                print(f"{idx}. {action.description()}")

            print("0. Exit")
            choice = input("Select an option: ")

            if choice == "0":
                print("Exiting...")
                break

            if choice.isdigit() and 1 <= int(choice) <= len(self.actions):
                action = self.actions[int(choice) - 1]
                if action.command().startswith("ssh_"):
                    self.ssh_submenu(action)
                else:
                    args = input("Enter IDs or IPs (comma-separated): ").split(",")
                    action.execute(args=args, id_mapping=self.id_mapping)
            else:
                print("Invalid choice. Try again.")

    def ssh_submenu(self, action):
        print("\nSSH Actions Submenu")
        while True:
            print(f"Executing SSH submenu for action: {action.description()}")
            args = input("Enter IDs or IPs (comma-separated, or type 'back' to return): ").strip()
            if args.lower() == "back":
                break
            action.execute(args=args.split(","), id_mapping=self.id_mapping)

    def run(self):
        args = self.parse_args()
        self.resolve_ips(args)
        self.display_active_ips()
        self.load_actions()
        self.interactive_menu()

if __name__ == "__main__":
    Main().run()
