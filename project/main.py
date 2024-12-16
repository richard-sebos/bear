# App: Bear
# Company: Sebos Technology
# Description: Main entry point for the Bear application.

import argparse
from action_loader import load_actions
from actions.list_action import ListAction
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

def interactive_session(active_ips, actions):
    """
    Start an interactive session to perform additional actions.
    """
    id_mapping = {idx + 1: ip for idx, ip in enumerate(active_ips)}
    print("\nEntering interactive session. Type 'help' to see available commands.")

    while True:
        command = input(">> ").strip().lower().split()
        if not command:
            continue
        
        action_name, *args = command

        if action_name == "help":
            print("\nAvailable commands (sorted alphabetically):")
            for action in sorted(actions, key=lambda x: x.command()):
                if action.include_in_menu():
                    print(f"  {action.command():<10} - {action.description()}")
            print("  help         - Show this help menu")
            print("  exit         - Exit the interactive session")
        
        elif action_name == "exit":
            print("\nExiting interactive session.")
            break
        
        else:
            matched_action = next((action for action in actions if action.command() == action_name), None)
            if matched_action:
                try:
                    matched_action.execute(args, id_mapping)
                except Exception as e:
                    print(f"Error running action '{action_name}': {e}")
            else:
                print(f"Unknown command: {action_name}. Type 'help' for a list of available commands.")

def main():
    """Main function orchestrates the flow of the application."""
    parser = argparse.ArgumentParser(description="Network Scanning Tool")
    parser.add_argument('--ip', type=str, help='Single IP address to scan')
    parser.add_argument('--cidr', type=str, help='CIDR subnet to scan')
    parser.add_argument('--list', type=str, help='File containing a list of IPs to scan')
    args = parser.parse_args()

    # Collect and validate targets
    targets = []
    if args.ip:
        targets.append(args.ip)
    if args.cidr:
        targets.extend(expand_cidr(args.cidr))
    if args.list:
        try:
            with open(args.list, 'r') as file:
                targets.extend(file.read().splitlines())
        except FileNotFoundError:
            print(f"Error: File '{args.list}' not found.")
            return

    valid_targets = validate_targets(targets)
    if not valid_targets:
        print("No valid targets provided. Exiting.")
        return

    # Load actions
    actions = load_actions()
    starting_action = next((action for action in actions if action.__class__.__name__ == "StartingAction"), None)

    if starting_action is None:
        print("Error: StartingAction is not defined. Ensure it's implemented and loaded.")
        return

    # Run StartingAction to validate targets
    print("Validating targets with StartingAction...")
    active_ips = []
    for target in valid_targets:
        try:
            status = starting_action.execute(target)
            if status == "UP":
                print(f"{target} is UP.")
                active_ips.append(target)
            else:
                print(f"{target} is {status}. Skipping.")
        except Exception as e:
            print(f"Error executing StartingAction on {target}: {e}")

    if not active_ips:
        print("No active IPs found. Exiting.")
        return

    # Add actions, including the ListAction and HiddenAction
    list_action = ListAction(active_ips)
    actions.append(list_action)


    # Start interactive session
    interactive_session(active_ips, actions)

if __name__ == "__main__":
    main()
