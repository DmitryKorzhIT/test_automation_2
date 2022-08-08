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


    def search_field(self, search_request: str = 'Denmark'):
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
            # Make 404 error.
            print('item:', item)

            # Get the name of the page.
            item_title = item.find_element(By.CLASS_NAME, 'autosuggestion__list-title').text
            item_title = item_title.split('\n')[1]

            # Get the URL of the page.
            item_url = item.get_attribute('href')

            # Check the page on the 404 error.
            item.click()
            time.sleep(5)
            if Base.is_404_error(self) == True:
                return {'no_error':False,
                        'item_title':item_title,
                        'item_url':item_url}

        return {'no_error':True,
                'item_title':'no title',
                'item_url':'no url'}

