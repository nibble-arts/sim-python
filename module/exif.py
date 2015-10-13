""" class for exif data extraction """
from PIL import Image
from PIL.ExifTags import TAGS

class Exif:

	exif = {}

	def __init__(self,path):

		# get image data
		img = Image.open(path)

		# self.exif["width"] = img.size[0]
		# self.exif["height"] = img.size[1]
		# self.exif["bits"] = img.bits

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
						self.exif["original_datetime"] = v

					# extract DateTime
					elif TAGS.get(k) == "DateTime":
						self.exif["datetime"] = v


					# insert rest of exif in string
					else:
						exifList.append(TAGS.get(k) + ":" + str(v))

			self.exif["exif"] = "|".join(exifList)
		pass
