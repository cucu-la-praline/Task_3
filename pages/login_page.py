import allure

from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Ввод email")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по ссылке 'Зарегистрироваться'")
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Логин пользователя")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()