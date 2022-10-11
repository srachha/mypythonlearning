# from pythonping import ping

# def pingtest(host,pingcount):
#     ping(host,verbose=True,count=pingcount)
    
devices = ['8.8.8.8','1.1.1.1']    
# for i in devices:
#     pingtest(i,10)


import subprocess

def ping_test(host):

    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' %ip)

        if ping_test == 0:
            print(ip + " is not reachable")
        else:
            print(ip + " is reachable")

ping_test(devices)