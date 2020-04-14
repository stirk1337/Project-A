from flask import Flask
from weather import getcity
import weather
app = Flask(__name__)

@app.route('/')
def Hello():
	currcity = getcity()
	t = weather.weather()
	return currcity + " " + str(t[0])

if __name__ == '__main__':
	app.run(debug=True)