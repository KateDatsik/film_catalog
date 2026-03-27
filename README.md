# Film Catalog

Веб-приложение на Django для просмотра каталога фильмов, комментариев и обратной связи.

## Возможности

- список опубликованных фильмов
- детальная страница фильма
- комментарии к фильмам (для авторизованных пользователей)
- регистрация и вход пользователей
- форма обратной связи
- загрузка постера для каждого фильма

## Технологии

- Python 3.13
- Django 5.x
- SQLite (по умолчанию)
- HTML/CSS

## Быстрый старт

```bash
git clone https://github.com/KateDatsik/film_catalog.git
cd film_catalog/films
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
