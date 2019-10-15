import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.get('http://suninjuly.github.io/execute_script.html')

value = int(browser.find_element_by_id('input_value').text)

y = str(calc(value))

submit = browser.find_element_by_class_name('btn')
browser.execute_script("return window.scrollBy(0, 200);")
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
submit.click()

time.sleep(30)

browser.quit()


