import requests
from bs4 import BeautifulSoup
import smtplib



URL = 'https://www.amazon.co.uk/Sennheiser-HD-598-Cs-Around-Ear-Matte-Black/dp/B01JP436TS/ref=sr_1_7?keywords=sennheiser+headset+598&qid=1571316520&sr=8-7'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:6])

    if(converted_price < 100):
        send_mail()



    print(converted_price)
    print(title.strip())

    if(converted_price > 100):
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('andysempai12@gmail.com', 'ocbhdmemnkvkvzea')

    subject = 'Price has decreased.'
    body = 'Check the amazon listing : https://www.amazon.co.uk/Sennheiser-HD-598-Cs-Around-Ear-Matte-Black/dp/B01JP436TS/ref=sr_1_7?keywords=sennheiser+headset+598&qid=1571316520&sr=8-7'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'andysempai12@gmail.com',
        'andytown@live.ie',
        msg
    )
    print("The e-mail has been sent")

    server.quit()


check_price()