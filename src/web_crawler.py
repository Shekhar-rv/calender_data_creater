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
        # Get the html page source of the current page
        
    def save_html(self):
        page_source = self.driver.page_source
        fileToWrite = open("page_source.html", "w")
        fileToWrite.write(page_source)
        print("Saved the page source")
        fileToWrite.close()
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()

    def find_elements(self, element_type: str, element_name: str):
        return self.driver.find_element(element_type, element_name)  # type: ignore
    
    def run(self):
        # search_property = self.find_elements("name", "search_property")  # type: ignore
        wait = WebDriverWait(self.driver, 10)
        search_property = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_property.search-text.form-control")))
        # search_property = wait.until(EC.presence_of_element_located((By.NAME, "search_property")))
        # search_property.click()
        print(f"Is your postcode: {self.postcode}")
        search_property.send_keys(self.postcode)  # type: ignore
        print("Sent the postcode")
        find_address = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-element-10.btn.btn-primary")))
        find_address.click()  # type: ignore
        self.save_html()
        assert "No results found." not in self.driver.page_source
        self.driver.close()
