import sys
from action_loader import load_actions

def display_menu(actions):
    """
    Display a menu of available actions.
    Args:
        actions (list): List of action instances.
    """
    print("\nAvailable Actions:")
    for idx, action in enumerate(actions, start=1):
        if action.include_in_menu():
            print(f"{idx}. {action.command()} - {action.description()}")
    print("0. Exit")


def main():
    # Load all actions dynamically
    actions = load_actions("actions")
    
    # Shared state for active IPs and ID mapping
    active_ips = []
    id_mapping = {}

    # Pass shared state to actions that require it
    for action in actions:
        if hasattr(action, 'set_active_ips'):
            action.set_active_ips(active_ips)

    # Interactive loop for user
    while True:
        display_menu(actions)
        try:
            choice = input("\nSelect an action (by number or command): ").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    print("Exiting...")
                    break
                elif 1 <= choice <= len(actions):
                    action = actions[choice - 1]
                else:
                    print("Invalid selection. Try again.")
                    continue
            else:
                action = next((a for a in actions if a.command() == choice), None)

            if not action:
                print("Invalid command. Try again.")
                continue

            # Execute the chosen action
            if action.command() == "list":
                action.execute(id_mapping=id_mapping)
            else:
                # Provide arguments dynamically
                args = input(f"Enter arguments for {action.command()} (space-separated): ").split()
                action.execute(args=args, id_mapping=id_mapping)

                # Update ID mapping if the action discovers new IPs
                if hasattr(action, "get_active_ips"):
                    active_ips = action.get_active_ips()
                    id_mapping = {idx + 1: ip for idx, ip in enumerate(active_ips)}

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
