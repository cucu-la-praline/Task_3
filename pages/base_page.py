import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        with allure.step("Найти элемент"):
            return self.driver.find_element(*locator)

    def click_element(self, locator, timeout=10):
        with allure.step(f"Клик по элементу: {locator}"):
            wait = WebDriverWait(self.driver, timeout)

            # 1. Ждем, что элемент присутствует в DOM
            element = wait.until(EC.presence_of_element_located(locator))

            # 2. Прокручиваем к элементу
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.3)  # Небольшая пауза для Firefox

            # 3. Ждем, что элемент стал видимым
            wait.until(EC.visibility_of(element))

            # 4. Ждем, что элемент стал кликабельным
            wait.until(EC.element_to_be_clickable(locator))

            # 5. Пробуем кликнуть
            try:
                element.click()
            except ElementClickInterceptedException:
                # Если перехвачено, пробуем клик через JS
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as e:
                # Если ошибка, делаем паузу и пробуем ещё раз
                time.sleep(1)
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()

    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        with allure.step(f"Получение текста из элемента: {locator}"):
            element = self.find_element(locator)
            return element.text

    def get_attribute(self, locator, value):
        with allure.step("Получить аттрибут"):
            element = self.find_element(locator)
            return element.get_attribute(value)

    def is_element_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def is_element_not_visible(self, locator):
        try:
            element = self.find_element(locator)
            return not element.is_displayed()
        except:
            return True

    def check_exists(self, selector, time=1):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(selector)
            )
            return True
        except:
            return False

    @allure.step("Перетаскиваем элемент {source_locator} в целевую зону {target_locator}")
    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        """
        Универсальный метод для перетаскивания элемента с поддержкой Firefox
        """
        source_element = self.wait.until(
            EC.presence_of_element_located(source_locator),
            message=f"Не найден источник: {source_locator}"
        )

        target_element = self.wait.until(
            EC.presence_of_element_located(target_locator),
            message=f"Не найдена цель: {target_locator}"
        )

        # Прокручиваем к элементам
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source_element)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_element)
        time.sleep(0.3)

        # Определяем браузер
        is_firefox = "firefox" in self.driver.capabilities["browserName"].lower()

        if is_firefox:
            # Для Firefox используем JavaScript + события
            self._drag_and_drop_firefox(source_element, target_element)
        else:
            # Для Chrome используем ActionChains
            try:
                actions = ActionChains(self.driver)
                actions.drag_and_drop(source_element, target_element).perform()
            except Exception as e:
                print(f"ActionChains failed: {e}, trying JS method")
                self._drag_and_drop_firefox(source_element, target_element)

    def _drag_and_drop_firefox(self, source_element, target_element):
        """
        Перетаскивание для Firefox через JavaScript и события
        """
        # JavaScript для эмуляции drag and drop
        js_code = """
        function simulateDragDrop(src, dst) {
            // Создаем данные для перетаскивания
            var dataTransfer = new DataTransfer();

            // Drag start
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            src.dispatchEvent(dragStartEvent);

            // Drag over
            var dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            dst.dispatchEvent(dragOverEvent);

            // Drop
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            dst.dispatchEvent(dropEvent);

            // Drag end
            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            src.dispatchEvent(dragEndEvent);
        }

        simulateDragDrop(arguments[0], arguments[1]);
        """

        try:
            self.driver.execute_script(js_code, source_element, target_element)
        except Exception as e:
            print(f"JS drag and drop failed: {e}, trying alternative method")
            self._drag_and_drop_click_hold(source_element, target_element)

    def _drag_and_drop_click_hold(self, source_element, target_element):
        """
        Альтернативный метод через click_and_hold
        """
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element)
        actions.move_to_element(target_element)
        actions.release()
        actions.perform()
