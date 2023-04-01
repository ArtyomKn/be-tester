import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
rd_button = driver.find_element_by_css_selector('[data-product_id="163"]')
rd_button.click()
rev_button = driver.find_element_by_class_name('reviews_tab')
rev_button.click()
star = driver.find_element_by_class_name('star-5')
star.click()
comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('Artyom')
email = driver.find_element_by_id('email')
email.send_keys('test@mail.ru')
subm = driver.find_element_by_id('submit')
subm.click()
driver.quit()