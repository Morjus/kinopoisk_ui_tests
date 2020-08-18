import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
import os
from dotenv import load_dotenv
load_dotenv()

import time


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Авторизация")
@allure.story("Авторизация с валидными данными")
def test_login(browser):
    page = MainPage(browser, url="https://www.kinopoisk.ru/")
    page.open()
    header = page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    assert header == "Главное сегодня"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Рейтинг фильма")
@allure.story("Выставление рейтинга фильма авторизованного пользователя")
def test_set_rating():
    pass


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Папки с фильмами юзера")
@allure.story()
def test_add_to_see_later():
    pass


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Смотреть онлайн на кинопоиск HD")
@allure.story("Переход из рекомендаций сразу к просмотру фильма онлайн")
def test_from_recommends_go_to_online():
    pass


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Детский профиль")
@allure.story("Создание детского профиля")
def test_create_child_profile():
    pass


@allure.epic("Акции для юзеров")
@allure.feature("Промокод")
@allure.story("Проверка использования промокода")
def test_promocode():
    pass


@allure.epic("Поиск")
@allure.feature("Поисковая строка")
@allure.story("Правильное название фильма в поиске ведет к результатам, где введенный в поиск фильм на первом месте")
def test_search():
    pass


@allure.epic("Статьи")
@allure.feature("Тесты")
@allure.story("Прохождение теста в статье приводит к результу")
def test_pass_tests():
    pass


@allure.epic("Кинотеатры")
@allure.feature("Покупка билетов")
@allure.story("Покупка билетов с главной страницы")
def test_buy_tickets_from_main_page():
    pass
