import pyowm
import json, requests

def getcity():
	send_url = "http://api.ipstack.com/check?access_key=c8cd22fb1b14683907b08be42a536a89"
	geo_req = requests.get(send_url)
	geo_json = json.loads(geo_req.text)
	return geo_json['city']

def weather():
	try:
		currcity = getcity()
		weather = []
		owm = pyowm.OWM('fbee165d5e5cc25bcfa5b036701304f5')
		city = owm.weather_at_place(currcity)
		w = city.get_weather()
		weather.append(w.get_temperature('celsius')['temp'])
		weather.append(w.get_detailed_status())
		return weather
	except:
		return ["NA"]

def toprintweather():
	currcity = getcity()
	t = weather()
	return currcity + " " + str(t[0])