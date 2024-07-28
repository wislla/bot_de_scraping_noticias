from scraping.scraper import fetch_news
from database.models import get_session, NewsArticle
from email.email_sender import send_email


def main():
    url = 'https://news.example.com'
    headlines = fetch_news(url)
    
    session = get_session()
    for headline in headlines:
        article = NewsArticle(id='some_id', headline=headline)
        session.add(article)
    session.commit()
    
    send_email('Daily News Summary', '\n'.join(headlines), ['recipient@example.com'])


if __name__ == '__main__':
    main()
