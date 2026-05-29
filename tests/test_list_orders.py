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
        main_page.click_order_feed()

        order_feed_page = OrderPage(browser)
        order_feed_page.click_order_in_feed()

        assert order_feed_page.is_order_details_modal_visible()

    @allure.title("Заказы пользователя из истории отображаются в ленте заказов")
    def test_user_orders_appear_in_feed(self, browser, base_url, registered_user):
        user_data, _ = registered_user

        # Создаем заказ
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(user_data["email"], user_data["password"])

        # Переходим в историю заказов
        main_page.click_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.click_order_history()

        history_orders = profile_page.get_orders_from_history()

        # Переходим в ленту заказов
        main_page.click_constructor()
        main_page.click_order_feed()

        assert len(history_orders) > 0