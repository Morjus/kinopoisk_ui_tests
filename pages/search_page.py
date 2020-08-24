import allure
import logging
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class SearchPage(HeaderPage):

    MOST_WANTED_EL = (By.CSS_SELECTOR, '.element.most_wanted .name [data-type="film"]')
    GUESS_HEADER = (By.XPATH, '//p[contains(text(), "Скорее")]')
    MOST_WANTED_NAME = (By.CSS_SELECTOR, ".element.most_wanted .info .name a")

    MOVIE_PAGE_NAME_HEADER = (By.CSS_SELECTOR, 'h1[itemprop="name"] span')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    def check_guessing_of_search(self):
        with allure.step("Ищу заголовок с догадкой о цели поиска"):
            self.is_element_present(locator=self.GUESS_HEADER)
        guess = self.find(locator=self.MOST_WANTED_EL)
        with allure.step(f"Найден заголовок {guess}"):
            return guess.text

    def go_to_guessing_movie(self):
        with allure.step("Переход по ссылке к найденному в поиске фильму"):
            movie_link = self.find(locator=self.MOST_WANTED_NAME)
            movie_link.click()

