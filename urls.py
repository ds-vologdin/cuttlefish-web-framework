from cuttlefish.cuttlefish_urls import UrlsHandlers
import view

# Шаблоны задаются в словаре вида
# {
#    '/path/<int:arg1>/<str:arg2>/': (view.handler,
#                                     {'argumet': argument_value, })
# }
# Где <int:arg1> аргумент типа int, <str:arg2> аргумент типа start_response
# Шаблону  будет соотвествовать такая строка:
# /path/2341/ok/
# при этом aplication запустит обработчик handler с аргументом args
# args = {'arg1': 2341, 'arg2': 'ok', 'argumet': argument_value}

urls_handlers = UrlsHandlers(
    {
        '/': (view.handler_1, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/': (view.handler_2, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/<int:arg1>/': (view.handler_2, {'arg_key1': 'arg1'}),
        '/article/<str:arg1>/': (view.handler_2, {}),
    }
)
