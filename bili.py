from selenium import webdriver
from selenium.webdriver.common.by import By
web=webdriver.Chrome()
web.get('https://bilibili.com')
sou=web.find_element(by=By.XPATH,value='//*[@id="nav-searchform"]/div[1]/input')
sou.send_keys('原神')
input()