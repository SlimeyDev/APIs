from fastapi import FastAPI
from random import choice
import requests
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()

@app.get("/random")
async def random_symbol():
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]\;',./{}|:\"<>"
    random_letter = choice(alphabet)
    return {"letter": random_letter}

@app.get("/weather")
async def get_weather(place: str):
    load_dotenv()
    key = os.getenv("W_KEY")
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": key,
        "q": place
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        pressure = data["current"]["pressure_mb"]
        wind_degree = data["current"]["wind_degree"]
        wind_speed_kph = data["current"]["wind_kph"]
        temp_feelslike = data["current"]["feelslike_c"]
        last_updated = data["current"]["last_updated"]
        city_o = data["location"]["name"]
        country = data["location"]["country"]
        output = {
            "last_updated": last_updated,
            "temp":temp,
            "temp_feelslike":temp_feelslike,
            "pressure_mb":pressure,
            "wind_degree":wind_degree,
            "wind_speed_kph":wind_speed_kph,
            "city":city_o,
            "country":country
        }
        return output
    else:
        data = response.json()
        print(data)
        return {"ERROR":"An error occurred!", "CODE":response.status_code}

# @app.get("/lyrics")
# async def get_lyrics(artist: str, track: str):
#     url = "https://scrapesoft-music-lyrics.p.rapidapi.com/api/lyrics"

#     querystring = {"access_token":"{accessToken}"}

#     payload = {
#         "songName": "ENTER_SONG_NAME",
#         "artistName": "ENTER_ARTIST_NAME"
#     }
#     headers = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
#         "X-RapidAPI-Host": "scrapesoft-music-lyrics.p.rapidapi.com"
#     }

#     response = requests.post(url, json=payload, headers=headers, params=querystring)

    # return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)