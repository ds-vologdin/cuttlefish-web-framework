# cuttlefish-web-framework
Отличный отечественный веб-фрэймворк. Всем врагам на зло... ;-)

## Отладка
Запускаем uwsgi
```
uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file cuttlefish_application.py
```
Хитрость в подгрузке плагина python3 (без него вопреки документации в [quickstart](http://uwsgi.readthedocs.io/en/latest/WSGIquickstart.html) не находит опцию --wsgi-file)

## Установка uwsgi
```
sudo apt-get install uwsgi uwsgi-plugin-python3
```
