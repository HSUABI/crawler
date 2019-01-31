from bs4 import BeautifulSoup
import requests
import selenium.webdriver as webdriver

'''
f = open("./list.txt","rt",encoding='UTF8')
lines = f.read().splitlines()
print(lines)
for line in lines:
	req = requests.get("https://www.instagram.com/explore/tags/"+line)
	html = req.text
'''
f = open("./list.txt","rt",encoding='UTF8')
f2 = open("./url.txt","wt",encoding='UTF8')
lines = f.read().splitlines()

for line in lines:
	req = requests.get('https://www.instagram.com/explore/tags/'+line)
	html = req.text
	urls = html.split('"shortcode":"')
	urls=urls[1:-1]
	f2.write("search item : "+line+"\n")
	for i in urls:
		index = i.find(",")
		url = i
		f2.write("\t"+url[0:index-1]+"\n") 
f.close()
f2.close()




