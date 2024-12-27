

from base.base_class import Base
from selenium import webdriver
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

    complete_order = (By.XPATH,'//input[@name="checkout"]') # кнопка перехода к оформлению заказа
    name_product = (By.XPATH, '//a[@class="bold"]')  # название продукта
    price_product = (By.XPATH, '//td[@class="align-top item-total nowrap"]') #цена товара в корзине
    btn_delete = (By.XPATH,'//a[@class="delete"]') # кнопка удаления товара
    successfully_delete =  (By.XPATH,'//p[text()="Ваша корзина пуста."]') # текст оповещение о пустой корзине





    # Getters

    def get_complete_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.complete_order))

    def get_name_product(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_product))

    def get_price_product(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.price_product))

    def get_btn_delete(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.btn_delete))

    def get_item_is_successfully(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.successfully_delete))


    # Actions
    def click_complete_order(self):
        self.get_complete_order().click()

    def text_name_product(self):
        return self.get_name_product().text

    def  text_price_product(self):
        return self.get_price_product().text







    #Methods
    @allure.step("Переход к заполнению персональных данных")
    def move_complete_order(self):
        self.click_complete_order()

    """Название и цена товара( для проверки со стартовой ценой)"""
    def comparison_price(self):
        return f"{self.text_name_product()} : {self.text_price_product()} Рублей"



    @allure.step("удаление всех товаров из корзины")
    def comparison_price_all(self):
            all_elem = self.get_btn_delete()
            for i in all_elem:
                i.click()




