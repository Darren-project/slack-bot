import os
import sys

# Add parent directory to sys.path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import adapter
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
