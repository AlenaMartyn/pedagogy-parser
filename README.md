# Парсер статей с Pedsovet.org

## Описание
Программа парсит главную страницу сайта pedsovet.org и извлекает названия статей и ссылки на них из карточек статей.

## Извлекаемые данные
- Название статьи
- Ссылка на полную статью
- Категории/теги статьи

## Источник данных
HTML-страница загружается напрямую с сайта: https://pedsovet.org/

## Установка зависимостей
```bash
git clone https://github.com/AlenaMartyn/pedagogy-parser.git
cd pedagogy-parser
pip install -r requirements.txt
