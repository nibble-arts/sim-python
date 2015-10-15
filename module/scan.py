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
	_insCnt = _updCnt = _skipCnt = 0

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

			if verbose:
				print "scan directory ",self._root+subdir

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
					# print "image: ",f
					m = media.Media(root=self._root,dir=subdir,name=f)
					# print m.get()

					if (m.get()):
						if verbose:
							stdout.write("\rfile: %s" % f)
							stdout.flush()

						id = self._db.exists("image",m.ident())

						# record exists
						if (id):
							# modification time differs => update
							if int(m.get()["mtime"]) != int(self._db.get("image",id)["mtime"]):
								
								self._db.update_by_id("image",id,m.get())
								self._updCnt += 1
							else:
								self._skipCnt += 1


						# create new record
						else:
							data = m.get()
							data["album"] = self._albumID

							# print data
							self._db.insert("image",data)
							self._insCnt += 1

						localCnt += 1


			if verbose:
				print " => ",localCnt," images indexed"
				print self._skipCnt," skipped /",self._insCnt," inserted /",self._updCnt," updated /",self._insCnt+self._updCnt+self._skipCnt," processed"

	def len(self):
		return self._insCnt+self._updCnt
		