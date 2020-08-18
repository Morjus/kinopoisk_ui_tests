import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def check_last_rating(self):
        pass