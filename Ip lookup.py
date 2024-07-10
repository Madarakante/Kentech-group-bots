import requests
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=6dd403fcf31644198eb2b6d4996086b2&ip_address=2a0d:3344:12ac:cf10:3084:f5c4:5381:42bc&fields= country,city")
print(response.status_code)
print(response.content)