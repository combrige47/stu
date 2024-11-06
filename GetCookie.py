import json
import time

from selenium import webdriver

bilibili = webdriver.Chrome()
bilibili.get("https://www.bilibili.com")
bilibili.delete_all_cookies()
time.sleep(30)
bilibili.refresh()
cookie=bilibili.get_cookies()
json_cookie=json.dumps(cookie)

with open("small_cat/cookie.json",'w') as f:
    f.write(json_cookie)
bilibili.close()
