### Updated Requirements Document for `main.py`

#### **Overview**
The `main.py` script is a command-line utility designed to validate and process IP-related inputs. It has been extended to include functionality for detailed device status checks. This document outlines the updated functional, non-functional, and implementation requirements.

---

### **Functional Requirements**

#### **1. Command-Line Arguments**

1. **`--ip`**
   - Accepts a single IP address as input.
   - Validates the IP address format using a dedicated validation class.
   - Performs a detailed status check for the IP address (e.g., `DOWN`, `DROPPED`, `REJECTED`, `ACCEPTED`).
   - Outputs the validation and status results.

2. **`--cidr`**
   - Accepts an IP address with CIDR notation (e.g., `192.168.1.0/24`).
   - Validates the IP and CIDR format.
   - Loops through all IPs in the subnet and performs a detailed status check for each.
   - Outputs the validation and status results.

3. **`--list`**
   - Accepts a file containing a list of IP addresses (one IP per line).
   - Reads and validates each IP in the file.
   - Performs a detailed status check for each valid IP.
   - Outputs the validation and status results.

4. **`--help`**
   - Displays a concise yet informative usage guide for all options.
   - Includes examples of valid inputs for each argument.

5. **`--verbose`**
   - Provides detailed output during execution.
   - Useful for debugging or understanding the script's internal processing.

6. **`--quiet`**
   - Limits output to only essential messages, suppressing detailed logs.

7. **`--strict`**
   - Enables strict mode for deeper validation checks (e.g., public/private classification, additional device probing).

---

### **New Functionalities**

1. **Detailed Device Status Checks**:
   - The script checks whether the device at a given IP is:
     - `DOWN`: Unreachable due to network or device issues.
     - `DROPPED`: No response within a timeout period.
     - `REJECTED`: Actively refused the connection.
     - `ACCEPTED`: Responded positively (e.g., via TCP or HTTP).

2. **Integration with Existing Options**:
   - The device status checks are integrated into `--ip`, `--cidr`, and `--list` operations.

3. **Output Management**:
   - Results are logged and optionally saved to an output file.
   - Valid IPs and their statuses are displayed or saved based on configuration.

---

### **Non-Functional Requirements**

1. **Performance**:
   - Efficiently handle large CIDR ranges and files with many IP addresses.
   - Include progress indicators for long-running tasks.

2. **Error Handling**:
   - Gracefully handle unreachable IPs, invalid inputs, and file read errors.
   - Log errors with meaningful messages for debugging.

3. **Logging**:
   - Implement configurable logging levels to support `--verbose` and `--quiet` options.
   - Logs include timestamps, status results, and error details.

4. **Extensibility**:
   - Modular architecture to easily integrate additional device status checks or future functionalities.

5. **Compatibility**:
   - Ensure compatibility across major operating systems (Linux, Windows, macOS).

---

### **Implementation Details**

1. **Modules**:
   - `validation_utils.py`:
     - Contains IP and CIDR validation logic.
   - `file_reader.py`:
     - Handles reading and processing files for `--list`.
   - `device_status_checker.py`:
     - Implements logic for detailed device status checks.
   - `logger.py`:
     - Configures logging for verbose, quiet, and standard modes.

2. **Output**:
   - **For `--ip`**:
     - Outputs validation and status results for the given IP.
   - **For `--cidr`**:
     - Outputs validation and status results for all IPs in the subnet.
   - **For `--list`**:
     - Outputs validation and status results for all valid IPs in the file.

3. **Testing**:
   - Unit tests for new functionality in `device_status_checker.py`.
   - Integration tests for `main.py` covering `--ip`, `--cidr`, and `--list` options.
   - End-to-end tests to verify expected script behavior in real-world scenarios.

---

### **Future Enhancements**

1. **Advanced Probing**:
   - Extend status checks to include additional protocols (e.g., SSH, HTTPS).

2. **Customizable Ports**:
   - Allow users to specify ports for TCP/HTTP probing.

3. **Report Generation**:
   - Generate detailed status reports in formats like JSON, CSV, or HTML.

4. **Scheduling**:
   - Add functionality to schedule periodic checks.

---

### **Summary**
The updated `main.py` script introduces robust device status checking functionality while maintaining modularity and scalability. It supports detailed logging and efficient handling of various input formats, making it a versatile tool for network diagnostics.

