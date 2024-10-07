import requests

# Define your OpenWeatherMap API key here
API_KEY = '595ced3eaa0f8671861199b8f1d06d39'

# OpenWeatherMap API URL
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(location):
    """
    Fetches and displays the weather information for a given location (city name or ZIP code).
    """
    # Define the parameters for the API request
    params = {
        'q': location,         # City name or ZIP code
        'appid': API_KEY,      # Your API key
        'units': 'metric',     # Use 'metric' for Celsius, 'imperial' for Fahrenheit
        'lang': 'en'           # Language of the response
    }

    try:
        # Make the request to the API
        response = requests.get(BASE_URL, params=params)

        # If the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Check if the API returned valid data
            if data.get("cod") != 200:
                print(f"Error: {data.get('message')}")
                return
            
            # Extract relevant weather data from the JSON response
            city_name = data['name']
            country = data['sys']['country']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_condition = data['weather'][0]['description']
            feels_like = data['main']['feels_like']
            wind_speed = data['wind']['speed']

            # Display the weather information
            print(f"\nWeather in {city_name}, {country}:")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_condition.capitalize()}")
            print(f"Wind Speed: {wind_speed} m/s\n")

        else:
            # If the API returned a status code other than 200, handle the error
            print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Catch any network-related or request errors
        print(f"Error: A network error occurred. {e}")

def get_user_input():
    """
    Prompts the user for the location and ensures that the input is valid.
    """
    while True:
        location = input("Enter the city name or ZIP code: ").strip()
        if location:
            return location
        else:
            print("Error: You must enter a location.")

def main():
    """
    Main function to handle user input and fetch weather data.
    """
    location = get_user_input()  # Get user input for location
    get_weather(location)        # Fetch and display the weather information

if __name__ == "__main__":
    main()

