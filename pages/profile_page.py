import allure

from locators.login_locators import LoginPageLocators
from locators.profile_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Клик по 'История заказов'")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по 'Выход'")
    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.is_element_visible(LoginPageLocators.ENTER_TITLE)

    @allure.step("Проверка наличия заказа в истории")
    def is_order_in_list(self, number):
        return self.check_exists(ProfilePageLocators.order_item_in_history(number))
