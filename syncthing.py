import time
import requests
import json

class Syncthing:
  def __init__(self, settings):
     self.settings = settings
     self.token = settings.syncthing_key

  def get_status(self):
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.syncthing_api_url}/system/status", headers=headers)
     return response.json()

  def get_health(self):
     settings = self.settings
     headers = {
               'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.syncthing_api_url}/noauth/health", headers=headers)
     return response.json()


