import http.server
import socketserver

PORT = 9000	

Handler = http.server.BaseHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)



def do_GET (self):
#	Handler.handle(self)
	print ("get handler called")


print ("serving at port", PORT)
httpd.serve_forever()