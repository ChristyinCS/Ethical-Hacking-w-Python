import subprocess

#use "ifconfig" command on your Linux to list all the interfaces on the current computer (network card)
#now we make variables to store the information we will use
interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface + "to" + new_mac)

subprocess.call("ifconfig " + interface + "down", shell=True)
subprocess.call("ifconfig " + interface + "hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + "up", shell=True)