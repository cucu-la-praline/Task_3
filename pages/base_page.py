from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        with allure.step(f"Получение текста из элемента: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))