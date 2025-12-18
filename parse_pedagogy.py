from bs4 import BeautifulSoup # Импортируем библиотеку BeautifulSoup для работы с HTML
import requests # Импортируем библиотеку requests для отправки запросов в интернет

def parse_articles():
    html = requests.get('https://pedsovet.org/').text # Отправляем запрос на сайт и получаем HTML-код
    soup = BeautifulSoup(html, 'html.parser') #Создать объект для анализа HTML, используя HTML-парсер, и записать его в переменную soup
    cards = soup.select('div.cards-unt-item') # Ищем ВСЕ элементы div с классом 'cards-unt-item' (это карточки статей)
    
    articles = []
    for card in cards:
        title = card.select_one('div.cards-unt-item__title') # В текущей карточке ищем ОДИН элемент div с классом 'cards-unt-item__title' (заголовок)
        link = card.find('a')
        
        if title and link:
            url = link['href'] #Берем то, что написано в href, а в нем записан адрес ссылки
            if url.startswith('/'):
                url = 'https://pedsovet.org' + url
                
            articles.append({
                'title': title.get_text(strip=True),
                'url': url
            })
    
    return articles

# Вывод результатов
for article in parse_articles():
    print(f"{article['title']}\n{article['url']}\n")
