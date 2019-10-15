import time

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/cats.html')

browser.find_element_by_id("button")

browser.quit()


