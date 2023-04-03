from googlesearch import search
import requests
from bs4 import BeautifulSoup


async def get_city_coord(city):
    query = f"Координаты города {city}"
    target_link = list(filter(lambda x: x if 'time-in.ru' in x else None, search(query)))

    try:
        target_link = target_link[0]
    except:
        return None

    response = requests.get(target_link)
    soap = BeautifulSoup(response.text, 'html.parser')
    info = soap.find('div', class_='coordinates-city-info').find('div').text.lstrip('Широта, долгота: ')
    coords = tuple(x.strip() for x in info.split(','))
    return coords
