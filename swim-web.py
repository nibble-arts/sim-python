from http.server import HTTPServer
import time
from module import database,httpd



hostName = "localhost"
hostPort = 9000


myServer = HTTPServer((hostName, hostPort), httpd.MyServer)

print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))