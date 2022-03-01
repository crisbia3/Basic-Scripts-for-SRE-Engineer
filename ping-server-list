#this simple script allows to ping a list of different IP in several subnets or public IP

import subprocess
def ping_test (host):

    reached = []                           
    not_reached = []                       

    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' % ip)       
        if ping_test == 0:                  
            reached.append(ip)

        else:
            not_reached.append(ip)                             

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
hosts = ["10.42.171.1","192.168.2.2","www.google.com",]         
ping_test (hosts)
