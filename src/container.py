from typing import Dict, List
from web_crawler import WebCrawler
from web_scraper import WebScraper
from data_wrangler import DataWrangler
from calendar_creator import CalendarCreator
from os import environ

HOUSE_NUMBER = environ.get('HOUSE_NUMBER', '')
STREET_NAME = environ.get('STREET_NAME', '')
CITY = environ.get('CITY', 'Test City')
POSTCODE = environ.get('POSTCODE', '')
WEBSITE_URL = environ.get('WEBSITE_URL', '')


def address_str_generator(house_number: str, street_name: str, city: str, postcode: str) -> str:
    return f"{house_number} {street_name}, {city}, {postcode}"


def get_address_str() -> str:
    return address_str_generator(
        house_number=HOUSE_NUMBER,
        street_name=STREET_NAME,
        city=CITY,
        postcode=POSTCODE
    )


def get_webcrawler() -> WebCrawler:
    return WebCrawler(
        website_url=WEBSITE_URL,
        postcode=POSTCODE,
        address_str=get_address_str()
    )


def get_webscraper() -> WebScraper:
    return WebScraper(html_file="data/page_source.html")


def get_data_wrangler(calendar_data: List[str]) -> DataWrangler:
    return DataWrangler(calendar_data=calendar_data)


def get_calendar_creator(data_dict: List[Dict]) -> CalendarCreator:
    return CalendarCreator(data_dict=data_dict)
