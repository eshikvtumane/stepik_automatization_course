import time

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element_by_name('firstname').send_keys('F')
browser.find_element_by_name('lastname').send_keys('L')
browser.find_element_by_name('email').send_keys('a@.re')


full_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
browser.find_element_by_id('file').send_keys(full_path)


submit = browser.find_element_by_class_name('btn')

submit.click()

time.sleep(30)

browser.quit()


