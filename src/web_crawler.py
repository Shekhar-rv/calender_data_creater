from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class WebCrawler:
    def __init__(self, website_url: str, postcode: str, address_str: str, browser_path: str, driver_path: str, teardown: bool = True):
        self.website_url = website_url
        self.postcode = postcode
        self.address_str = address_str
        self.browser_path = browser_path
        self.driver_path = driver_path
        self.teardown = teardown
        print(f"browser_path: {self.browser_path} driver_path: {self.driver_path}")
        options = Options()
        options.binary_location = self.browser_path
        # options.add_argument('--headless')  # type: ignore
        # options.add_argument('--no-sandbox')  # type: ignore
        # options.add_argument('--disable-dev-shm-usage')  # type: ignore
        # Path to chromedriver driver on your system
        chrome_driver_binary = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=chrome_driver_binary, options=options)  # Or you can use Chrome(), Safari(), etc.
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # self.driver = webdriver.Chrome(options=options)  # Or you can use Chrome(), Safari(), etc.
        self.driver.get(website_url)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()

    def find_elements(self, element_name: str):
        return self.driver.find_element_by_name(element_name)  # type: ignore
    
    def run(self):
        search_property = self.find_elements("search_property")  # type: ignore
        print("search_property: ", search_property)
        search_property.send_keys(self.postcode)  # type: ignore
        search_property.send_keys(Keys.RETURN)  # type: ignore
        assert "No results found." not in self.driver.page_source
        self.driver.close()
