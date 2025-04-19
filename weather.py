import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url).json()
    if response.get("main"):
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {description}."
    else:
        return "Sorry, I couldn't fetch the weather for that location."
