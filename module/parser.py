import pickle, configparser, dicttoxml, io
from urllib.parse import urlparse,parse_qs
from module import database, thesaurus, template

class Parser:

	url = None
	param = None

	def __init__ (self,script,param):
		self.script = script
		self.param = param
		pass


	def transform (self,xml):

	# load create config
		config = configparser.RawConfigParser(allow_no_value = True)
		config.read("create/thesaurus.ini")

		dataPath = "data"
		thesname = "familie_thes"
		albumName = "familie"

		xml.seek(0)
		#print (xml.read())


		f = io.StringIO()

		# if id => get thesaurus
		if "id" in self.param:

			id = self.param["id"][0]

			db = database.Database(dataPath,thesname)
			db.create(config)

			thes = thesaurus.Thesaurus(thesdb=db,thesname="familie_thes",album=albumName,verbose=False)
			data = thes.get(id)

			# load template and transform data
			xmlData = dicttoxml.dicttoxml(data)

			xsl = template.Template("thesaurus")
			#self.html(xsl.transform(xmlData))

			f.write(str(xsl.transform(xmlData,self.param),"utf-8"))

			f.seek(0)

			return f

		else:
			return False