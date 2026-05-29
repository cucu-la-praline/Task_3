import allure

from locators.profile_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Клик по 'История заказов'")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по 'Выход'")
    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверка, что история заказов отображается")
    def is_order_history_visible(self):
        return self.is_element_visible(ProfilePageLocators.ORDER_IN_HISTORY)

    @allure.step("Получение списка заказов из истории")
    def get_orders_from_history(self):
        orders = self.driver.find_elements(*ProfilePageLocators.ORDER_IN_HISTORY)
        return [order.text for order in orders]