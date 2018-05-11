from cuttlefish.cuttlefish_urls import UrlsHandlers
import view


urls_handlers = UrlsHandlers(
    {
        '/': (view.handler_1, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
        '/web/': (view.handler_2, {'arg_key1': 'arg1', 'arg_key2': 'arg2'}),
    }
)
