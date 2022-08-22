import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)


from functions_dir.constant import BASE_URL
from functions_dir.news_base_url import NewsBaseUrl

BASE_URL = BASE_URL


def test_1():
    """Check each news from the base page on 404 error, when opening it."""

    news_base_url = NewsBaseUrl()

    news_base_url.load_specific_page(BASE_URL)
    news_base_url.accept_cookies()
    flag = news_base_url.click_each_news()

    assert flag


def test_2():
    """Check the image, date, and title in each news."""

    news_base_url = NewsBaseUrl()

    news_base_url.load_specific_page(BASE_URL)
    news_base_url.accept_cookies()
    flag = news_base_url.check_each_news_data()

    assert flag
