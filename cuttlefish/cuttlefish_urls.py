import re


class UrlsHandlers:
    def __init__(self, urls_handlers={}):
        self.urls_handlers = self.parse_urls_handlers(urls_handlers)
        # urls_re используется для упрощения поиска вхождения url
        # в зарегистрированные
        self.urls_re = self.get_urls_re()

    def get_registered_urls(self):
        return self.urls_handlers

    def is_registered_urls(self, url):
        ''' ищем по шаблонам self.urls_re '''
        for url_re in self.urls_re:
            if re.findall(url_re, url):
                return True
        return False

    def get_handler(self, url):
        if not self.is_registered_urls(url):
            return None
        for url_handler in self.urls_handlers:
            if re.findall(url_handler.get('url_re'), url):
                args = self.parse_url_args(url_handler.get('url_re'), url)
                # не забываем про аргументы из urls.py
                args.update(url_handler.get('args_url'))
                return {
                    'handler': url_handler.get('handler'),
                    'args': args,
                }
        return None

    def get_urls_re(self):
        urls_re = []
        for url_handler in self.urls_handlers:
            urls_re.append(self.get_url_args_re(url_handler.get('url')))
        return urls_re

    def parse_urls_handlers(self, urls_handlers_raw):
        urls_handlers = []
        for url in urls_handlers_raw:
            handler, args = urls_handlers_raw.get(url)
            url_handler = self.parse_url(url)
            url_handler.update({'handler': handler, 'args_url': args})
            urls_handlers.append(url_handler)
        return urls_handlers

    def parse_url(self, url):
        # url_re, args = self.get_url_args_re(url)
        url_re = self.get_url_args_re(url)
        return {
            'url': url,
            'url_re': url_re,
        }

    def get_url_args_re(self, url):
        # Прасим шаблоны типа /path/<int:arg1>/<int:arg2>/
        args = re.findall(r'<\w+:\w+>', url)
        url_re = '^{}$'.format(url)
        for arg in args:
            arg_name = arg[1:-1].replace(':', '_')
            url_re = url_re.replace(arg, r'(?P<{}>\w+)'.format(arg_name))
        return url_re

    def parse_url_args(self, templete, url_current):
        match = re.search(templete, url_current)

        args = match.groupdict()
        for arg in args.copy():
            type_arg = arg.split('_')[0]
            if type_arg == 'int':
                try:
                    args[arg[4:]] = int(args[arg])
                    del args[arg]
                except:
                    # Здесь надо как-то обработать ошибку
                    # пока обработку оставляю на совесть views
                    pass
            if type_arg == 'str':
                args[arg[4:]] = args[arg]
                del args[arg]
        return args
