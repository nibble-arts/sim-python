# encoding=utf-8
""" class for exif data extraction """
import sys
import pyexiv2

class Exif:

	_exif = {}
	_iptc = {}

	def __init__(self,path):

		# get metadata
		metadata = pyexiv2.ImageMetadata(path)
		metadata.read()

		try
		# print (metadata.iptc_keys)
 
		# get exif data
		if "Exif.Image.DateTime" in metadata:
			self._exif["datetime"] = (metadata["Exif.Image.DateTime"].raw_value)

		if "Exif.Image.ImageWidth" in metadata:
			self._exif["width"] = (metadata["Exif.Image.ImageWidth"].raw_value)

		if "Exif.Image.ImageLength" in metadata:
			self._exif["height"] = (metadata["Exif.Image.ImageLength"].raw_value)

		if "Exif.Photo.DateTimeOriginal" in metadata:
			self._exif["datetimeoriginal"] = (metadata["Exif.Photo.DateTimeOriginal"].raw_value)


		# get iptc data
		if "Iptc.Application2.Keywords" in metadata:
			self._iptc["keywords"] = (metadata["Iptc.Application2.Keywords"].value)


	# get exif value by index
	# if no index, return dictionary
	def exif(self,index = ""):
		if index:
			# return index value
			if index in self._exif.keys():
				return self._exif[index]

			# index not found
			else:
				return False

		# return exif dictionary
		else:
			return self._exif


	# get exif value by index
	# if no index, return dictionary
	def keywords(self):
		if "keywords" in self._iptc:
			return self._iptc["keywords"]
		else:
			return False

