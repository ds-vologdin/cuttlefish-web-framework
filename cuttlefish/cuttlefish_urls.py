import re


class UrlsHandlers:
    def __init__(self, urls_handlers={}):
        self.urls_handlers = self.parse_urls_handlers(urls_handlers)
        # urls_re используется для упрощения поиска вхождения url
        # в зарегистрированные
        self.urls_re = self.get_urls_re()
        print(self.urls_handlers)
        print(self.urls_re)

    def get_registered_urls(self):
        return self.urls_handlers

    def is_registered_urls(self, url):
        ''' ищем по шаблонам self.urls_re '''
        for url_re in self.urls_re:
            if re.findall(url_re, url):
                return True
        return False
        # return url in self.urls_handlers

    def get_handler(self, url):
        if not self.is_registered_urls(url):
            return None
        for url_handler in self.urls_handlers:
            if re.findall(url_handler.get('url_re'), url):
                return url_handler.get('handler')
        return None

    # def register_url(self, url=None, handler=None):
    #     if url and handler:
    #         self.urls_handlers.update({url: handler})
    #     return self.urls_handlers

    def get_urls_re(self):
        urls_re = []
        for url_handler in self.urls_handlers:
            urls_re.append(self.get_url_args_re(url_handler.get('url'))[0])
        return urls_re

    def parse_urls_handlers(self, urls_handlers_raw):
        urls_handlers = []
        for url in urls_handlers_raw:
            url_handler = self.parse_url(url)
            url_handler.update({'handler': urls_handlers_raw.get(url)})
            urls_handlers.append(url_handler)
        return urls_handlers

    def parse_url(self, url):
        url_re, args = self.get_url_args_re(url)
        return {
            'url': url,
            'url_re': url_re,
            'args_url': args,
        }

    def get_url_args_re(self, url):
        # Прасим шаблоны типа /path/<int:arg1>/<int:arg2>/
        args = re.findall(r'<\w*:\w*>', url)
        url_re = '^{}$'.format(url)
        for arg in args:
            url_re = url_re.replace(arg, r'\w*')
        return url_re, args
