import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.key = api_key
        self.base_current = 'https://api.openweathermap.org/data/2.5/weather'
        self.base_forecast = 'https://api.openweathermap.org/data/2.5/forecast'  # free 5-day/3-hour

    def get_by_city(self, city_name):
        # current weather
        params = {'q': city_name, 'appid': self.key, 'units': 'metric'}
        r1 = requests.get(self.base_current, params=params, timeout=10)
        r1.raise_for_status()
        current = r1.json()

        # forecast (5 days, 3-hour interval)
        r2 = requests.get(self.base_forecast, params=params, timeout=10)
        r2.raise_for_status()
        forecast = r2.json()

        return current, forecast

    def get_by_coords(self, lat, lon):
        params = {'lat': lat, 'lon': lon, 'appid': self.key, 'units': 'metric'}
        r1 = requests.get(self.base_current, params=params, timeout=10)
        r1.raise_for_status()
        current = r1.json()

        r2 = requests.get(self.base_forecast, params=params, timeout=10)
        r2.raise_for_status()
        forecast = r2.json()

        return current, forecast
