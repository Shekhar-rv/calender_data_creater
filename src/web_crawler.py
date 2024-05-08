from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        self.driver.delete_all_cookies()  # Clear cache
        self.driver.get(website_url)
        # Get the html page source of the current page
        
    def save_html(self):
        page_source = self.driver.page_source
        fileToWrite = open("data/page_source2.html", "w")
        fileToWrite.write(page_source)
        print("Saved the page source")
        fileToWrite.close()
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.driver.close()
    
    def run(self):
        try:
            search_property = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_property"]')))
            print("Found the search property")
        except Exception as e:
            print(e)
        else:
            search_property.click()
            print("Clicked the search property")
            print(f"Is your postcode: {self.postcode}")
            search_property.send_keys(self.postcode)
            search_property.send_keys(Keys.RETURN)

        self.save_html()
        self.driver.close()
