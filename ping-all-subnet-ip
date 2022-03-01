#this simple script verifies all IP in a subnet and gives you feedback about pinging or not responding status of the devices connected to

import ipaddress
from subprocess import Popen, PIPE

net4 = ipaddress.ip_network('10.42.159.0/24')
for x in net4.hosts():
    x = str(x)
    hostup = Popen(["ping", "-c1", x], stdout=PIPE)
    output = hostup.communicate()[0]
    val1 = hostup.returncode
    if val1 == 0:
        print(x, "is pinging")
    else:
        print(x, "is not responding")
