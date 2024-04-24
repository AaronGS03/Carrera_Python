import requests

api_key= "226e28976f599ab6d15d39b8e8a684af"
params={"q":"Vigo","mode":"json","units":"metric","APPID":api_key}

r=requests.get("https://api.openweathermap.org/data/2.5/weather", params)

print("URL:",r.url)

print("Resultado:\n",r.json())

datos=r.json()

print("Temperatura:",datos["main"]["temp"])