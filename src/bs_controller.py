import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class RootIndex:
    def __init__(self, text: str, filetype: str):
        self.text = text
        self.filetype = filetype
        self.get_url()
        self.read_page()

    def get_url(self):
        search_text = f"{self.text} filetype:{self.filetype}"
        self.url = f"https://www.google.com/search?{urlencode({'q': search_text})}"

    def read_page(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text)
        self.results = soup.find_all('div', class_='egMi0')

    def get_href(self, href: str) -> str:
        temp = href.split('&')
        return temp[0][7:] or ''

    def create_results(self):
        ret = []
        for result in self.results:
            title = result.find('h3').text
            result_url = result.find('a').get('href')

            ret.append({
                "title": title,
                "url": self.get_href(result_url)
            })
        return ret
