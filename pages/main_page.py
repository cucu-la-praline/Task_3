import allure

from locators.main_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по 'Конструктор'")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по 'Лента заказов'")
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON_MAIN)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self, ingredient_name):
        locator = IngredientLocators.get_ingredient_by_name(ingredient_name)
        self.click_element(locator)

    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_modal(self):
        self.click_element(IngredientLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверка, что модальное окно с деталями отображается")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(IngredientLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Получение каунтера ингредиента")
    def get_ingredient_counter(self, ingredient_name):
        locator = IngredientLocators.get_ingredient_counter(ingredient_name)
        text = self.get_text(locator)
        return int(text) if text.isdigit() else 0

    @allure.step("Клик по 'Оформить заказ'")
    def click_place_order(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Добавление ингредиента в бургер")
    def add_ingredient_to_burger(self, ingredient_name):
        self.click_ingredient(ingredient_name)
        self.close_ingredient_modal()

    @allure.step("Проверка отображения кнопки 'Оформить заказ'")
    def is_place_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.PLACE_ORDER_BUTTON)