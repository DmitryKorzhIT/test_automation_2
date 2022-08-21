from selenium.webdriver.common.by import By

from functions_dir.base import Base

from . import constant as const

EMPLOYEES_URL = const.EMPLOYEES_URL


class Employees(Base):
    def open_accordion(self):
        accordion_btn = self.find_element(By.CSS_SELECTOR, "button.employees-filter-top__toggle")
        accordion_btn.click()

    def is_accordion_opened(self):
        try:
            employees_filter = self.find_element(By.CLASS_NAME, "employees-filter.employees-filter--opened")
            employees_filter.find_element(By.CSS_SELECTOR, "ul.employees-filter-bottom")
            return True
        except:
            return False

    def check_professions_titles(self):
        """Checking title after clicking on each profession."""

        employees_filter_items = self.find_elements(By.CSS_SELECTOR, "button.employees-filter-bottom-item__toggle")
        employees_filter_items = employees_filter_items[:-1]  # the last element was "show all"

        for profession in employees_filter_items:
            title_before = self.find_element(By.CLASS_NAME, "employees-filter-top__title")
            title_before_text = title_before.get_attribute("innerHTML")

            profession.click()

            title_after = self.find_element(By.CLASS_NAME, "employees-filter-top__title")
            title_after_text = title_after.get_attribute("innerHTML")

            profession.click()

            if title_before_text == title_after_text:
                return False

        return True

    def check_existence_of_employees(self):
        """Checking the existence of at least one employee in each profession.
        It returns True if in each profession at least one employee.
        It returns False if in at least one profession zero employees."""

        employees_list_panel = self.find_element(By.CLASS_NAME, "employees-list-panel-wrapper")
        employees_list_panel = employees_list_panel.find_element(By.CLASS_NAME, "employees-list-panel.js-tracking-area")
        employees_filter_items = self.find_elements(By.CSS_SELECTOR, "button.employees-filter-bottom-item__toggle")
        employees_filter_items = employees_filter_items[:-1]  # the last element was "show all"

        for profession in employees_filter_items:
            profession.click()
            flag = employees_list_panel.find_elements(By.CLASS_NAME, "list__item")

            profession.click()
            if flag == []:
                return False

        return True
