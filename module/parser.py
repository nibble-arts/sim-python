import pickle, configparser, dicttoxml
from urllib.parse import urlparse,parse_qs

class Parser:

	url = None
	param = None

	def __init__ (self,data,script,param):
		print ("init parser")

		print (data)
		print (param)

		pass


	def transform (self):
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

			#xsl = template.Template("test")
			#self.html(xsl.transform(xmlData))