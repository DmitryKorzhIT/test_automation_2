from functions_dir.competitions_and_results import CompetitionsAndResults
from functions_dir.constant import COMPETITIONS_AND_RESULTS_URL
import time


COMPETITIONS_AND_RESULTS_URL = COMPETITIONS_AND_RESULTS_URL

def test_1():
    ''' Check is accordion opens. '''

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