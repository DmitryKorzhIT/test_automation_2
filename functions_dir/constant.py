import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = os.getenv("BASE_URL")
EMPLOYEES_URL = os.getenv("EMPLOYEES_URL")
COMPETITIONS_AND_RESULTS_URL = os.getenv("COMPETITIONS_AND_RESULTS_URL")
