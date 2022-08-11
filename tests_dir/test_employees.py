from functions_dir.employees import Employees
from functions_dir import constant as const


EMPLOYEES_URL = const.EMPLOYEES_URL

def test_1():
    ''' Check is accordion opens. '''

    employees = Employees()

    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    flag = employees.is_accordion_opened()

    assert flag


def test_2():
    ''' Check if the title of professions changes after clicking on a profession. '''

    employees = Employees()

    flag = True
    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    assert employees.check_professions_titles()


def test_3():
    ''' Checking each profession for the presence of at least one employee. '''

    employees = Employees()

    employees.load_specific_page(url=EMPLOYEES_URL)
    employees.accept_cookies()
    employees.open_accordion()
    flag = employees.check_existence_of_employees()

    assert flag
