import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from helpers import create_user_via_api, delete_user_via_api
from pages.login_page import LoginPage
from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")
    parser.addoption("--base-url", action="store",
                     default="https://stellarburgers.education-services.ru",
                     help="Base URL")


@pytest.fixture
def browser(request):
    """Фикстура браузера с поддержкой Chrome и Firefox"""
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base-url")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=960,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        # Важные настройки для Firefox
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        options.set_preference("pdfjs.disabled", True)

        # Отключаем автоматические обновления
        options.set_preference("app.update.auto", False)
        options.set_preference("app.update.enabled", False)

        # Указываем путь к Firefox (если нужно)

        try:
            # Используем webdriver-manager для Firefox
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        except Exception as e:
            print(f"Error with Firefox: {e}")
            # Пробуем без service
            driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(base_url)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def api_base_url():
    return "https://stellarburgers.education-services.ru"


@pytest.fixture
def registered_user(api_base_url):
    """Создание пользователя через API для тестов"""
    user_data, token = create_user_via_api(api_base_url)
    yield user_data, token

    # Очистка после тестов
    delete_user_via_api(api_base_url, token)


@pytest.fixture
def login_user(browser, base_url, registered_user):
    """Авторизованный пользователь"""
    user_data, token = registered_user
    main_page = MainPage(browser)

    browser.get(base_url)
    main_page.click_login_button()

    login_page = LoginPage(browser)
    login_page.login(user_data["email"], user_data["password"])

    yield browser, user_data, token
