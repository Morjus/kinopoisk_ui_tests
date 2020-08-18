import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#passp-field-login')
    PASSW_FIELD = (By.CSS_SELECTOR, '#passp-field-passwd')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SKIP_PHONE_BUTTON = (By.XPATH, '//button[@type="button"]')
    MAIN_HEADER = (By.CSS_SELECTOR, 'section.main-page-media-block__main h1')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def _set_email(self, email):
        with allure.step(f"Отправка {email} в {self.EMAIL_FIELD}"):
            self.find(locator=self.EMAIL_FIELD).send_keys(email)

    def _set_passw(self, passw):
        with allure.step(f"Отправка {passw} в {self.PASSW_FIELD}"):
            self.find(locator=self.PASSW_FIELD).send_keys(passw)

    def login(self, email, passw):
        with allure.step(f"Нажатие на 'Войти' на главной странице"):
            self.find(locator=self.LOGIN_BUTTON).click()
        self._set_email(email)
        with allure.step(f"Нажимаю кнопку {self.SUBMIT_BUTTON}"):
            self.find(locator=self.SUBMIT_BUTTON).click()
        self._set_passw(passw)
        with allure.step(f"Нажимаю кнопку {self.SUBMIT_BUTTON}"):
            self.find(locator=self.SUBMIT_BUTTON).click()
        # with allure.step(f"Пропуск предложения привязать телефон"):
        #     self.find(locator=self.SKIP_PHONE_BUTTON).click()
        with allure.step(f"Ищу главный заголовок на странице"):
            text = self.find(locator=self.MAIN_HEADER).text
        return text
