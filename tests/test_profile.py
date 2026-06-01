import time

import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()

        assert "account" in browser.current_url

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)

        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()
        profile_page.click_order_history()

        assert "order-history" in browser.current_url

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, browser, base_url, registered_user):
        user_data, _ = registered_user
        browser.get(base_url)
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)

        main_page.click_login_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()
        profile_page.click_logout()
        assert "login" in browser.current_url