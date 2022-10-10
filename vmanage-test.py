import requests
import json
import pprint


class Authentication:
    def get_jsessionid(vmanage_host, username, password):
        api = "/j_security_check"
        base_url = "https://%s"%(vmanage_host)
        url = base_url + api
        payload = {'j_username' : username, 'j_password' : password}

        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            print("No valid JSESSION ID returned\n")
            exit()

    def get_token(vmanage_host, jsessionid):
        headers = {'Cookie': jsessionid}
        base_url = "https://%s"%(vmanage_host)
        api = "/dataservice/client/token"
        url = base_url + api      
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            print(response.text)
            return(response.text)
            
        else:
            return None

def parsename():
    data = requests.get(url=url, headers=header)
    r_json = data.json()['data']
    for each in r_json:
        # print(json.dumps(each, sort_keys=False, indent=9))
        pprint.pprint('Controller Name : ' + each['deviceModel'])


vmanage_host = 'sandbox-sdwan-2.cisco.com'
vmanage_username = 'devnetuser'
vmanage_password = 'RG!_Yw919_83'
vmanage_port = None
base_url = 'https://' + vmanage_host 
api = '/dataservice/system/device/controllers'
url = base_url + api

jsessionid = Authentication.get_jsessionid(vmanage_host, vmanage_username, vmanage_password)
token = Authentication.get_token(vmanage_host, jsessionid)

if token is not None:
    header = {'Content-Type': "application/json",'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    header = {'Content-Type': "application/json",'Cookie': jsessionid}

parsename()

# for eachdevice in r_json:
#     print(eachdevice)
