from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
serch = driver.find_element('name', 'q')
serch.send_keys('날씨')
serch.send_keys(Keys.RETURN)

time.sleep(1000)