import subprocess
import optparse
#usinf function to store our code
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to" + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

#calling function 
change_mac(options.interface, options.new_mac)
#now we can just call the function and change interface and mac anywhere we want