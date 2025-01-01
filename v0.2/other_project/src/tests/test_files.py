import unittest
from unittest.mock import patch, mock_open
from file_editor import FileEditor

class TestFileEditor(unittest.TestCase):
    """
    Unit tests for the FileEditor class.
    """

    def setUp(self):
        """
        Set up a fresh instance of FileEditor for each test.
        """
        self.file_editor = FileEditor()

    @patch("builtins.open", new_callable=mock_open, read_data="Sample content.")
    def test_read_file(self, mock_file):
        """
        Test that reading a file returns the correct content.
        """
        path = "test_file.txt"
        content = self.file_editor.read_file(path)

        self.assertEqual(content, "Sample content.")
        mock_file.assert_called_once_with(path, "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_file_plain(self, mock_file):
        """
        Test that writing plain data to a file works correctly.
        """
        path = "test_file.txt"
        data = "New content."

        self.file_editor.write_file(path, data, encrypt=False)

        mock_file.assert_called_once_with(path, "w")
        mock_file().write.assert_called_once_with(data)

    @patch("builtins.open", new_callable=mock_open)
    @patch("file_editor.EncryptionManager.encrypt", return_value="Encrypted content.")
    def test_write_file_encrypted(self, mock_encrypt, mock_file):
        """
        Test that writing encrypted data to a file works correctly.
        """
        path = "test_file.txt"
        data = "Sensitive content."

        self.file_editor.write_file(path, data, encrypt=True)

        mock_encrypt.assert_called_once_with(data)
        mock_file.assert_called_once_with(path, "w")
        mock_file().write.assert_called_once_with("Encrypted content.")

    @patch("file_editor.FileEditor.write_file")
    def test_edit_file(self, mock_write_file):
        """
        Test that editing a file calls write_file with the new content.
        """
        path = "test_file.txt"
        new_content = "Updated content."

        self.file_editor.edit_file(path, new_content)

        mock_write_file.assert_called_once_with(path, new_content)

if __name__ == "__main__":
    unittest.main()
