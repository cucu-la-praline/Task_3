from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_TITLE = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    @staticmethod
    def order_item_in_history(number):
        return By.XPATH, f"//div[contains(@class, 'OrderHistory_text')]/p[contains(text(), '{number}')]"
