from selenium import webdriver
username = 'xc9dv4d4vyb9'
password = '#Alleycafe123'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.alleymenu.com/cpanel')
user_input = driver.find_element_by_id('user')
user_input.send_keys(username)
user_pass = driver.find_element_by_id('pass')
user_pass.send_keys(password)
login_button = driver.find_elements_by_id('login_submit')
login_button[0].click()