from . import constant as const
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


BASE_URL = const.BASE_URL
PASSWORD = const.PASSWORD


class Base(webdriver.Chrome):
    def __init__(self, teardown=False):  # the teardown is a condition for the __exit__ method
        self.teardown = teardown
        super(Base, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()



