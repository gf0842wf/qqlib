# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
)


def truncated_gauss(mu, sigma, min, max):
    counter = 0
    while True:
        v = random.gauss(mu, sigma)
        if counter >= 10:
            return random.choice([min, max])
        if min <= v <= max:
            return v
        counter += 1


os.environ["SELENIUM_SERVER_JAR"] = '/Users/flyking/Documents/work/selenium/selenium-server-standalone-2.53.1.jar'

browser = webdriver.Safari()
# browser = webdriver.PhantomJS(executable_path='./phantomjs', desired_capabilities=dcap)
browser.set_window_position(20, 40)
browser.set_window_size(1100, 700)
url = 'http://i.qq.com/'
browser.get(url)
browser.switch_to_frame("login_frame")
browser.find_element_by_id('switcher_plogin').click()
browser.find_element_by_id('u').clear()
browser.find_element_by_id("u").send_keys("2932263438")
browser.find_element_by_id('p').clear()
browser.find_element_by_id("p").send_keys("fqfhhr57")
browser.find_element_by_id("login_button").click()
print browser.execute_script("return document.getElementsByTagName('html')[0].outerHTML;",
                             browser.find_element_by_xpath("//*"))
time.sleep(100)
browser.quit()
