from selenium import webdriver
from bs4 import BeautifulSoup


# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:/chromedriver')


driver.implicitly_wait(3)
driver.get('https://www.naver.com/')
string = driver.find_element_by_xpath("//*[@id='PM_ID_ct']/div[1]/div[2]/div[2]/div[1]/div/ul")

#selenium , only 1st
#print("selenium : %s" %(string.text) )


#bs4
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
rank = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_r")
content = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")



#rank_list=rank[0].text.split()
for i,j in zip(rank,content):
	print(i.text ,"위 :", j.text)



