from http.server import BaseHTTPRequestHandler
from module import database, thesaurus, template
import pickle, configparser, dicttoxml
from urllib.parse import urlparse,parse_qs



class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        url = urlparse(self.path)
        path = url.path
        param = parse_qs(url.query)

        print (param)
        if (path.endswith("index.html")):


    		# load create config
            config = configparser.RawConfigParser(allow_no_value = True)
            config.read("create/thesaurus.ini")

            dataPath = "data"
            thesname = "familie_thes"
            albumName = "familie"


            # if id => get thesaurus
            if "id" in param:
                id = param["id"][0]

                db = database.Database(dataPath,thesname)
                db.create(config)

                thes = thesaurus.Thesaurus(thesdb=db,thesname="familie_thes",album=albumName,verbose=False)
                data = thes.get(id)

                # load template and transform data
                xmlData = dicttoxml.dicttoxml(data)

                xsl = template.Template("test")
                self.html(xsl.transform(xmlData))


        else:
            self.html_open("page not found")
            self.html("<h2>Page '%s' not found on this server</h2>" % path)
            self.html_close()



    def do_POST(self):
        pass


    def html(self,string):
        self.wfile.write(string)

