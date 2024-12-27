

import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Base):
    """ Класс содержащий локаторы и методы для главной страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    url = "https://fuji-san.ru/japonskie-sladosti/" # url тестируемого сайта

    # Locators

    menu_promotion = (By.XPATH,  '//a[@href="/akcija/"]') # меню Акции
    btn_submit = (By.XPATH,  '//div[@class="float-right empty"]') # кнопка перехода в корзину


    # Getters

    def get_menu_promotion(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menu_promotion))

    def get_btn_submit(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_submit))


    # Actions
    """ Перейти в меню акции"""
    def click_menu_promotion(self):
        self.get_menu_promotion().click()
        print('Переходим в меню со скидками')




    #Methods
    @allure.step('Переход на страницу "Акции"')
    def go_to_the_promo(self):
        self.get_current_url()
        self.click_menu_promotion()



