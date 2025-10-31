from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from utils.weather_api import WeatherAPI
from utils.format_data import format_current_and_forecast

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')

API_KEY = os.getenv('OPENWEATHER_API_KEY')
print("DEBUG: Loaded API key:", bool(API_KEY))

if not API_KEY:
    raise RuntimeError('OPENWEATHER_API_KEY not found in environment. Create a .env file and set it.')

weather_api = WeatherAPI(API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    payload = request.json or {}
    city = payload.get('city')
    lat = payload.get('lat')
    lon = payload.get('lon')

    try:
        if city:
            current, forecast = weather_api.get_by_city(city)
        elif lat is not None and lon is not None:
            current, forecast = weather_api.get_by_coords(lat, lon)
        else:
            default = os.getenv('DEFAULT_CITY', 'Delhi,IN')
            current, forecast = weather_api.get_by_city(default)

        formatted = format_current_and_forecast(current, forecast)
        return jsonify({'status': 'ok', 'data': formatted})
    except Exception as e:
        # log exception server-side and return readable message
        print("ERROR in /weather:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
