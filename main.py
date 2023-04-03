from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from settings import API_KEY
from fastapi.middleware.cors import CORSMiddleware
from weather import get_weather
from service import get_city_coord

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"],
)


@app.get("/weather/now/")
async def get_weather_by_coords(latitude, longitude, api_key):
    if api_key == API_KEY:
        result = await get_weather(latitude, longitude)
        return result
    else:
        return {
            'status': '403',
            'descr': 'Доступ запрещен'
        }


@app.get("/weather/city/")
async def get_weather_by_city(city, api_key):
    if api_key == API_KEY:
        coords = await get_city_coord(city)
        if coords:
            latitude = coords[0]
            longitude = coords[1]
            result = await get_weather(latitude, longitude)
            return result

        else:
            return {
                'status': '404',
                'descr': 'Город не найден'
            }
    else:
        return {
            'status': '403',
            'descr': 'Доступ запрещен'
        }
