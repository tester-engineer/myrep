'''
本篇主要讲如何用Python调用webdriver框架的API，对浏览器做一些常规的操作，如打开、前进、后退、刷新、设置窗口大小、截屏、退出等操作。
'''

#coding:utf-8
# 导入webdriver模块
from selenium import webdriver
import time
#打开浏览器
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
#打开百度
driver.get('http://www.baidu.com')
time.sleep(2)
# 刷新
driver.refresh()
driver.get('http://www.sogo.com')
time.sleep(2)
#返回上一页
driver.back()
time.sleep(2)
# 下一页
driver.forward()
# 设置窗口大小
time.sleep(2)
driver.set_window_size(500,900)
time.sleep(2)
driver.maximize_window()

driver.get_screenshot_as_file('./img/1_browwser.png')

driver.close() # 关闭当前浏览器窗口
driver.quit()  # 推出浏览器进程
