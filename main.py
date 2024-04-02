import socket
import subprocess
import sys

from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

t1 = datetime.now()

try:
    for port in range (1, 5000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r = s.connect_ex((remoteServerIP, port))
        if r == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("You Pressed Ctrl + C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Closing Program.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server. Closing Program.")
    sys.exit()

t2 = datetime.now()

totaltime = t2 - t1

print("Scanning Completed in: ", totaltime)