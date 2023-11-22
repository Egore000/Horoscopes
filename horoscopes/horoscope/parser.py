import requests
from bs4 import BeautifulSoup 
from .models import Predictions
from datetime import datetime
import time
import schedule

def get_page(url: str):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_prediction(urls: dict):
    prediction = {}

    for zodiak, url in urls.items():    
        soup = get_page(url)

        text = ''
        div = soup.find('div', class_='article__text')
        for p in div.find_all('p'):
            text += p.text + '\n'

        prediction[zodiak] = text 

    return prediction

def load_to_db(prediction):
    for zodiak, text in prediction.items():
        if not Predictions.objects.filter(zodiak_sign = zodiak):
            data = Predictions.objects.create(
                zodiak_sign = zodiak,
                content = text
            )
            data.save()
        else:
            data = Predictions.objects.filter(zodiak_sign = zodiak)

            data.update(
                zodiak_sign = zodiak,
                content = text,
            )


def get_data():
    urls = {
        'aries': 'https://horo.mail.ru/prediction/aries/today/',
        'taurus': 'https://horo.mail.ru/prediction/taurus/today/', 
        'gemini': 'https://horo.mail.ru/prediction/gemini/today/', 
        'cancer': 'https://horo.mail.ru/prediction/cancer/today/', 
        'leo': 'https://horo.mail.ru/prediction/leo/today/', 
        'virgo': 'https://horo.mail.ru/prediction/virgo/today/', 
        'libra': 'https://horo.mail.ru/prediction/libra/today/', 
        'scorpion': 'https://horo.mail.ru/prediction/scorpio/today/', 
        'sagittarius': 'https://horo.mail.ru/prediction/sagittarius/today/',
        'capricorn': 'https://horo.mail.ru/prediction/capricorn/today/', 
        'aquarius': 'https://horo.mail.ru/prediction/aquarius/today/',
        'pisces': 'https://horo.mail.ru/prediction/pisces/today/'
    }
    prediction = get_prediction(urls)
    load_to_db(prediction)
    return
    
# schedule.every().day.at("01:00").do(get_data)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
