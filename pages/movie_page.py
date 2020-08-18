import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MoviePage(BasePage):

    STARS = (By.CSS_SELECTOR, '[name="star"]+span')
    MY_RATING = (By.CSS_SELECTOR, 'div h4+span')
    DELETE_RATING = (By.XPATH, '//button[contains(text(), "Удалить")]')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url
        self.number = None

    def set_rating(self, number: int):
        self.number = number

        with allure.step("Поиск звезд для выставления рейтинга"):
            stars = self.finds(locator=self.STARS)
        with allure.step(f"Выставляю фильму рейтинг {self.number}"):
            stars[number-1].click()

    def check_rating_on_page(self):
        with allure.step("Ищу выставленную оценку на странице"):
            rating = self.find(locator=self.MY_RATING).text
            return rating

    def delete_rating_on_page(self):
        with allure.step("Ищу кнопку удаления оценки и нажимаю"):
            self.find(locator=self.DELETE_RATING).click()
        with allure.step("Удаляю оценку"):
            self.find(locator=self.DELETE_RATING).click()

    def check_rating_is_not_presented(self):
        res = self.is_not_element_present(locator=MoviePage.MY_RATING)
        return res
