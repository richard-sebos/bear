import logging
from config.settings import LOG_LEVEL, LOG_FILE_PATH

def configure_logger():
    """Set up and configure the application logger."""
    logger = logging.getLogger('main_logger')
    logger.setLevel(LOG_LEVEL)

    # Create file handler
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(LOG_LEVEL)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger