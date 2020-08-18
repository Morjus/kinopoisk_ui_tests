from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time
import os
import allure
from dotenv import load_dotenv
load_dotenv()


class BasePage:
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#passp-field-login')
    PASSW_FIELD = (By.CSS_SELECTOR, '#passp-field-passwd')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SKIP_PHONE_BUTTON = (By.XPATH, '//button[@type="button"]')

    def __init__(self, driver, url=None):
        self.driver = driver
        self.base_url = url

    def find(self, locator, time=10):
        with allure.step(f"Поиск элемента, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")

    def find_interactable(self, locator, time=10):
        with allure.step(f"Поиск интерактивного элемента, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator),
                message=f"Can't find element by locator {locator}")

    def finds(self, locator, time=10):
        with allure.step(f"Поиск элементов, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")

    def is_element_present(self, locator, time=10):
        with allure.step(f"Поиск видимых элементов на странице, {locator}"):
            try:
                WebDriverWait(self.driver, time).until(
                    EC.visibility_of_element_located(locator),
                    message=f"Can't find elements by locator {locator}")
            except NoSuchElementException:
                return False
            return True

    def is_not_element_present(self, locator, time=10):
        with allure.step(f"Поиск элемента, которого не должно быть на странице, {locator}"):
            try:
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located(locator),
                    message=f"Can find elements by locator {locator}")
            except TimeoutException:
                return True
            return False

    def is_disappeared(self, locator, time=1):
        with allure.step(f"Поиск элемента, которого должен пропасть, {locator}"):
            try:
                WebDriverWait(self.driver, time, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located(locator))
            except TimeoutException:
                return False
            return True

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

    def open(self):
        with allure.step(f"Переход на страницу, {self.base_url}"):
            return self.driver.get(self.base_url)
