import http.client
rapidApiKey = "" #put your rapid api key here;
ip_address = "" #set your ip address here;

conn = http.client.HTTPSConnection("ip-geolocation-find-ip-location-and-ip-info.p.rapidapi.com")

headers = {
    'x-rapidapi-key': rapidApiKey, 
    'x-rapidapi-host': "ip-geolocation-find-ip-location-and-ip-info.p.rapidapi.com"
}

conn.request("GET", f"/backend/ipinfo/?ip={ip_address}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))