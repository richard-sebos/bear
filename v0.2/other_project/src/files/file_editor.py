from encryption_manager import EncryptionManager

class FileEditor:
    """
    Manages reading, writing, and editing files with optional encryption.

    Attributes:
        encryption_manager (EncryptionManager): Handles encryption and decryption of file contents.
    """

    def __init__(self):
        """
        Initializes the FileEditor with an EncryptionManager.
        """
        self.encryption_manager = EncryptionManager()

    def read_file(self, path: str) -> str:
        """
        Reads the content of a file from the given path.

        Args:
            path (str): The file path.

        Returns:
            str: The file content.
        """
        print(f"Reading file from {path}.")
        with open(path, 'r') as file:
            content = file.read()
        print(f"File content read: {content[:50]}...")
        return content

    def write_file(self, path: str, data: str, encrypt: bool = False) -> None:
        """
        Writes data to a file at the given path, optionally encrypting it.

        Args:
            path (str): The file path.
            data (str): The data to write.
            encrypt (bool): Whether to encrypt the data before writing.
        """
        if encrypt:
            print("Encrypting data before writing to file.")
            data = self.encryption_manager.encrypt(data)
        print(f"Writing data to {path}.")
        with open(path, 'w') as file:
            file.write(data)
        print("File write complete.")

    def edit_file(self, path: str, new_content: str) -> None:
        """
        Edits an existing file by replacing its content.

        Args:
            path (str): The file path.
            new_content (str): The new content for the file.
        """
        print(f"Editing file at {path}.")
        self.write_file(path, new_content)

    def __repr__(self) -> str:
        """
        Provides a string representation of the FileEditor.

        Returns:
            str: A string describing the FileEditor.
        """
        return "FileEditor()"
