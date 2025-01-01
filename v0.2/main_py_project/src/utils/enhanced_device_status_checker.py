import socket
from ping3 import ping
import http.client

def check_with_icmp(ip, timeout=2):
    """
    Perform an ICMP Echo (Ping) check for additional validation.

    Args:
        ip (str): IP address to check.
        timeout (int): Timeout for the ping operation.

    Returns:
        bool: True if the device responds to ICMP, False otherwise.
    """
    try:
        response_time = ping(ip, timeout=timeout)
        return response_time is not None
    except Exception:
        return False

def udp_probe(ip, port=53, timeout=2):
    """
    Perform a UDP probe to check if the device is reachable on a specific port.

    Args:
        ip (str): IP address to check.
        port (int): Port to probe.
        timeout (int): Timeout for the probe operation.

    Returns:
        bool: True if the device responds, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        sock.sendto(b"test", (ip, port))
        sock.recvfrom(1024)
        return True
    except socket.timeout:
        return False
    except Exception:
        return False
    finally:
        sock.close()

def check_device_status(ip, port=80, udp_port=53, timeout=2):
    """
    Check the status of a device using multiple methods.

    Args:
        ip (str): IP address to check.
        port (int): TCP port for connection testing.
        udp_port (int): UDP port for probing.
        timeout (int): Timeout for each operation.

    Returns:
        str: One of the statuses: 'DOWN', 'DROPPED', 'REJECTED', 'ACCEPTED'.
    """
    try:
        # First, check ICMP
        if check_with_icmp(ip, timeout=timeout):
            # Proceed with TCP validation if ICMP responds
            try:
                with socket.create_connection((ip, port), timeout=timeout):
                    return "ACCEPTED"
            except socket.timeout:
                return "DROPPED"
            except ConnectionRefusedError:
                return "REJECTED"
            except Exception:
                return "DOWN"
        else:
            # If ICMP does not respond, validate with UDP
            if udp_probe(ip, udp_port, timeout=timeout):
                return "ACCEPTED"
            return "DOWN"
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    # Example usage for testing
    ip_to_test = "192.168.1.1"
    status = check_device_status(ip_to_test)
    print(f"Device {ip_to_test} is {status}.")
