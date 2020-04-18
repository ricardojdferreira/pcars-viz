import requests as rq

class Crest():
    def __init__(self):
        self.session = rq.Session()
        self.session.trust_env = False
    
    def getWheelsAndTyres(self):
        request = self.session.get("http://localhost:8080/crest/v1/api?wheelsAndTyres=true")
        return request.json()["wheelsAndTyres"]
    