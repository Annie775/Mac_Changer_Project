# MAC Address Changer

This is a Python-based command-line tool that allows users to change the MAC address of a specified network interface. It also supports generating a random MAC address for added functionality and privacy.

---

## Features
- Change the MAC address of a specified network interface to a user-provided value.
- Generate and assign a random MAC address to the specified interface.
- Validate the provided interface and handle errors for incorrect input.

---

## Prerequisites
- Python 3.x
- Administrative/root privileges
- The `ifconfig` command-line tool (available on most Unix/Linux systems)

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/mac-address-changer.git
    cd mac-address-changer
    ```
2. Ensure Python 3 is installed on your system:
    ```bash
    python3 --version
    ```

3. (Optional) Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

---

## Usage
Run the script with one of the following options:

### 1. Change MAC Address to a User-Specified Value
```bash
python3 mac_changer.py -i <interface> -m <new_mac_address>
