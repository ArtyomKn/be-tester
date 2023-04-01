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
acc_btn = driver.find_element_by_id('menu-item-50')
acc_btn.click()
email = driver.find_element_by_id('reg_email')
email.send_keys('tester23@mail.ru')
password = driver.find_element_by_id('reg_password')
password.send_keys ('Qazwsx123456qwertyABC')
submit = driver.find_element_by_name('register')
submit.click()
time.sleep(10)
driver.quit()


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
acc_btn = driver.find_element_by_id('menu-item-50')
acc_btn.click()
email = driver.find_element_by_id('username')
email.send_keys('tester23@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys ('Qazwsx123456qwertyABC')
login = driver.find_element_by_name('login')
login.click()
logout = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/customer-logout/"]')
logout_text = logout.text
assert logout_text == 'Logout'
driver.quit()