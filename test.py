import sys
import pyexiv2

path = "/media/datenserver/media/bilder/Familie/Jitka/cimg2377.jpg"

metadata = pyexiv2.ImageMetadata(path)
metadata.read()


print (metadata.iptc_keys)
print (metadata["Iptc.Application2.Keywords"])

# metadata["Iptc.Application2.Keywords"] = ["Mödling"]
# metadata.write()