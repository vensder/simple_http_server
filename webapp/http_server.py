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

docker run -d --name my-http -p 3001:3001 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:2-alpine python http4.py

"""

from sys import argv
from platform import python_version

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json

current_python_version = str(python_version())

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>You're welcome!</h1><p>Python version: " + current_python_version + "</p></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        try:
            parsed = json.loads(post_body)
            print(json.dumps(parsed, indent=4, sort_keys=True))
        except:
            print("Probably it is not a json")
            print(post_body)
        
        #self.wfile.write(post_body)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
