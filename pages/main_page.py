import allure
from random import choice
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class MainPage(HeaderPage):
    MAIN_HEADER = (By.CSS_SELECTOR, 'section.main-page-media-block__main h1')
    RECOMMENDATION_LINK = (By.XPATH, '//h3/a[contains(text(), "Рекомендации")]')
    RECOMMENDATION_HEADER = (By.XPATH, '//h1[contains(text(), "Рекомендации")]')
    ONLINE_TAB = (By.XPATH, '//span[contains(text(), "Онлайн")]')

    TODAY_IN_CINEMA = (By.CSS_SELECTOR, '.today-in-cinema__carousel .carousel__item a[kind="primary"]')
    CHOSEN_MOVIE_HEADER = (By.CSS_SELECTOR, ".link.film-header__title")
    ALL_AVAILABLE_SESSIONS = (By.CSS_SELECTOR, ".schedule-item__session-button-wrapper")

    INFO_ABOUT_SESSION_IN_ELEMENT = (By.CSS_SELECTOR, "span")

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

    def select_random_movie_from_today_in_cinema(self):
        with allure.step("Поиск всех ссылок на покупку билета в кинотеатр"):
            movies = self.finds(locator=self.TODAY_IN_CINEMA)
        with allure.step("Выбор случайного фильма"):
            selected_movie = choice(movies)
        with allure.step("Перехожу к покупке билета"):
            selected_movie.click()
            movie_name = self.find(locator=self.CHOSEN_MOVIE_HEADER)
        with allure.step(f"Выбран фильм {movie_name.text}"):
            print(movie_name.text)

    def buy_random_tickets(self):
        with allure.step("Ищу все сеансы фильма"):
            sessions = self.finds(locator=self.ALL_AVAILABLE_SESSIONS)
        with allure.step("Выбираю случайный сеанс"):
            random_session = choice(sessions)

            info_about_session = random_session.finds(locator=self.INFO_ABOUT_SESSION_IN_ELEMENT)
            time_of_session = info_about_session[0].text
            cost_of_session = info_about_session[1].text
            print(time_of_session, cost_of_session)


        # with allure.step(f"Выбран сеанс в {random_session} за {random_session}")


