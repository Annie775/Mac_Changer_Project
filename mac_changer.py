import subprocess
import optparse
import re

def mac_changer(intf, new_mac):
    subprocess.call(["ifconfig", intf, "down"])
    subprocess.call(["ifconfig", intf, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", intf, "up"])
    print(f"\n[+] Changing MAC Address of {intf} to {new_mac}\n")
    new_mac_result(intf)

def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC Address")
    # parser.add_option("-p", "--permanent", dest="permanent", help="Restore back to permanent address")
    (value, args) = parser.parse_args()
    if not value.interface:
        parser.error("[-] Please Specify Interface.")
    elif not value.mac_address:
        parser.error("[-] Please Specify New Mac Address.")
    else:
        mac_changer(value.interface, value.mac_address)

def new_mac_result(interface):
    ifc_r = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifc_r))
    if mac_result:
        print("[+] New MAC Address is",mac_result.group(0))
    else:
        print("[-] Could not read MAC Address")

arguments()


