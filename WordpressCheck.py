#Checks the metatags of a site for WordPress
import requests
from bs4 import BeautifulSoup
import html5lib


def addHTML(url1):
    if "http" in url1:
        return url1
    else:
        return "http://" + url1


def checker(url):
    newurl = addHTML(url)

    try:
        r = requests.get(newurl)

        soup = BeautifulSoup(r.content, "html5lib")
        meta_check = soup.find_all('meta', attrs={'name': 'generator'})
        soup_string = str(meta_check)

        if "WordPress" or "Wordfence" in soup_string:
            return "Yes, this site contains WordPress"
        else:
            return "No, I don't believe this site was made with WordPress"
    except requests.exceptions.MissingSchema:
        return "Not a valid HTTP code"
    except requests.exceptions.ConnectionError:
        return "not Connecting right"



