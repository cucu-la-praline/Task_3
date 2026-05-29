import allure

from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Клик по заказу в ленте")
    def click_order_in_feed(self, index=0):
        orders = self.driver.find_elements(*OrderPageLocators.ORDER_IN_FEED)
        if orders and len(orders) > index:
            orders[index].click()

    @allure.step("Проверка, что модальное окно с деталями заказа открыто")
    def is_order_details_modal_visible(self):
        return self.is_element_visible(OrderPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Получение счетчика 'Выполнено за всё время'")
    def get_completed_total_counter(self):
        text = self.get_text(OrderPageLocators.COMPLETED_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_completed_today_counter(self):
        elements = self.driver.find_elements(*OrderPageLocators.TODAY_COMPLETED_COUNTER)
        if len(elements) >= 2:
            text = elements[1].text
            return int(text) if text.isdigit() else 0
        return 0

    @allure.step("Получение заказов в работе")
    def get_orders_in_progress(self):
        orders = self.driver.find_elements(*OrderPageLocators.ORDERS_IN_PROGRESS)
        return [order.text for order in orders]

    @allure.step("Получение номера последнего заказа")
    def get_last_order_number(self):
        text = self.get_text(OrderPageLocators.ORDER_NUMBER)
        return text