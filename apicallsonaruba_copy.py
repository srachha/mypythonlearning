import json,requests,time,sys

class api_session:
  def __init__(self, api_url, username, password, port=4343, SSL=True, check_ssl=True, verbose=False, retrys=3, retry_wait=0.5):
    if SSL:
      protocol = "https"
    else:
      protocol = "http"
    
    self.session = None
    self.api_token = None
    self.api_url = "{}://{}:{}/v1/".format(protocol,api_url,port)
    self.username = username
    self.password = password
    self.check_ssl = check_ssl
    self.verbose = verbose
    self.retrys = retrys
    self.retry_wait = retry_wait

  def login(self):
    self.session = requests.Session()
    for i in range(1,self.retrys+1):
      if self.verbose:
        print("Verbose: login, try {}".format(str(i)))
      response = self.session.get("{}api/login?username={}&password={}".format(self.api_url,self.username,self.password), verify=self.check_ssl)
      login_data = json.loads(response.text)
      if self.verbose:
        print ("Verbose: {}".format(login_data["_global_result"]["status_str"]))
      if login_data["_global_result"]["status"] == "0":
        self.api_token = login_data["_global_result"]["UIDARUBA"]
        return
      if i == self.retrys:
        if self.verbose:
          print("There was an Error with the login. Please check the credentials.",file=sys.stderr)
          print("Controller-IP: {}, Username: {}".format(self.api_url,self.username),file=sys.stderr)
        raise PermissionError("There was an Error with the login. Please check the credentials of the User >{}< at host >{}<".format(self.username,self.api_url))
      time.sleep(self.retry_wait)

  def logout(self):
    response = self.session.get(self.api_url + "api/logout")
    logout_data = json.loads(response.text)
    self.api_token = None
    if self.verbose:
      print ("Verbose: {}".format(logout_data["_global_result"]["status_str"]))

  def get(self, api_path, config_path=None):
    if self.api_token == None:
      login()
    node_path = None
    if config_path is not None:
      node_path = "&config_path={}".format(config_path)
    else:
      node_path = ""
    response = self.session.get("{}{}?UIDARUBA={}{}".format(self.api_url,api_path,self.api_token,node_path))
    data = json.loads(response.text)
    if self.verbose:
      print ("\nVerbose: " + str(data))
    return data

  def post(self, api_path, data, config_path="/md"):
    if self.api_token == None:
      login()
    response = self.session.post("{}{}?UIDARUBA={}&config_path={}".format(self.api_url,api_path,self.api_token,config_path), json=data)
    data = json.loads(response.text)
    if self.verbose:
      print ("Verbose: {}".format(str(data)))
    return data

  def write_memory(self, config_path):
    node_path = "?config_path=" + config_path
    nothing = json.loads('{}')
    response = self.session.post("{}configuration/object/write_memory{}&UIDARUBA={}".format(self.api_url,node_path,self.api_token),json=nothing)
    data = json.loads(response.text)
    if self.verbose:
      print ("Verbose: {}".format(str(data)))
    return data

  def cli_command(self, command):
    mod_command = command.replace(" ", "+")
    response = self.session.get("{}configuration/showcommand?command={}&UIDARUBA={}".format(self.api_url,mod_command,self.api_token))
    data = json.loads(response.text)
    if self.verbose:
      print ("Verbose: {}".format(str(data)))
    return data
  
  def print_urlname(self,newaction):
    print("{}api/login?username={}&password={}{}".format(self.api_url,self.username,self.password,newaction))

  






