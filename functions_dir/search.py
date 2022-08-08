from . import constant as const
from .base import Base
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


BASE_URL = const.BASE_URL


class Search(Base):
    def press_search_btn(self):
        header = self.find_element(By.CLASS_NAME, 'header__wrap')
        search_btn = header.find_element(By.CLASS_NAME, 'search__btn')
        search_btn.click()


    def search_field(self, search_request: str = 'Jungleuusddz'):
        header = self.find_element(By.CLASS_NAME, 'header__wrap')
        search_field = header.find_element(By.CSS_SELECTOR, 'input[title="search"]')
        search_field.clear()
        search_field.send_keys(search_request)


    def click_on_autosuggestion_element(self):
        autosuggestion__list = self.find_element()


    def check_pages_elastic_search(self):
        ''' Check all the pages in the results of the elastic search on the 404 error. '''

        autosuggestion_list = self.find_element(By.CSS_SELECTOR, 'ul.autosuggestion__list')
        autosuggestion_list_results = autosuggestion_list.find_elements(By.CSS_SELECTOR, 'a.autosuggestion__list-link')
        autosuggestion_list_results = autosuggestion_list_results[:-1]  # The last element was the search button.

        for item in autosuggestion_list_results:
            item.click()
            time.sleep(5)
            if Base.is_404_error(self) == True:
                return False

        return True

