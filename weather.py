# weather.py

def get_weather(city):
    # Simulating weather data (Contains type issues)
    print("Getting weather data for " + city)
    return {'city': city, 'temperature': 25, 'condition': "Sunny"}

def format_weather(weather_data):
    return "The weather in " + weather_data['city'] + " is " + str(weather_data['temperature']) + "°C with " + weather_data['condition'] + " conditions."

# Example usage (contains deliberate issues)
weather_data = get_weather("Sydney")
print(format_weather(weather_data))