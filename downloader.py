import urllib
import requests
from readDocx import doc_reader

def download():
	

	url_list = doc_reader()
	#return url_list

#print(download())
	

    #iterating through each url in the list and downloading them
	for url in url_list:
		print(url)
		print('Begining file download.....')
		urllib.request.urlretrieve(url,'/home/kamal_pasha/First_Project/minemaster.zip')
		print('Completed')

download()




