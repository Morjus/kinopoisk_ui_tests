import allure
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HdProfilesPage(BasePage):

    CREATE_CHILD_HEADER = (By.XPATH, '//div/h1[contains(text(), "Как зовут ребенка?")]')
    WHAT_MOVIES_TO_SHOW_HEADER = (By.XPATH, '//div/h1[contains(text(), "Какое кино ему показывать?")]')
    GENDER_SELECTION_HEADER = (By.XPATH, '//div/h1[contains(text(), "Чтобы рекомендации были точнее, укажите пол")]')
    BIRTH_DATE_HEADER = (By.XPATH, '//div/h1[contains(text(), "... и день рождения")]')
    CARTOON_WORLD_HEADER = (By.CSS_SELECTOR, 'div h1')

    CHILD_NAME = (By.CSS_SELECTOR, '#name')
    DAY_BIRTH = (By.CSS_SELECTOR, '#day')
    MONTH_BIRTH = (By.CSS_SELECTOR, '#month')
    YEAR_BIRTH = (By.CSS_SELECTOR, '#year')

    NEXT_CHILD_STEP = (By.XPATH, '//a/div/button')
    CANCEL_BUTTON = (By.XPATH, '//button/span[contains(text(), "Отмена")]')


    CENSORING_AGE_0 = (By.CSS_SELECTOR, 'input[value="0"]')
    CENSORING_AGE_6 = (By.CSS_SELECTOR, 'input[value="6"]')
    CENSORING_AGE_12 = (By.CSS_SELECTOR, 'input[value="12"]')
    CENSORING_AGE_16 = (By.CSS_SELECTOR, 'input[value="16"]')
    CENSORING_AGE_18 = (By.CSS_SELECTOR, 'input[value="18"]')
    SELECT_GIRL = (By.CSS_SELECTOR, 'input[value="FEMALE"]')

    SIMPLE_PROFILE_HEADER = (By.CSS_SELECTOR, 'div h1')
    EDIT_PROFILES_BUTTON = (By.CSS_SELECTOR, 'button')
    CHILD_PROFILE_BUTTON = (By.CSS_SELECTOR, "[href^='/profiles']")
    DELETE_CHILD_PROFILE_BUTTON = (By.XPATH, '//div/button[span[contains(text(), "Удалить профиль")]]')
    ACCEPT_DELETE_CHILD_BUTTON = (By.XPATH, '//div/button[span[contains(text(), "Да, удаляем")]]')
    AVATAR_MENU = (By.CSS_SELECTOR, "button[class^='ProfileMenu']")
    RULE_PROFILES = (By.XPATH, '//li/a[span[contains(text(), "Управление профилями")]]')


    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url
        self.logger = logging.getLogger(type(self).__name__)

    def create_child_profile(self, name):
        with allure.step(f"Ввожу {name} детского профиля"):
            self.find(locator=self.CHILD_NAME).send_keys(name)
        with allure.step("Переход к следующему шагу в процессе создания детского профиля"):
            self.find(locator=self.NEXT_CHILD_STEP).click()
            self.find(locator=self.WHAT_MOVIES_TO_SHOW_HEADER)
        with allure.step("Выбор возрастную политику фильмов"):
            self.find(locator=self.CENSORING_AGE_6).click()
            self.find(locator=self.NEXT_CHILD_STEP).click()
            self.find(locator=self.GENDER_SELECTION_HEADER)
        with allure.step("Выбираю пол ребенка"):
            self.find(locator=self.SELECT_GIRL).click()
            self.find(locator=self.NEXT_CHILD_STEP).click()
            self.find(locator=self.BIRTH_DATE_HEADER)
        with allure.step("Ввожу дату рождения ребенка"):
            self.find(locator=self.DAY_BIRTH).send_keys("25")
            self.find(locator=self.MONTH_BIRTH).send_keys("12")
            self.find(locator=self.YEAR_BIRTH).send_keys("2010")
            self.find(locator=self.NEXT_CHILD_STEP).click()
            self.is_disappeared(locator=self.CANCEL_BUTTON, time=5)
        with allure.step("Ищу заголовок после регистрации"):
            return self.find(locator=self.CARTOON_WORLD_HEADER).text

    def delete_child_profile(self):
        main_hd_link = "https://hd.kinopoisk.ru/"
        with allure.step(f"Перехожу на {main_hd_link} для удаления созданного детского профиля"):
            self.driver.get(main_hd_link)
        with allure.step("Открываю меню профиля через аватар"):
            self.find(locator=self.AVATAR_MENU).click()
        with allure.step("Открываю управление профилями"):
            self.find(locator=self.RULE_PROFILES).click()
        with allure.step('Нажимаю кнопку "Редактировать"'):
            self.find(locator=self.EDIT_PROFILES_BUTTON).click()
        with allure.step("Перехожу к профилю для удаления"):
            self.find(locator=self.CHILD_PROFILE_BUTTON).click()
            with allure.step("Ищу заголовок с настройками"):
                self.find(locator=self.SIMPLE_PROFILE_HEADER)
        with allure.step("Ищу кнопку удаления детского профиля и нажимаю"):
            self.find(locator=self.DELETE_CHILD_PROFILE_BUTTON).click()
        with allure.step("Ищу кнопку подтверждения удаления детского профиля и нажимаю"):
            self.find(locator=self.ACCEPT_DELETE_CHILD_BUTTON).click()
        with allure.step("Ищу кнопку редактирования профиля"):
            self.find(locator=self.CHILD_PROFILE_BUTTON)
            return True

