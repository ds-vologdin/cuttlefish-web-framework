# cuttlefish-web-framework
Отличный отечественный WSGI совместиммый веб-фрэймворк. Всем врагам на зло... ;-)

## Установка

```git clone https://github.com/ds-vologdin/cuttlefish-web-framework.git```

### Установка uwsgi

```sudo apt-get install uwsgi uwsgi-plugin-python3```

## Отладка
Запускаем uwsgi

```uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file application.py```

Хитрость в подгрузке плагина python3 (без него вопреки документации в [quickstart](http://uwsgi.readthedocs.io/en/latest/WSGIquickstart.html) не находит опцию --wsgi-file). Хотя это локальная проблема, чаще всего плагины python3 будут подключаться по умолчанию. Если у вас возникают какие-то проблемы с uwsgi обратитесь к его [документации](http://uwsgi.readthedocs.io/en/latest/).

## Структура фреймфорка
cuttlefish/cuttlefish_application.py - основа фреймфорка

cuttlefish/cuttlefish_urls.py - описывает класс UrlsHandlers

application.py - обработчик отвечающий за взаимодействие с uwsgi (его пользователю трогать не нужно)

urls.py - пользовательское объявление экземпляра класса (здесь задаются url и их обработчики)

controler.py -  пользовательские обработчики

## Пример использования
В urls.py описываем нужные нам url, их обработчики и аргументы, которые нужно передать обработчику при вызове
```
urls_handlers = UrlsHandlers(
    {
        '/': (view.handler_1, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/': (view.handler_2, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/<int:arg1>/': (view.handler_2, {'arg_key1': 'arg1'}),
        '/article/<str:arg1>/': (view.handler_2, {}),
    }
)
```
В controler.py размещаем, указанные в urls_handlers обработчики
```
def handler_1(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 1</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(json.dump(arg_dict))
    return respone


def handler_2(request, arg_dict={}):
    respone = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Handler 2</h1>
        <p>Hello from cuttlefish</p>
        <p>arguments:</p>
        <p>{}</p>
    </body>
</html>
    '''.format(json.dumps(arg_dict))
    return respone
```

Запускаем uwsgi. Например так:
```
uwsgi --plugin python3 --http-socket localhost:9090 --wsgi-file application.py
```
В браузер заходим на http://localhost:9090/
