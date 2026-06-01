import time
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
        self.is_element_visible(ResetPasswordPageLocators.RASSWORD_RECOVERY_TITLE)
        time.sleep(1)

    @allure.step("Клик по кнопке показа/скрытия пароля")
    def click_show_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        return self.check_exists(ResetPasswordPageLocators.PASSWORD_ACTIVE)
