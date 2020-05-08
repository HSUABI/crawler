#빠삭 사이트 자동댓글
from selenium import webdriver

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/Users/Gullabjamun/Downloads/chromedriver.exe')

## url에 접근한다.
driver.get('https://bbasak.com/')

driver.implicitly_wait(3)
closebtn = driver.find_element_by_class_name("close_btn")
closebtn2 = driver.find_element_by_css_selector("#divpop > table > tbody > tr:nth-child(2) > td > input[type=checkbox]")


closebtn2.click()
closebtn.click()



idfield = driver.find_element_by_id("login_id")
pwfield = driver.find_element_by_class_name('ip2')

idfield.send_keys("ID");
pwfield.send_keys("PW");
loginbtn = driver.find_element_by_class_name('btn_login')

loginbtn.click()


menu_story = driver.find_element_by_css_selector("#gnb2 > li:nth-child(6) > span > a")
menu_story.click()

driver.find_element_by_css_selector("#fboardlist > table:nth-child(12) > tbody > tr:nth-child(2) > td.tit > p > a").click()

for i in (0,150):
	driver.implicitly_wait(30)
	driver.find_element_by_id("wr_content").send_keys("좋은글이네요 잘 읽고갑니다.")
	element = driver.find_element_by_css_selector('#comment_write > div > div:nth-child(2) > button.cmt_btn.btn-show-control')
	driver.execute_script("arguments[0].click();", element)
	driver.find_element_by_css_selector('#board_href_move > li:nth-child(2) > a').click()
	driver.implicitly_wait(30)