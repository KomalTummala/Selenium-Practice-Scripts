from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def run_test():
    #Test Case 1 : To close the Pop Up.
    driver = webdriver.Chrome()
    driver.get("https://www.candymapper.net/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID,'comp-lx0kg6on').click()
    time.sleep(4)

    # Test case 2 : To fill up contact form 
    driver.find_element(By.XPATH,"//input[@placeholder='First name']").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//input[@placeholder='First name']").send_keys('Komal')
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,'#form-field-input-a3d611ef-b210-4c6a-774d-5d74017a2727-comp-lvvqr5lq5-').send_keys('Tummala')
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="form-field-input-37274bb7-95a4-40a5-430b-fe940c1ffac1-comp-lvvqr5lq5-"]').send_keys("Komal.tummala@gmail.com")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,'s__35_i7B').click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,'input[data-hook="country-search"]').send_keys("India")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'span[aria-label="India"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="form-field-input-e748788c-1134-4c9d-060b-c0e20b9efd43-comp-lvvqr5lq5-"]').send_keys("9940108376")
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="form-field-input-ec56f152-7a85-4f85-d098-ebe96cc55048-comp-lvvqr5lq5-"]').send_keys("This Test is successful")
    time.sleep(4)
    input("⚠️ Please solve CAPTCHA if visible, then press Enter to continue...")
    driver.find_element(By.CSS_SELECTOR,'button[data-hook ="submit-button"]').click()
    
    # If encountered Captcha solve it manually and move on with the test 
    time.sleep(30)
    
    
    # Test 3 : Simple way to check if the test were successful
    driver.save_screenshot("Success Message.png")
    driver.quit()

# Test Run Successfully Message    
    print("Test Completed Successfully")

for i in range(2):
    print(f"Running Test Iteration {i+1}...")
    run_test()
