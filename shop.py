import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
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
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
html_btn = driver.find_element_by_css_selector('[data-product_id="181"]')
html_btn.click()
title_name = driver.find_element_by_css_selector('[itemprop="name"]')
title_text = title_name.text
assert title_text == 'HTML5 Forms'
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
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
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
ht_btn = driver.find_element_by_css_selector('.cat-item-19 > a')
ht_btn.click()
item_count = driver.find_elements_by_css_selector('[rel="nofollow"]')
assert len(item_count) == 3
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
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
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
sel = driver.find_element_by_css_selector('[value="menu_order"]')
sel_value = sel.get_attribute("selected")
assert sel_value is not None
ctor = driver.find_element_by_class_name('orderby')
sel_ctor = Select(ctor)
sel_ctor.select_by_value('price-desc')
ctor1 = driver.find_element_by_css_selector('[value="price-desc"]')
ctor1_1 = ctor1.get_attribute('selected')
assert ctor1_1 is not None
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
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
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
android = driver.find_element_by_css_selector('[alt="Android Quick Start Guide"]')
android.click()
del_price = driver.find_element_by_css_selector('del > span')
del_count = del_price.text
assert del_count == '₹600.00'
price = driver.find_element_by_css_selector('ins > span')
price_text = price.text
assert price_text == '₹450.00'
title_img = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'[title="Android Quick Start Guide"]'))
)
title_img1 = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
title_img1.click()
img_clos = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'pp_close'))
)
img_clos1 = driver.find_element_by_class_name('pp_close')
img_clos1.click()
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
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
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
product = driver.find_element_by_css_selector('[data-product_id="165"]')
product.click()
time.sleep(5)
items = driver.find_element_by_class_name('cartcontents')
items_text = items.text
assert items_text == '1 Item'
amount = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
amount_text = amount.text
assert amount_text == '₹350.00'
items.click()
ama = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[data-title="Subtotal"] > .woocommerce-Price-amount'),'₹350.00')
)
ana = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'strong > .amount'),'₹357.00')
)
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
product = driver.find_element_by_css_selector('[data-product_id="165"]')
product.click()
time.sleep(5)
items = driver.find_element_by_class_name('cartcontents')
items.click()
time.sleep(5)
remove = driver.find_element_by_class_name('remove')
remove.click()
time.sleep(7)
undo = driver.find_element_by_css_selector('.woocommerce-message > a')
undo.click()
quanity = driver.find_element_by_css_selector('.input-text.qty')
quanity.clear()
quanity.send_keys(3)
time.sleep(5)
update = driver.find_element_by_css_selector('[value="Update Basket"]')
update.click()
quan = quanity.get_attribute('value')
assert quan == '3'
time.sleep(5)
coupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
coupon.click()
time.sleep(5)
error = driver.find_element_by_css_selector('.woocommerce-error > li')
error_text = error.text
assert error_text == 'Please enter a coupon code.'
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
product = driver.find_element_by_css_selector('[data-product_id="165"]')
product.click()
time.sleep(5)
items = driver.find_element_by_class_name('cartcontents')
items.click()
proceed_text = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'checkout-button'))
)
proceed = driver.find_element_by_class_name('checkout-button')
proceed.click()
zag = driver.find_element_by_css_selector('.woocommerce-billing-fields > h3')
zag1 = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.woocommerce-billing-fields > h3'),'Billing Details')
)
name = driver.find_element_by_id('billing_first_name')
name.send_keys('Artyom')
last = driver.find_element_by_id('billing_last_name')
last.send_keys('Ivanov')
ema = driver.find_element_by_id('billing_email')
ema.send_keys('tester23@mail.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('+79999999999')
adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Lenina 43')
town = driver.find_element_by_id('billing_city')
town.send_keys('Moscow')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('653066')
country = driver.find_element_by_id('s2id_billing_country')
country.click()
country1 = driver.find_element_by_id('s2id_autogen1_search')
country1.send_keys('rus')
time.sleep(3)
country2 = driver.find_element_by_css_selector('#select2-results-1 > li:nth-child(3)')
country2.click()
state = driver.find_element_by_id('billing_state')
state.send_keys('Moscow')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_pay = driver.find_element_by_css_selector('[for="payment_method_cheque"]')
check_pay.click()
btn = driver.find_element_by_id('place_order')
btn.click()
text_1 = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME,'woocommerce-thankyou-order-received'),'Thank you. Your order has been received.')
)
text_2 = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'tfoot > tr:nth-child(3) > td'),'Check Payments')
)
driver.quit()