import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

host, port = '', int(sys.argv[1])

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

class Server(HTTPServer):
    def run(host='', port=8000, server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
        server_address = (host, port)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()

Server.run(host, port, handler_class=Handler)
