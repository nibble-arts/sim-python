import lxml.etree as ET


class Template:

	xml_filename = ""
	xsl_filename = ""

	def __init__(self,name):

		self.xsl_filename = "html/"+name+".xsl"


	def transform(self,xml,param):

		dom = ET.fromstring(xml)
		xslt = ET.parse(self.xsl_filename)

		transParam = self.unlist(param)
		
		transform = ET.XSLT(xslt)
		result = transform(dom, **transParam)

		return ET.tostring(result, pretty_print=True)


	def unlist(self,list):
		newList = {}

		for key in list:
			newList[key] = "'"+list[key][0]+"'"

		return newList
