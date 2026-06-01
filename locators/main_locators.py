from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (By.XPATH, "//header[@class='AppHeader_header__X9aJA pb-4 pt-4']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    COLLECT_BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    DRAG_TO_TOP = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")