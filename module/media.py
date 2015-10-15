""" media class identifies media
and loades corresponding metadata """

from module import exif
import os.path,sys


class Media:
	""" media object class """

	_types = {"jpg":"image","jpeg":"image","png":"image","tif":"image","tiff":"image","mpg":"video","mpeg":"video","mp4":"video","avi":"video"}
	_ident = ["dirname","basename","extension","type","size","original_datetime","height","width"]

	_metadata = {}
	_root = ""
	_dir = ""

	def __init__(self,root,dir,name):
		self._root = root
		self._dir = dir
		self._parse(name)

		# valid type found -> add dirname
		if (len(self._metadata) > 1):
			self._metadata["dirname"] = unicode(dir)

		pass


	# get metadata, false if no media
	def get(self):
		if (len(self._metadata) > 1):
			return self._metadata
		else:
			return False


	# get different definition
	def ident(self):
		ret = {}

		for field in self._ident:

			if field in self._metadata:
				ret[field] = self._metadata[field]

		return ret


	# parse filename for type
	def _parse(self,name):
		self._metadata = {}

		# print self._types
		extension = os.path.splitext(name)[1][1:].lower()

		# extension found
		if extension:

			# is valid type
			if extension in self._types.keys():
				path = self._root + self._dir + name

				self._metadata["size"] = os.path.getsize(path)

				# has size != 0
				if self._metadata["size"] > 0:
					self._metadata["basename"] = name
					self._metadata["extension"] = extension
					self._metadata["type"] = self._types[extension]
					self._metadata["mtime"] = os.path.getatime(path)


					# get exif data from jpg and tif
					if extension == "jpg" or extension == "jpeg" or extension == "tif" or extension == "tiff":
						e = exif.Exif(path)

						self._metadata.update(e.get())

				# if no size => no image
				else:
					self._metadata = {}
				# print self._metadata
