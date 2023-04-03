from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from settings import API_KEY
from fastapi.middleware.cors import CORSMiddleware

cookies = {
    'is_gdpr': '0',
    'is_gdpr_b': 'CKC8ChCErwEoAg==',
    'gdpr': '0',
    '_ym_uid': '1680256667288142951',
    'yandexuid': '4037664151679544414',
    'yuidss': '4037664151679544414',
    'i': 'm10gjuVSrdyHA1QAV6ntfI5UXggEvOksjZNFK8HyitLDK9pJyXg+B01vYbFKFff+ORCG3JL9iwqRJl1Lmw+0M96lK7c=',
    'KIykI': '1',
    'my': 'YwA=',
    '_ym_isad': '1',
    'ymex': '1682848667.oyu.7868612771680256665#1995617559.yrts.1680257559',
    'spravka': 'dD0xNjgwMjU3NTY2O2k9OTUuODIuODcuMjc7RD1DOEYwODVBOTg3Mzk3RjMwRDVBOENEQzdBM0M1OTRDMUY3MkUyQjZDNTdENjdGRENCRjIzNzFGRDA5RDk5NEU4MjU1M0U0MDg0NEI3MjRDNTAxO3U9MTY4MDI1NzU2NjM3MjEwNzI4OTtoPTVkYmYxNDVhMTg4YmQ0ZmZhMTk2NzZjOTMyNWQ3Zjgy',
    'yandex_gid': '221',
    'yp': '1682849566.ygu.1#1680343067.yu.7868612771680256665#1696024668.szm.1%3A1920x1080%3A1846x948#4294967295.skin.s',
    '_ym_d': '1680257567',
    'bh': 'EkAiR29vZ2xlIENocm9tZSI7dj0iMTExIiwgIk5vdChBOkJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMTEiKgI/MDoHIkxpbnV4Ig==',
    '_yasc': 'Vh3yf7amwnphB5upmQVr3ltr5in+siDCAkcQO3/D1oCJZkdIEovEEDLzq5kURb+wX3wK/9xHuT7P',
    '_ym_visorc': 'b',
    'coockoos': '1',
}

headers = {
    'authority': 'yandex.kz',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,kk-KZ;q=0.8,kk;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': 'is_gdpr=0; is_gdpr_b=CKC8ChCErwEoAg==; gdpr=0; _ym_uid=1680256667288142951; yandexuid=4037664151679544414; yuidss=4037664151679544414; i=m10gjuVSrdyHA1QAV6ntfI5UXggEvOksjZNFK8HyitLDK9pJyXg+B01vYbFKFff+ORCG3JL9iwqRJl1Lmw+0M96lK7c=; KIykI=1; my=YwA=; _ym_isad=1; ymex=1682848667.oyu.7868612771680256665#1995617559.yrts.1680257559; spravka=dD0xNjgwMjU3NTY2O2k9OTUuODIuODcuMjc7RD1DOEYwODVBOTg3Mzk3RjMwRDVBOENEQzdBM0M1OTRDMUY3MkUyQjZDNTdENjdGRENCRjIzNzFGRDA5RDk5NEU4MjU1M0U0MDg0NEI3MjRDNTAxO3U9MTY4MDI1NzU2NjM3MjEwNzI4OTtoPTVkYmYxNDVhMTg4YmQ0ZmZhMTk2NzZjOTMyNWQ3Zjgy; yandex_gid=221; yp=1682849566.ygu.1#1680343067.yu.7868612771680256665#1696024668.szm.1%3A1920x1080%3A1846x948#4294967295.skin.s; _ym_d=1680257567; bh=EkAiR29vZ2xlIENocm9tZSI7dj0iMTExIiwgIk5vdChBOkJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMTEiKgI/MDoHIkxpbnV4Ig==; _yasc=Vh3yf7amwnphB5upmQVr3ltr5in+siDCAkcQO3/D1oCJZkdIEovEEDLzq5kURb+wX3wK/9xHuT7P; _ym_visorc=b; coockoos=1',
    'device-memory': '8',
    'downlink': '3.6',
    'dpr': '1',
    'ect': '4g',
    'referer': 'https://yandex.kz/pogoda/search?lat=42.315514&lon=69.586907&via=srp&request=%D1%88%D1%8B%D0%BC%D0%BA%D0%B5%D0%BD%D1%82',
    'rtt': '150',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"111.0.5563.110"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="111.0.5563.110", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"5.19.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'viewport-width': '1291',
}


async def get_weather(latitude, longitude):
    params = {
        'lat': latitude,
        'lon': longitude,
        'via': 'srp',
    }
    response = requests.get('https://yandex.kz/pogoda/', params=params, cookies=cookies, headers=headers)
    soap = BeautifulSoup(response.text, 'html.parser')
    city = soap.find('h1', class_='title title_level_1 header-title__title').text
    forecast_now = soap.find('div', class_='temp fact__temp fact__temp_size_s').find('span',
                                                                                     class_='temp__value temp__value_with-unit').text
    feelings_now = soap.find('div', class_='link__feelings fact__feelings')
    condition = feelings_now.find('div').text
    feeling_temp = feelings_now.find('span', class_="temp__value temp__value_with-unit").text
    wind = soap.find('div', class_='term term_orient_v fact__wind-speed').find('span',
                                                                               class_='a11y-hidden').text.lstrip(
        'Ветер: ')
    wet = soap.find('div', class_='term term_orient_v fact__humidity').find('span', class_='a11y-hidden').text.lstrip(
        'Влажность: ')
    press = soap.find('div', class_='term term_orient_v fact__pressure').find('span', class_='a11y-hidden').text.lstrip(
        'Давление: ')

    return [{
        'city': city,
        "weather": forecast_now,
        'condition': condition,
        'feeling': feeling_temp,
        'wind': wind,
        'wetness': wet,
        'pressure': press
    }]
