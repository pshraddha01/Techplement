import time
import requests

API_KEY = "565c19562032beb685f6a465a5e161ea"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
favorite_cities = []

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print("Error: Unable to fetch weather data")
        return None

def add_favorite_city(city):
    favorite_cities.append(city)
    print(f"{city} added to favorites.")

def remove_favorite_city(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in favorites.")

def display_favorite_cities():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

def display_weather(weather_data):
    if weather_data:
        print("Weather Information for", weather_data["name"])
        print("Temperature:", weather_data["main"]["temp"], "°C")
        print("Humidity:", weather_data["main"]["humidity"], "%")
        print("Description:", weather_data["weather"][0]["description"])
    else:
        print("No weather data available")

def refresh_weather(city):
    while True:
        weather_data = get_weather(city)
        display_weather(weather_data)
        time.sleep(15)  # Refresh every 15 seconds

def main():
    while True:
        print("\n1. Check Weather by City Name")
        print("2. Add City to Favorites")
        print("3. Remove City from Favorites")
        print("4. Display Favorites")
        print("5. Auto-refresh weather")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_data = get_weather(city)
            if weather_data:
                display_weather(weather_data)
        elif choice == "2":
            city = input("Enter city name to add to favorites: ")
            add_favorite_city(city)
            display_favorite_cities()
        elif choice == "3":
            city = input("Enter city name to remove from favorites: ")
            remove_favorite_city(city)
            display_favorite_cities()
        elif choice == "4":
            display_favorite_cities()
        elif choice == "5":
            refresh_weather(city)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
