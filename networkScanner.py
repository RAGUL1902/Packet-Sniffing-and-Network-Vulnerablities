#!/usr/bin/env python3

import scapy.all as scapy
import re
from colorama import Fore, Back, Style


def setIpPattern():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    return ip_add_range_pattern

def getInput(ip_add_range_pattern):
    while True:
        print(Fore.BLUE,"[+] Please enter the ip address range to scan (example: 192.168.1.0/24): ",end='')
        ip_add_range_entered =  input()
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(Fore.GREEN,f"[+] {ip_add_range_entered} is a valid ip address range")
            break
        else:
            print(Fore.RED,"[+] Enter a valid IP Range")
            print(Style.RESET_ALL)
    return ip_add_range_entered


def startArPing(ip_add_range_entered):
    arp_result = scapy.arping(ip_add_range_entered)



ip_range_pattern = setIpPattern()
ip_range_entered = getInput(ip_range_pattern)
startArPing(ip_range_entered)
