from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Base:

    """Базовый класс содержит универсальные методы"""
    def __init__(self,driver):
        self.driver = driver

    """Проверка URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL : {get_url}')

    @allure.step("Переход в корзину")
    def open_cart(self):
        cart = (By.XPATH,'//i[@class="icon-shopping-cart icon-2x"]')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(cart)).click()




