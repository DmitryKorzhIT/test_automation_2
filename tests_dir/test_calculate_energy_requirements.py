# import os
# import sys
#
# path = os.getcwd()  # get current directory
# parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
# sys.path.append(parent_path)
#
#
# import time
#
# from functions_dir import constant as const
# from functions_dir.calculate_energy_requirements import \
#     CalculateEnergyRequirements
#
# CALCULATE_ENERGY_REQUIREMENTS_URL = const.CALCULATE_ENERGY_REQUIREMENTS_URL
#
#
# def test_1():
#     """ """
#
#     calculate_energy_requirements = CalculateEnergyRequirements()
#
#     calculate_energy_requirements.load_specific_page(url=CALCULATE_ENERGY_REQUIREMENTS_URL)
#     calculate_energy_requirements.accept_cookies()
#     calculate_energy_requirements.fill_base_metabolism()
#
#     time.sleep(0)
