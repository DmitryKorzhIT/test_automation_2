from . import constant as const
from functions_dir.elasticsearch import Elasticsearch
from selenium.webdriver.common.by import By


BASE_URL = const.BASE_URL

class Search(Elasticsearch):
    def press_search_btn_2(self):
        ''' Press the search button in the header after enter a search request. '''

        header_element = self.find_element(By.CLASS_NAME, 'header__inner')
        search_btn = header_element.find_element(By.CLASS_NAME,
            'autosuggestion__entry-btn.js-autosuggestion__entry-btn')

        search_btn.click()


    def check_pages_search(self):
        ''' Check each page in a search results on 404 error. '''

        pages_links_list = []
        search_result = self.find_element(By.CLASS_NAME, 'content.search-result')
        search_pages = search_result.find_elements(By.CSS_SELECTOR, 'a.search-result__list-link')

        for page in search_pages:
            pages_links_list.append(page.get_attribute('href'))

        return pages_links_list

