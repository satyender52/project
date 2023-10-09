import requests
import json
city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=897aa6c43b694289ace202023232709&q={city}"
r = requests.get(url)
print(r.text)
weatherdic = json.loads(r.text)
print(weatherdic["current"]["temp_c"])

import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
text = weatherdic
speak.Speak(text)