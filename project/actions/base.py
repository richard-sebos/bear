# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Base class for all actions in the Bear application.

class Action():
    def command(self):
        return "hidden"

    def description(self):
        return "This action is hidden and not available in the menu."

    def include_in_menu(self):
        return False  # Exclude from the menu

    def execute(self, args, id_mapping):
        print("This action is executed but not listed in the menu.")
