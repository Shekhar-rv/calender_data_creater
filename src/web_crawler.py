from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class WebCrawler:
    def __init__(self, website_url: str, postcode: str, address_str: str):
        self.website_url = website_url
        self.postcode = postcode
        self.address_str = address_str
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/brave-browser"
        # Path to chromedriver driver on your system
        chrome_driver_binary = Service("./selenium_driver/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_binary, options=options)  # Or you can use Chrome(), Safari(), etc.
        self.driver.get(website_url)
    
    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     if self.teardown:
    #         self.driver.close()

    def find_elements(self, element_name: str):
        return self.driver.find_element_by_name(element_name)  # type: ignore
    
    def run(self):
        search_property = self.find_elements("search_property")  # type: ignore
        print("search_property: ", search_property)
        search_property.send_keys(self.postcode)  # type: ignore
        search_property.send_keys(Keys.RETURN)  # type: ignore
        assert "No results found." not in self.driver.page_source
        self.driver.close()
