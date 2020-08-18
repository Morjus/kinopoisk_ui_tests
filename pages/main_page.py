import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    MAIN_HEADER = (By.CSS_SELECTOR, 'section.main-page-media-block__main h1')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def check_main_header(self):
        with allure.step(f"Ищу главный заголовок на странице"):
            text = self.find(locator=self.MAIN_HEADER).text
        return text

    def go_to_recommendations(self):
        pass

    def go_to_get_tickets(self):
        pass

    def go_to_promo_code(self):
        pass

    def go_to_hd(self):
        pass

    def search_movie(self):
        pass
