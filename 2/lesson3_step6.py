import time

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element_by_class_name('btn').click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

value = int(browser.find_element_by_id('input_value').text)

y = str(calc(value))

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_class_name('btn').click()

time.sleep(30)

browser.quit()


