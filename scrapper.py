import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/gp/product/B07SQYTHGK/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=2S4FK3XPHMCAD5TEQ65N&pf_rd_t=101&pf_rd_p=0b001d93-3a9d-453e-9bc6-24730b78af61&pf_rd_i=15096150031&th=1'

headers = { "User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

def check_price():
    """used to check product price goes down or not"""

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    print("\nProduct_title:", title.strip())

    price = price.replace(',','')
    price = int(price[2:7])
    print("\nProduct_price:", price)
    
    if(price < 57500):
        print("\nMail sending...")
        send_mail()
    
    

def send_mail():
    """used to send gmail for price drop"""
    #password= "password"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    your_email = 'yourmail@gmail.com'
    password= "password"

    receipient_email = 'yourmail@gmail.com'

    server.login(your_email,password)

    subject = 'Price fell down'
    body = 'Chech the amazon link:' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        your_email,
        receipient_email,
        msg
    )
    print("\nMail send successfully to",receipient_email)

check_price()


