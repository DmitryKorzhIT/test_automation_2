import time

from selenium.webdriver.common.by import By

from functions_dir.base import Base

from . import constant as const

CALCULATE_ENERGY_REQUIREMENTS = const.CALCULATE_ENERGY_REQUIREMENTS_URL


class CalculateEnergyRequirements(Base):
    def fill_base_metabolism(self):
        self.implicitly_wait(2)

        base_metabolism_fields = self.find_element(By.CLASS_NAME, "main")
        base_metabolism_fields = base_metabolism_fields.find_element(By.CLASS_NAME, "article-page")
        base_metabolism_fields = base_metabolism_fields.find_element(By.CLASS_NAME, "umb-grid")
        base_metabolism_fields = base_metabolism_fields.find_element(By.CLASS_NAME, "grid-section")
        base_metabolism_fields = base_metabolism_fields.find_element(By.CLASS_NAME, "row.clearfix")

        time.sleep(5)
        element = self.execute_script(
            """return document.querySelector("td-calculator").shadowRoot.querySelector(".section.section--bmr")"""
        )
        print(element)

        # self.get("https://www.immowelt.de/immobilienpreise")
        # time.sleep(5)
        # element = self.execute_script(
        #     """return document.querySelector('#usercentrics-root').shadowRoot
        #     .querySelector("button[data-testid='uc-accept-all-button']")""")
        # element.click()
