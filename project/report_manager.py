# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Generate reports based on notes managed in the Bear application.

from notes_manager import NotesManager

class ReportManager:
    """Generate reports based on notes."""

    def __init__(self, notes_manager):
        """Initialize the ReportManager with a NotesManager instance."""
        self.notes_manager = notes_manager

    def generate_report(self, ip):
        """Generate a report for a specific IP."""
        notes = self.notes_manager.view_notes(ip)
        if notes == "No notes found for this IP.":
            return f"No report available for IP: {ip}"

        report = f"Report for {ip}\n{'=' * 40}\n{notes}"
        return report

    def generate_global_summary(self):
        """Generate a summary report for all IPs with notes."""
        all_notes = []
        for file_name, content in self.notes_manager.search_notes(""):
            ip = file_name.replace(".md", "")
            all_notes.append(f"IP: {ip}\n{'-' * 20}\n{content}\n")

        if not all_notes:
            return "No notes found for any IPs."

        summary = "Global Notes Summary\n" + "=" * 40 + "\n" + "\n".join(all_notes)
        return summary

