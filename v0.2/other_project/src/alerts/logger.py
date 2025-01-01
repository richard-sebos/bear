class Logger:
    """
    Centralized logging utility for the system.
    """

    def log(self, message: str) -> None:
        """
        Logs a message to the console or an external system.

        Args:
            message (str): The message to log.
        """
        print(f"LOG: {message}")

    def log_error(self, error_message: str) -> None:
        """
        Logs an error message.

        Args:
            error_message (str): The error message to log.
        """
        print(f"ERROR: {error_message}")

    def log_warning(self, warning_message: str) -> None:
        """
        Logs a warning message.

        Args:
            warning_message (str): The warning message to log.
        """
        print(f"WARNING: {warning_message}")

    def log_info(self, info_message: str) -> None:
        """
        Logs an informational message.

        Args:
            info_message (str): The informational message to log.
        """
        print(f"INFO: {info_message}")

    def __repr__(self) -> str:
        """
        Provides a string representation of the Logger.

        Returns:
            str: A string describing the Logger.
        """
        return "Logger()"
