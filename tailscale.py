import time
import requests
import json

class Tailscale:
  def __init__(self, settings):
     self.settings = settings
     self.token = ''
     self.lasttoken = 0

  def get_token(self):
    if not self.lasttoken:
        pass
    if int(time.time()) - self.lasttoken > 3600:
       pass
    else:
       print("[Tailscale] Using existing access token")
       return
    print("[Tailscale] Requested new access token")
    settings = self.settings
    data = {
        'client_id': settings.ts_cid,
        'client_secret': settings.ts_cs
    }
    response = requests.post(settings.ts_api_oauth_url, data=data)
    self.token = json.loads(response.text)['access_token']
    self.lasttoken = int(time.time())

  def get_servers(self):
     self.get_token()
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.ts_api_url}/tailnet/{settings.ts_name}/devices?fields=all", headers=headers)
     return response.json()

  def get_dns(self):
     self.get_token()
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.ts_api_url}/tailnet/{settings.ts_name}/dns/nameservers", headers=headers)
     return response.json()
