import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)


from functions_dir.constant import BASE_URL
from functions_dir.news_news_url import NewsNewsUrl


def test_1():
    news_news_url = NewsNewsUrl()

    news_news_url.load_specific_page(BASE_URL)
    news_news_url.accept_cookies()
    news_news_url.all_news_btn()
    flag = news_news_url.check_main_news()

    assert flag


def test_2():
    news_news_url = NewsNewsUrl()

    news_news_url.load_specific_page(BASE_URL)
    news_news_url.accept_cookies()
    news_news_url.all_news_btn()
    flag = news_news_url.check_main_news_data()

    assert flag


def test_3():
    news_news_url = NewsNewsUrl()

    # Create a report file.
    header = "News number,News date,News title,News link\n"
    file_name = news_news_url.create_report_file(test_name="news_news_url_check_all_news", header=header)

    news_news_url.load_specific_page(BASE_URL)
    news_news_url.accept_cookies()
    news_news_url.all_news_btn()
    news_news_url.show_all_news()
    flag = news_news_url.check_all_news(file_name)

    assert flag


def test_4():
    news_news_url = NewsNewsUrl()

    # Create a report file.
    header = "News date,News title,News image\n"
    file_name = news_news_url.create_report_file(test_name="news_news_url_check_all_news_data", header=header)

    news_news_url.load_specific_page(BASE_URL)
    news_news_url.accept_cookies()
    news_news_url.all_news_btn()
    news_news_url.show_all_news()
    flag = news_news_url.check_all_news_data(file_name)

    assert flag
