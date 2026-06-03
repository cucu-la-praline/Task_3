import time

import allure
from selenium.webdriver.common.by import By

from locators.ingredient_locators import IngredientLocators
from locators.main_locators import MainPageLocators
from locators.order_locators import OrderPageLocators
from locators.profile_locators import ProfilePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ожидание шапки страницы")
    def wait_header(self):
        self.is_element_visible(MainPageLocators.HEADER)

    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.is_element_visible(ProfilePageLocators.PROFILE_TITLE)

    @allure.step("Клик по 'Конструктор'")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по 'Лента заказов'")
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.is_element_visible(OrderPageLocators.ORDER_FEED_TITLE)

    @allure.step("Клик по 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON_MAIN)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(IngredientLocators.INGREDIENT)

    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_modal(self):
        self.click_element(IngredientLocators.CLOSE_MODAL_BUTTON)
        self.is_element_not_visible(IngredientLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Проверка, что модальное окно с деталями отображается")
    def is_ingredient_modal_visible(self):
        return self.check_exists(IngredientLocators.OPEN_MODAL)

    @allure.step("Получение каунтера ингредиента")
    def get_ingredient_counter(self):
        text = self.get_attribute((By.XPATH, IngredientLocators.INGREDIENT[1]
                                   + IngredientLocators.INGREDIENT_COUNTER[1]), "textContent")
        return int(text)

    @allure.step("Клик по 'Оформить заказ'")
    def click_place_order(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.is_element_visible(OrderPageLocators.ORDER_NUMBER)
        time.sleep(0.5)
        order_number = self.get_attribute(OrderPageLocators.ORDER_NUMBER, "textContent")
        return f"0{order_number}"

    @allure.step("Закрыть окно уведомления")
    def close_modal(self):
        self.click_element(IngredientLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверка отображения 'Ваш заказ начали готовить'")
    def is_ordered(self):
        return self.check_exists((By.XPATH, OrderPageLocators.ORDER_DETAILS_MODAL[1]
                                 + OrderPageLocators.YOUR_HAS_BEEN_PREPARED[1]))

    @allure.step("отображения 'Соберите бургер'")
    def collect_button_visible(self):
        self.is_element_visible(MainPageLocators.COLLECT_BURGER_TITLE)

    @allure.step("Проверка отображения 'Соберите бургер'")
    def is_collect_button_visible(self):
        return self.check_exists(MainPageLocators.COLLECT_BURGER_TITLE)

    @allure.step("Перетаскиваем булку в верхнюю часть конструктора")
    def drag_bun_to_top(self):
        """Перетаскивает булку в зону 'Перетяните булочку сюда (верх)'"""
        self.drag_and_drop(IngredientLocators.INGREDIENT, MainPageLocators.DRAG_TO_TOP)