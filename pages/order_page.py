import allure

from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Клик по заказу в ленте")
    def click_order_in_feed(self, index=1):
        self.is_element_visible(OrderPageLocators.ORDER_FEED_LIST)
        self.click_element(OrderPageLocators.order_item(index))

    @allure.step("Проверка, что модальное окно с деталями заказа открыто")
    def is_order_details_modal_visible(self):
        return self.check_exists(OrderPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Получение выполненных заказов за сегодня")
    def get_completed_today_counter(self):
        return self.get_attribute(OrderPageLocators.COMPL_TODAY, "textContent")

    @allure.step("Получение выполненных заказов за все время")
    def get_completed_total_counter(self):
        return self.get_attribute(OrderPageLocators.COMPL_IN_ALL_TIME, "textContent")

    @allure.step("Получение номера заказа В работе")
    def get_order_in_work(self):
        return self.get_attribute(OrderPageLocators.IN_WORK, "textContent")