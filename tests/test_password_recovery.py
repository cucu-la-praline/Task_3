import allure
import pytest
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()

        assert "forgot-password" in browser.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_restore_password_with_email(self, browser, base_url, registered_user):
        user_data, _ = registered_user

        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()

        forgot_page = ForgotPasswordPage(browser)
        forgot_page.enter_email(user_data["email"])
        forgot_page.click_restore_button()

        assert "reset-password" in browser.current_url

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_activates_field(self, browser, base_url):
        browser.get(base_url)
        main_page = MainPage(browser)
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()

        forgot_page = ForgotPasswordPage(browser)
        forgot_page.enter_email("test@test.com")
        forgot_page.click_restore_button()

        reset_page = ResetPasswordPage(browser)
        reset_page.click_show_password_button()

        assert reset_page.is_password_field_active()