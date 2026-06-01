from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_TITLE = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")