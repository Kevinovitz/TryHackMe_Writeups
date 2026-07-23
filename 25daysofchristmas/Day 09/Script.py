import requests

path = ''
host = 'http://10.10.169.100:3000/'

values = ''

response = requests.get(host + path)
print(response)
json_respons = response.json()
path = "/" + json_respons["next"]
if path != "/end":
	values += json_respons["value"]

print("The flag is " + values)
