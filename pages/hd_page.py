import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HdPage(BasePage):

    MOVIE_NAME = (By.CSS_SELECTOR, 'div div span img')


    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def get_name_of_opened_movie(self):
        with allure.step("Проверяю, что открылся фильм"):
            element = self.find(locator=self.MOVIE_NAME)
            movie_name = element.get_attribute("alt")

        with allure.step(f"Открылся фильм: {movie_name}"):
            print(movie_name)
