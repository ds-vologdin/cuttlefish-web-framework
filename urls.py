from cuttlefish_urls import UrlsHandlers
import view


urls_handlers = UrlsHandlers(
    {
        '/': view.handler_1,
        '/web/': view.handler_2
    }
)
