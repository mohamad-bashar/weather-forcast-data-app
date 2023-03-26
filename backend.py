import requests

API_KEY = "7e7591b087e3e3acdd892cfca3afbb37"


def get_data(place, forecast_days, kind):
    nr_values = forecast_days * 8
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
