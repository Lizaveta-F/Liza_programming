from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as dt

chrome_driver_path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

initial_time = dt.datetime.now()
cookies = int(driver.find_element(By.ID,"money").text)


game_on = True
portal = driver.find_element(By.CSS_SELECTOR,"#buyPortal b").text
portal_cookies = int(portal.split("-")[1].strip().replace(",",""))


shipment = driver.find_element(By.CSS_SELECTOR,"#buyShipment b").text
shipment_cookies = int(portal.split("-")[1].strip().replace(",",""))

mine = driver.find_element(By.CSS_SELECTOR,"#buyMine b").text
mine_cookies = int(portal.split("-")[1].strip().replace(",",""))

factory = driver.find_element(By.CSS_SELECTOR,"#buyFactory b").text
factory_cookies = int(portal.split("-")[1].strip().replace(",",""))

grandma = driver.find_element(By.CSS_SELECTOR,"#buyGrandma b").text
grandma_cookies = int(portal.split("-")[1].strip().replace(",",""))

coursor = driver.find_element(By.CSS_SELECTOR,"#buyCursor b").text
coursor_cookies = int(portal.split("-")[1].strip().replace(",",""))



while game_on:
    cookie = driver.find_element(By.ID,"cookie")
    cookie.click()
    if dt.datetime.now()==initial_time+dt.timedelta(seconds=100):
        game_on = False
        print(driver.find_element(By.ID, "cps"))
    elif dt.datetime.now().second %5==0:
        if cookies>=coursor_cookies:
            coursor = driver.find_element(By.CSS_SELECTOR,"#buyCursor b")
            coursor.click()
        elif cookies>=grandma_cookies:
            grandma = driver.find_element(By.CSS_SELECTOR,"#buyGrandma b")
            grandma.click()
        elif cookies>=factory_cookies:
            factory = driver.find_element(By.CSS_SELECTOR,"#buyFactory b")
            factory.click()
        elif cookies>=mine_cookies:
            mine = driver.find_element(By.CSS_SELECTOR,"#buyMine b")
            mine.click()
        elif cookies>=shipment_cookies:
            shipment = driver.find_element(By.CSS_SELECTOR,"#buyShipment b")
            shipment.click()
        elif cookies>=portal_cookies:
            portal = driver.find_element(By.CSS_SELECTOR,"#buyPortal b")
            portal.click()
        


        