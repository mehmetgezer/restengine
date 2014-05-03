
class RequestHandler(object):

    def handle(self, REQUEST, response):
        api, path = self.findRestApi(REQUEST.PATH_INFO)
        print("method: ", REQUEST.REQUEST_METHOD, " path: ", REQUEST.PATH_INFO)
        print("api: ", api)
        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
        response(status, headers)
        return [str(api["api"] + "\n").encode()]
