import requests
from bs4 import BeautifulSoup


def fetch_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extrair dados conforme a estrutura do site
    headlines = [headline.get_text() for headline in soup.find_all('h2')]
    return headlines
