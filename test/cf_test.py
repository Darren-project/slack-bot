import os
import sys
# Add parent directory to sys.path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import adapter
import cloudflare
class Settings:
    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name):
        # If the attribute is not found, return None or raise an AttributeError
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError(f"'Settings' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name == '_attributes':
            # Directly set the internal _attributes dictionary
            super().__setattr__(name, value)
        else:
            # Set the attribute in the _attributes dictionary
            self._attributes[name] = value

# Instantiate the Settings class
settings = Settings()
dbset = adapter.get_settings()

for key in dbset:
    setattr(settings, key, dbset[key])


cf = cloudflare.Cloudflare(settings)

print("-------- Get Tunnels --------")
print(cf.get_cf_tunnels(settings.cf_tunnel_uuid))
print("\n")

print("-------- Get whois --------")
print(cf.get_whois("darrenmc.xyz"))
print("\n")

print("-------- Create dns record (Correct) --------")
dns_c = cf.create_dns_record(settings.cf_zone_id, "cf_test_correct.darrenmc.xyz", "cname.darrenmc.xyz", "CNAME")
print(dns_c)
print("\n")

print("-------- Create dns record (Incorrect) --------")
dns_inc = cf.create_dns_record(settings.cf_zone_id, "cf_test_incorrect.darrenmc.xyz", "fake_cname.darrenmc.xyz", "CNAME")
print(dns_inc)
print("\n")

print("-------- Get dns records with correct hostname --------")
print(cf.list_dns_record(settings.cf_zone_id, "cname.darrenmc.xyz"))
print("\n")


d_id = dns_inc["result"]["id"]
print("-------- Update dns records with correct hostname --------")
print(cf.update_dns_record(settings.cf_zone_id, "cf_test_corrected.darrenmc.xyz", "cname.darrenmc.xyz", "CNAME", d_id))
print("\n")

print("-------- Get dns records with correct hostname --------")
print(cf.list_dns_record(settings.cf_zone_id, "cname.darrenmc.xyz"))
print("\n")


d_id_2 = dns_c["result"]["id"]
print("-------- Delete both dns record --------")
print(cf.delete_dns_record(settings.cf_zone_id, d_id))
print("\n")
print(cf.delete_dns_record(settings.cf_zone_id, d_id_2))
print("\n")

print("-------- Get dns records with correct hostname --------")
print(cf.list_dns_record(settings.cf_zone_id, "cname.darrenmc.xyz"))
print("\n")
