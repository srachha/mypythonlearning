
datacenter = {'spine': [{'routers': ('r1','r2')}, {'switches': ('sw1','sw2')}]}


for key,value in datacenter.items():
    for devicetype in value:
        for devices,names in devicetype.items():
            print(devices,":",names)
