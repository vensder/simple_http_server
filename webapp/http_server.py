#!/usr/bin/env python

"""
Very simple HTTP server in python.

Usage:
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

docker run -d --name my-http -p 5555:5555 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:2-alpine python http4.py

"""

from sys import argv
from platform import python_version
#from platform import node
from socket import gethostname

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

current_python_version = str(python_version())
current_hostname = str(gethostname())

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write('''
                <html>
                <body>
                <h1>Python version: %s</h1>
                <h2>Hostname: %s</h2>
                </body>
                </html>''' % (current_python_version, current_hostname))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=5555):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
