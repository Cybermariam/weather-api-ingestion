from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

import requests
import json
import logging
url = "https://api.openweathermap.org/data/2.5/weather"

params ={

    "q":"Lagos",
    "appid":api_key,
    "units":"metric"
}

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/weather.log", mode="w")


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def fetch_weather():

    logger.info("Fetching Weather Data")
    try :
      response = requests.get(url , params=params, timeout=5)
      response.raise_for_status()
      data = response.json()

      clean_data = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "wind_speed":data["wind"]["speed"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
      }
      logger.info("Weather Data: %s",clean_data)
      with open("logs/weather_data.json", "w") as output_file:
          json.dump(clean_data, output_file,indent=4)
      logger.info("Weather data saved successfully")
      return clean_data

    except requests.RequestException as e:
        logger.exception(e)
weather = fetch_weather()



