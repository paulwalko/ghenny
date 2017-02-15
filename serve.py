#!/usr/bin/python

from http.server import HTTPServer, CGIHTTPRequestHandler
import urllib

class POSTHandler(CGIHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        print(post_data)
        # You now have a dictionary of the post data
        self.send_response(200)
        self.end_headers()
        return

if __name__ == '__main__':
        server = HTTPServer(('localhost', 5001), POSTHandler)
        print('Starting server...')
        server.serve_forever()	
