import subprocess
import optparse
import re

def mac_changer(intf, new_mac):
    subprocess.call(["ifconfig", intf, "down"])
    subprocess.call(["ifconfig", intf, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", intf, "up"])
    print(f"\n[+] Changing MAC Address of {intf} to {new_mac}\n")
    curr_mac_add(intf)

def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC Address")
    parser.add_option("-r", "--random", dest="random_mac", help="Random Mac Address")
    
    (value, args) = parser.parse_args()
    if not value.interface:
        parser.error("[-] Please Specify Interface.")
    elif not value.mac_address:
        parser.error("[-] Please Specify New MAC Address.")
    else:
        mac_changer(value.interface, value.mac_address)

def curr_mac_add(interface):
    ifc_r = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifc_r))
    if mac_result:
        return ("[+] New MAC Address is",mac_result.group(0))
    else:
        print("[-] Could not read MAC Address")

arguments()


