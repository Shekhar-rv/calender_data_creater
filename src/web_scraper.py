from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, html_file: str ):
        self.html_file = html_file

    def get_li_titles(self):
        with open(self.html_file, 'r') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            # Find all 'li' elements with a class
            li_elements = soup.find_all('li', class_=True)
            return [li.get('title') for li in li_elements if li.get('title') is not None]
