import argparse
from utils.validation_utils import is_valid_ip, is_valid_cidr
from utils.file_reader import read_file
from utils.logger import configure_logger
from utils.enhanced_device_status_checker import check_device_status
from config.settings import VALID_IPS_OUTPUT_PATH, STRICT_MODE

# Configure logger
logger = configure_logger()

def write_valid_ips_to_file(valid_ips):
    """Write the list of valid IPs to the valid_ips.txt file."""
    try:
        with open(VALID_IPS_OUTPUT_PATH, 'w') as file:
            for ip in valid_ips:
                file.write(f"{ip}\n")
        logger.info(f"Valid IPs written to {VALID_IPS_OUTPUT_PATH}")
    except Exception as e:
        logger.error(f"Error writing valid IPs to file: {e}")

def process_ip(ip):
    """Validate and check the status of a single IP address."""
    if is_valid_ip(ip):
        status = check_device_status(ip)
        logger.info(f"IP {ip} status: {status}")
        if status in ["ACCEPTED", "REJECTED"]:
            return [ip]
        return []
    else:
        logger.error(f"Invalid IP: {ip}")
        return []

def process_cidr(cidr):
    """Validate CIDR and check the status of all IPs in the range."""
    valid_ips = []
    if is_valid_cidr(cidr):
        from ipaddress import ip_network
        network = ip_network(cidr, strict=False)
        for ip in network:
            status = check_device_status(str(ip))
            logger.info(f"IP {ip} status: {status}")
            if status in ["ACCEPTED", "REJECTED"]:
                valid_ips.append(str(ip))
    else:
        logger.error(f"Invalid CIDR: {cidr}")
    return valid_ips

def process_list(file_path):
    """Validate and check the status of IPs in a file."""
    valid_ips = []
    ips = read_file(file_path)
    for ip in ips:
        if is_valid_ip(ip):
            status = check_device_status(ip)
            logger.info(f"IP {ip} status: {status}")
            if status in ["ACCEPTED", "REJECTED"]:
                valid_ips.append(ip)
        else:
            logger.error(f"Invalid IP: {ip}")
    return valid_ips

def main():
    parser = argparse.ArgumentParser(description="IP Validation and Device Status Checker")
    parser.add_argument("--ip", help="Validate and check the status of a single IP address")
    parser.add_argument("--cidr", help="Validate and check the status of all IPs in a CIDR range")
    parser.add_argument("--list", help="Validate and check the status of all IPs in a file")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode for deeper validation")
    parser.add_argument("--verbose", action="store_true", help="Enable detailed output")
    parser.add_argument("--quiet", action="store_true", help="Suppress detailed output")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel("DEBUG")
    elif args.quiet:
        logger.setLevel("ERROR")

    if args.strict:
        global STRICT_MODE
        STRICT_MODE = True
        logger.info("Strict mode enabled")

    valid_ips = []

    if args.ip:
        valid_ips = process_ip(args.ip)
    elif args.cidr:
        valid_ips = process_cidr(args.cidr)
    elif args.list:
        valid_ips = process_list(args.list)
    else:
        parser.print_help()

    if valid_ips:
        write_valid_ips_to_file(valid_ips)

if __name__ == "__main__":
    main()
