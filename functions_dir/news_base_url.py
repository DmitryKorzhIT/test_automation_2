from selenium.webdriver.common.by import By

from functions_dir.base import Base

from . import constant as const

BASE_URL = const.BASE_URL


class NewsBaseUrl(Base):
    def click_each_news(self):
        """Check each news from the base page on 404 error, when opening it."""

        news_links_list = []
        news_panel = self.find_element(By.CLASS_NAME, "news-panel")
        news_items = news_panel.find_elements(By.CSS_SELECTOR, "a.list__link")

        for news_item in news_items:
            news_links_list.append(news_item.get_attribute("href"))

        for news_link in news_links_list:
            self.get(news_link)
            local_flag = self.is_404_error()

            if local_flag is True:
                return False

        return True

    def check_each_news_data(self):
        """Check the image, date, and title in each news."""

        news_panel = self.find_element(By.CLASS_NAME, "news-panel")
        news_items = news_panel.find_elements(By.CLASS_NAME, "list__item")

        for news_item in news_items:

            news_image = news_item.find_element(By.CSS_SELECTOR, "img.js-news-img")
            news_image = news_image.get_attribute("src")

            news_date = news_item.find_element(By.CLASS_NAME, "list__publish").text

            news_title = news_item.find_element(By.CLASS_NAME, "list__title").text

            if (news_image == "") or (news_date == "") or (news_title == ""):
                return False

        return True
