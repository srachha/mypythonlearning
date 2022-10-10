
def get_value(listOfDicts, key):
    for subVal in listOfDicts:
        if key in subVal:
            return subVal[key]

datacenters = {'spine': [{'routers': ('r1','r2')}, {'switches': ('sw1','sw2')}]}


vendors = ['Cisco','Aruba','Juniper']
vendors.append("F5")
vendors.append("Palo Alto")
vendors.insert(0,"Checkpoint")
y = []
for x in vendors:
    x = x.upper()
    y.append(x)
vendors = {"more vendors": y}

print(vendors)
datacenters1 = datacenters['spine'][0]['switches']
print(datacenters['spine'][0]['switches'])
