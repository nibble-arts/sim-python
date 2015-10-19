''' album class '''


class Album:
	''' create or load the album metadata '''

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