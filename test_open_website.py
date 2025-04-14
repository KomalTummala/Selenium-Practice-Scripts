# test_open_website.py

from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get('https://www.google.com')
driver.maximize_window()
time.sleep(2)
if driver.title:
    print("Test Passed")
else:
    print("Test Failed")
time.sleep(10) 
driver.quit()
