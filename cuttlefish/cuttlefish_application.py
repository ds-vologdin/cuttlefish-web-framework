def cuttlefish_application(env, start_response, urls_handlers):
    request_uri = env['PATH_INFO']
    respone = cuttlefish_aplication_url(request_uri, urls_handlers, env)
    start_response(respone['http_code'], respone['http_content'])
    return [respone['respone']]


def url_not_found(request_uri):
    respone = 'uri "{}" not registered'.format(request_uri)
    return {
        'respone': respone.encode('utf-8'),
        'http_code': '404 Not Found',
        'http_content': [('Content-Type', 'text/html')],
    }


def cuttlefish_aplication_url(request_uri, urls_handlers=None, env=None):
    if not urls_handlers or not request_uri:
        return url_not_found(request_uri)

    if not urls_handlers.is_registered_urls(request_uri):
        return url_not_found(request_uri)

    handler = urls_handlers.get_handler(request_uri)

    if not handler:
        return url_not_found(request_uri)

    # Хендлер скрывается за словарём:
    # {'args': {'arg1': '34342', 'arg2': '432'}, 'handler': <function handler>}
    respone_handler = handler['handler'](env, handler.get('args', {}))

    return {
        'respone': respone_handler.encode('utf-8'),
        'http_code': '200 OK',
        'http_content': [('Content-Type', 'text/html')],
    }
