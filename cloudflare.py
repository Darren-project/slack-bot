import time
import requests
import json

class Cloudflare:
  def __init__(self, settings):
     self.settings = settings
     self.token = settings.cf_token

  def get_cf_tunnels(self, uuid):
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.cf_api_url}/accounts/{settings.cf_account_id}/cfd_tunnel?uuid={uuid}", headers=headers)
     return response.json()

  def get_whois(self, domain):
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.cf_api_url}/accounts/{settings.cf_account_id}/intel/whois?domain={domain}", headers=headers)
     return response.json()

  def list_dns_record(self, zone_id, search_content):
     settings = self.settings
     headers = {
        'Authorization': f'Bearer {self.token}', 
        'Content-Type': 'application/json'
     }
     response = requests.get(f"{settings.cf_api_url}/zones/{zone_id}/dns_records?name={search_content}", headers=headers)
     return response.json()

