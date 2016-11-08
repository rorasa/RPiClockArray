#!/usr/bin/env python

import serial, time, sys

s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"

try:
    s.open()
except serial.SerialException, e:
    sys.stderr.write("Could not open port %r: %s\n" % (s.port, e))
    sys.exit(1)

s.write("$$$ALLL,OFFF\r")
time.sleep(0.5)

while True:
    s.write("F")
    time.sleep(0.5)
