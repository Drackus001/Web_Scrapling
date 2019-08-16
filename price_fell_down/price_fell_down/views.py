from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from .forms import MyForm


def home(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['product_link']
            price = form.cleaned_data['price']
            email = form.cleaned_data['email']
            scrapper(url, price, email)
            print(price, email, url)


    form = MyForm()
    return render(request, 'home.html',{'form': form})


def scrapper(url, price, email):
    """ scrapper(url,price and email)"""

    #URL = 'https://www.amazon.in/gp/product/B07SQYTHGK/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=2S4FK3XPHMCAD5TEQ65N&pf_rd_t=101&pf_rd_p=0b001d93-3a9d-453e-9bc6-24730b78af61&pf_rd_i=15096150031&th=1'
    
    
    URL = url
    fell_price = int(price)
    #price = int(fell_price)
    email = email


    while(True):
        print("Checking for price drop...")
        time.sleep(3)
        check_price(URL, fell_price, email)
        print('\nWaiting for one hour for again checking...')
        time.sleep(60 * 60 * 1)  # checks every two hour


    

def check_price(URL, fell_price, email):
    """used to check product price goes down or not"""

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    try:

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id='productTitle').get_text()
        link_price = soup.find(id='priceblock_ourprice').get_text()
        title = title.strip()
        print("\nProduct_title:", title[:23])

        link_price = link_price.replace(',', '')
        
        link_price = int(link_price[2:-3])
        print("\nProduct_price:", link_price)
        
        if(link_price < fell_price):
            print("\nMail sending...")
            send_mail(URL, title, link_price, email)
        else:
            print('\nprice is '+str(link_price) +
                    ' which is still more than ', str(fell_price))

    except:
        print('invaled url')
        raise('')

    


def send_mail(URL, title, price, email):
    """used to send gmail for price drop"""
    #password= "password"
    #email = "your_mail"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    your_email = 'your_email'
    password = "password"

    receipient_email = email

    server.login(your_email, password)

    subject = 'Price fell down for ' + title[:23]
    body = 'New Price:' + str(price) + '\nChech the amazon link:' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        your_email,
        receipient_email,
        msg
    )
    print("\nMail send successfully to", receipient_email)

 
