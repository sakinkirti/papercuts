import yaml

class KeyReader:
    
    def __init__(self, keys:str):
        with open(keys, 'r') as stream:
            self.keys = yaml.safe_load(stream)
        
    def get(self, key:str):
        return self.keys[key]