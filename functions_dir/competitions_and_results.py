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


