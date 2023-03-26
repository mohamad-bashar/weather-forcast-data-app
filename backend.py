import requests

API_KEY = "7e7591b087e3e3acdd892cfca3afbb37"


def get_data(place, forecast_days):
    nr_values = forecast_days * 8
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    filtered_data = filtered_data[:nr_values]
    return filtered_data
