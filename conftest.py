import pytest
from selenium import webdriver

# @pytest.fixture
# def browser(request, base_url):
#     driver = webdriver.Chrome()
#     base_url = request.config.getoption("--base-url", default="https://qa-mesto.praktikum-services.ru")
#     driver.get(base_url)
#
#     yield driver
#     driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")
    parser.addoption("--base-url", action="store",
                     default="https://stellarburgers.nomoreparties.site",
                     help="Base URL")


@pytest.fixture
def browser(request):
    """Фикстура браузера"""
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base-url")

    if browser_name == "chrome":
        # Selenium 4.6+ автоматически скачает правильный драйвер
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
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
    return "https://stellarburgers.nomoreparties.site"

#
# @pytest.fixture
# def browser(request, base_url):
#     options = Options()
#     driver = webdriver.Firefox(options=options)
#
#     base_url = request.config.getoption("--base-url", default='https://stellarburgers.nomoreparties.site')
#     driver.get(base_url)
#     driver.maximize_window()
#
#     yield driver
#     driver.quit()


@pytest.fixture
def registered_user(api_base_url):
    """Создание пользователя через API для тестов"""
    from helpers import create_user_via_api, delete_user_via_api

    user_data, token = create_user_via_api(api_base_url)
    yield user_data, token

    # Очистка после тестов
    delete_user_via_api(api_base_url, token)


@pytest.fixture
def login_user(browser, base_url, registered_user):
    """Авторизованный пользователь"""
    from pages.login_page import LoginPage
    from pages.main_page import MainPage

    user_data, token = registered_user
    main_page = MainPage(browser)

    browser.get(base_url)
    main_page.click_login_button()

    login_page = LoginPage(browser)
    login_page.login(user_data["email"], user_data["password"])

    yield browser, user_data, token