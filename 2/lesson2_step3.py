import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.get('http://suninjuly.github.io/selects2.html')

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)
total = num1 + num2

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(total))

# browser.find_element_by_id('answer').send_keys(y)
# browser.find_element_by_id('robotCheckbox').click()
# browser.find_element_by_id('robotsRule').click()
browser.find_element_by_class_name('btn').click()

time.sleep(30)

browser.quit()


