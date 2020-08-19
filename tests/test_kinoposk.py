import pytest
import allure
from pages.main_page import MainPage
from pages.movie_page import MoviePage
from pages.user_page import UserPage
from pages.recommendation_page import RecommendationPage
from pages.hd_profiles_page import HdProfilesPage
from pages.hd_page import HdPage
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
    movie_page = MoviePage(browser, url="https://www.kinopoisk.ru/film/693969/")
    movie_page.open()
    movie_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    movie_page.add_to_watch_later()
    movie_name = movie_page.get_movie_name()
    movie_page.go_to_watch_later_list()
    user_page = UserPage(movie_page.driver, movie_page.driver.current_url)
    name = user_page.get_first_movie_in_watch_later_list()
    assert movie_name == name, f"Имена {movie_name} на странице фильма и {name} в списке 'Буду смотреть' не совпадают"

    result = user_page.del_first_from_watch_later()
    assert result is True, f"Фильм из списка не удален"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Смотреть онлайн на кинопоиск HD")
@allure.story("Переход из рекомендаций сразу к просмотру фильма онлайн по плюс подписке")
def test_from_recommends_go_to_online(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    main_page.go_to_recommendations()

    recom_page = RecommendationPage(main_page.driver, main_page.driver.current_url)
    recom_page.switch_tab_to_online()
    recom_page.go_to_watch_online_random_movie_from_list()

    hd_page = HdPage(recom_page.driver, recom_page.driver.current_url)
    movie_name = hd_page.get_name_of_opened_movie()
    assert movie_name is not None, f"Названия фильма на странице нет, есть {movie_name}"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Детский профиль")
@allure.story("Создание детского профиля")
def test_create_child_profile(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    main_page.go_to_hd()
    hd_page = HdPage(main_page.driver, main_page.driver.current_url)
    hd_page.go_to_create_child_profile()

    create_profile_page = HdProfilesPage(hd_page.driver, hd_page.driver.current_url)
    final_header = create_profile_page.create_child_profile("Зайка")
    assert final_header == 'Волшебный мир мультфильмов скрыт за подпиской', f"Заголовок найден, но иной:{final_header}"
    # should add method for removing profile


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
