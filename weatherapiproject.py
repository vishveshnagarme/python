import requests

my_api_key = "$$$"
my_city = input(" Welcome to the Weather App!!! created by Vishvesh Nagar!!! What city do you want to check? ")

web_link = "http://api.openweathermap.org/data/2.5/weather?q=" + my_city + "&appid=" + my_api_key + "&units=metric"

print("Fetching weather...")
the_response = requests.get(web_link)

if the_response.status_code == 200:
    
    weather_dictionary = the_response.json()
    
    main_box = weather_dictionary['main']
    the_temperature = main_box['temp']
    the_humidity = main_box['humidity']
    
    weather_list = weather_dictionary['weather']
    first_weather_item = weather_list[0]
    the_description = first_weather_item['description']

    print("--- HERE IS YOUR WEATHER ---")
    print("City:", my_city)
    print("Temperature:", the_temperature, "Celsius")
    print("Conditions:", the_description)
    print("Humidity:", the_humidity, "%")
    print(" Visit vishvesh.nagar.me for more such stuff.")

else:
    print("Oops! Something went wrong!")