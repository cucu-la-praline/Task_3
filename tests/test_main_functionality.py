import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_order_feed()
        main_page.click_constructor()

        assert main_page.is_collect_button_visible()

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
        main_page.collect_button_visible()
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_modal(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.collect_button_visible()
        main_page.click_ingredient()
        main_page.close_ingredient_modal()

        assert not main_page.is_ingredient_modal_visible()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.wait_header()
        initial_counter = main_page.get_ingredient_counter()
        main_page.drag_bun_to_top()
        new_counter = main_page.get_ingredient_counter()

        assert new_counter > initial_counter

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_user_can_place_order(self, browser, base_url, registered_user):
        user_data, _ = registered_user

        browser.get(base_url)
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        main_page.wait_header()
        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.drag_bun_to_top()
        main_page.click_place_order()

        assert main_page.is_ordered()
