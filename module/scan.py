""" scan the directory starting at root
dive into subdirectories with maximal depth
depth = 0: use maximal depth  """

import os,sys
from module import media,album
from sys import stdout

class Scanner:
	"""directory scanner class"""

	_album = ""
	_root = False
	_albumID = 0
	_db = ""
	_insCnt = _updCnt = _skipCnt = _dirCnt = 0

	def __init__(self,database,root,albumName):
		self._db = database
		
		self._album = album.Album(database=database,root=root,albumName=albumName)

		# set album id
		self._albumID = self._album.id()

		# get album root
		self._root = self._album.root()

		if not self._root.endswith("/"):
			self._root += "/"


	# scan album from subdirectory subdir
	def scan(self,subdir = "",depth = 0,level = 0,verbose = True):

		if not subdir:
			subdir = ""
		else:
			if not subdir.endswith("/"):
				subdir += "/"


		# if subdir exists, start scan
		if os.path.exists(self._root+subdir):
			print (depth)

			fileCnt = len(os.listdir(self._root+subdir))

			if verbose:
				print ("scan directory ",self._root+subdir)
				self._dirCnt += 1

			# loop directory
			localCnt = 0

			for f in os.listdir(self._root+subdir):

				# recursion if directory and level <= depth
				if os.path.isdir(self._root+subdir+f):
					if level+1 < depth or depth == 0:
						self.scan(subdir+f,depth,level+1)


				# get image from file
				# insert into database
				else:
					m = media.Media(root=self._root,dir=subdir,name=f)

					if (m.get()):
						if verbose:
							percent = int((10*localCnt) / fileCnt)

							stdout.write("\r[")
							stdout.write("-" * int(percent))
							stdout.write(" " * int(10 - percent))
							stdout.write("]")

							stdout.write(" file: %s" % f)
							stdout.flush()

							# stdout.write("\rfile: %s" % f)
							# stdout.flush()
							pass

						imageid = self._db.exists("image",m.ident())


						# record exists
						if (imageid):
							# modification time differs => update
							if int(m.get()["mtime"]) != int(self._db.get("image",imageid)["mtime"]):
								
								self._db.update_by_id("image",imageid,m.get())
								self._updCnt += 1
							else:
								self._skipCnt += 1


						# create new record
						else:
							data = m.get()
							data["album"] = self._albumID

							# print data
							imageid = self._db.insert("image",data)
							self._insCnt += 1

						localCnt += 1

						
						# link keywords
						if m.keywords():
							for key in m.keywords():
								keyid = self._db.exists("keyword",{"term":key})
								
#								print ("albumID",albumID)
								
								# keyword dont exist
								# insert keyword an set link
								if not keyid:
									keyid = self._db.insert("keyword",{"term":key,"album":self._albumID})
									self._db.insert("keyword_use",{"term":keyid,"image":imageid})

								# keyword exist
								else:

									# set link if dont exist
									if not self._db.exists("keyword_use",{"term":keyid}):
										self._db.insert("keyword_use",{"term":keyid,"image":imageid})


			if verbose:
				print (" => ",localCnt," images indexed")
				print (self._dirCnt," dirs with ",self._skipCnt," skipped /",self._insCnt," inserted /",self._updCnt," updated /",self._insCnt+self._updCnt+self._skipCnt," files processed")

	def len(self):
		return self._insCnt+self._updCnt
		