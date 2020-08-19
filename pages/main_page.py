import allure
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class MainPage(HeaderPage):
    MAIN_HEADER = (By.CSS_SELECTOR, 'section.main-page-media-block__main h1')
    RECOMMENDATION_LINK = (By.XPATH, '//h3/a[contains(text(), "Рекомендации")]')
    RECOMMENDATION_HEADER = (By.XPATH, '//h1[contains(text(), "Рекомендации")]')
    ONLINE_TAB = (By.XPATH, '//span[contains(text(), "Онлайн")]')

    SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='text']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def check_main_header(self):
        with allure.step(f"Ищу главный заголовок на странице"):
            text = self.find(locator=self.MAIN_HEADER).text
        return text

    def go_to_recommendations(self):
        with allure.step("Перехожу в рекомендации через главный блок"):
            self.find(locator=self.RECOMMENDATION_LINK).click()
            self.find(locator=self.RECOMMENDATION_HEADER)

    def switch_tab_to_online(self):
        with allure.step("Переключение на вкладку онлайн в рекомендациях"):
            self.find(locator=self.ONLINE_TAB)

    def go_to_get_tickets(self):
        pass
