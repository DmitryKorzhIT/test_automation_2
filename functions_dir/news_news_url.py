import os
import time

from selenium.webdriver.common.by import By

from functions_dir.base import Base

from . import constant as const

BASE_URL = const.BASE_URL


class NewsNewsUrl(Base):
    def all_news_btn(self):
        all_news_btn = self.find_element(By.CLASS_NAME, "news-panel__link")
        self.execute_script("arguments[0].click();", all_news_btn)

    def check_main_news(self):
        """Check the main news page on the 404 error."""

        news_title = self.find_element(By.CLASS_NAME, "top-news__title")
        self.execute_script("arguments[0].click();", news_title)

        if self.is_404_error() is True:
            return False

        return True

    def check_main_news_data(self):
        """Check the main data of the main news."""

        news_image = self.find_element(By.CSS_SELECTOR, "img.top-news__img")
        news_image = news_image.get_attribute("src")

        news_date = self.find_element(By.CLASS_NAME, "top-news__publish-date").text

        news_title = self.find_element(By.CLASS_NAME, "top-news__title").text

        news_description = self.find_element(By.CLASS_NAME, "top-news")
        news_description = news_description.find_element(By.CLASS_NAME, "rte").text

        news_btn = self.find_element(By.CLASS_NAME, "top-news__btn").text

        if (
            (news_image == "")
            or (news_date == "")
            or (news_title == "")
            or (news_description == "")
            or (news_btn == "")
        ):
            return False

        return True

    def show_all_news(self):
        """Open all news on the news page."""

        news_block = self.find_element(By.CLASS_NAME, "news-overview-page__content")
        show_more_news_btn = self.find_element(By.CLASS_NAME, "btn.filter__btn.js-news-overview-page__show-more")
        news_shown = news_block.find_element(By.CLASS_NAME, "js-news-skip").get_attribute("value")
        news_total = news_block.find_element(By.CLASS_NAME, "js-news-total-count").get_attribute("value")

        while int(news_shown) < int(news_total):
            news_shown = news_block.find_element(By.CLASS_NAME, "js-news-skip").get_attribute("value")
            news_total = news_block.find_element(By.CLASS_NAME, "js-news-total-count").get_attribute("value")

            self.execute_script("arguments[0].click();", show_more_news_btn)
            time.sleep(2)

    def check_all_news(self, file_name):
        """Check each page in news on the 404 error."""

        all_news_info = []
        local_flag = True

        news_block = self.find_element(By.CLASS_NAME, "news-overview-page__content")
        news_items = news_block.find_elements(By.CLASS_NAME, "list__link")

        for item in news_items:
            news_link = item.get_attribute("href")
            news_date = item.find_element(By.CLASS_NAME, "list__publish-date").text
            news_title = item.find_element(By.CLASS_NAME, "list__title").text
            all_news_info.append([news_link, news_date, news_title])

        for item_info in range(len(all_news_info)):
            self.get(all_news_info[item_info][0])

            if self.is_404_error() is True:
                local_flag = False

                news_date = all_news_info[item_info][1]
                news_title = all_news_info[item_info][2]
                news_link = all_news_info[item_info][0]
                news_info_row = f'"{item_info}","{news_date}","{news_title}","{news_link}"\n'

                self.news_add_to_report(file_name, news_info_row)

        return local_flag

    def news_add_to_report(self, file_name, news_info_row):
        """Write the row with the error in the report file."""

        with open(os.path.dirname(__file__) + f"/../reports/{file_name}", "a") as file:
            file.write(news_info_row)

    def check_all_news_data(self, file_name):
        """Check the main data of all news."""

        self.implicitly_wait(1)
        local_flag = True

        news_block = self.find_element(By.CLASS_NAME, "news-overview-page__content")
        news_items = news_block.find_elements(By.CLASS_NAME, "list__link")

        for item in news_items:
            news_image = ""

            try:
                news_image = item.find_element(By.CSS_SELECTOR, "img.list__img")
                news_image = news_image.get_attribute("src")
            except:
                pass

            news_date = item.find_element(By.CLASS_NAME, "list__publish-date").text
            news_title = item.find_element(By.CLASS_NAME, "list__title").text

            if (news_image == "") or (news_date == "") or (news_title == ""):
                local_flag = False

                news_info_row = f'"{news_date}","{news_title}","{news_image}"\n'
                self.news_add_to_report(file_name, news_info_row)

        self.implicitly_wait(15)
        return local_flag
