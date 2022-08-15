from functions_dir.competitions_and_results import CompetitionsAndResults
from functions_dir.constant import COMPETITIONS_AND_RESULTS_URL
import time


COMPETITIONS_AND_RESULTS_URL = COMPETITIONS_AND_RESULTS_URL

''' In each sport category in each year in each month in each row this function checks:
1. Existence of data.
2. If the medal exists, then should be at least one person. '''

# Create a report file.
competitions_and_results = CompetitionsAndResults()
file_name = competitions_and_results.create_report_file(test_name='competitions_and_results')

competitions_and_results.load_specific_page(COMPETITIONS_AND_RESULTS_URL)
competitions_and_results.accept_cookies()

# Figure out how many sports and years categories
len_sports = competitions_and_results.amount_of_sports_titles()
len_years = competitions_and_results.amount_of_years_titles()

# Go through all sports, through all years, through all competitions
for sport in range(len_sports):
    competitions_and_results.choose_sport(sport_number=sport)
    time.sleep(0.5)
    for year in range(len_years):
        competitions_and_results.choose_year(year_number=year)
        time.sleep(0.3)
        print('000.')
        competitions_and_results.check_each_competition(file_name)
        print('004.')