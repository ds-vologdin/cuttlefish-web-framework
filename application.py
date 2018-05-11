from cuttlefish.cuttlefish_application import cuttlefish_application
import urls


def application(env, start_response):
    urls_handlers = urls.urls_handlers
    return cuttlefish_application(env, start_response, urls_handlers)
