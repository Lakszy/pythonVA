import requests
import json
import pyttsx3
city=input("Enter the name of the City: ")

url = f"https://api.weatherapi.com/v1/current.json?key=d7c0218eca0847e6a0a150311230109&q={city}"

r= requests.get(url)
# loads the string
wdic= json.loads(r.text)
# diving to the api
w= wdic["current"]["temp_c"]


x=f"The temp in {city} is {w} degree celsius"
engine = pyttsx3.init()
engine.say(x)
engine.runAndWait()
print(w,"°C")