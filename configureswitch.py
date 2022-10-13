import json
import requests
from urllib3 import Timeout


url = "http://10.254.77.1:80/rest/v3/"
# command = "show ip"

def switchlogin(host,username,password):
    fullurl = url + "login-sessions"
    data = {"userName":username,"password":password} 
    r = requests.Session()
    urlsession = r.post(fullurl, data=data, timeout=1)
    if urlsession.status_code != 200:
        print("The API Login session to {} is unsuccessfull. Session Response={}".format(host,urlsession.status_code))
    else:
        responsecookie = urlsession["cookie"]
        print(responsecookie)
        return responsecookie

def commandsinput(command):
    c = {"cmd":command}
    sessioncookie = switchlogin("10.254.77.1","ecyt4t7","WuWosJagWi17") 
    r = requests.post(url+ 'cli', header={"cookie":sessioncookie}, data=json.dumps(c), timeout=1)
    print(r.text)


def configureswitch():
    with open('pln9configuration.txt','r') as f:
        linecommand = f.readlines()
        commandsinput(linecommand)
    print(commandsinput)


configureswitch()
             
# switchlogin("10.254.77.1","ecyt4t7","WuWosJagWi17"