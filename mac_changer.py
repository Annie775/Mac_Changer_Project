import subprocess
import optparse
import re
import random

def generate_random_mac():
    # Generate a random MAC address
    mac = [0x00, random.randint(0x00, 0x7f),  
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

def mac_changer(intf, new_mac):
    try:
        subprocess.check_output(["ifconfig", intf], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError:
        print(f"Error: Interface '{intf}' not found. Please provide a valid interface name.")
        exit(0)

    subprocess.call(["ifconfig", intf, "down"])
    subprocess.call(["ifconfig", intf, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", intf, "up"])
    print(f"\n[+] Changing MAC Address of {intf} to {new_mac}\n")
    curr_mac_add(intf)

def arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC Address")
    parser.add_option("-r", "--random", action="store_true", dest="random_mac", help="Random Mac Address")
    
    (value, args) = parser.parse_args()
    if not value.interface:
        parser.error("[-] Please specify an interface with -i")
    else:
        if value.random_mac and value.mac_address:
            parser.error("[-] Please use either -r for a random MAC or -m for a specific MAC, but not both.")

        if value.random_mac:
            random_mac = generate_random_mac()
            print(f"[+] Generated Random MAC Address: {random_mac}")
            mac_changer(value.interface, random_mac)
        elif value.mac_address:
            mac_changer(value.interface, value.mac_address)
        else:
            parser.error("[-] Please specify either -i and -m together, or -r with -i.")
        return value.interface

def curr_mac_add(interface):
    ifc_r = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifc_r))
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read MAC Address")

option = arguments()
print("[+] Current MAC Address: " + str(curr_mac_add(option)))
