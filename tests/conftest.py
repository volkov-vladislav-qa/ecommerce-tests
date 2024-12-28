import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

"""Настройки браузера"""
@pytest.fixture
def chrome_driver():
    # Настройки Chrome
    options = Options()
    #options.add_argument("--headless")  # Включаем headless mode
    options.add_argument("--incognito")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")

    # Запуск WebDriver с заданными параметрами
    driver = webdriver.Chrome(options=options)
    default_url = "https://fuji-san.ru/"
    driver.get(default_url)
    driver.maximize_window()

    # Передаем драйвер в тест
    yield driver

    # Закрытие браузера после выполнения теста
    driver.quit()


"""Вход"""
@pytest.fixture
def login_fix(chrome_driver):
    login = LoginPage(chrome_driver)
    login.authorization()  # авторизация