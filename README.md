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
В urls.py описываем нужные нам url, их обработчики и аргументы, которые нужно передать обработчику при вызове
```
urls_handlers = UrlsHandlers(
    {
        '/': (view.handler_1, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/': (view.handler_2, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
    }
)
```
В view.py пишем, указанные в urls_handlers обработчики
```
def handler_1(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish<p>
        <p>argument 1: {0}<p>
    </body>
</html>
    '''.format(arg_dict.get('arg_key1', 'arg_key1 is not set'))
    return respone


def handler_2(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish<p>
        <p>argument 2: {0}<p>
    </body>
</html>
    '''.format(arg_dict.get('arg_key2', 'arg_key2 is not set'))
    return respone
```

Запускаем uwsgi. Например так:
```
uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file application.py
```
В браузер заходим на http://localhost:9090/
