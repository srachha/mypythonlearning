import requests

Class facebooklogintry:
    def __init__(self, username, password):
        self.user = username
        self.password = password
        self.urlfb = "www.facebook.com" + {}.format(username,password)
     
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

data = '{"userName":"test", "password":"test"}'

response = requests.post('http://10.100.167.104:80/rest/v1/login-sessions', headers=headers, data=data)

