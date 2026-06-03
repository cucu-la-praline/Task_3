import time

import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик на заказ - открывается всплывающее окно с деталями")
    def test_order_modal_appears(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        order_feed_page = OrderPage(browser)

        main_page.wait_header()
        main_page.click_order_feed()
        order_feed_page.click_order_in_feed()

        assert order_feed_page.is_order_details_modal_visible()

    @allure.title("Заказы пользователя из истории отображаются в ленте заказов")
    def test_user_orders_appear_in_feed(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        main_page = MainPage(browser)

        # Создаем заказ
        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.drag_bun_to_top()
        order_number = main_page.click_place_order()
        main_page.close_modal()

        # Переходим в историю заказов
        main_page.click_personal_account()
        profile_page.click_order_history()
        assert profile_page.is_order_in_list(order_number)

        # Переходим в ленту заказов
        main_page.click_order_feed()
        assert profile_page.is_order_in_list(order_number)

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_completed_total_counter_increases(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order = OrderPage(browser)

        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])

        # Переходим в ленту заказов и запоминаем текущий счетчик
        main_page.click_order_feed()
        initial_total_counter = order.get_completed_total_counter()

        # Возвращаемся в конструктор и создаем заказ
        main_page.click_constructor()
        main_page.drag_bun_to_top()
        main_page.click_place_order()
        main_page.close_modal()

        # Снова переходим в ленту заказов и проверяем счетчик
        main_page.click_order_feed()
        new_total_counter = order.get_completed_total_counter()

        assert new_total_counter > initial_total_counter

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_completed_today_counter_increases(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order = OrderPage(browser)

        # Авторизация
        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])

        # Переходим в ленту заказов и запоминаем текущий счетчик
        main_page.click_order_feed()
        initial_today_counter = order.get_completed_today_counter()

        # Возвращаемся в конструктор и создаем заказ
        main_page.click_constructor()
        main_page.drag_bun_to_top()
        main_page.click_place_order()
        main_page.close_modal()

        # Снова переходим в ленту заказов и проверяем счетчик
        main_page.click_order_feed()
        new_today_counter = order.get_completed_today_counter()

        assert new_today_counter > initial_today_counter

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        order = OrderPage(browser)

        # Авторизация
        main_page.wait_header()
        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])

        # в конструктор и создаем заказ
        main_page.click_constructor()
        main_page.drag_bun_to_top()
        new_order = main_page.click_place_order()
        main_page.close_modal()

        # Переходим в ленту заказов и проверяем появление номера в "В работе"
        main_page.click_order_feed()
        time.sleep(3) # Надо подождать пока обновится список
        order = order.get_order_in_work()

        assert new_order == order
