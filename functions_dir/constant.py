import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DRIVER_PATH = os.getenv("DRIVER_PATH")
BASE_URL = os.getenv("BASE_URL")
EMPLOYEES_URL = os.getenv("EMPLOYEES_URL")
COMPETITIONS_AND_RESULTS_URL = os.getenv("COMPETITIONS_AND_RESULTS_URL")
CALCULATE_ENERGY_REQUIREMENTS_URL = os.getenv("CALCULATE_ENERGY_REQUIREMENTS_URL")
CALCULATE_LIQUID_TEST_URL = os.getenv("CALCULATE_LIQUID_TEST_URL")
