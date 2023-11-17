import requests
from bs4 import BeautifulSoup 
import json
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

def write_to_file(prediction: dict, path: str) -> None:
    with open(path+'.json', 'w', encoding='UTF-8') as file:
        json.dump(prediction, file, ensure_ascii=False, indent=2)

    return

def main():
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
    write_to_file(prediction, 'horoscope')
    print('hello')
    return

if __name__ == "__main__":
    # schedule.every().day.at("08:00").do(main)

    # while True:
    #     schedule.run_pending()
    main()