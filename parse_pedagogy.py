# parse_pedagogy.py

from bs4 import BeautifulSoup
import requests

def load_page():
    url = "https://pedsovet.org/"
    
    # Добавляем заголовки чтобы сайт не блокировал нас
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return None

def parse_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = []
    
    # Ищем все карточки статей
    cards = soup.find_all('div', class_='cards-unt-item')
    
    print(f"Найдено карточек: {len(cards)}")
    
    for card in cards:
        # Ищем заголовок статьи 
        title_element = card.find('div', class_='cards-unt-item__title')
        if title_element:
            title_link = title_element.find('a')
            if title_link:
                title = title_link.text.strip()
            else:
                title = "Не удалось найти заголовок"
        else:
            title = "Не удалось найти заголовок"
        
        # Ищем ссылку
        link_element = card.find('div', class_='cards-unt-item__title').find('a')
        if link_element and link_element.get('href'):
            link = link_element['href']
            # Если ссылка относительная, добавляем домен
            if link.startswith('/'):
                link = "https://pedsovet.org" + link
        else:
            link = "Не удалось найти ссылку"
        
        # Ищем категории (теги)
        categories = []
        category_elements = card.find_all('a', href=True)
        for cat in category_elements:
            if '/tag/' in cat['href'] or '/rubric/' in cat['href']:
                categories.append(cat.text.strip())
        
        # Добавляем статью в список
        articles.append({
            'title': title,
            'link': link,
            'categories': categories
        })
    
    return articles

def main():
    print("Начинаем парсинг сайта pedsovet.org...")
    
    html = load_page()
    
    if html:
        articles = parse_articles(html)
        
        print(f"\nУспешно спаршено статей: {len(articles)}")
        print("\nСписок статей:")
        print("-" * 50)
        
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Ссылка: {article['link']}")
            if article['categories']:
                print(f"   Теги: {', '.join(article['categories'])}")
            print()
    else:
        print("Не удалось загрузить страницу")

if __name__ == "__main__":
    main()