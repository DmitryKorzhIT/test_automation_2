import time

from functions_dir.base import Base

from . import constant as const

CALCULATE_ENERGY_REQUIREMENTS = const.CALCULATE_ENERGY_REQUIREMENTS_URL


class CalculateEnergyRequirements(Base):
    def fill_base_metabolism(self):
        self.implicitly_wait(2)

        time.sleep(5)

        shadow_root_1 = self.execute_script(
            """return document.querySelector("td-calculator")
            .shadowRoot.querySelector("iron-pages[attr-for-selected='name']")"""
        )

        print(shadow_root_1)

        # inner_texts = [my_elem.get_attribute("outerHTML") for my_elem in driver.execute_script(
        #     """return document.querySelector('game-app').shadowRoot.querySelector('game-row').
        #     shadowRoot.querySelectorAll('game-tile[letter]')""")]
        #
        # "return document.querySelector('downloads-manager').shadowRoot.querySelector('downloads-toolbar#toolbar')" \
        # ".shadowRoot.querySelector('cr-toolbar#toolbar').shadowRoot.querySelector('cr-toolbar-search-field#search')" \
        # ".shadowRoot.querySelector('div#searchTerm input#searchInput')"

        # metabolism_weight = metabolism.find_element(By.ID, 'weight')
        # print(f'Weight: {metabolism_weight}')

        # self.get("https://www.immowelt.de/immobilienpreise")
        # time.sleep(5)
        # element = self.execute_script(
        #     """return document.querySelector('#usercentrics-root').shadowRoot
        #     .querySelector("button[data-testid='uc-accept-all-button']")""")
        # element.click()
