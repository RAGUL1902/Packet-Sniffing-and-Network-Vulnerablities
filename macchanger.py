#!/usr/bin/env python3

import subprocess
import random
import optparse
import time
import sys
from colorama import Fore, Back, Style

reader = optparse.OptionParser()
reader.add_option("-i", "--interface", dest="interface", help="Enter the interface name")
reader.add_option("-m", "--mac", dest="new_mac", help="Enter the macAddress")
reader.add_option("-o", "--option", dest="option", help="option 1 for custom mac, 2 for random mac")
reader.add_option("-t", "--time", dest="wait_time", help="Enter time in seconds to change random mac")

(values, keys) = reader.parse_args()


def changeMacAddressToSpecified(interface, macAddress):
    if not interface:
        print(Fore.RED, "Enter a interface name using -i, use --help for usage")
        sys.exit(1)
    elif not macAddress:
        print(Fore.RED, "Enter the new mac address -m, use --help for usage")
        sys.exit(1)
    print(Fore.BLUE, "[+] Changing MAC of interface " + interface + " to " + macAddress)
    print(Style.RESET_ALL)

    proc1 = subprocess.Popen(["ifconfig", interface, "down"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.wait()
    (stdout1, stderr1) = proc1.communicate()
    proc2 = subprocess.Popen(["ifconfig", interface, "hw", "ether", macAddress], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    proc2.wait()
    (stdout2, stderr2) = proc2.communicate()
    proc3 = subprocess.Popen(["ifconfig", interface, "up"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc3.wait()
    (stdout3, stderr3) = proc3.communicate()
    if proc1.returncode != 0 or proc2.returncode != 0 or proc3.returncode != 0:
        print(Fore.RED, stderr1)
        print(stderr2)
        print(stderr3)
        print()
        print("Tried MacAddress: " + macAddress + " Tried Interface: " + interface)
        sys.exit(0)
    print(Fore.GREEN, "[+] Changed sucessfully")
    print(Style.RESET_ALL)
    showConfig(interface)


def showConfig(interface):
    print(Fore.YELLOW, "[+] showing ifconfig of " + interface)
    print()
    subprocess.call(["ifconfig", interface])
    print(Style.RESET_ALL)


def changeRandomMacAddress(wait_time, interface):
    if not wait_time:
        print(Fore.RED, "Enter time interval(in secs) using -t for changing mac randomly, use --help for usage")
        sys.exit(1)
    try:
        wait_time = int(wait_time)
    except:
        print(Fore.RED, "Enter a valid time interval using -t")
        sys.exit(1)

    print(Fore.BLUE, "[+] Changing macAddress randomly every " + str(wait_time) + " seconds")
    print(Style.RESET_ALL)
    print(Fore.RED, "[+] Use Ctrl+c to stop")
    print(Style.RESET_ALL)
    try:
        while (True):
            macAddress = getRandomMacAddress()
            changeMacAddressToSpecified(interface, macAddress)
            time.sleep(int(wait_time))

    except KeyboardInterrupt:
        print(Fore.RED, "[+] KeyboardInterupt")
        print("[+] Quitting the program")
        sys.exit(0)


def getRandomMacAddress():
    characters = "1234567890abcdef"
    randomAddress = "00"
    for i in range(5):
        randomAddress += (":" + random.choice(characters) + random.choice(characters))
    return randomAddress


interface = values.interface
macAddress = values.new_mac
option = values.option
wait_time = values.wait_time

if (option == '1'):
    changeMacAddressToSpecified(interface, macAddress)
elif (option == '2'):
    changeRandomMacAddress(wait_time, interface)
else:
    print(Fore.RED, "[+] Enter a valid option(1 or 2) using -o, use --help for usage")
