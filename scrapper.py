import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/gp/product/B07SQYTHGK/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=2S4FK3XPHMCAD5TEQ65N&pf_rd_t=101&pf_rd_p=0b001d93-3a9d-453e-9bc6-24730b78af61&pf_rd_i=15096150031&th=1'

headers = { "User-Agent" :"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

title = soup.find(id='productTitle').get_text()
#mrp = soup.find(class='priceBlockStrikePriceString a-text-strike').get_text()
price = soup.find(id='priceblock_ourprice').get_text()

print("Product title:", title.strip())
#print("Product M.R.P:", )
print("Product price:", price[2:8])
