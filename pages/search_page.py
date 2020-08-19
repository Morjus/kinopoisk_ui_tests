import allure
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class SearchPage(HeaderPage):

    MOST_WANTED_EL = (By.CSS_SELECTOR, ".element.most_wanted")
    GUESS_HEADER = (By.XPATH, '//p[contains(text(), "Скорее")]')
    MOST_WANTED_NAME = (By.CSS_SELECTOR, ".element.most_wanted .info .name a")

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def check_guessing_of_search(self):
        self.is_element_present(locator=self.GUESS_HEADER)
        self.find(locator=self.MOST_WANTED_EL)
        return self.find(locator=self.MOST_WANTED_NAME).text