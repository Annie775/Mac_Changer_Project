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

    Example:
    python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### 2. Assign a Random MAC Address
    python3 mac_changer.py -i <interface> -r
     
    Example:
    python3 mac_changer.py -i eth0 -r

## Options 
      - -i or --interface : The name of the network interface (e.g., eth0, wlan0) whose MAC address you want to change.
      - -m or --mac : The new MAC address to assign to the interface.
      - -r or --random : Generates a random MAC address and assigns it to the specified interface.
 
 ## Changing to a Specific MAC Address
    $ python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
    [+] Changing MAC Address of eth0 to 00:11:22:33:44:55
    [+] Current MAC Address: 00:11:22:33:44:55
 ## Assigning a Random MAC Address
    $ python3 mac_changer.py -i eth0 -r
    [+] Generated Random MAC Address: 3c:2e:3f:1a:8b:7c
    [+] Changing MAC Address of eth0 to 3c:2e:3f:1a:8b:7c
    [+] Current MAC Address: 3c:2e:3f:1a:8b:7c
 ## Error Handling
     The tool checks for:- Invalid or non-existent network interfaces.- Conflicting options, such as using -r and -m together.- Missing required arguments.
     Example error messages:
    [-] Please specify an interface with -i.
    [-] Please use either -r for a random MAC or -m for a specific MAC, but not both.
    [-] Could not read MAC Address.
 
 ## Disclaimer 
     This tool is for educational purposes only. Use responsibly.- Changing MAC addresses may violate the policies of your network provider or organization.
     Proceed with caution
