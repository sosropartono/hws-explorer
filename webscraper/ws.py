# Using of beautiful soup
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.reddit.com/r/hardwareswap/")