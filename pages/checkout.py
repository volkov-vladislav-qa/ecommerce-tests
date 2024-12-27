

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import allure






class CheckOut(Base):
    """ Класс содержащий локаторы и методы для страницы Оформление заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    customer_name = (By.XPATH,'//input[@name="customer[firstname]"]')
    customer_phone= (By.XPATH, '//input[@name="customer[phone]"]')
    customer_email = (By.XPATH, '//input[@name="customer[email]"]')
    customer_lastname = (By.XPATH, '//input[@name="customer[lastname]"]')
    customer_address = (By.XPATH, '//input[@name="customer[address.shipping][street]"]')





    # Getters

    def get_customer_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.customer_name))

    def get_customer_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.customer_phone))

    def get_customer_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.customer_email))

    def get_customer_lastname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.customer_lastname))

    def get_customer_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.customer_address))




    # Actions

    def input_customer_name(self,text):
        return self.get_customer_name().send_keys(text)

    def input_customer_phone(self,text):
        return self.get_customer_email().send_keys(text)

    def input_customer_email(self, text):
        return self.get_customer_email().send_keys(text)

    def input_customer_lastname(self, text):
        return self.get_customer_lastname().send_keys(text)

    def input_customer_address(self, text):
        return self.get_customer_address().send_keys(text)

    #Methods


    """Заполняем форму данными"""

    @allure.step("Заполнены данные для оформления заказа")
    def fill_form(self):
        fake = Faker()
        self.input_customer_name(fake.name())
        self.input_customer_phone(fake.name())
        self.input_customer_email(fake.name())
        self.input_customer_lastname(fake.name())
        self.input_customer_address(fake.name())




