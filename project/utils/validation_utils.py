# App: Bear
# Company: Sebos Technology
# Date: 
# Description: Utility functions for validating IP addresses and CIDR ranges in the Bear application.

import ipaddress

def is_valid_ip(ip):
    """Validate a single IP address or CIDR."""
    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError:
        return False

def validate_targets(targets):
    """Filter out invalid IP addresses or CIDR ranges from a list."""
    return [target for target in targets if is_valid_ip(target)]

