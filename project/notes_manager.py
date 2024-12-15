# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Manage Markdown-formatted notes for IPs in the Bear application.

import os
import datetime

class NotesManager:
    """Manage notes for each IP."""

    def __init__(self, notes_dir="notes"):
        """Initialize the NotesManager with a specified directory."""
        if not notes_dir:
            print("Error: notes_dir parameter is required to initialize NotesManager.\nExample: NotesManager(notes_dir='path/to/notes')")
            return
        self.notes_dir = notes_dir
        os.makedirs(notes_dir, exist_ok=True)

    def add_entry(self, ip, entry):
        """Add a timestamped entry for a given IP."""
        if not ip or not entry:
            print("Error: Both ip and entry parameters are required to add an entry.\nExample: add_entry(ip='192.168.1.1', entry='Some note.')")
            return
        note_file = os.path.join(self.notes_dir, f"{ip}.md")
        timestamp = datetime.datetime.now().isoformat()
        with open(note_file, "a") as file:
            file.write(f"[{timestamp}] {entry}\n")

    def view_notes(self, ip):
        """View notes for a specific IP."""
        if not ip:
            return "Error: ip parameter is required to view notes.\nExample: view_notes(ip='192.168.1.1')"
        note_file = os.path.join(self.notes_dir, f"{ip}.md")
        if os.path.exists(note_file):
            with open(note_file, "r") as file:
                return file.read()
        else:
            return "No notes found for this IP."

    def edit_notes(self, ip, editor="nano"):
        """Open notes for editing using the specified editor."""
        if not ip:
            print("Error: ip parameter is required to edit notes.\nExample: edit_notes(ip='192.168.1.1', editor='vim')")
            return
        note_file = os.path.join(self.notes_dir, f"{ip}.md")
        os.system(f"{editor} {note_file}")

    def search_notes(self, keyword):
        """Search all notes for a specific keyword."""
        if keyword is None:
            print("Error: keyword parameter is required to search notes.\nExample: search_notes(keyword='search term')")
            return []
        results = []
        for file_name in os.listdir(self.notes_dir):
            if file_name.endswith(".md"):
                with open(os.path.join(self.notes_dir, file_name), "r") as file:
                    content = file.read()
                    if keyword in content:
                        results.append((file_name, content))
        return results
