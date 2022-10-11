import csv
import json,requests
import apicallsonaruba_copy

apgroup = "CMC1" #define the name of the site

# apdatabase = {'ip_address' : '10.102.163.37', 'mac_address' : 'CC:D0:83:C8:0E:0A'}

# def print_urlname(self):
#     print("{}api/login?username={}&password={}".format(self.api_url,self.username,self.password))

  
# session = apicallsonaruba_copy.api_session("asb2-wlan-mm1","ecyt4t7","WuWOsJagWi17")
# session.print_urlname("/api/login/configure")

# session.login()

def getapdatabase(siteapipaddress): #Reading the AP database file from the MM
    f = open('apdatabasefile.json')
    data = json.load(f)
    finalap = []
    for eachap in data['AP Database']:    
        if eachap["IP Address"].startswith(siteapipaddress):
            finalap.append(eachap)
    return finalap
            
def readcsvfile(): #Reading the CSV File for the AP MAC reservation
    with open('CMC1_AP_macreserv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        eachaparg = getapdatabase("10.102.163.")
        # print(eachaparg)
        for row in reader:
            macofap,apip,apname = row['mac_address'].lower(),row['addresses'],row['fqdn'].replace('.mckesson.com','')
            apfeature = [macofap,apip,apname]
            for eachrow in eachaparg:
                # print(eachrow)
                if apfeature[0] == eachrow["Wired MAC Address"] and apfeature[1] == eachrow['IP Address']:
                    if eachrow["Group"] == 'default':
                        provisionap(apfeature)
                        return eachrow
        

def provisionap(apfeature):      #Method to call provision each AP which is in Default Group
    print("provision-ap ap-group " + apgroup)
    print("provision-ap ap-name " + apfeature[2])

readcsvfile()    
