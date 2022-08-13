from functions_dir.competitions_and_results import CompetitionsAndResults
from functions_dir.constant import COMPETITIONS_AND_RESULTS_URL
import time


COMPETITIONS_AND_RESULTS_URL = COMPETITIONS_AND_RESULTS_URL

def test_1():
    ''' Check is accordion with sports opens. '''

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_sports()
    flag = competitions_and_results.is_competitions_accordion_sports_opened()
    assert flag


def test_2():
    ''' Check if the title of the sports changes after clicking on a sport. '''

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_sports()
    flag = competitions_and_results.check_sports_titles()

    assert flag


def test_3():
    ''' Check is accordion with years opens. '''

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_years()
    flag = competitions_and_results.is_competitions_accordion_years_opened()
    time.sleep(20)

    assert flag


def test_4():
    ''' Check each year is it changes after clicking. '''

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    flag = competitions_and_results.check_years_titles()

    assert flag


def test_5():
    ''' In each sport category in each year in each month in each row this function checks:
    1. Existence of data.
    2. If the medal exists, then should be at least one person. '''

    # Create a report file.
    competitions_and_results = CompetitionsAndResults()
    file_name = competitions_and_results.create_report_file(test_name='competitions_and_results')

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.check_each_competition(file_name)














