from http.server import BaseHTTPRequestHandler
from module import database, thesaurus
import pickle, configparser


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        # send reply
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>SIM-web</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><h1>SIM-web started</h1>", "utf-8"))
        self.wfile.write(bytes("<p>url: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

		# load create config
        config = configparser.RawConfigParser(allow_no_value = True)
        config.read("create/thesaurus.ini")

        dataPath = "data"
        thesname = "familie_thes"
        albumName = "familie"

        db = database.Database(dataPath,albumName)

        thes = thesaurus.Thesaurus(thesdb=db,thesname="familie_thes",album=albumName,verbose=True)

        print (thes.get(1))