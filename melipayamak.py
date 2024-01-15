
from rest import*
from soap import*
from restAsync import*
from soapAsync import*



class Api:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sms(self, _method="rest", _type=""):
        if _method == "rest":
            if _type == "async":
                return RestAsync(self.username, self.password)
            else:
                return Rest(self.username, self.password)
        else:
            if _type == "async":
                return SoapAsync(self.username, self.password)
            else:
                return Soap(self.username, self.password)
