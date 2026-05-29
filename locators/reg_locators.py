from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    BACK_TO_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")