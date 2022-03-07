import os

hostnames = [
    '10.42.171.1',
    '10.42.169.249',
    '10.44.109.137',
    '10.42.158.184',
]

for hostname in hostnames:
    response = os.system('ping -c 2 ' + hostname)
    if response == 0:
        print(hostname, 'is up')
    else:
        print(hostname, 'is down')

