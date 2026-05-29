import allure

from locators.reg_locators import ForgotPasswordPageLocators, ResetPasswordPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    @allure.step("Ввод email для восстановления пароля")
    def enter_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step("Клик по ссылке 'Войти'")
    def click_back_to_login(self):
        self.click_element(ForgotPasswordPageLocators.BACK_TO_LOGIN_LINK)

    @allure.step("Клик по кнопке показа/скрытия пароля")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        return self.is_element_visible(ResetPasswordPageLocators.PASSWORD_ACTIVE)

    @allure.step("Ввод нового пароля")
    def enter_new_password(self, password):
        self.send_keys(ResetPasswordPageLocators.PASSWORD_INPUT, password)