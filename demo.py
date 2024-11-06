from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time
import video
cat=video.Cat('https://www.youtube.com/watch?v=C13rgCjaOXI')
cat.download_video()
web=webdriver.Chrome()
web.get('https://bilibili.com')
wait = WebDriverWait(web, 10)
original_window = web.current_window_handle
f=open('small_cat/cookie.json','r')
Cookie=json.loads(f.read())
for cookie in Cookie:
    web.add_cookie(cookie)
web.refresh()
web.execute_script("window.open('https://member.bilibili.com/platform/upload/video/frame?spm_id_from=333.1007.top_bar.upload');") 
all_windows = web.window_handles   

# 切换到新打开的窗口  
for window in all_windows:  
    if window != original_window:  
        web.switch_to.window(window)  
        break  # 找到新窗口后跳出循环  
# tougao=web.find_element(by=By.XPATH,value='//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[7]/li/a/div')
# tougao.click()
# wait = WebDriverWait(web, 10)
time.sleep(10)
chuanru=web.find_element(by=By.XPATH,value='//*[@id="video-up-app"]/div[1]/div[2]/div/div[1]/div/div/input')
bi=video.BiliUpload(video_title='test',video_type=0,video_path=f'{cat.output_path}',main_partition='游戏',minor_partition='网络游戏',video_tag=True)
chuanru.send_keys(f"{bi.video_path}")
guodu=web.find_element(by=By.XPATH,value='//*[@id="video-up-app"]/div[3]/div/div[3]/button')
guodu.click()
# title=web.find_element(by=By.XPATH,value='//*[@id="video-up-app"]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/input')
# title.send_keys(f"{bi.title}")

transshipment = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="转载"]')))
zizhi=web.find_element(by=By.XPATH,value='//span[text()="自制"]')
time.sleep(2)
if bi.video_tag:
    transshipment.click()
else:
    zizhi.click()
fenqu=web.find_element(by=By.XPATH,value='//*[@class="select-controller"]')
fenqu.click()
main_partition=bi.main_partition
minor_partition=bi.minor_partition
parent_main_partition = web.find_element(by=By.XPATH,value=f'{main_partition}')
parent_main_partition.click()
parent_minor_partition = web.find_element(by=By.XPATH,value=f'{minor_partition}')
# parent_main_partition = main_partition.find_element(By.XPATH, './parent::*')
# parent_minor_partition = minor_partition.find_element(By.XPATH, './parent::*')
parent_minor_partition.click()
input()