""" media class identifies media
and loades corresponding metadata """

from module import exif
import os.path


class Media:
	""" media object class """

	_types = {"jpg":"image","jpeg":"image","png":"image","tif":"image","tiff":"image","mpg":"video","mpeg":"video","mp4":"video","avi":"video"}
	
	_metadata = {}
	_dir = ""

	def __init__(self,dir,name):
		self._dir = dir
		self._parse(name)

		# valid type found -> add dirname
		if (len(self._metadata) > 1):
			self._metadata["dirname"] = dir

		pass


	# get metadata, false if no media
	def get(self):
		if (len(self._metadata) > 1):
			return self._metadata
		else:
			return False


	# parse filename for type
	def _parse(self,name):
		self._metadata = {}

		# print self._types
		extension = os.path.splitext(name)[1][1:]

		# extension found
		if extension:

			# is valid type
			if extension in self._types.keys():
				path = self._dir + name

				self._metadata["basename"] = name
				self._metadata["extension"] = extension
				self._metadata["type"] = self._types[extension]
				self._metadata["size"] = os.path.getsize(path)
				self._metadata["mtime"] = os.path.getatime(path)

				# get exif data
				e = exif.Exif(path)

				# self._metadata["original_datetime"] = e.exif["original_datetime"]

				# self._metadata["exif"] = e.exif["exif"]

				print self._metadata