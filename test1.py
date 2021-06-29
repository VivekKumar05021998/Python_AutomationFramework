from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", chrome_options=chrome_options)
driver.get("https://www.screener.in/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(10)

driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()
driver.find_element_by_xpath("//*[@type='text'][@name='username']").send_keys("novigo.rpa@gmail.com")
driver.find_element_by_xpath("//*[@type='password'][@name='password']").send_keys("Password")
print("After Password.")
driver.find_element_by_link_text("LOGIN").click()
#driver.find_element_by_xpath("//*[contains(text(),'LOGIN')]").click()
#driver.find_element_by_xpath("//*[contains(text(),'remi')]").click()
