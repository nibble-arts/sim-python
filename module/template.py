import lxml.etree as ET


class Template:

	xml_filename = ""
	xsl_filename = ""

	def __init__(self,name):

		self.xsl_filename = "html/"+name+".xsl"


	def transform(self,xml):

		dom = ET.fromstring(xml)
		xslt = ET.parse(self.xsl_filename)

		transform = ET.XSLT(xslt)

		result = transform(dom, title="'SWIM'")

		return ET.tostring(result, pretty_print=True)