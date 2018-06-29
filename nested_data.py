#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    interfaces_data = json.loads(file.read())
#     GigabitEthernet1: 198.18.134.11 255.255.192.0
# GigabitEthernet2: 172.16.255.1 255.255.255.0
# Loopback0: 10.0.0.1 255.255.255.255
# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
for interface in interfaces_data["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"] + ": ", end="")
    for address in interface["ietf-ip:ipv4"]["address"]:
        print(address["ip"], address["netmask"])


