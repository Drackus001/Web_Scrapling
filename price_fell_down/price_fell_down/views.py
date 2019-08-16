from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import smtplib
import time

def button(request):
    
    return render(request,'home.html')
    
def output(request):

    URL = 'https://www.amazon.in/gp/product/B07SQYTHGK/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=2S4FK3XPHMCAD5TEQ65N&pf_rd_t=101&pf_rd_p=0b001d93-3a9d-453e-9bc6-24730b78af61&pf_rd_i=15096150031&th=1'

    headers = { "User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

    def check_price():
        """used to check product price goes down or not"""

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id='productTitle').get_text()
        price = soup.find(id='priceblock_ourprice').get_text()
        title = title.strip()
        print("\nProduct_title:", title[:23])

        price = price.replace(',','')
        price = int(price[2:7])
        print("\nProduct_price:", price)
        fell_price = 57000
        if(price < fell_price):
            print("\nMail sending...")
            send_mail(title, price)
        else:
            print('\nprice is '+str(price)+' which is still more than ',str(fell_price))
        
        

    def send_mail(title, price):
        """used to send gmail for price drop"""
        #password= "password"
        #email = "your_mail"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        your_email = 'your_mail@gmail.com'
        password= "password"

        receipient_email = 'your_mail@gmail.com'

        server.login(your_email,password)

        subject = 'Price fell down for ' + title[:23]
        body = 'New Price:'+ str(price) + '\nChech the amazon link:' + URL

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            your_email,
            receipient_email,
            msg
        )
        print("\nMail send successfully to",receipient_email)

    while(True):
        print("Checking for price drop...")
        time.sleep(3)
        check_price()
        print('waiting for two hour for again checking...')
        time.sleep(60 * 60 * 2) #checks every two hour
