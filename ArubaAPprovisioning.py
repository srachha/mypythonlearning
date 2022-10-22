import csv,subprocess
import json,requests
import apicallsonaruba_copy


controller_url = "/md/McKesson_NA/MMS/CMC1/20:4c:03:be:eb:d6"
apgroup = "CMC1" #define the name of the site

# apdatabase = {'ip_address' : '10.102.163.37', 'mac_address' : 'CC:D0:83:C8:0E:0A'}

# def print_urlname(self):
#     print("{}api/login?username={}&password={}".format(self.api_url,self.username,self.password))

  
session = apicallsonaruba_copy.api_session("mmname","username","password")
# session.print_urlname("/api/login/configure")

session.login()

def getapdatabase(siteapipaddress): #Reading the AP database file from the MM
    data = session.cli_command("show ap database long")
    # data = json.load(requestapdatabase.text)
    finalap = []
    for eachap in data['AP Database']:    
        if eachap["IP Address"].startswith(siteapipaddress):
            finalap.append(eachap)
    print(finalap)
    return finalap
    
            
def parseapdata(): #Reading the CSV File for the AP MAC reservation
    with open('CMC1_AP_macreserv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        eachaparg = getapdatabase("10.102.163.")
        newapname = []
        # print(eachaparg)
        for row in reader:
            macofap,apip,apname = row['mac_address'].lower(),row['addresses'],row['fqdn'].replace('.mckesson.com','')
            apfeature = [macofap,apip,apname]
            for eachrow in eachaparg:
                # print(eachrow)
                if apfeature[0] == eachrow["Wired MAC Address"] and apfeature[1] == eachrow['IP Address']:
                    if eachrow["Group"] == 'default':
                        provisionapname(apfeature)
                        return newapname.append(apfeature[1])
        for eachhost in newapname:
            pingtestresult = ping_test(apfeature[1])
            if pingtestresult == "Device is Up":
                provisionapgroup(apfeature)
            else:
                
            




def ping_test(host):
    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' %ip)
        if ping_test == 0:
            return "Device is Up"
        else:
            return "Device is still Down"

def provisionapname(apfeature):      #Method to call provision each AP which is in Default Group
    rename_body = {"wired-mac": {},"new-name": {}}.format(apfeature[0],apfeature[2])
    session.post("/object/ap_rename",data=rename_body,config_path=controller_url)

def provisionapgroup(apfeature):
    regroup_body = {"wired-mac": {},"ap-name": {},"new-group": {}}.format(apfeature[0],apfeature[2],apgroup)
    session.post("/object/ap_regroup",data=regroup_body,config_path=controller_url)


parseapdata() 
