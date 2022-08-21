import os.path
import time

from selenium.webdriver.common.by import By

from . import constant as const
from .base import Base

BASE_URL = const.BASE_URL


class ElasticsearchShortResult(Base):
    def press_search_btn(self):
        header = self.find_element(By.CLASS_NAME, "header__wrap")
        search_btn = header.find_element(By.CLASS_NAME, "search__btn")
        search_btn.click()

    def search_field(self, search_request: str = "Denmark"):
        """Enter the search request into the search field."""

        header = self.find_element(By.CLASS_NAME, "header__wrap")
        search_field = header.find_element(By.CSS_SELECTOR, 'input[title="search"]')
        search_field.clear()
        search_field.send_keys(search_request)

    def check_pages_elasticsearch(self, file_name: str, search_query: str):
        """Check all the pages in the results of the short elasticsearch on the 404 error."""

        flag = True

        autosuggestion_list = self.find_element(By.CSS_SELECTOR, "ul.autosuggestion__list")
        autosuggestion_list_results = autosuggestion_list.find_elements(By.CSS_SELECTOR, "a.autosuggestion__list-link")
        autosuggestion_list_results = autosuggestion_list_results[:-1]  # The last element was the search button.

        for page in autosuggestion_list_results:

            # Get the name of the page.
            page_title = page.find_element(By.CLASS_NAME, "autosuggestion__list-title").text
            page_title = page_title.split("\n")[1]

            # Get the URL of the page.
            page_url = page.get_attribute("href")

            # Check the page on the 404 error.
            page.click()
            time.sleep(5)
            # self.get(page_url)
            if Base.is_404_error(self) is True:
                flag = False
                self.check_pages_elasticsearch_report(file_name, search_query, page_title, page_url)

        return flag

    def check_pages_elasticsearch_report(self, file_name, search_query, page_title, page_url):
        """Write the data about the error page in the report file."""

        with open(os.path.dirname(__file__) + f"/../reports/{file_name}", "a") as file:
            file.write(f'"{search_query}","{page_title}","{page_url}"\n')
