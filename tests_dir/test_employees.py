from functions_dir.employees import Employees
from functions_dir import constant as const


EMPLOYEES_URL = const.EMPLOYEES_URL


def test_1():
    ''' Check accordion is opened. '''

    employees = Employees()

    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    flag = employees.is_accordion_opened()

    assert flag


def test_2():
    ''' Check if the title of the profession changes after clicking on a profession. '''

    employees = Employees()

    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    flag = employees.check_professions_titles()

    assert flag


def test_3():
    ''' Checking each profession for the presence of at least one employee. '''

    employees = Employees()

    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    flag = employees.check_existence_of_employees()

    assert flag
