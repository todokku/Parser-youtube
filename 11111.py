login = "babchenko1983@gmail.com"
password = "Igor1983!"
import time

from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\1\Desktop\New_Project\Insta\chromedriver.exe")

browser.get("https://www.youtube.com/")

browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string").click()

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(login)

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
time.sleep(2)

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
time.sleep(3)
urls = []
browser.get("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252Fwatch%253Fv%253DHozWlQNY8xE%26hl%3Duk%26feature%3Dplaylist%26app%3Ddesktop%26action_handle_signin%3Dtrue&amp;hl=uk&amp;passive=true&amp;service=youtube&amp;uilel=3")
time.sleep(5)
element = browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button")
a = 0
while len(urls) < 100:
    a += 1
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, window.scrollY + 800)", element)
    time.sleep(2)
    persons = browser.find_elements_by_id("author-text")
    for i in persons:
        urls.append(i.get_attribute('href'))

f = open("c:/Users/1/Desktop/New_Project/Insta/person.txt", 'w')
for pers in urls:
    f.write(str(pers))
    f.write("\n")
f.close()

print(len(urls))
