from flask import Flask, render_template, request
from weather import getcity
import weather

app = Flask(__name__)

@app.route('/')
def Hello():
	return render_template('main.html', weather = weather.toprintweather(),
										temperature = weather.gettemperature())

if __name__ == '__main__':
	app.run(debug=True)