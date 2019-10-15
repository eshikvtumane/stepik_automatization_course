from selenium import webdriver
import time


def main(link):
    browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

    browser.get(link)
    elements = browser.find_elements_by_tag_name('input')

    browser.find_element_by_xpath('//label[text()="First name*"]')
    browser.find_element_by_xpath('//label[text()="Last name*"]')
    browser.find_element_by_xpath('//label[text()="Email*"]')
    browser.find_element_by_xpath('//label[text()="Phone:"]')
    browser.find_element_by_xpath('//label[text()="Address:"]')

    for element in elements:
        element.send_keys("М")

    button = browser.find_element_by_xpath('//button[@type="submit"]')

    button.click()
    browser.quit()


if __name__ == '__main__':
    main("http://suninjuly.github.io/registration1.html")
    print('Test 1 Success')
    main("http://suninjuly.github.io/registration2.html")
    print('Test 2 Success')
