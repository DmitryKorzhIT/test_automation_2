import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)


from functions_dir.competitions_and_results import CompetitionsAndResults
from functions_dir.constant import COMPETITIONS_AND_RESULTS_URL

COMPETITIONS_AND_RESULTS_URL = COMPETITIONS_AND_RESULTS_URL


def test_1():
    """Check is accordion with sports opens."""

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_sports()
    flag = competitions_and_results.is_competitions_accordion_sports_opened()

    assert flag


def test_2():
    """Check if the titles of the sport change after clicking on a sport."""

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_sports()
    flag = competitions_and_results.check_sports_titles()

    assert flag


def test_3():
    """Check is accordion with years opens."""

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    competitions_and_results.competitions_open_accordion_years()
    flag = competitions_and_results.is_competitions_accordion_years_opened()

    assert flag


def test_4():
    """Check each year is it changes after clicking."""

    competitions_and_results = CompetitionsAndResults()

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()
    flag = competitions_and_results.check_years_titles()

    assert flag


def test_5():
    """In each sport category, in each year, in each month, and in each row this function checks:
    1. Existence of data.
    2. If the medal exists, then should be at least one person."""

    flag = True

    # Create a report file.
    competitions_and_results = CompetitionsAndResults()
    header = "Sport category,Year,Month,Competition dates,Medal,Type red,Type,Athletes,Error type\n"

    file_name = competitions_and_results.create_report_file(test_name="competitions_and_results", header=header)

    competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
    competitions_and_results.accept_cookies()

    # Figure out how many sports and years categories.
    len_sports = competitions_and_results.amount_of_sports_titles()
    len_years = competitions_and_results.amount_of_years_titles()

    # Go through all sports.
    for sport in range(len_sports):
        sport_btn_text = competitions_and_results.choose_sport(sport_number=sport)

        # Go through all years.
        for year in range(len_years):
            year_btn_text = competitions_and_results.choose_year(year_number=year)

            # Go through all competitions.
            flag_local = competitions_and_results.check_each_competition(file_name, sport_btn_text, year_btn_text)

            if flag_local is False:
                flag = False

    assert flag
