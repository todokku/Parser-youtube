import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login = "+"
password = ""

browser = webdriver.Chrome(r'C:\Users\1\Desktop\New_Project\Insta\chromedriver')
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(login)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(password)

browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]").click()

time.sleep(3)

browser.get("https://www.instagram.com/natgeotravel/")
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(3)
element = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a")
#



# actions = ActionChains(browser)
# elem = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/a")
# actions.move_to_element(elem)
# actions.click()
# actions.send_keys(Keys.ARROW_DOWN)
# actions.send_keys(Keys.ARROW_DOWN)
# actions.send_keys(Keys.ARROW_DOWN)
# actions.perform()
# actions.reset_actions()
# browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[1]").send_keys(Keys.END)
# element.send_keys(Keys.END)
# time.sleep(0.5)
#
# browser.find_element_by_tag_name('body').send_keys(Keys.END)
# persons = browser.find_elements_by_xpath("/html/body/div[4]/div/div[1]/div/h1")

#
# f = open("c:/Users/1/Desktop/New_Project/insta/person.txt", 'w')
# f.write(str(persons))
# f.close()
#
#
#
# browser.execute_script("window.scrollTo(0, window.scrollY + 400)")
