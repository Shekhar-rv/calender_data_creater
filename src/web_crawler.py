from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class WebCrawler:
    def __init__(self, website_url: str, postcode: str, address_str: str, teardown: bool = True):
        self.website_url = website_url
        self.postcode = postcode
        self.address_str = address_str
        self.teardown = teardown
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)  # Or you can use Chrome(), Safari(), etc.
        self.driver.get(website_url)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()

    def find_elements(self, element_type: str, element_name: str):
        return self.driver.find_element(element_type, element_name)  # type: ignore
    
    def run(self):
        search_property = self.find_elements("name", "search_property")  # type: ignore
        print(f"Is your postcode: {self.postcode} {type(self.postcode)}?")
        search_property.clear()
        search_property.send_keys(self.postcode)  # type: ignore
        search_property.submit()  # type: ignore
        assert "No results found." not in self.driver.page_source
        self.driver.close()
