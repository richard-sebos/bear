class EncryptionManager:
    """
    Handles encryption and decryption of data.
    """

    def encrypt(self, data: str) -> str:
        """
        Encrypts the provided data.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data.
        """
        print("Encrypting data.")
        # Simple mock encryption logic (reversing the string)
        encrypted_data = data[::-1]
        print(f"Encrypted data: {encrypted_data[:50]}...")
        return encrypted_data

    def decrypt(self, data: str) -> str:
        """
        Decrypts the provided data.

        Args:
            data (str): The data to decrypt.

        Returns:
            str: The decrypted data.
        """
        print("Decrypting data.")
        # Simple mock decryption logic (reversing the string back)
        decrypted_data = data[::-1]
        print(f"Decrypted data: {decrypted_data[:50]}...")
        return decrypted_data

    def __repr__(self) -> str:
        """
        Provides a string representation of the EncryptionManager.

        Returns:
            str: A string describing the EncryptionManager.
        """
        return "EncryptionManager()"
