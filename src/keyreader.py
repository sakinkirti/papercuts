import yaml

class KeyReader:
    
    def __init__(self, keys:str):
        self.keys = yaml.safe_load(keys)
        
    def get(self, key:str):
        return self.keys[key]