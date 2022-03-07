import subprocess

hostsfile = open("hostlistping.csv", "r")   # hostlistping.csv is the csv file in thhis folder with the IP to be pinged

lines = hostsfile.readlines()

for line in lines:
    response = subprocess.Popen(["ping", "-n", "1", line.strip()],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    stdout, stderr = response.communicate()

    if (response.returncode == 0):
        status = line.rstrip() + " is Reachable"
    else:
        status = line.rstrip() + " is Not reachable"
    print(status)
