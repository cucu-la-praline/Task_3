import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_order_feed()
        main_page.click_constructor()

        assert main_page.is_place_order_button_visible()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_order_feed()

        assert "feed" in browser.current_url

    @allure.title("Клик на ингредиент - появляется всплывающее окно с деталями")
    def test_ingredient_modal_appears(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_ingredient("Флюоресцентная булка R2-D3")

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_modal(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_ingredient("Флюоресцентная булка R2-D3")
        main_page.close_ingredient_modal()

        assert not main_page.is_ingredient_modal_visible()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)

        initial_counter = main_page.get_ingredient_counter("Флюоресцентная булка R2-D3")
        main_page.add_ingredient_to_burger("Флюоресцентная булка R2-D3")
        new_counter = main_page.get_ingredient_counter("Флюоресцентная булка R2-D3")

        assert new_counter > initial_counter

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_user_can_place_order(self, browser, base_url, registered_user):
        user_data, _ = registered_user

        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_login_button()

        from pages.login_page import LoginPage
        login_page = LoginPage(browser)
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_place_order()

        assert main_page.is_place_order_button_visible()