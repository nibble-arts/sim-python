from http.server import BaseHTTPRequestHandler
from module import database, thesaurus
import pickle, configparser
from urllib.parse import urlparse,parse_qs


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)
        path = url.path
        param = parse_qs(url.query)

        print (param)
        if (path.endswith("index.html")):

            self.html_open("SWIM-webcontroll")

            # send reply
            self.html("<h2>SWIM</h2>")
#            self.html("<p>page path: %s</p>" % path)

#            for key in param:
#                self.html("<p>%s = %s" % (key,param[key]))

    		# load create config
            config = configparser.RawConfigParser(allow_no_value = True)
            config.read("create/thesaurus.ini")

            dataPath = "data"
            thesname = "familie_thes"
            albumName = "familie"


            # if id => get thesaurus
            if "id" in param:
                id = param["id"][0]

#                self.html("<p>Get Term id=%s" % id)

                db = database.Database(dataPath,thesname)
                db.create(config)

                thes = thesaurus.Thesaurus(thesdb=db,thesname="familie_thes",album=albumName,verbose=True)
                data = thes.get(id)

                for key in data:
                    self.html("%s = %s<br>" % (key,data[key]))

            self.html_close()

        else:
            self.html_open("page not found")
            self.html("<h2>Page '%s' not found on this server</h2>" % path)
            self.html_close()



    def do_POST(self):
        pass


    def html_open(self,title):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>%s</title></head>" % title, "utf-8"))


    def html_close(self):
        self.wfile.write(bytes("</body></html>", "utf-8"))


    def html(self,string):
        self.wfile.write(bytes(string, "utf-8"))

