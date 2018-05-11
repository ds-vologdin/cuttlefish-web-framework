class UrlsHandlers:
    def __init__(self, urls_handlers={}):
        self.urls_handlers = urls_handlers

    def get_registered_urls(self):
        return self.urls_handlers

    def register_url(self, url=None, handler=None):
        if url and handler:
            self.urls_handlers.update({url: handler})
        return self.urls_handlers
