import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Accept-Language':'en-US',
    'Request Line':'GET / HTTP/1.1',
            }

link = "https://www.amazon.com/New-Apple-Watch-GPS-44mm/dp/B08KTW1YD3/ref=sr_1_7?keywords=apple+watch&qid=1671400857&sr=8-7"
response = requests.get(url='https://www.amazon.com/New-Apple-Watch-GPS-44mm/dp/B08KTW1YD3/ref=sr_1_7?keywords=apple+watch&qid=1671400857&sr=8-7',
                        headers=headers)

soup = BeautifulSoup(response.content, 'lxml')

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user="wifihsj56@gmail.com", 
                 password="diiboyjzmcdtkjth")

if price < 200:
    connection.sendmail(from_addr="wifihsj56@gmail.com", 
                        to_addrs="ellizabetta.fadeeva@gmail.com", 
                        msg=f"Subject:Price drop: don't miss out! \n\n The price for the product Apple Watch has dropped to {price}$! Follow the link to buy: {link} .")
    connection.close
