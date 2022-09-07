import requests 
from bs4 import BeautifulSoup

jobs_in_wales = 'https://www.jobsinwales.com/results?t=Wales&r=10'
r = requests.get(jobs_in_wales)
soup = BeautifulSoup(r.text,'lxml')

block = soup.find('li',class_='list-group-item job-list enhanced').find('div',class_='job-salary').text
print(block[block.find('£')+1:block.find(' ')])