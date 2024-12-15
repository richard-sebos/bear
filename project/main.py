# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Main entry point for the Bear application. This script orchestrates the application flow, including user input parsing, target validation, and action execution.

import argparse
from action_loader import load_actions
from utils.validation_utils import validate_targets
import ipaddress

def expand_cidr(cidr):
    """Expand a CIDR range into individual IP addresses."""
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        print(f"Error: Invalid CIDR format '{cidr}'.")
        return []

def main():
    """Main function orchestrates the flow of the application."""
    parser = argparse.ArgumentParser(description="Network Scanning Tool")
    parser.add_argument('--ip', type=str, help='Single IP address to scan')
    parser.add_argument('--cidr', type=str, help='CIDR subnet to scan')
    parser.add_argument('--list', type=str, help='File containing a list of IPs to scan')
    parser.add_argument('--note-mode', action='store_true', help='Enable notes mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    # Validate at least one target input
    if not (args.ip or args.cidr or args.list):
        print("Error: At least one of --ip, --cidr, or --list must be provided to specify targets.")
        print("Usage Examples:")
        print("  --ip 192.168.1.1")
        print("  --cidr 192.168.1.0/24")
        print("  --list targets.txt")
        return

    # Collect targets from user input
    targets = []
    if args.ip:
        targets.append(args.ip)
    if args.cidr:
        targets.extend(expand_cidr(args.cidr))  # Expand CIDR to individual IPs
    if args.list:
        try:
            with open(args.list, 'r') as file:
                targets.extend(file.read().splitlines())
        except FileNotFoundError:
            print(f"Error: File '{args.list}' not found.")
            print("Ensure the file exists and try again.")
            return

    # Validate targets
    valid_targets = validate_targets(targets)
    if not valid_targets:
        print("No valid targets provided. Exiting.")
        return

    # Load actions
    actions = load_actions()
    if args.debug:
        print("Loaded actions:", [action.__class__.__name__ for action in actions])

    # Execute actions on targets
    for target in valid_targets:
        print(f"Processing target: {target}")
        for action in actions:
            try:
                action.execute(target)
            except Exception as e:
                print(f"Error executing action {action.__class__.__name__} on {target}: {e}")

if __name__ == "__main__":
    main()
