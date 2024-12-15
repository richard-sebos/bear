# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Centralized logging utilities for the Bear application.

import logging

# Configure logging
logging.basicConfig(
    filename='bear_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_action(unit, action, ip, state, message):
    """Log an action with details."""
    log_entry = f"UNIT={unit} ACTION={action} IP={ip} STATE={state} MESSAGE={message}"
    logging.info(log_entry)

