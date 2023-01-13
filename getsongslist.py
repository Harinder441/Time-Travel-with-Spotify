import requests as req
from bs4 import BeautifulSoup


def generate_top25(date="2022-06-10")-> list:
    """return a list of top 25 indian songs from billboard.
    date start from 2022-02-00"""
    res = req.get(url=f"https://www.billboard.com/charts/india-songs-hotw/{date}/")
    content = res.text
    soup = BeautifulSoup(content, "html.parser")
    songs_list = soup.select(selector=".chart-results-list .c-title")
    songs_list = [(item.string).strip("\n\t") for item in songs_list]
    songs_list25 = songs_list[2:]
    return songs_list25


if __name__ == "__main__":
    generate_top25()
