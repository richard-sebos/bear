import socket
import http.client

def check_device_status(ip, port=80, timeout=2):
    """
    Check the status of a device at the given IP using a TCP connection and HTTP probing.

    Args:
        ip (str): The IP address to check.
        port (int): The port to use for the check (default: 80).
        timeout (int): Timeout for the check in seconds (default: 2).

    Returns:
        str: One of the statuses: 'DOWN', 'DROPPED', 'REJECTED', 'ACCEPTED'.
    """
    try:
        # TCP Connect Test
        with socket.create_connection((ip, port), timeout=timeout):
            # HTTP HEAD Request Test (optional for more detail)
            try:
                conn = http.client.HTTPConnection(ip, port, timeout=timeout)
                conn.request("HEAD", "/")
                response = conn.getresponse()
                if 200 <= response.status < 400:
                    return "ACCEPTED"
                else:
                    return "REJECTED"
            except Exception:
                return "ACCEPTED"
    except socket.timeout:
        return "DROPPED"
    except ConnectionRefusedError:
        return "REJECTED"
    except Exception:
        return "DOWN"

if __name__ == "__main__":
    # Example usage for testing
    ip_to_test = "192.168.1.1"
    status = check_device_status(ip_to_test)
    print(f"Device {ip_to_test} is {status}.")
