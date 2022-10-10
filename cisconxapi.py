
import requests
import json

client_cert_auth=False
switchuser='admin'
switchpassword='Admin_1234!'

url='https://sandbox-nxos-1.cisco.com/'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh int status",
      "version": 1
    },
    "id": 1
  }
]

if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
else:
    url='https://sandbox-nxos-1.cisco.com/'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()

# url='http://sandbox-nxos-1.cisco.com/'
# switchuser='admin'
# switchpassword='Admin_1234!'

# myheaders={'content-type':'application/json-rpc'}
# payload=[
#  {
#    "jsonrpc": "2.0",
#    "method": "cli",
#    "params": {
#      "cmd": "show interface status",
#      "version": 1.2
#    },
#    "id": 1
#  }
# ]

# response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
# import pandas as pd

# response = {
#   "jsonrpc": "2.0",
#   "result": {
#     "body": {
#       "TABLE_interface": {
#         "ROW_interface": [
#           {
#             "interface": "mgmt0",
#             "name": "DO NOT TOUCH CONFIG ON THIS INTERFACE",
#             "state": "connected",
#             "vlan": "routed",
#             "duplex": "full",
#             "speed": "1000",
#             "type": "--"
#           },
#           {
#             "interface": "Ethernet1/1",
#             "state": "connected",
#             "vlan": "trunk",
#             "duplex": "full",
#             "speed": "1000",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/2",
#             "state": "connected",
#             "vlan": "trunk",
#             "duplex": "full",
#             "speed": "1000",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/3",
#             "state": "connected",
#             "vlan": "1",
#             "duplex": "full",
#             "speed": "1000",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/4",
#             "state": "connected",
#             "vlan": "1",
#             "duplex": "full",
#             "speed": "1000",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/5",
#             "name": "L3 Link",
#             "state": "disabled",
#             "vlan": "1",
#             "duplex": "auto",
#             "speed": "auto",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/6",
#             "state": "notconnect",
#             "vlan": "1",
#             "duplex": "auto",
#             "speed": "auto",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/7",
#             "state": "notconnect",
#             "vlan": "1",
#             "duplex": "auto",
#             "speed": "auto",
#             "type": "10g"
#           },
#           {
#             "interface": "Ethernet1/8",
#             "state": "notconnect",
#             "vlan": "1",
#             "duplex": "auto",
#             "speed": "auto",
#             "type": "10g"
#           }]}}}}


# # #bodyresponse = response['result']['body']['TABLE_interface']['ROW_interface']

f = open("Interface_status.txt","w")

for allinterfaces in response['result']['body']['TABLE_interface']['ROW_interface']: 
    # intname =  
#    for eachparam in allinterfaces:
#        print(eachparam)
    if allinterfaces['state'] == "connected":
        print(allinterfaces['interface'] + " is Up\n")
        f.write(allinterfaces['interface'] + " is Up\n")
    else:
        print(allinterfaces['interface'] + " is Down\n")
        f.write(allinterfaces['interface'] + " is Down\n")

f.close()
#    for {keys,values} in allinterfaces.items():
#        if keys['state'] == 'notconnect'
#            print(keys,":",values)


# for allinterfaces in response['result']['body']['TABLE_interface']['ROW_interface']: 
#     intname = allinterfaces['interface'] 
#     status = allinterfaces['state']
# #    for eachparam in allinterfaces:
# #        print(eachparam)
#     if allinterfaces['state'] == "connected":
#         data = pd.DataFrame(intname,status)
#         data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)  
#     # else:
#     #     data = pd.DataFrame(intname,status)

      