import requests

url = "http://localhost:5000/"

payload = "{\"data\": {\"action\": \"open\"},\"user\": {\"name\": \"tomaszew\"}}"
headers = {'content-type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.status_code)
print(response.text)
