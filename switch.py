#!/usr/bin/env python

from os.path import basename
from sys import argv

from enc_send import send

IP = "192.168.0.123"

if len(argv) < 4 or len(argv) > 5:
    print("Usage: {} [system] [unit] [on|off] [gateway ip]".format(basename(argv[0])))
    print("system: 5 digit binary code")
    print("unit: one char unit code (a, b, c or d), case insensitive")
    print("gateway ip (optional): the ip address of the gateway, overrides the ip set in the script")
    exit(1)

system = argv[1]
unit = argv[2]
state = argv[3]

if len(argv) == 5:
    IP = argv[4]

send(IP, system, unit, state)
