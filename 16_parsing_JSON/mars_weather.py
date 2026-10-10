
import json
import urllib.request
api_key = "uhW8IZRzaF53YcaZklBEgymBAfdDn2Q5cgOkky05"

url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())

    for sol in data["sol_keys"]:
        print("\nMars Day:", sol)

        weather = data[sol]

        print("Temperature:", weather["AT"]["av"], "°C")
        print("Pressure:", weather["PRE"]["av"], "Pa")
        print("Wind Speed:", weather["HWS"]["av"], "m/s")

except Exception as e:
    print("Error:", e)
