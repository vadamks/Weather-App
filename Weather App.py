import requests

# Retrieving and formatting date

from datetime import datetime

# Get weather data from API and create dictionary to filter results
def get_weather_data(location):

    # Add your API key here

    api_key = " "
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    response = requests.get(url)
    weather = response.json()

    return {

        "id": weather["weather"][0]["id"],
        "condition": weather["weather"][0]["main"],
        "description": weather["weather"][0]["description"],
        "temp": int(weather["main"]["temp"])
    }

# Dictionary of clothes and weather properties

my_wardrobe = {

        "Long raincoat with padding and taped seams": {
            "type": "coat",
            "warmth": "warm",
            "waterproof": True,
        },
        "Canvas coat lined with fleece": {
            "type": "coat",
            "warmth": "medium",
            "waterproof": False,
        },
        "Pea coat": {
            "type": "coat",
            "warmth": "warm",
            "waterproof": False,
        },
        "Leather boots": {
            "type": "shoes",
            "warmth": "warm",
            "waterproof": False,
        },
        "Basic trainers": {
            "type": "shoes",
            "warmth": "medium",
            "waterproof": False,
        },
        "Summer sandals": {
            "type": "shoes",
            "warmth": "very light",
            "waterproof": False,
        },
        "Denim jacket": {
            "type": "coat",
            "warmth": "light",
            "waterproof": False,
        },
        "Basic rain jacket with hood": {
            "type": "coat",
            "warmth": "medium",
            "waterproof": True,
        },
        "Packable jacket": {
            "type": "coat",
            "warmth": "light",
            "waterproof": False,
        },
        "Wellies": {
            "type": "shoes",
            "warmth": "medium",
            "waterproof": True,
        },
        "Ski jacket with fur hood": {
            "type": "coat",
            "warmth": "very warm",
            "waterproof": True,
        },
        "Wool and feather coat": {
            "type": "coat",
            "warmth": "very warm",
            "waterproof": False,
        },
    }

# Dictionary of warmth temperature scales

temperature_clothing_scale = {
    "very light": (25, 58),
    "light": (17, 25),
    "medium": (12, 17),
    "warm": (0, 12),
    "very warm": (-40, 0)
}

# Dictionary of rephrased conditions

new_weather_condition = {
    "Rain": "it's rainy",
    "Snow": "it's snowy",
    "Clear": "there are clear skies",
    "Clouds": "it's cloudy",
    "Drizzle": "there is some drizzle",
    "Thunderstorm": "there is a thunderstorm",
    "Mist": "it's misty",
    "Smoke": "it's smokey",
    "Haze": "it's hazy",
    "Dust": "there is dust in the air",
    "Fog": "it's foggy",
    "Sand": "there is sand in the air",
    "Ash": "there is ash in the air",
    "Squall": "there is a squall",
    "Tornado": "there is a tornado"
}

# Get weather for user location
def get_user_location_weather():

    user_location = input("Please enter the city you would like to know the weather in: ")

    user_weather_data = get_weather_data(user_location)

    return user_location, user_weather_data

# Getting and formatting date

def get_date():

    get_datetime = datetime.now()
    current_datetime = get_datetime.strftime("%d/%m/%Y")
    long_current_datetime = get_datetime.strftime("%A %d of %B")

    return current_datetime, long_current_datetime

# Starting main application

def run():

    #Loop for continuous use

    need_weather = "yes"
    while need_weather == "yes":

        # Empty list for appropriate clothes

        clothing_for_weather = []

        #Get date

        current_datetime, long_current_datetime = get_date()

        # Get user location and weather data

        user_location, user_weather_data = get_user_location_weather()

        # Concatenate data into a string and slice date

        user_weather_output = current_datetime + user_location + user_weather_data["condition"] + str(user_weather_data["temp"])

        current_date = user_weather_output[:10]

        # Mapping weather condition to make them more readable

        if user_weather_data["condition"] in new_weather_condition:
            rephrased_weather = new_weather_condition[user_weather_data["condition"]]

        # Printing final results for user

        print(f"Today ({current_date}), {rephrased_weather} in {user_location}. The temperature is {user_weather_data['temp']}°C.")

        # Asking user if they'd like clothing recommendations
        # Conditional structure to get appropriate clothes in wardrobe

        clothing_recommendation = input("Do you need help deciding what to wear for today's weather? ").lower()
        if clothing_recommendation == "yes":
            for clothing_name, clothing_info in my_wardrobe.items():
                temperature_range = temperature_clothing_scale.get(clothing_info["warmth"])
                if user_weather_data["id"] in range(200, 702) or user_weather_data["id"] == 741:
                    if clothing_info["waterproof"] and temperature_range[0] <= user_weather_data["temp"] <= temperature_range[1]:
                        clothing_for_weather.append(clothing_name)
                elif user_weather_data["id"] in range(800, 805):
                    if not clothing_info["waterproof"] and temperature_range[0] <= user_weather_data["temp"] <= temperature_range[1]:
                        clothing_for_weather.append(clothing_name)
                else:
                    print("Weather may be hazardous, take caution if going outside.")

            #Print results in a user-friendly way

            if clothing_for_weather:
                clothing_for_weather = ", ".join(clothing_for_weather)
                print(f"You have the option of wearing: {clothing_for_weather}")
            else:
                print("There's nothing in your wardrobe that matches the weather outside.")
                clothing_for_weather = "Currently no suitable clothing in your wardrobe."

        elif clothing_recommendation == "no":
            print("No problem.")

        # Writing both weather and clothing results to file

        with open("weather_report.txt", "w") as weather_results:
            weather_results.write(f"Weather in {user_location} on {long_current_datetime}!\nIn {user_location}, {rephrased_weather} and the temperature is {user_weather_data['temp']}°C.\nToday you could choose to wear: {clothing_for_weather}")
            weather_results.close()

        # Asking user whether they'd like to continue or close app loop

        need_weather = input("Would you like to find out the weather in a new location? ").lower()
        if need_weather == "no":
            print("No problem, come back soon and enjoy your day!")

# Calling function to run app

run()
