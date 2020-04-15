from flask import Flask, render_template, request
from weather import getcity
import weather
app = Flask(__name__)

@app.route('/')
def Hello():
	return weather.toprintweather()

if __name__ == '__main__':
	app.run(debug=True)