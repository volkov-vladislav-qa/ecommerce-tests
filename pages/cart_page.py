

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure





class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы Корзина"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    complete_order = (By.XPATH,'//input[@name="checkout"]')
    name_product = (By.XPATH, '//a[@class="bold"]')
    price_product = (By.XPATH, '//td[@class="align-top item-total nowrap"]')





    # Getters

    def get_complete_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.complete_order))

    def get_name_product(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_product))

    def get_price_product(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.price_product))



    # Actions
    def click_complete_order(self):
        self.get_complete_order().click()

    def text_name_product(self):
        return self.get_name_product().text

    def  text_price_product(self):
        return self.get_price_product().text





    #Methods
    @allure.step("Заполнение персональных данных")
    def move_complete_order(self):
        self.click_complete_order()

    """Название и цена товара( для проверки со стартовой ценой)"""
    def comparison_price(self):
        return f"{self.text_name_product()} : {self.text_price_product()} Рублей"




