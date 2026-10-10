import requests

url = "https://api.currencylayer.com/live"
params = {
    "access_key": "8cbdaaad2789acaba122c1df46f0d184",
    "arjun" : "332"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

print(data)