from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.instagram.com/p/BtQAyDFHD6C/")
driver.implicitly_wait(3)
#v1Nh3 kIKUG  _bz0w
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
f = open("./html.txt","wt",encoding='UTF8')
f.write(str(soup))
f.close()
title = soup.find('title')
print(title.text)
'''
f = open("./list.txt","rt",encoding='UTF8')
lines = f.read().splitlines()
for line in lines:
	driver.get("https://www.insctagram.com/explore/tags/"+line)
	print(a)
f.close()
'''