import requests
from bs4 import BeautifulSoup
import html5lib

url = input("Please Enter the Website you would like to check for WordPress: ")
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")
meta_check = soup.find_all('meta', attrs={'name': 'generator'})
soup_string = str(meta_check)

if "WordPress" in soup_string:
    print("Yes, this site contains WordPress")
else:
    print("No, I don't believe this site was made with WordPress")





