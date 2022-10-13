import requests

BASE = "https://jhubmodule9.azurewebsites.net" #cloud based API URL taken from the host site

response = requests.put(BASE + 'event/' + "Scotland" + "/10" + "/20kts at 012 degrees")
print(response)
response = requests.put(BASE + 'event/' + "England" + "/20" + "/20kts at 012 degrees")
print(response)
response = requests.put(BASE + 'event/' + "Ireland" + "/40" + "/20kts at 012 degrees")
print(response)
response = requests.put(BASE + 'event/' + "France" + "/50" + "/20kts at 012 degrees")
print(response)
response = requests.get(BASE + 'getevents/')
print(response.json())

input()
response = requests.get(BASE + 'getWind/' + "Scotland")
print(response.json())

input()
response = requests.get(BASE + 'getTemp/' + "Scotland")
print(response.json())

input()
response = requests.get(BASE + 'getTemp/' + "Scotland")
print(response.json())

input()
response = requests.get(BASE + 'deleteOne/' + "France")

input()
response = requests.get(BASE + 'getevents/')
print(response.json())
input()
response = requests.get(BASE + 'deleteAll/')
input()
response = requests.get(BASE + 'getevents/')
print(response.json())



