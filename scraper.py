from requests import get
from bs4 import BeautifulSoup

from sys import argv
from re import sub
import json


def scraper():
    """
    Scrapes the osu! country leaderboard and returns the top 50 players
    """

    try:
        country = str(argv[1]).upper()
    except IndexError:
        return print('You need to input a country code')
    try:
        gamemode = str(argv[2])
    except IndexError:
        gamemode = 'osu'

    print('Scraping...')
    data = get(f'https://osu.ppy.sh/rankings/{gamemode}/performance?country={country}')
    scraped = BeautifulSoup(data.text, 'html.parser')
    users = scraped.find_all('a', class_='ranking-page-table__user-link-text')

    userinfo = {}
    for user in users:
        name = sub(r'\s*', '', user.text) # Fix later
        userinfo[name] = user['data-user-id']

    userinfo = json.dumps(userinfo, indent=4, sort_keys=True)
    with open(f'top50-{country}.json', 'w', encoding='utf-8') as f:
        f.write(userinfo)

    print('FINISHED!')


scraper() # Runs the program