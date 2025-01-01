# Help text for the command-line interface
HELP_TEXT = """
Usage: main.py [OPTIONS]

Options:
  --ip <IP_ADDRESS>         Validate a single IP address.
  --cidr <IP/CIDR>          Validate an IP address and CIDR notation.
  --list <FILE_PATH>        Validate a list of IP addresses from a file.
  --help                    Show this help message and exit.
  --verbose                 Enable detailed output during execution.
  --quiet                   Suppress detailed output and show only essential messages.

Examples:
  Validate a single IP:
    python3 main.py --ip 192.168.1.1

  Validate an IP with CIDR:
    python3 main.py --cidr 192.168.1.0/24

  Validate a list of IPs from a file:
    python3 main.py --list ip_list.txt

"""
