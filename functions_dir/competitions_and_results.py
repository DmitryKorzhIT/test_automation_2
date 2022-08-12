from functions_dir.base import Base
from selenium.webdriver.common.by import By
import time


class CompetitionsAndResults(Base):
    def competitions_open_accordion_sports(self):
        accordion_element = self.find_element(By.CLASS_NAME, 'foldable.foldable--organizations')
        accordion_btn = accordion_element.find_element(By.CSS_SELECTOR, 'button.foldable-top__toggle')
        self.execute_script("arguments[0].click();", accordion_btn)  # instead of ".click()" method.


    def is_competitions_accordion_sports_opened(self):
        try:
            self.find_element(By.CLASS_NAME, 'foldable.foldable--opened.foldable--organizations')
            return True
        except:
            return False


    def check_sports_titles(self):
        ''' Check if the title of the sports changes after clicking on a sport. '''

        accordion_element = self.find_element(By.CLASS_NAME, 'foldable.foldable--organizations')
        sports_btns = accordion_element.find_elements(By.CLASS_NAME, 'organization-filter-bottom-item__toggle')
        sports_btns = sports_btns[:-1]  # the last button is "show all".

        for sport_btn in sports_btns:
            title_before = accordion_element.find_element(By.CLASS_NAME, 'foldable-top__title')
            title_before_text = title_before.get_attribute('innerHTML')

            self.execute_script("arguments[0].click();", sport_btn)  # instead of ".click()" method.

            title_after = accordion_element.find_element(By.CLASS_NAME, 'foldable-top__title')
            title_after_text = title_after.get_attribute('innerHTML')

            self.execute_script("arguments[0].click();", sport_btn)  # instead of ".click()" method.

            if title_before_text == title_after_text:
                return False

        return True


    def competitions_open_accordion_years(self):
        accordion_element = self.find_element(By.CLASS_NAME, 'foldable.foldable--years')
        accordion_btn = accordion_element.find_element(By.CSS_SELECTOR, 'button.foldable-top__toggle')
        self.execute_script("arguments[0].click();", accordion_btn)  # instead of ".click()" method.


    def is_competitions_accordion_years_opened(self):
        try:
            self.find_element(By.CLASS_NAME, 'foldable.foldable--opened.foldable--years')
            return True
        except:
            return False


    def check_years_titles(self):
        ''' Check if the year changes after clicking on a year. '''

        self.competitions_open_accordion_years()
        all_years = self.find_elements(By.CLASS_NAME, 'years-item__btn')
        self.competitions_open_accordion_years()
        print('All years len:', len(all_years))

        for year in range(len(all_years)):
            pass


    def check_competitions_existence(self):
        '''  '''

        accordion_elements = self.find_elements(By.CSS_SELECTOR, 'button.month__toggle')

        for accordion_element in accordion_elements:
            accordion_element.click()
            month_element = self.find_element(By.CLASS_NAME, 'month--open')

            competitions_list = month_element.find_elements(By.CLASS_NAME, 'info__row.row.no-gutters.event-item')

            for competition_row in competitions_list:
                month_name = month_element.find_element(By.CLASS_NAME, 'month__name')
                month_name_text = month_name.text

                competition_dates = competition_row.find_element(By.CLASS_NAME, 'col.event-item__date')
                competition_dates_text = competition_dates.text

                competition_medal = competition_row.find_element(By.CLASS_NAME, 'col.event-item__medal')
                competition_medal_text = competition_medal.text

                competition_type = competition_row.find_element(By.CLASS_NAME, 'col.event-item__type')
                competition_type_text = competition_type.text

                competition_type_red = competition_type.find_element(By.CLASS_NAME, 'red')
                competition_type_red_text = competition_type_red.text

                competition_athletes = competition_row.find_element(By.CLASS_NAME, 'col.event-item__athletes')
                competition_athletes_text = competition_athletes.text

                print(f'Month_name: {month_name_text}; '
                      f'Dates: {competition_dates_text}; '
                      f'Medal: {competition_medal_text}; '
                      f'Type_red: {competition_type_red_text}; '
                      f'Type: {competition_type_text}; '
                      f'Athletes: {competition_athletes_text}.')

            accordion_element.click()


