import os
import time

from selenium.webdriver.common.by import By

from functions_dir.base import Base


class CompetitionsAndResults(Base):
    def competitions_open_accordion_sports(self):
        """Open the accordion with sports."""

        accordion_element = self.find_element(By.CLASS_NAME, "foldable.foldable--organizations")
        accordion_btn = accordion_element.find_element(By.CSS_SELECTOR, "button.foldable-top__toggle")
        self.execute_script("arguments[0].click();", accordion_btn)

    def is_competitions_accordion_sports_opened(self):
        """Check if the accordion with sports opened."""

        try:
            self.find_element(By.CLASS_NAME, "foldable.foldable--opened.foldable--organizations")
            return True
        except:
            return False

    def check_sports_titles(self):
        """Check if the title of the sports changes after clicking on a sport."""

        accordion_element = self.find_element(By.CLASS_NAME, "foldable.foldable--organizations")
        sports_btns = accordion_element.find_elements(By.CLASS_NAME, "organization-filter-bottom-item__toggle")
        sports_btns = sports_btns[:-1]  # the last button is "show all".

        for sport_btn in sports_btns:
            title_before = accordion_element.find_element(By.CLASS_NAME, "foldable-top__title")
            title_before_text = title_before.get_attribute("innerHTML")

            self.execute_script("arguments[0].click();", sport_btn)

            title_after = accordion_element.find_element(By.CLASS_NAME, "foldable-top__title")
            title_after_text = title_after.get_attribute("innerHTML")

            self.execute_script("arguments[0].click();", sport_btn)

            if title_before_text == title_after_text:
                return False

        return True

    def competitions_open_accordion_years(self):
        """Open the accordion with years."""

        accordion_element = self.find_element(By.CLASS_NAME, "foldable.foldable--years")
        accordion_btn = accordion_element.find_element(By.CSS_SELECTOR, "button.foldable-top__toggle")
        self.execute_script("arguments[0].click();", accordion_btn)

    def is_competitions_accordion_years_opened(self):
        """Check if the accordion with years opened"""

        try:
            self.find_element(By.CLASS_NAME, "foldable.foldable--opened.foldable--years")
            return True
        except:
            return False

    def check_years_titles(self):
        """Check each year is it changes after clicking."""

        self.competitions_open_accordion_years()
        years_block = self.find_element(By.CLASS_NAME, "years-wrapper")
        all_years = years_block.find_elements(By.CLASS_NAME, "years-item__btn")
        year_title = self.find_element(By.CLASS_NAME, "years-label__label")
        self.competitions_open_accordion_years()

        for year_item in range(len(all_years)):
            self.competitions_open_accordion_years()
            years_block = self.find_element(By.CLASS_NAME, "years-wrapper")
            years_elements = years_block.find_elements(By.CLASS_NAME, "years-item__btn")
            year_element_text = years_elements[year_item].text.strip()

            self.execute_script("arguments[0].click();", years_elements[year_item])

            year_title_text = year_title.text.strip()

            if year_title_text != year_element_text:
                return False

        return True

    def check_each_competition(self, file_name, sport_btn_text, year_btn_text):
        """In particular sport category, in particular year, in each month, and in each row this function checks:
        1. Existence of data.
        2. If the medal exists, then should be at least one person."""

        time.sleep(4)  # wait for loading data
        flag_local = True

        try:
            self.implicitly_wait(0)
            accordion_elements = self.find_elements(By.CSS_SELECTOR, "button.month__toggle")
            self.implicitly_wait(15)

            if len(accordion_elements) >= 1:
                for accordion_element in accordion_elements:
                    self.execute_script("arguments[0].click();", accordion_element)
                    month_element = self.find_element(By.CLASS_NAME, "month--open")

                    competitions_list = month_element.find_elements(
                        By.CLASS_NAME, "info__row.row.no-gutters.event-item"
                    )

                    for competition_row in competitions_list:
                        month_name = month_element.find_element(By.CLASS_NAME, "month__name")
                        month_name_text = month_name.text

                        competition_dates = competition_row.find_element(By.CLASS_NAME, "col.event-item__date")
                        competition_dates_text = competition_dates.text

                        competition_medal = competition_row.find_element(By.CLASS_NAME, "col.event-item__medal")
                        competition_medal_text = competition_medal.text

                        competition_type = competition_row.find_element(By.CLASS_NAME, "col.event-item__type")
                        competition_type_text = competition_type.text

                        competition_type_red = competition_type.find_element(By.CLASS_NAME, "red")
                        competition_type_red_text = competition_type_red.text

                        competition_athletes = competition_row.find_element(By.CLASS_NAME, "col.event-item__athletes")
                        competition_athletes_text = competition_athletes.text

                        competition_row_text = (
                            f'"{sport_btn_text}",'
                            f'"{year_btn_text}",'
                            f'"{month_name_text}",'
                            f'"{competition_dates_text}",'
                            f'"{competition_medal_text}",'
                            f'"{competition_type_red_text}",'
                            f'"{competition_type_text}",'
                            f'"{competition_athletes_text}"\n'
                        )

                        if (
                            (month_name_text == "")
                            or (competition_dates_text == "")
                            or (competition_type_text == "")
                            or (competition_type_red_text == "")
                        ):
                            self.competitions_add_to_report(
                                file_name=file_name,
                                competition_row_text=competition_row_text,
                            )
                            flag_local = False

                        if ((competition_medal_text != "") and (competition_athletes_text == "")) or (
                            (competition_medal_text == "") and (competition_athletes_text != "")
                        ):
                            self.competitions_add_to_report(
                                file_name=file_name,
                                competition_row_text=competition_row_text,
                            )
                            flag_local = False

                    self.execute_script("arguments[0].click();", accordion_element)
                    return flag_local

            else:
                return

        except:
            competition_row_text = (
                f'"{sport_btn_text}",'
                f'"{year_btn_text}",,,,,,'
                f'"Ошибка Python в выполнении программы. '
                f'Возможно, этот элемент на сайте работает корректно."\n'
            )
            self.competitions_add_to_report(file_name=file_name, competition_row_text=competition_row_text)
            flag_local = False
            return flag_local

    def competitions_add_to_report(self, file_name, competition_row_text):
        """Write the row with the error in the report file."""

        with open(os.path.dirname(__file__) + f"/../reports/{file_name}", "a") as file:
            file.write(competition_row_text)

    def amount_of_sports_titles(self):
        self.competitions_open_accordion_sports()
        sports_btns = self.find_elements(By.CLASS_NAME, "organization-filter-bottom-item__toggle")
        len_sports = len(sports_btns) - 1

        return len_sports

    def amount_of_years_titles(self):
        self.competitions_open_accordion_years()
        years_btns = self.find_elements(By.CLASS_NAME, "years-item__btn")
        len_years = len(years_btns)
        self.competitions_open_accordion_years()

        return len_years

    def choose_sport(self, sport_number):
        """Click on a sport name."""

        sports_btns = self.find_elements(By.CLASS_NAME, "organization-filter-bottom-item__toggle")
        sport_btn_text = sports_btns[sport_number].text
        self.execute_script("arguments[0].click();", sports_btns[sport_number])

        if sport_number >= 1:
            self.execute_script("arguments[0].click();", sports_btns[sport_number - 1])

        return sport_btn_text

    def choose_year(self, year_number):
        """Click on a year name."""

        years_block = self.find_element(By.CLASS_NAME, "foldable.foldable--years")
        accordion_btn = years_block.find_element(By.CSS_SELECTOR, "button.foldable-top__toggle")
        self.execute_script("arguments[0].click();", accordion_btn)

        years_btns = self.find_elements(By.CLASS_NAME, "years-item__btn")
        year_btn_text = years_btns[year_number].text
        self.execute_script("arguments[0].click();", years_btns[year_number])

        return year_btn_text
