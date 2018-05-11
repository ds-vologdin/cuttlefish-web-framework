# cuttlefish-web-framework
Отличный отечественный WSGI совместиммый веб-фрэймворк. Всем врагам на зло... ;-)

## Установка

```git clone https://github.com/ds-vologdin/cuttlefish-web-framework.git```

### Установка uwsgi

```sudo apt-get install uwsgi uwsgi-plugin-python3```

## Отладка
Запускаем uwsgi

```uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file application.py```

Хитрость в подгрузке плагина python3 (без него вопреки документации в [quickstart](http://uwsgi.readthedocs.io/en/latest/WSGIquickstart.html) не находит опцию --wsgi-file)

## Структура фреймфорка
cuttlefish/cuttlefish_application.py - основа фреймфорка

cuttlefish/cuttlefish_urls.py - описывает класс UrlsHandlers

application.py - обработчик отвечающий за взаимодействие с uwsgi (его пользователю трогать не нужно)

urls.py - пользовательское объявление экземпляра класса (здесь задаются url и их обработчики)

view.py -  пользовательские обработчики

## Пример использования
В urls.py описываем нужные нам url и их обработчики
```
urls_handlers = UrlsHandlers(
    {
        '/': view.handler_1,
        '/web/': view.handler_2
    }
)
```
В view.py пишем, указанные в urls_handlers обработчики
```
def handler_1(request):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish<p>
    </body>
</html>
    '''
    return respone


def handler_2(request):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish<p>
    </body>
</html>
    '''
    return respone
```

Запускаем uwsgi. Например так:
```
uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file application.py
```
В браузе заходим на http://localhost:9090/
