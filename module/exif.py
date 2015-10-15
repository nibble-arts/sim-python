# encoding=utf-8
""" class for exif data extraction """
from PIL import Image
from PIL.ExifTags import TAGS
# from iptcinfo import IPTCInfo

# import pillow

class Exif:

	_exif = {}

	def __init__(self,path):

		# get image data
		img = Image.open(path)

		# get width and height
		if hasattr (img,"size"):
			self._exif["width"] = img.size[0]
			self._exif["height"] = img.size[1]

		# get colour depth
		if hasattr (img,"bits"):
			self._exif["bits"] = img.bits

		# get exif data
		if hasattr (img,"_getexif"):

			exifData = img._getexif()
			exifList = []

			# parse exif block
			if exifData != None:

				# loop exif data
				for (k,v) in img._getexif().iteritems():
					
					# exif defined
					if TAGS.get(k) != None:
						# extract DateTimeOriginal
						if TAGS.get(k) == "DateTimeOriginal":
							self._exif["original_datetime"] = v

						# extract DateTime
						elif TAGS.get(k) == "DateTime":
							self._exif["datetime"] = v


						# insert rest of exif in string
						else:
							exifList.append(TAGS.get(k) + ":" + str(v))

				#TODO pipe | separated list of all other exif tags
				# encoding problem
				# self._exif["exif"] = "|".join(exifList)


	# get exif value by index
	# if no index, return dictionary
	def get(self,index = ""):
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

