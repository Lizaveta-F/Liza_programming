from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import time

chrome_driver_path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.yahoo.com/')

# number = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# # number.click()
# # driver.quit()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

login = driver.find_element(By.CSS_SELECTOR,"#ybarAccountProfile a")
login.click()

driver.quit()

# driver.get("https://login.yahoo.com/?.lang=en-US&src=homepage&activity=ybar-signin&pspid=2023538075&done=https%3A%2F%2Fwww.yahoo.com%2F&add=1")
# sign_in = driver.find_element(By.ID,"login-username")
# sign_in.send_keys("john1ivanov20635@yahoo.com")
# sign_in_button = driver.find_element(By.ID,"login-signin")
# sign_in_button.click()

# driver.get("https://login.yahoo.com/account/challenge/password?.lang=en-US&src=homepage&activity=ybar-signin&pspid=2023538075&done=https%3A%2F%2Fwww.yahoo.com%2F&add=1&sessionIndex=QQ--&acrumb=hDbUTe3v&display=login&authMechanism=primary")
# password = driver.find_element(By.ID,"login-passwd")
# password.send_keys("John567!*7g")
# password_button = driver.find_element(By.ID, "login-signin")
# password_button.click()





