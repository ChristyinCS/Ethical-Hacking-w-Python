#this is more secure code to control users input
import subprocess

#using input from the user to automate script (python3)
# if you want to use it for python2 simply add "raw_" before "input"
interface = input("interface: ")
new_mac = input("new MAC: ")

print("[+] Changing MAC address for " + interface + "to" + new_mac)

#this is more secure version of the code, because Python knows the interface and down are all part of the same command
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])