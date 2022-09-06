import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)

from functions_dir import constant as const
from functions_dir.calculate_liquid_test import CalculateLiquidTest

CALCULATE_LIQUID_TEST_URL = const.CALCULATE_LIQUID_TEST_URL


def test_1():
    calculate_liquid_test = CalculateLiquidTest()

    calculate_liquid_test.load_specific_page(CALCULATE_LIQUID_TEST_URL)
    calculate_liquid_test.accept_cookies()
    if calculate_liquid_test.check_report_data_equal_zero():
        calculate_liquid_test.fill_data()
        flag = calculate_liquid_test.check_report_data()
    else:
        flag = False

    assert flag
