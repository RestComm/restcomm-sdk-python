import sys
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

def main():

    HandlerClass = SimpleHTTPRequestHandler
    ServerClass  = HTTPServer
    Protocol     = "HTTP/1.0"

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('192.168.1.76', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print ("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()

if __name__ == '__main__':
    main()

