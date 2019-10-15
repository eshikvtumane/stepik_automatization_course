import time

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import math

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price_element = browser.find_element_by_id('price')
WebDriverWait(browser, 25).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))

browser.find_element_by_id('book').click()

value = int(browser.find_element_by_id('input_value').text)

y = str(calc(value))

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id('solve').click()

time.sleep(30)

browser.quit()


