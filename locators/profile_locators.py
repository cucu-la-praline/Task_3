from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    ORDER_IN_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_list')]//div[contains(@class, 'OrderHistory_item')]")
