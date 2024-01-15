from melipayamak import Api
username = '09173819218'
password = 'PH5OF'
api = Api(username,password)
sms = api.sms()
to = '09177826532'
_from = '50002710019218'
text = 'خوبی مامانم'
response = sms.send(to,_from,text)
print(response)
