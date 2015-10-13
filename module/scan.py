""" scan the directory starting at root
dive into subdirectories with maximal depth
depth = 0: use maximal depth  """

import os
from module import media

class Scanner:
	"""directory scanner class"""

	_root = False
	_db = ""

	def __init__(self,database):
		self._db = database
		pass


	def scan(self,root,depth = 0):

		# if root exists, start scan
		if os.path.exists(root):
			self._root = root

		album = []


		for f in os.listdir(self._root):
			m = media.Media(self._root,f)

			if (m.get()):
				self._db.insert("image",m.get(),"CREATE_NEW")


		# for root,dirs,files in os.walk(self._root,topdown=False):
		# 	for file in files:
		# 		if file.endswith(".jpg"):
		# 			album.append([root,file])

		# 			# fh.write(root+"|"+file+"\m")
		# 			print "path: ",root," file: ",file
		# 	pass
		# 	print album
		