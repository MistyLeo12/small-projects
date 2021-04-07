"""
Web Scraper for getting drinks dat to add to my random drink recepie project
"""
import requests

def scraper(url):
    res = requests.get(url)
    text = res.text
    status_code = res.status_code     
    print(status_code)
    return (text, status_code)

scraper('https://www.esquire.com/food-drink/drinks/g32402296/best-rum-cocktails/')