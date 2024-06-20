import time
import requests
import json

class Portainer:
  def __init__(self, settings):
     self.settings = settings
     self.token = ''

  def _token_get(self):
      settings = self.settings
      body = {
           "password": settings.portainer_pass,
           "username": settings.portainer_user
      }
      response = requests.post(f"{settings.portainer_api_url}/auth", json=body, verify=False)
      self.token = response.json()["jwt"]

  def get_envs(self):
     settings = self.settings
     self._token_get()
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.portainer_api_url}/endpoints", headers=headers, verify=False)
     return response.json()
