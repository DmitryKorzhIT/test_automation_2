import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from . import constant as const

DRIVER_PATH = const.DRIVER_PATH
BASE_URL = const.BASE_URL


class Base(webdriver.Chrome):
    def __init__(self, teardown=False):  # the teardown is a condition for the __exit__ method
        self.driver_path = DRIVER_PATH
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_argument("headless")  # run code without opening a browser
        super(Base, self).__init__()  # __init__(options=options) - for running without opening a browser
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_specific_page(self, url=BASE_URL):
        self.get(url)

    def accept_cookies(self):
        try:
            cookies_btns = self.find_element(By.CLASS_NAME, "coi-button-group")
            accept_cookies_btn = cookies_btns.find_element(
                By.CSS_SELECTOR,
                'button[onclick="CookieInformation.submitAllCategories()"]',
            )
            accept_cookies_btn.click()
        except:
            pass

    def is_404_error(self):
        try:
            self.implicitly_wait(0)
            error_element = self.find_element(By.CLASS_NAME, "page-not-found__title._show-tablet")
            error_element = error_element.find_element(By.CLASS_NAME, "page-not-found__title-text")
            error_text = error_element.get_attribute("innerHTML").strip()
            if str(error_text) == "404":
                return True

        except:
            return False

        finally:
            self.implicitly_wait(15)

    def create_report_file(self, test_name: str, header: str):
        current_date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{test_name}_{current_date_time}.csv"
        file = open(os.path.dirname(__file__) + f"/../reports/{file_name}", "w")
        file.write(header)
        file.close()
        return file_name
