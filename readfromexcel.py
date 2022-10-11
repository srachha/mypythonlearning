import csv
from itertools import count
import json,requests
import apicallsonaruba_copy

apgroup = "CMC1"

# apdatabase = {'ip_address' : '10.102.163.37', 'mac_address' : 'CC:D0:83:C8:0E:0A'}

# def print_urlname(self):
#     print("{}api/login?username={}&password={}".format(self.api_url,self.username,self.password))

  
# session = apicallsonaruba_copy.api_session("asb2-wlan-mm1","ecyt4t7","WuWOsJagWi17")
# session.print_urlname("/api/login/configure")

# session.login()

def getapdatabase(siteapipaddress):
    f = open('apdatabasefile.json')
    data = json.load(f)
    finalap = []
    for eachap in data['AP Database']:  
        # print(eachap)
        if eachap["IP Address"].startswith(siteapipaddress):
            
            # print(eachap)
            finalap.append(eachap)

    return finalap
            

# print(getapdatabase("10.102.163."))
def readcsvfile():
    with open('CMC1_AP_macreserv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        eachaparg = getapdatabase("10.102.163.")
        # print(eachaparg)
        for row in reader:
            macofap,apip,apname = row['mac_address'].lower(),row['addresses'],row['fqdn'].replace('.mckesson.com','')
            apfeature = [macofap,apip,apname]
            # print(apfeature)
            # print(apfeature)
            # eachaparg = getapdatabase("10.102.163.")
            # print(eachaparg)
            # print(apfeature[0])
            for eachrow in eachaparg:
                # print(eachrow)
                if apfeature[0] == eachrow["Wired MAC Address"] and apfeature[1] == eachrow['IP Address']:
                    if eachrow["Group"] == 'default':
                        provisionap(apfeature)
                        return eachrow
        

def provisionap(apfeature):      
    print("provision-ap ap-group " + apgroup)
    print("provision-ap ap-name " + apfeature[2])

readcsvfile()    

# print(json_object)
# def getapdatabase(ipaddress):
#     with open('apdatabasefile.json', 'r') as openfile:
#      # Reading from json file
#         apdata = json.load(openfile)
#         ipaddressofap = apdata[0]["IP Address"]
#         print(ipaddressofap)
#         if ipaddressofap.startswith(ipaddress):
#             print(apdata["Wired MAC Address"])


# getapdatabase('10.102.163.')

# # def readcsvfile():
# #     with open('CMC1_AP_macreserv.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             macofap,apip,apname = row['mac_address'],row['addresses'],row['fqdn'].replace('.mckesson.com','')
#             # # print(macofap)
#             # apip = row['addresses']
#             # # print(apip)
#             # apname = row['fqdn'].replace('.mckesson.com','')
#             # # print(apname)
#             apfeature = [macofap,apip,apname]
#         # print(apfeature)
#         # return(apfeature)
#             # print(macofap)
#             provisionap(apfeature)
        

# def provisionap(apfeature):            
#     if apfeature[0] == apdatabase['mac_address'] and apfeature[1] == apdatabase['ip_address']:
#         print("provision-ap ap-group " + apgroup)
#         print("provision-ap ap-name " + apfeature[2])

# readcsvfile()
# provisionap(macofap,apip,apname)
