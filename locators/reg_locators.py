from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")


class ResetPasswordPageLocators:
    RASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")