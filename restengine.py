from wsgiref.simple_server import make_server
#===============================================================================
# from __future__ import print_function
# from gevent import monkey, _socket3
# monkey.patch_all(ssl=False)
# from gevent.pywsgi import WSGIServer
#===============================================================================
import re

from requesthandler import RequestHandler
from router import Router
from request import Request

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style envrironment variables and the
# second variable is the callable object (see PEP 333).

API_PATTERN = "^/\w+(/(numeric)?:\w+)*/$|^(/\w+(/(numeric)?:\w+)+)+(/\w+)?/$"

class RestEngine(RequestHandler, Router):

    api_pattern = re.compile(API_PATTERN)

    rest = {}

    def __init__(self, base_url, api_list):
        self.initializeApi(base_url, api_list)

    def __call__(self, environ, response):
        request = Request(environ)
        api, path = self.findRestApi(request.PATH_INFO)
        return self.handle(request, response)


