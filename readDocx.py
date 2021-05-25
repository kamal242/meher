#specific to extracting information from word documents
import os
import zipfile

#useful tool for extracting information from XML
import re

#to pretty print our xml:
import xml.dom.minidom





def doc_reader():
	#reading docx file
	document = zipfile.ZipFile('./headings.docx')

	#Gets the xml that has the text contained in the document
	uglyXml = xml.dom.minidom.parseString(document.read('word/document.xml')).toprettyxml(indent='  ')

	text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
	prettyXml = text_re.sub('>\g<1></', uglyXml)


	#converts xml content into a string
	xml_content = document.read('word/document.xml')
	document.close()
	xml_str = str(xml_content)

	#Applying regex to extract hyperlinks in the string
	link_list = re.findall('http.*?\<',xml_str)[1:]
	link_list = [x[:-1] for x in link_list]

	return link_list

