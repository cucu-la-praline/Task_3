from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    BUN_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]")
    SAUCE_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    FILLING_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]")