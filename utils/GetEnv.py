import os

class GetEnv:
    
    def __init__(self):
        self.env = os.environ

    def get(self, envvar):
        if envvar in self.env:
            return self.env[envvar]
        Exception(envvar + " is not set")