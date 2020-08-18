import pytest
import allure
from pages.main_page import MainPage
from pages.movie_page import MoviePage
from pages.user_page import UserPage
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
    page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    header = page.check_main_header()
    assert header == "Главное сегодня", f"Заголовок 'Главное сегодня' не найден. Найдено: {header}"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Рейтинг фильма")
@allure.story("Выставление оценки фильму авторизованного пользователя и удаление оценки")
@pytest.mark.parametrize("rating", [10])
def test_set_rating(browser, rating):
    page = MoviePage(browser, url="https://www.kinopoisk.ru/film/693969/")
    page.open()
    page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    page.set_rating(rating)
    result_rating = page.check_rating_on_page()
    assert int(result_rating) == rating, f"Оценка на странице: {result_rating} не соответствует ожидаемой {rating}"
    page.delete_rating_on_page()
    assert page.check_rating_is_not_presented() is True, "Оценка фильма не удалена"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Папки с фильмами юзера")
@allure.story("Добавление фильма в папку 'Смотреть позже' и его удаление")
def test_add_to_watch_later(browser):
    page = MoviePage(browser, url="https://www.kinopoisk.ru/film/693969/")
    page.open()
    page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    page.add_to_watch_later()
    movie_name = page.get_movie_name()
    page.go_to_watch_later_list()
    page = UserPage(page.driver, page.driver.current_url)
    page.open()
    name = page.get_first_movie_in_watch_later_list()
    assert movie_name == name, f"Имена {movie_name} на странице фильма и {name} в списке 'Буду смотреть' не совпадают"

    result = page.del_first_from_watch_later()
    assert result is True, f"Фильм из списка не удален"



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
