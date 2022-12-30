from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR,"div.event-widget time")
   
list_dates = [date.text for date in dates]


names = driver.find_elements(By.CSS_SELECTOR,'div.event-widget li a')
names_list = [name.text for name in names]
events = {}

for n in range (len(dates)):
    events[n] = {
        'date':list_dates[n],
        'name':names_list[n],
    }
print(events)
    
driver.quit()

