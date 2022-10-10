import csv
import apicallsonaruba_copy

apgroup = "CMC1"

apdatabase = {'ip_address' : '10.102.163.37', 'mac_address' : 'CC:D0:83:C8:0E:0A'}

# def print_urlname(self):
#     print("{}api/login?username={}&password={}".format(self.api_url,self.username,self.password))

  
printurl = apicallsonaruba_copy.api_session("asb2-wlan-mm1","ecyt4t7","WuWOsJagWi17")
printurl.print_urlname("/api/login")





# def readcsvfile():
#     with open('CMC1_AP_macreserv.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             macofap = row['mac_address']
#             # print(macofap)
#             apip = row['addresses']
#             # print(apip)
#             apname = row['fqdn'].replace('.mckesson.com','')
#             # print(apname)
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
