from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/Adithan/Documents/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://www.instagram.com/accounts/login/')

sleep(3)

username = "username"
password = "password"

login = driver.find_elements_by_class_name('_2hvTZ.pexuQ.zyHYP')

login[0].send_keys(username)
login[1].send_keys(password)


login_button = driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
login_button.click()

sleep(3)

name = "friends_username"

search = driver.find_element_by_class_name('XTCLo.x3qfX')
search.send_keys(name)

sleep(3)

search_name = driver.find_elements_by_class_name('yCE8d')
search_name[0].click()

sleep(3)

try:
	post = driver.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
	post[0].click()

	while 1:
		sleep(1)

		like = driver.find_elements_by_class_name('wpO6b')

		like_svg = like[1].find_element_by_class_name('_8-yf5')
		if str(like_svg.get_attribute('aria-label')) == "Like":
			like[1].click()

		try:
			next_button = driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow')
			next_button.click()
		except:
			print("Viewed all the posts")
			break

except:
	print("No post found")




# sleep(3)

# comment = "Nice"

# comment_box = driver.find_element_by_class_name('Ypffh')
# try:
# 	comment_box.click()
# 	comment_box.send_keys(comment)
# except:
# 	print("hello")
# 	comment_box1 = driver.find_element_by_class_name('Ypffh.focus-visible')
# 	driver.execute_script("arguments[0].value = arguments[1]", comment_box1, comment);
# 	comment_button = driver.find_elements_by_class_name('sqdOP.yWX7d.y3zKF')
# 	comment_button[3].submit()
	
