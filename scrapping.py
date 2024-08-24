import requests
from bs4 import BeautifulSoup
import argparse
import time


def search(user_url, user_author):
    # check for empty input
    if not user_author.strip():
        return

    url = user_url
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            author = quote.find('small', class_='author').text
            if user_author.lower() == author.lower() or user_author.lower() in author.lower():
                text = quote.find('span', class_='text').text
                print(f'{author} \nQuote: {text}\n')

        next_button = soup.find('li', class_='next')
        if next_button:
            next_link = next_button.find('a')['href']
            url = f'http://quotes.toscrape.com{next_link}'
        else:
            url = None


if __name__ == '__main__':
    print('Search for your favorite quotes by author name')
    time.sleep(5)

    parser = argparse.ArgumentParser(description='Search for quotes by author on quotes.toscrape.com')
    parser.add_argument('--author', type=str, help="Name of author to search for")

    args = parser.parse_args()
    if args.author:
        user_author = args.author
    else:
        user_author = input('Enter author name: ')
    base_url = 'http://quotes.toscrape.com/'

    search(base_url, user_author)
