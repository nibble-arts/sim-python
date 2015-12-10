''' album class '''
import sys, configparser
from module import database

class Album:

	_db = ""
	_album = {}

	def __init__ (self,albumName,args,verbose):

		albumRoot = args["albumRoot"]

		dataPath = args["datapath"]
		thumbPath = args["thumbpath"]
		thumbSize = args["thumbsize"]


		# load album configuration data
		albumConfig = configparser.RawConfigParser(allow_no_value = True)
		albumConfig.read("create/album.ini")

		# load or create album database
		self._db = database.Database(dataPath,"_album_")
		self._db.create(albumConfig)


		# check for existing database
		if (not self._db.exists("album",{"name":albumName})):

		# database dont exist
		# create if --album-root defined
			if (verbose):
				print ("album '"+albumName+"' don't exist")

			if (albumRoot):
				if (verbose):
					print ("create album: '"+albumName+"'")
					print ("album root:",albumRoot)
					print ("database path:",dataPath)
					print ("data path:",dataPath)
					print ("thumb path:",thumbPath)
					print ("thumb size:",thumbSize)

					self._db.insert("album",{"root":albumRoot,"datapath":dataPath,"name":albumName,"thumbroot":thumbPath,"thumbsize":thumbSize})

			else:
				print ("no album root defined to create new album")
				print ("scan abborted")
				sys.exit()

		self._db.select("select * from album where name='"+albumName+"'")
		albumData = self._db.fetch()

		fields = albumConfig["album"]

		for f, d in zip(fields,albumData):
			self._album[f] = d



	def album (self):
		if (len(self._album)):
			return self._album
		else:
			return False 


	def name (self):
		return self._album["name"]


	def root (self):
		return self._album["root"]


	def dataPath (self):
		return self._album["datapath"]


	def thumbPath (self):
		return self._album["thumbpath"]


	def thumbSize (self):
		return self._album["thumbsize"]


	def id (self):
		return self._album["id"]



'''
class Album:

	_root = ""
	_albumName = ""
	_id = 0
	_data = {}

	def __init__(self,database,root,albumName):

		self._db = database
		self._albumName = albumName

		# get album / create if don't exists
		id = self._db.exists("album",{"name":self._albumName})

		# create new album
		if not id:

			if not root:
				print ("no album root directory found; use --album-root")
				sys.exit()

			id = self._db.insert("album",{"root":root,"name":self._albumName})

		# set album id
		self._id = id
		self._data = self._db.get("album",self._id)


	# return album id
	def id(self):
		return self._id

	# return album name 
	def albumName(self):
		return self._albumName

	# return album root
	def root(self):
		return self._data["root"]
'''